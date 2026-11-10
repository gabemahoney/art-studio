#!/usr/bin/env python3
"""Promote an approved candidate to the head revision, with provenance.

Approval is the one step where the package's invariants are easiest to break by
hand: copy the wrong file, forget the sidecar, or edit reference.png in place and
silently orphan its provenance. So do it here.

  PKG/assets/<type>/<slug>/candidates/vNNN/image.png  ->  reference.png + reference.md
  OUT/<scene>/vNNN/image.png                          ->  final.png    + final.md

The kind is read from the path itself: a vNNN under a `candidates/` directory is an
asset candidate; any other vNNN is a scene version.

In a Layered Scene (its Scene Journal's current plan is layered) the path is read
first as one of the scene's record folders:

  OUT/<scene>/layers/<id>/vNNN   a Layer Version: approved as that Layer's Approved
                                 Layer Version, in a Layer approval record
  OUT/<scene>/vNNN               a Combined Image: one scene approval record, then
                                 final.png, final.md and final-layers/NN-<id>.png
  OUT/<scene>/drafts/vNNN        a Draft: never approved

Both need --approval and --based-on N, the journal number the dry run printed. When
final.png, final.md or final-layers/ don't match the latest scene approval record,
running this on the Combined Image it names completes them from that record instead.

Refuses to overwrite an existing head revision unless --replace is given, and
verifies byte-identity afterwards — the same check rules.md requires before any
reference may be attached to a generation.

  python3 scripts/promote.py ~/book/art/harbour-at-dusk/v002 \
      --approval "I agree. Make this the reference image."

Stdlib only; no venv required.
"""

from __future__ import annotations

import sys

# A compiled copy of this file in __pycache__ is a copy that does not carry
# later changes — including the paid-call gate. Never leave one behind.
sys.dont_write_bytecode = True

import argparse
import hashlib
import os
import re
import shutil
import tempfile
from datetime import date
from pathlib import Path

# python3 -I leaves this script's folder off sys.path; gen and scene_state live beside it.
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
import gen  # noqa: E402
import scene_state  # noqa: E402
from gen import Fail  # noqa: E402


def md5(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("candidate", help="the vNNN directory to promote")
    p.add_argument("--approval", help="the user's approval, verbatim, for the sidecar")
    p.add_argument("--replace", action="store_true",
                   help="allow overwriting an existing reference.png / final.png, or "
                        "superseding a Layered Scene's approvals")
    p.add_argument("--based-on", type=int, metavar="N",
                   help="Layered Scene only: the journal number the dry run printed")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    cand = Path(args.candidate).expanduser().resolve()
    if not re.fullmatch(r"v\d+", cand.name):
        raise Fail(f"{args.candidate} is not a vNNN candidate directory")
    image, receipt = cand / "image.png", cand / "generation.md"
    for f in (image, receipt):
        if not f.exists():
            raise Fail(f"{f} is missing — candidate is incomplete")
    if layered := layered_kind(cand):
        return promote_layered(args, cand, *layered)
    if cand.parent.name == "candidates":
        head_dir, head_name, sidecar_name = cand.parent.parent, "reference.png", "reference.md"
    else:
        head_dir, head_name, sidecar_name = cand.parent, "final.png", "final.md"

    head, sidecar = head_dir / head_name, head_dir / sidecar_name
    if head.exists() and not args.replace:
        prior = ""
        if sidecar.exists():
            m = re.search(r"candidates/(v\d+)|(?:^|/)(v\d+)", sidecar.read_text())
            prior = f" (currently from {m.group(0)})" if m else ""
        raise Fail(f"{head} already exists{prior}. "
                   "Pass --replace if the user approved superseding it.")

    # The candidate's own path, relative to where the sidecar will live, is what
    # rules.md's validation walks back down.
    provenance = str(cand.relative_to(head_dir))
    body = [
        f"Promoted from {provenance}",
        "",
        f"Date: {date.today().isoformat()}",
        f"md5: {md5(image)}",
    ]
    if args.approval:
        body.insert(1, f"User approval, verbatim: {args.approval}")

    if args.dry_run:
        print(f"  would write {head} from {provenance}/image.png")
        print(f"  would write {sidecar}: Promoted from {provenance}")
        return 0

    shutil.copy2(image, head)
    sidecar.write_text("\n".join(body) + "\n")

    if md5(head) != md5(image):
        raise Fail("post-copy byte check FAILED — head revision does not match "
                   "the candidate. Do not attach this reference.")
    print(f"  wrote {head}  (byte-identical to {provenance}/image.png)")
    print(f"  wrote {sidecar}")

    # Reflect approval back into the frozen receipt so status lives in one place.
    status = (f"approved and promoted to {head_name} on {date.today().isoformat()}"
              + (f'. User approval: "{args.approval}"' if args.approval else ""))
    if not set_status(receipt, status):
        # Receipts written by hand (everything before gen.py existed) use their
        # own wording, so there is nothing to rewrite. Say so — silently leaving a
        # promoted candidate reading as unapproved is worse than the extra line.
        print(f"  note: {receipt} has no "
              "'Status: awaiting user evaluation' line, so its status was NOT "
              "updated. Edit it by hand to record the approval.", file=sys.stderr)
    return 0


def set_status(receipt: Path, status: str) -> bool:
    """Replace a receipt's 'awaiting user evaluation' Status line; False if it has none.
    The line is an informational copy, so a receipt that can't be rewritten warns."""
    try:
        text = receipt.read_text()
        if "Status: awaiting user evaluation" not in text:
            return False
        receipt.write_text(text.replace("Status: awaiting user evaluation", f"Status: {status}"))
    except OSError as e:
        print(f"  warn: could not update {receipt} status line ({e.strerror or e}); edit it "
              "by hand to record the approval", file=sys.stderr)
        return True
    print(f"  updated {receipt} status line")
    return True


# ------------------------------------------------------------- Layered Scenes


def layered_kind(cand: Path) -> tuple[str, Path, str | None] | None:
    """(kind, scene folder, Layer ID) when cand is a Layer Version, Draft or Combined
    Image folder of a scene whose current plan is layered (SR-10.1), else None, so a
    folder that only happens to sit under one named layers/ or drafts/ promotes as
    today. Read before today's candidates/ test."""
    up = cand.parents
    for kind, depth, fits in (("layer", 2, len(up) > 3 and up[1].name == "layers"),
                              ("draft", 1, len(up) > 2 and up[0].name == "drafts"),
                              ("combined", 0, len(up) > 1)):
        if fits and scene_state.is_layered(scene_state.read_journal(up[depth])):
            return kind, up[depth], cand.parent.name if kind == "layer" else None
    return None


def promote_layered(args, cand: Path, kind: str, scene: Path, lid: str | None) -> int:
    rel = lambda p: f"output:{Path(p).relative_to(scene.parent)}"
    if kind == "draft":
        raise Fail(f"{rel(cand)} is a Draft, a reference for placement, scale and light "
                   "only, so it is never approved. Approve a Layer Version or a Combined "
                   "Image.")
    records = scene_state.read_journal(scene)                   # read
    view = scene_state.journal_view(records)
    if kind == "combined" and (done := view["scene_approval"]) and \
            done["combined"] == rel(cand) and scene_state.copies_mismatch(scene, done):
        return complete_copies(args, cand, scene, done, rel)
    if not args.dry_run and not (args.approval or "").strip():
        raise Fail("--approval is required: the User's approval, verbatim, for the Scene "
                   "Journal")
    if not args.dry_run and args.based_on is None:
        raise Fail("--based-on is required: the journal number the dry run printed, "
                   "so a decision is never recorded against a state the User wasn't shown")
    versions = lambda ids: {i: scene_state.layer_versions(scene, i, view["plan"],
                                                          gen.deleted_numbers, gen.identify)
                            for i in ids}
    record = {"number": view["latest"] + 1,
              "kind": "layer-approval" if kind == "layer" else "scene-approval",
              "date": date.today().isoformat(), "words": args.approval}
    if kind == "layer":                                         # check
        before = scene_state.check_layer_approval(view, lid, versions([lid])[lid],
                                                  cand.name, args.replace)
        sound(cand, rel, records, lid)
        record |= {"layer": lid, "version": cand.name,
                   "md5": md5(cand / "image.png"),
                   "replaces": before and {"record": before["number"],
                                           "version": scene_state.named_versions(before)[lid]}}
        print(f"  approve {rel(cand)} as Layer {lid}'s Approved Layer Version")
        if before:
            print(f"  it replaces {record['replaces']['version']} "
                  f"(journal/{before['number']:03d}.json)")
        held = view["scene_approval"] and scene_state.named_versions(
            view["scene_approval"]).get(lid)
        if held and held != cand.name:
            print(f"  note: the scene's approved image, "
                  f"{view['scene_approval']['combined'].rsplit('/', 1)[-1]}, holds {lid} {held}; "
                  "it and final-layers/ stay unchanged. Tell the User.")
    else:
        stack = combined_stack(cand, scene, rel)
        found = versions(dict.fromkeys(view["ever"] + [s["layer"] for s in stack]))
        replaces = scene_state.check_scene_approval(view, found, stack, args.replace)
        sound(cand, rel)
        for s in stack:
            if trouble := scene_state.journal_problem(records, s["layer"], s["dir"]):
                raise Fail(f"{rel(cand)} can't be approved: {rel(s['dir'] / 'image.png')} is "
                           f"{trouble}.")
        copies_writable(scene)
        record |= {"combined": rel(cand),
                   "md5": md5(cand / "image.png"),
                   "layers": [{"layer": s["layer"], "version": s["version"], "md5": s["md5"]}
                              for s in stack],
                   "replaces": {"scene": replaces["scene"] and replaces["scene"]["number"],
                                "layers": replaces["layers"]}}
        print(f"  approve {rel(cand)} as the scene's approved image; each Layer Version it "
              "holds becomes that Layer's Approved Layer Version: "
              + ", ".join(f"{s['layer']} {s['version']}" for s in stack))
        if replaces["scene"]:
            print(f"  it replaces the approved image "
                  f"{replaces['scene']['combined'].rsplit('/', 1)[-1]} "
                  f"(journal/{replaces['scene']['number']:03d}.json)")
        for l in replaces["layers"]:
            print(f"  it replaces Layer {l['layer']}'s Approved Layer Version {l['version']} "
                  f"(journal/{l['record']:03d}.json)")
    if args.dry_run:
        print(f"  dry run: nothing written. To record the User's approval, pass --based-on "
              f"{view['latest']} and --approval.")
        return 0
    scene_state.check_based_on(records, args.based_on)
    gen.writable_base(scene_state.journal_dir(scene))
    dest = scene_state.publish(scene, record)                   # publish
    print(f"  wrote {dest}")
    today = date.today().isoformat()
    if kind == "layer":
        set_status(cand / "generation.md",
                   f"approved as Layer {lid}'s Approved Layer Version on {today} "
                   f"(journal/{record['number']:03d}.json). User approval: \"{args.approval}\"")
        return 0
    copy_out(cand, scene, record)
    return 0


def sound(cand: Path, rel, records: list[dict] = (), lid: str | None = None) -> None:
    """SR-1.8: the image being approved exists and is the one its receipt, and any
    journal record naming it, records."""
    if trouble := scene_state.problem(cand, gen.deleted_numbers):
        raise Fail(f"{rel(cand)} can't be approved: {rel(cand / 'image.png')} is {trouble}; "
                   f"{rel(cand / 'generation.md')} names it.")
    if lid and (trouble := scene_state.journal_problem(records, lid, cand)):
        raise Fail(f"{rel(cand)} can't be approved: {rel(cand / 'image.png')} is {trouble}.")


def copies_writable(scene: Path) -> None:
    """Refuse before recording an approval whose copies couldn't then be written."""
    gen.writable_base(scene)
    for f in (scene / "final.png", scene / "final.md"):
        if f.exists() and not (f.is_file() and os.access(f, os.W_OK)):
            raise Fail(f"{f} can't be replaced (not a writable file), so the approval's "
                       "copies couldn't be written. Fix it (e.g. chmod u+w) and rerun; "
                       "nothing was recorded.")


def copy_out(cand: Path, scene: Path, rec: dict) -> None:
    """The copies and Status lines, after the record that is the approval."""
    try:
        write_copies(cand, scene, rec)
    except OSError as e:
        raise Fail(f"journal/{rec['number']:03d}.json records the approval, but writing its "
                   f"copies failed ({e.strerror or e}). Fix that and run promote.py on "
                   f"{cand.name} again: it completes them without another record.") from None
    statuses(cand, scene, rec)


def combined_stack(cand: Path, scene: Path, rel) -> list[dict]:
    """The Combined Image's stack from its receipt, each Layer Version checked to be
    this scene's and to match the md5 the Stack records (SR-1.8)."""
    receipt = scene_state.read_receipt(cand)
    named = rel(cand / "generation.md")
    if receipt.get("Kind") != "Combined Image" or not receipt["stack"]:
        raise Fail(f"{named} records no Combined Image stack, so it can't be approved")
    if receipt["stack_errors"]:
        raise Fail(f"{named} has a Stack line that can't be read: {receipt['stack_errors'][0]!r}")
    stack = []
    for s, sv in zip(receipt["stack"], scene_state.stack_of(receipt)):
        vdir = scene.parent / s["path"].removeprefix("output:")
        what = scene_state.classify(scene, vdir / "image.png")
        if not s["path"].startswith("output:") or not what or what["kind"] != "layer" \
                or what["layer"] != s["layer"]:
            raise Fail(f"{named}'s Stack line {s['position']} names {s['path']}, which is not "
                       f"one of this scene's {s['layer']} Layer Versions")
        trouble = scene_state.problem(vdir, gen.deleted_numbers)
        if trouble is None and md5(vdir / "image.png") != s["md5"]:
            trouble = f"not the md5 {s['md5']} the Stack records"
        if trouble:
            raise Fail(f"{rel(cand)} can't be approved: {rel(vdir / 'image.png')} is {trouble}; "
                       f"{named}'s Stack line {s['position']} names it.")
        stack.append(sv | {"md5": s["md5"], "dir": vdir})
    return stack


def complete_copies(args, cand: Path, scene: Path, rec: dict, rel) -> int:
    """SR-10.9: the copies don't match the latest scene approval record, which names
    this Combined Image: complete them from the record, writing no record."""
    if md5(cand / "image.png") != rec["md5"]:
        raise Fail(f"{rel(cand / 'image.png')} is not the md5 {rec['md5']} that "
                   f"journal/{rec['number']:03d}.json records, so its copies can't be completed.")
    for l in rec["layers"]:
        image = scene / "layers" / l["layer"] / l["version"] / "image.png"
        if not image.is_file() or md5(image) != l["md5"]:
            raise Fail(f"{rel(image)} is missing or not the md5 {l['md5']} that "
                       f"journal/{rec['number']:03d}.json records, so final-layers/ can't be "
                       "completed.")
    missing = scene_state.copies_mismatch(scene, rec)
    print(f"  completing the copies of the scene approval in journal/{rec['number']:03d}.json "
          f"({'; '.join(missing)}); no new record is written")
    if args.dry_run:
        print("  dry run: nothing written")
        return 0
    copies_writable(scene)
    copy_out(cand, scene, rec)
    print("  completed; promote.py on this Combined Image now records a new approval")
    return 0


def write_copies(cand: Path, scene: Path, rec: dict) -> None:
    """final.png, then final-layers/ (built aside and swapped in), then final.md, all
    from the scene approval record (SR-10.7, SR-10.8)."""
    final = scene / "final.png"
    shutil.copy2(cand / "image.png", final)
    if md5(final) != rec["md5"]:
        raise Fail("post-copy byte check FAILED — final.png does not match the approved "
                   "Combined Image. Run promote.py on it again to complete the copies.")
    print(f"  wrote {final}  (byte-identical to {cand.name}/image.png)")
    new = Path(tempfile.mkdtemp(dir=scene, prefix=".final-layers-"))
    try:
        for name, l in scene_state.layer_files(rec):
            shutil.copy2(scene / "layers" / l["layer"] / l["version"] / "image.png", new / name)
            if md5(new / name) != l["md5"]:
                raise Fail(f"post-copy byte check FAILED — final-layers/{name} does not match "
                           f"{l['layer']} {l['version']}. Run promote.py on the Combined Image "
                           "again to complete the copies.")
        new.chmod(0o777 & ~current_umask())
        folder, old = scene / "final-layers", scene / f".final-layers-old-{new.name[-8:]}"
        if folder.exists():
            folder.rename(old)
        new.rename(folder)
    finally:
        shutil.rmtree(new, ignore_errors=True)
        shutil.rmtree(scene / f".final-layers-old-{new.name[-8:]}", ignore_errors=True)
    for name, l in scene_state.layer_files(rec):
        print(f"  wrote {folder / name}  (byte-identical to layers/{l['layer']}/{l['version']}"
              "/image.png)")
    (scene / "final.md").write_text(scene_state.final_md(rec))
    print(f"  wrote {scene / 'final.md'}")


def current_umask() -> int:
    umask = os.umask(0)
    os.umask(umask)
    return umask


def statuses(cand: Path, scene: Path, rec: dict) -> None:
    """Each receipt that still awaits evaluation records the approval (SR-10.7)."""
    when, words = rec["date"], f'User approval: "{rec["words"]}"'
    set_status(cand / "generation.md", f"approved and promoted to final.png on {when} "
               f"(journal/{rec['number']:03d}.json). {words}")
    for l in rec["layers"]:
        set_status(scene / "layers" / l["layer"] / l["version"] / "generation.md",
                   f"approved in Combined Image {cand.name} on {when} "
                   f"(journal/{rec['number']:03d}.json). {words}")


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (Fail, scene_state.Fail) as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
