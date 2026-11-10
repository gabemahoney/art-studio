"""A scene's state: its Scene Journal, read and written in one place, and the rules
that decide what the journal allows.

A Layered Scene keeps every decision that changes which version a Layer uses or what
is approved as one numbered, frozen JSON record in OUT/<scene>/journal/NNN.json.
Everything else about the scene is derived from that journal and the record folders
beside it; final.png, final.md and receipt Status lines are copies, never inputs.

Writing a record has three separate steps, so a decision is never published against
a state the User was not shown:
  read     read_journal()                       the records as they stand
  check    check_based_on() and the pure checks  refuse before anything is written
  publish  publish()                            temp file, then a hard link that
                                                fails if the number is taken

The rules here work on parsed records, apart from file access. This module never
imports gen.py (gen.py imports it): deletion logs reach it as gen.deleted_numbers,
passed in by the caller.

Stdlib only; no venv required.
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import json
import os
import re
import tempfile
from pathlib import Path

# Scene slugs and Layer IDs share one pattern, so a Layer ID is always a safe
# folder name under layers/.
SLUG = r"[a-z0-9][a-z0-9._-]*"
KINDS = ("plan", "keep", "layer-approval", "scene-approval")
RECORD = re.compile(r"(\d{3,})\.json")   # temp files start with "." and never match


class Fail(Exception):
    """A check failed. Nothing was written."""


class Stale(Fail):
    """The journal moved past the state the User decided on."""


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def same_entry(a: str, b: str) -> bool:
    """Two Layer Entries say the same when they match after whitespace is collapsed."""
    return norm(a) == norm(b)


# ------------------------------------------------------------------- reading


def journal_dir(scene_dir: Path) -> Path:
    return Path(scene_dir) / "journal"


def read_journal(scene_dir: Path) -> list[dict]:
    """Every published record of the scene, in numeric order (empty if no journal)."""
    jdir = journal_dir(scene_dir)
    try:
        names = sorted(p.name for p in jdir.iterdir())
    except FileNotFoundError:
        return []
    except OSError as e:
        raise Fail(f"cannot read the Scene Journal {jdir} ({e.strerror or e}). Fix it "
                   "(e.g. chmod u+rx) and rerun.") from None
    records: dict[int, dict] = {}
    for name in names:
        m = RECORD.fullmatch(name)
        if not m:
            continue
        n, f = int(m.group(1)), jdir / name
        try:
            rec = json.loads(f.read_text())
        except (OSError, ValueError) as e:
            raise Fail(f"{f} is not a readable journal record ({e}). Records are never "
                       "edited; restore it from a backup.") from None
        if not isinstance(rec, dict) or rec.get("number") != n or rec.get("kind") not in KINDS:
            raise Fail(f"{f} is not a journal record: its number must be {n} and its "
                       f"kind one of {', '.join(KINDS)}.")
        if rec["kind"] == "plan" and not well_formed_plan(rec):
            raise Fail(f"{f} is not a whole plan record: it needs date, words and "
                       "layered, and a layered plan a frame and its layers. Records are "
                       "never edited; restore it from a backup.")
        if n in records:
            raise Fail(f"{jdir} holds record {n} twice. Records are never renamed; "
                       "restore the journal from a backup.")
        records[n] = rec
    return [records[n] for n in sorted(records)]


def well_formed_plan(rec: dict) -> bool:
    if not (isinstance(rec.get("date"), str) and isinstance(rec.get("words"), str)
            and isinstance(rec.get("layered"), bool)):
        return False
    if not rec["layered"]:
        return True
    frame, layers = rec.get("frame"), rec.get("layers")
    return (isinstance(frame, dict) and all(isinstance(frame.get(k), int)
                                            for k in ("width", "height"))
            and isinstance(layers, list)
            and all(isinstance(l, dict) and isinstance(l.get("id"), str)
                    and isinstance(l.get("entry"), str) for l in layers))


def latest(records: list[dict]) -> int:
    """The number to pass as --based-on: the highest record read, 0 for none."""
    return records[-1]["number"] if records else 0


def generated(scene_dir: Path, deleted_numbers) -> bool:
    """Whether anything has been generated for the scene: any vNNN folder in it, in
    drafts/ or in layers/<id>/, or any number a deletion log beside them records.

    deleted_numbers is gen.deleted_numbers, passed in."""
    scene_dir = Path(scene_dir)
    if not scene_dir.is_dir():
        return False
    layers = scene_dir / "layers"
    bases = [scene_dir, scene_dir / "drafts",
             *(sorted(p for p in layers.iterdir() if p.is_dir()) if layers.is_dir() else [])]
    for base in bases:
        if base.is_dir() and any(c.is_dir() and re.fullmatch(r"v\d+", c.name)
                                 for c in base.iterdir()):
            return True
        if deleted_numbers(base):
            return True
    return False


# --------------------------------------------------------------------- plans


def plans(records: list[dict]) -> list[dict]:
    return [r for r in records if r["kind"] == "plan"]


def current_plan(records: list[dict]) -> dict | None:
    """The highest-numbered plan record; None means a Single-Layer Scene with no plan."""
    found = plans(records)
    return found[-1] if found else None


def is_layered(records: list[dict]) -> bool:
    plan = current_plan(records)
    return bool(plan and plan["layered"])


def describe(plan: dict | None) -> str:
    if plan is None:
        return "single (no Layer Plan recorded)"
    if not plan["layered"]:
        return "single"
    f = plan["frame"]
    return f"layered, Frame {f['width']}x{f['height']}, {len(plan['layers'])} Layers"


def entry_from(records: list[dict], number: int, layer_id: str) -> str:
    """The Layer Entry text plan record `number` holds for layer_id, verbatim."""
    rec = next((r for r in records if r["number"] == number), None)
    if rec is None or rec["kind"] != "plan":
        raise Fail(f"--layer {layer_id}=@{number}: the journal holds "
                   + ("no record" if rec is None else "no plan record")
                   + f" {number}. Run layers.py status to see the current plan.")
    for layer in rec.get("layers") or []:
        if layer["id"] == layer_id:
            return layer["entry"]
    raise Fail(f"--layer {layer_id}=@{number}: plan record {number} holds no Layer "
               f"{layer_id!r}.")


def plan_changes(records: list[dict], proposal: dict) -> list[str]:
    """What the proposal changes about the current plan (SR-2.4: Layer changes)."""
    cur = current_plan(records)
    if cur is None:
        return []
    if cur["layered"] != proposal["layered"]:
        kind = ("single", "layered")
        return [f"switches from {kind[cur['layered']]} to {kind[proposal['layered']]}"]
    if not proposal["layered"]:
        return []
    out = []
    old_f, new_f = cur["frame"], proposal["frame"]
    if old_f != new_f:
        out.append(f"changes the Frame from {old_f['width']}x{old_f['height']} to "
                   f"{new_f['width']}x{new_f['height']}")
    old = {l["id"]: l["entry"] for l in cur["layers"]}
    new = {l["id"]: l["entry"] for l in proposal["layers"]}
    for lid, entry in new.items():
        if lid in old:
            if not same_entry(old[lid], entry):
                out.append(f"changes Layer {lid}'s Layer Entry")
            continue
        earlier = [r for r in plans(records) if r["layered"]
                   and any(l["id"] == lid for l in r["layers"])]
        if not earlier:
            out.append(f"adds Layer {lid}")
            continue
        last = earlier[-1]
        was = next(l["entry"] for l in last["layers"] if l["id"] == lid)
        out.append(f"puts back Layer {lid}, " + (
            f"with its Layer Entry from plan record {last['number']}"
            if same_entry(was, entry) else
            f"with a Layer Entry that differs from plan record {last['number']}'s"))
    out += [f"removes Layer {lid}" for lid in old if lid not in new]
    kept_old = [lid for lid in old if lid in new]
    kept_new = [lid for lid in new if lid in old]
    if kept_old != kept_new:
        out.append("reorders Layers, bottom to top: " + ", ".join(kept_new))
    return out


def check_plan(records: list[dict], proposal: dict, has_generated: bool) -> list[str]:
    """Refuse a proposal SR-2.2/2.3 forbids; otherwise return what it changes."""
    if proposal["layered"]:
        layers = proposal["layers"]
        seen = set()
        for layer in layers:
            lid = layer["id"]
            if not re.fullmatch(SLUG, lid):
                raise Fail(f"Layer ID {lid!r}: use lowercase letters, digits, . _ - "
                           "(starting with a letter or digit), as scene slugs do.")
            if lid in seen:
                raise Fail(f"Layer ID {lid!r} is given twice; each Layer needs its own ID.")
            seen.add(lid)
            if not norm(layer["entry"]):
                raise Fail(f"Layer {lid!r} has an empty Layer Entry; say which parts of "
                           "the scene it holds.")
        if len(layers) < 2:
            msg = (f"a layered plan needs two or more Layers; this one has {len(layers)}.")
            if has_generated:
                msg += (" The scene already has generations, so add the replacement "
                        "Layer first, or in the same change.")
            raise Fail(msg)
    cur = current_plan(records)
    if has_generated:
        was_layered = bool(cur and cur["layered"])
        if was_layered != proposal["layered"]:
            raise Fail("this scene already has generations, so it can't switch between "
                       "single and layered. Offer the User a new scene instead.")
        if was_layered and cur["frame"] != proposal["frame"]:
            raise Fail("this scene already has generations, so its Frame is locked. "
                       "Offer the User a new scene for a different Frame.")
    return plan_changes(records, proposal)


# ------------------------------------------------------------------- writing


def check_based_on(records: list[dict], based_on: int) -> None:
    """Refuse when the journal holds a record the User's decision didn't see."""
    now = latest(records)
    if based_on != now:
        raise Stale(f"--based-on {based_on} is not the journal's latest record ({now}). "
                    "The scene changed since the User decided: show the User its new "
                    "state (layers.py status, then the command's --dry-run) and ask again.")


def publish(scene_dir: Path, record: dict, fallback: bool = False) -> Path:
    """Publish record under journal/NNN.json, whole or not at all.

    The record is written to a hidden temp file and hard-linked to its number; the
    link fails when another writer took that number. fallback (a Single-Layer Scene's
    plan record, SR-1.10) lets a filesystem without hard links create the numbered
    file exclusively and then write it instead."""
    jdir = journal_dir(scene_dir)
    dest = jdir / f"{record['number']:03d}.json"
    taken = Stale(f"{dest.name} was published by another writer while this one ran, "
                  "so the scene changed since the User decided: show the User its new "
                  "state (layers.py status, then the command's --dry-run) and ask again.")
    data = json.dumps(record, indent=2, ensure_ascii=False) + "\n"
    unwritable = lambda e: Fail(f"could not write in the Scene Journal {jdir} "
                                f"({e.strerror or e}); nothing was recorded.")
    try:
        jdir.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=jdir, prefix=".", suffix=".tmp")
    except OSError as e:
        raise unwritable(e) from None
    try:
        # mkstemp makes the file 0600 and the link keeps that mode; give the record
        # the umask's mode, so whoever can read the scene's images can read its journal
        umask = os.umask(0)
        os.umask(umask)
        try:
            os.fchmod(fd, 0o666 & ~umask)
            with os.fdopen(fd, "w") as f:
                f.write(data)
        except OSError as e:
            raise unwritable(e) from None
        try:
            os.link(tmp, dest)
            return dest
        except FileExistsError:
            raise taken from None
        except OSError as e:
            if not fallback:
                raise Fail(f"could not publish {dest.name} in the Scene Journal {jdir} "
                           f"({e.strerror or e}); nothing was recorded. A Layered "
                           "Scene's journal needs a filesystem with hard links (APFS "
                           "and other usual local filesystems have them).") from None
        try:
            f = open(dest, "x")
        except FileExistsError:
            raise taken from None
        except OSError as e:
            raise unwritable(e) from None
        try:
            with f:
                f.write(data)
            return dest
        except OSError as e:
            dest.unlink(missing_ok=True)   # never a whole record, so never published
            raise unwritable(e) from None
    finally:
        Path(tmp).unlink(missing_ok=True)
