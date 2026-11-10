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
    return " ".join(text.split())   # as re.sub(r"\s+", " ", text).strip(), faster


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
        if rec["kind"] != "plan" and not well_formed_decision(rec):
            raise Fail(f"{f} is not a whole {rec['kind']} record: it needs date, words "
                       + ("and combined, md5 and layers" if rec["kind"] == "scene-approval"
                          else "and layer, version and md5")
                       + ". Records are never edited; restore it from a backup.")
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


def well_formed_decision(rec: dict) -> bool:
    """A keep, Layer approval or scene approval record holds what SR-1.4 says it names."""
    named = lambda d: (isinstance(d, dict) and isinstance(d.get("layer"), str)
                       and isinstance(d.get("version"), str)
                       and VNNN.fullmatch(d["version"]) is not None
                       and isinstance(d.get("md5"), str))
    if not (isinstance(rec.get("date"), str) and isinstance(rec.get("words"), str)):
        return False
    if rec["kind"] == "scene-approval":
        return (isinstance(rec.get("combined"), str) and isinstance(rec.get("md5"), str)
                and isinstance(rec.get("layers"), list) and all(map(named, rec["layers"])))
    return named(rec)


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

    size_of is gen.identify, passed in; assess() decides what counts."""
    found = []
    for v in folders(Path(scene_dir) / "layers" / layer_id, deleted_numbers):
        v["layer"], v["entry"] = layer_id, read_receipt(v["dir"]).get("Layer Entry")
        v["size"] = None if v["deleted"] else sized(v["dir"], size_of)
        found.append(v)
    return assess(found, layer_id, plan)


def assess(versions: list[dict], layer_id: str, plan: dict) -> list[dict]:
    """SR-8.1, apart from file access: copies of one Layer's versions (each with
    "entry", "size" and "deleted"), each with "counts" and "why_not" added.

    A version counts when its Layer is in the current plan, its image.png is the
    Frame's pixel size, and the Layer Entry its receipt records says the same as the
    Layer's current one."""
    current = next((l["entry"] for l in plan["layers"] if l["id"] == layer_id), None)
    frame = (plan["frame"]["width"], plan["frame"]["height"])
    out = []
    for v in versions:
        why = []
        if v["deleted"]:
            why.append("deleted")
        else:
            if current is None:
                why.append("its Layer is removed (not in the current plan)")
            if v["size"] is None:
                why.append("image.png is missing or unreadable")
            elif v["size"] != frame:
                w, h = v["size"]
                why.append(f"{w}x{h} doesn't match the Frame's aspect ratio"
                           if not ratio_matches(v["size"], plan["frame"])
                           else f"{w}x{h} is not the Frame's pixel size")
        if not v["deleted"] and current is not None and not same_entry(v["entry"] or "",
                                                                        current):
            why.append("made under another Layer Entry")
        out.append({**v, "counts": not why, "why_not": why})
    return out


def find(versions: list[dict], name: str) -> dict | None:
    if m := VNNN.fullmatch(name):
        n = int(m.group(1))
        for v in versions:
            if v["number"] == n:
                return v
    return None


# ------------------------------------------------------- which version is used


APPROVALS = ("layer-approval", "scene-approval")


def named_versions(rec: dict) -> dict[str, str]:
    """{layer: vNNN} for each Layer Version a keep or approval record names."""
    if rec["kind"] == "scene-approval":
        return {l["layer"]: l["version"] for l in rec["layers"]}
    return {rec["layer"]: rec["version"]} if rec["kind"] in ("keep", "layer-approval") else {}


def journal_view(records: list[dict]) -> dict:
    """What SR-8 reads from the journal, in one pass: the current plan, the latest
    scene approval, and per Layer its latest approval record (SR-8.2) and the keep
    still in force by the journal (SR-8.4: no later keep or approval of that Layer,
    and every later plan holds it with a Layer Entry that says the same as when it was
    kept). Whether the kept version is deleted is checked against the versions."""
    view = {"records": records, "latest": latest(records), "plan": None,
            "scene_approval": None, "approval": {}, "keep": {}, "ever": []}
    entries: dict[str, str] = {}     # each Layer's entry under the plan read so far
    kept_under: dict[str, str] = {}
    for r in records:
        if r["kind"] == "plan":
            view["plan"] = r
            entries = {l["id"]: l["entry"] for l in r["layers"]} if r["layered"] else {}
            view["ever"] += [lid for lid in entries if lid not in view["ever"]]
            for lid in [k for k in view["keep"]
                        if k not in entries or not same_entry(entries[k], kept_under[k])]:
                del view["keep"][lid]   # removed or its Layer Entry changed: ended for good
            continue
        for lid in named_versions(r):
            if r["kind"] == "keep":
                view["keep"][lid], kept_under[lid] = r, entries.get(lid, "")
            else:
                view["approval"][lid] = r
                view["keep"].pop(lid, None)
        if r["kind"] == "scene-approval":
            view["scene_approval"] = r
    return view


def layer_state(view: dict, layer_id: str, versions: list[dict]) -> dict:
    """One Layer's versions in use, from the journal view and its assessed versions:
    "approval" (the record) and "approved" (its version, counting or not, None when
    that folder is gone), "keep" and "kept" (the keep in force), "latest", and
    "default" with "default_why" (SR-8.5: kept, approved or latest; None for none)."""
    approval, keep = view["approval"].get(layer_id), view["keep"].get(layer_id)
    approved = approval and find(versions, named_versions(approval)[layer_id])
    kept = keep and find(versions, keep["version"])
    if kept is not None and kept["deleted"]:
        keep = kept = None   # deleting a kept version ends its keep (SR-8.4)
    counting = [v for v in versions if v["counts"]]
    latest_v = counting[-1] if counting else None
    for why, v in (("kept", kept), ("approved", approved), ("latest", latest_v)):
        if v and v["counts"]:
            break
    else:
        why, v = None, None
    return {"approval": approval, "approved": approved or None, "keep": keep,
            "kept": kept or None, "latest": latest_v, "default": v, "default_why": why}


def layered_view(records: list[dict]) -> dict:
    view = journal_view(records)
    if not (view["plan"] and view["plan"]["layered"]):
        raise Fail("this scene is not a Layered Scene (" + describe(view["plan"]) + "), so "
                   "it has no Layers to keep or approve.")
    return view


def check_keep(view: dict, layer_id: str, versions: list[dict], name: str) -> dict:
    """SR-8.3: refuse a keep of a version that doesn't count. Returns the version."""
    ids = [l["id"] for l in view["plan"]["layers"]]
    if layer_id not in ids:
        raise Fail(f"Layer {layer_id!r} is not in the current Layer Plan "
                   f"(journal/{view['plan']['number']:03d}.json), so none of its versions "
                   "can be kept.")
    v = find(versions, name)
    if v is None:
        raise Fail(f"Layer {layer_id} has no version {name} (layers.py status lists them)")
    if not v["counts"]:
        raise Fail(f"Layer {layer_id}'s {v['name']} doesn't count ({'; '.join(v['why_not'])}), "
                   "so it can't be kept.")
    return v


def check_layer_approval(view: dict, layer_id: str, versions: list[dict], name: str,
                         replace: bool) -> dict | None:
    """SR-10.2 and SR-10.3. Returns the approval record this one replaces, if any."""
    v = find(versions, name)
    if v is None:
        raise Fail(f"Layer {layer_id} has no version {name} (layers.py status lists them)")
    if not v["counts"]:
        raise Fail(f"Layer {layer_id}'s {v['name']} can't be approved: "
                   + "; ".join(v["why_not"]) + ".")
    before = view["approval"].get(layer_id)
    was = before and named_versions(before)[layer_id]
    if was and was != v["name"] and not replace:
        raise Fail(f"Layer {layer_id}'s Approved Layer Version is {was} "
                   f"(journal/{before['number']:03d}.json, counting or not). Name it to the "
                   "User, and pass --replace if they approved superseding it.")
    return before


def check_scene_approval(view: dict, versions: dict[str, list[dict]], stack: list[dict],
                         replace: bool) -> dict:
    """SR-10.5 and SR-10.6 for a Combined Image whose stack is [{"layer", "version"}],
    bottom first; versions holds every Layer's assessed versions. Returns what the
    approval replaces: "scene" (the latest scene approval, or None) and "layers"
    ({"layer", "version", "record"} for each Layer it holds whose Approved Layer
    Version, counting or not, is another version)."""
    ids = [l["id"] for l in view["plan"]["layers"]]
    held = [s["layer"] for s in stack]
    fails = [f"{lid}: missing from the Combined Image" for lid in ids if lid not in held]
    fails += [f"{lid}: " + ("removed" if lid in view["ever"] else "not in any Layer Plan")
              for lid in held if lid not in ids]
    now = [lid for lid in held if lid in ids]
    fails += [f"{lid}: in an old order" for lid, want in
              zip(now, [lid for lid in ids if lid in held]) if lid != want]
    for s in stack:
        if s["layer"] not in ids:
            continue
        v = find(versions.get(s["layer"], []), s["version"])
        if v is None:
            fails.append(f"{s['layer']}: holds {s['version']}, which isn't recorded")
        elif not v["counts"]:
            fails.append(f"{s['layer']}: {v['name']} " + "; ".join(
                "is made under a different Layer Entry" if w == "made under another Layer Entry"
                else w for w in v["why_not"]))
    if fails:
        raise Fail("this Combined Image can't be approved: " + "; ".join(fails)
                   + f". The current plan (journal/{view['plan']['number']:03d}.json) holds, "
                   f"bottom to top: {', '.join(ids)}.")
    scene, layers = view["scene_approval"], []
    for s in stack:
        if (r := view["approval"].get(s["layer"])) and \
                (was := named_versions(r)[s["layer"]]) != s["version"]:
            layers.append({"layer": s["layer"], "version": was, "record": r["number"]})
    if (scene or layers) and not replace:
        named = ([f"the approved image {scene['combined'].rsplit('/', 1)[-1]} "
                  f"(journal/{scene['number']:03d}.json)"]
                 if scene else []) + [
            f"Layer {l['layer']}'s Approved Layer Version {l['version']} "
            f"(journal/{l['record']:03d}.json, counting or not)" for l in layers]
        raise Fail("approving it would replace " + "; ".join(named) + ". Name these to the "
                   "User, and pass --replace if they approved superseding them.")
    return {"scene": scene, "layers": layers}


def journal_problem(records: list[dict], layer_id: str, folder: Path) -> str | None:
    """SR-1.8 for journal records: how a Layer Version's image.png differs from the md5
    a keep or approval record naming it records, or None."""
    folder, found = Path(folder), None
    for r in records:
        if named_versions(r).get(layer_id) != folder.name:
            continue
        want = r["md5"] if r["kind"] != "scene-approval" else next(
            l["md5"] for l in r["layers"] if l["layer"] == layer_id)
        if found is None:
            found = md5(folder / "image.png") if (folder / "image.png").is_file() else ""
        if found != want:
            return f"not the md5 {want} that journal/{r['number']:03d}.json records"
    return None


# ------------------------------------------------- the approved image's copies


def layer_files(rec: dict) -> list[tuple[str, dict]]:
    """SR-17.4: final-layers/NN-<layer-id>.png for each Layer a scene approval record
    names, from 01 at the bottom, with what the record says of it."""
    return [(f"{i:02d}-{l['layer']}.png", l) for i, l in enumerate(rec["layers"], start=1)]


def final_md(rec: dict) -> str:
    """final.md for a scene approval record (SR-10.8): today's provenance, approval,
    date and md5 lines, then the Layer files in stacking order."""
    return "\n".join([
        f"Promoted from {rec['combined'].rsplit('/', 1)[-1]}",
        f"User approval, verbatim: {rec['words']}",
        "",
        f"Date: {rec['date']}",
        f"md5: {rec['md5']}",
        f"Scene approval record: journal/{rec['number']:03d}.json",
        "Layer files, bottom to top (final-layers/, each a byte copy of the Layer Version "
        "it names):",
        *(f"- {name}: layers/{l['layer']}/{l['version']} md5={l['md5']}"
          for name, l in layer_files(rec)),
        "A Layer's Approved Layer Version can later differ from its Layer file: approving "
        "a Layer Version on its own leaves these files unchanged (layers.py status names "
        "each Layer's).",
        "",
    ])


def copies_mismatch(scene_dir: Path, rec: dict) -> list[str]:
    """How final.png, final.md and final-layers/ differ from the latest scene approval
    record (SR-10.9); empty when they match."""
    scene_dir, out = Path(scene_dir), []
    final, md, folder = scene_dir / "final.png", scene_dir / "final.md", scene_dir / "final-layers"
    if not final.is_file() or md5(final) != rec["md5"]:
        out.append("final.png " + ("is missing" if not final.is_file() else
                                   "is not the approved Combined Image"))
    try:
        md_ok = md.read_text() == final_md(rec)
    except OSError:
        md_ok = False
    if not md_ok:
        out.append("final.md " + ("is missing" if not md.is_file() else
                                  "doesn't match the scene approval record"))
    want = dict(layer_files(rec))
    have = {p.name: p for p in folder.iterdir() if not p.name.startswith(".")} \
        if folder.is_dir() else {}   # Finder's .DS_Store is not a Layer file
    if not folder.is_dir():
        out.append("final-layers/ is missing")
    else:
        out += [f"final-layers/{n} is missing" for n in want if n not in have]
        out += [f"final-layers/{n} isn't a Layer file of the approved image"
                for n in have if n not in want]
        out += [f"final-layers/{n} is not a byte copy of {l['layer']} {l['version']}"
                for n, l in want.items() if n in have and
                (not have[n].is_file() or md5(have[n]) != l["md5"])]
    return out


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


def stack_of(receipt: dict) -> list[dict]:
    """A Combined Image receipt's stack as [{"layer", "version"}], bottom first."""
    return [{"layer": s["layer"], "version": s["path"].rsplit("/", 1)[-1]}
            for s in receipt.get("stack", [])]


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


def plan_effects(records: list[dict], proposal: dict, versions: dict[str, list[dict]]) -> list[str]:
    """SR-2.4: each Approved Layer Version that the proposal would make stop counting
    or count again, and each keep it would end. versions holds each Layer's versions
    (with "entry", "size" and "deleted"), for every Layer ever planned or proposed."""
    cur = current_plan(records)
    if not (cur and cur["layered"] and proposal["layered"]):
        return []
    now = journal_view(records)
    after = journal_view(records + [{"number": latest(records) + 1, "kind": "plan",
                                     **proposal}])
    out = []
    for lid, vs in versions.items():
        was = layer_state(now, lid, assess(vs, lid, cur))
        will = layer_state(after, lid, assess(vs, lid, proposal))
        if was["approved"] and was["approved"]["counts"] != will["approved"]["counts"]:
            out.append(f"Layer {lid}'s Approved Layer Version {was['approved']['name']} "
                       f"(journal/{was['approval']['number']:03d}.json) would "
                       + ("stop counting" if was["approved"]["counts"] else "count again"))
        if was["keep"] and not will["keep"]:
            out.append(f"the keep of Layer {lid}'s {was['keep']['version']} "
                       f"(journal/{was['keep']['number']:03d}.json) would end, for good")
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
