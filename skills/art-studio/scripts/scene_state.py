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

import hashlib
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


def read_receipt(folder: Path) -> dict:
    """A record folder's generation.md as {label: value} for its labelled lines (the
    first of each label), plus "stack": the Combined Image stack lines, bottom first,
    and "stack_errors": numbered lines after Stack: that aren't in the stack format.
    Empty when there is no receipt."""
    try:
        text = (Path(folder) / "generation.md").read_text(errors="replace")
    except OSError:
        return {}
    fields: dict = {"stack": [], "stack_errors": []}
    in_stack = False
    for line in text.split("\n## ", 1)[0].splitlines():
        if in_stack and re.match(r"\s*\d+\.", line):
            if m := STACK_LINE.fullmatch(line.strip()):
                fields["stack"].append(dict(zip(
                    ("position", "layer", "path", "md5", "style", "approved", "removed",
                     "entry"), m.groups())))
            else:
                fields["stack_errors"].append(line.strip())
            continue
        in_stack = False
        if m := re.fullmatch(r"([A-Za-z][A-Za-z0-9 ]*?):[ \t]*(.*)", line):
            fields.setdefault(m.group(1), m.group(2).strip())
            in_stack = m.group(1) == "Stack"
    return fields


STACK_LINE = re.compile(r"(\d+)\. (\S+) (\S+) md5=([0-9a-f]{32}) style=(\S+) "
                        r"approved=(yes|no) removed=(yes|no) entry=(.*)")


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


# ------------------------------------------------------------------ versions

VNNN = re.compile(r"v(\d+)")
RATIO_TOLERANCE = 0.01   # gen.py's one number for "two aspect ratios differ" (SR-3.5)


def md5(path: Path) -> str:
    return hashlib.md5(Path(path).read_bytes()).hexdigest()


def frame_text(frame: dict) -> str:
    return f"{frame['width']}x{frame['height']}"


def ratio_matches(size: tuple[int, int], frame: dict) -> bool:
    w, h = size
    return abs(w / h - frame["width"] / frame["height"]) <= RATIO_TOLERANCE


def folders(base: Path, deleted_numbers) -> list[dict]:
    """Every vNNN record folder in base, plus every number its deletion log records,
    in numeric order. A logged number is deleted whether or not its folder remains."""
    deleted = deleted_numbers(base)
    found = {int(m.group(1)): c for c in (base.iterdir() if base.is_dir() else [])
             if c.is_dir() and (m := VNNN.fullmatch(c.name))}
    return [{"name": f"v{n:03d}" if n not in found else found[n].name, "number": n,
             "dir": found.get(n, base / f"v{n:03d}"), "deleted": n in deleted}
            for n in sorted(set(found) | deleted)]


def problem(folder: Path, deleted_numbers) -> str | None:
    """Why the image a record folder holds can't be combined, attached or rebuilt from
    (SR-1.8): deleted, missing, or not the md5 its receipt records. None when sound."""
    folder = Path(folder)
    if int(folder.name[1:]) in deleted_numbers(folder.parent):
        return "deleted (its deletion log records it)"
    image = folder / "image.png"
    if not image.is_file():
        return "missing (image.png is gone)"
    recorded = read_receipt(folder).get("md5")
    if not recorded:
        return "unverifiable (its receipt records no md5)"
    if md5(image) != recorded:
        return f"altered (image.png's md5 is {md5(image)}; its receipt records {recorded})"
    return None


def sized(folder: Path, size_of) -> tuple[int, int] | None:
    try:
        return size_of(Path(folder) / "image.png")
    except Exception:   # missing or unreadable: reported by problem()
        return None


def layer_versions(scene_dir: Path, layer_id: str, plan: dict, deleted_numbers,
                   size_of) -> list[dict]:
    """Each recorded version of a Layer, with whether it counts (SR-8.1) and why not.

    A version counts when its Layer is in the current plan, its image.png is the
    Frame's pixel size, and the Layer Entry its receipt records says the same as the
    Layer's current one. size_of is gen.identify, passed in."""
    current = {l["id"]: l["entry"] for l in plan["layers"]}
    out = []
    for v in folders(Path(scene_dir) / "layers" / layer_id, deleted_numbers):
        v["layer"], v["entry"] = layer_id, read_receipt(v["dir"]).get("Layer Entry")
        v["size"] = None if v["deleted"] else sized(v["dir"], size_of)
        why = []
        if v["deleted"]:
            why.append("deleted")
        elif layer_id not in current:
            why.append("its Layer is not in the current plan")
        elif v["size"] is None:
            why.append("image.png is missing or unreadable")
        elif v["size"] != (plan["frame"]["width"], plan["frame"]["height"]):
            w, h = v["size"]
            why.append(f"{w}x{h} doesn't match the Frame's aspect ratio"
                       if not ratio_matches(v["size"], plan["frame"])
                       else f"{w}x{h} is not the Frame's pixel size")
        if (not v["deleted"] and layer_id in current
                and not same_entry(v["entry"] or "", current[layer_id])):
            why.append("made under another Layer Entry")
        v["counts"], v["why_not"] = not why, why
        out.append(v)
    return out


def latest_version(versions: list[dict]) -> dict | None:
    """A Layer's latest version: its highest-numbered counting version."""
    counting = [v for v in versions if v["counts"]]
    return counting[-1] if counting else None


def approved_version(records: list[dict], layer_id: str) -> dict | None:
    """SR-8.2: the version the latest Layer or scene approval naming the Layer names.
    Nothing records an approval yet, so no Layer has one."""
    return None


def default_version(records: list[dict], versions: list[dict]) -> dict | None:
    """A Layer's Default Version (SR-8.5). With no keeps or approvals recorded, it is
    the Layer's latest version, or None."""
    return latest_version(versions)


def classify(scene_dir: Path, path: Path, follow: bool = True) -> dict | None:
    """What a file is to the scene, from its path: None when it lies outside
    OUT/<scene>/; otherwise a dict whose "kind" is "layer" (with "layer", its Layer
    ID), "draft", "combined", "adjusted" (a sources/ copy whose sidecar names one of
    the scene's Layer Versions or Combined Images: "source" classifies that image and
    "source_md5" is the md5 the sidecar records) or "other". All but "other" carry
    "dir", the record folder whose image it is or was derived from."""
    scene_dir = Path(scene_dir).resolve()
    try:
        parts = Path(path).resolve().relative_to(scene_dir).parts
    except ValueError:
        return None
    vn = lambda s: VNNN.fullmatch(s) is not None
    if len(parts) == 4 and parts[0] == "layers" and vn(parts[2]) and parts[3] == "image.png":
        return {"kind": "layer", "layer": parts[1], "dir": scene_dir.joinpath(*parts[:3])}
    if len(parts) == 3 and parts[0] == "drafts" and vn(parts[1]) and parts[2] == "image.png":
        return {"kind": "draft", "dir": scene_dir.joinpath(*parts[:2])}
    if len(parts) == 2 and vn(parts[0]) and parts[1] == "image.png":
        return {"kind": "combined", "dir": scene_dir / parts[0]}
    # follow=False: an adjusted copy comes from a Layer Version or Combined Image,
    # never from another sources/ image, so a sidecar naming one is not followed
    if follow and len(parts) == 2 and parts[0] == "sources" and parts[1].endswith(".png"):
        try:
            text = (scene_dir / "sources" / parts[1]).with_suffix(".md").read_text()
        except OSError:
            text = ""
        m = re.search(r"^Derived from:\s*output:(\S+)\s+md5=([0-9a-f]{32})\s*$", text, re.M)
        if m:
            src = scene_dir.parent / m.group(1)
            src = classify(scene_dir, src if src.suffix == ".png" else src / "image.png",
                           follow=False)
            if src and src["kind"] in ("layer", "combined"):
                return {"kind": "adjusted", "source": src, "source_md5": m.group(2),
                        "dir": src["dir"]}
    return {"kind": "other"}


def holds(info: dict | None, layer_id: str) -> Path | None:
    """The version folder of layer_id that a classified image holds (SR-5.4): the
    image itself when it is a version of that Layer, the version a Combined Image's
    receipt stacks for it, or what an adjusted copy's source holds. None for none."""
    if info is None:
        return None
    if info["kind"] == "adjusted":
        return holds(info["source"], layer_id)
    if info["kind"] == "layer":
        return info["dir"] if info["layer"] == layer_id else None
    if info["kind"] == "combined":
        for s in read_receipt(info["dir"]).get("stack", []):
            if s["layer"] == layer_id and s["path"].startswith("output:"):
                return info["dir"].parents[1] / s["path"].removeprefix("output:")
    return None


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
