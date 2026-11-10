#!/usr/bin/env python3
"""Plan a scene as single or layered, and report a scene's state. Calls no image model.

Every scene starts with a Layer Plan the User confirmed: single (made as one image,
as before) or layered (a Frame and two or more Layers, bottom to top). The plan is a
record in the scene's Scene Journal, OUT/<scene>/journal/NNN.json, so any later
session reads it from the output folder alone.

  python3 scripts/layers.py plan --package ~/my-art --output ~/book/art \
      --scene harbour --frame 1536x1024 \
      --layer sky="Sky and distant hills" --layer boats="The two fishing boats" \
      --dry-run
  python3 scripts/layers.py plan ... --confirmation "Yes, those two layers." --based-on 0
  python3 scripts/layers.py status --package ~/my-art --output ~/book/art --scene harbour

Every command that records a decision takes --based-on N: the journal number its dry
run printed, i.e. the state the User was shown. If the journal has moved on since,
the command refuses and the User is asked again.

Stdlib only; no venv required.
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import argparse
import re
from datetime import date
from pathlib import Path

# python3 -I leaves this script's folder off sys.path; gen and scene_state live beside it.
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
import gen  # noqa: E402
import scene_state  # noqa: E402
from gen import Fail  # noqa: E402


def scene_dir(args) -> Path:
    gen.set_locations(args.package, args.output)   # refuses an overlapping --output
    if not re.fullmatch(scene_state.SLUG, args.scene):
        raise Fail(f"scene slug {args.scene!r}: use lowercase letters, digits, . _ -")
    return gen.OUT / args.scene


def show_plan(plan: dict) -> list[str]:
    if not plan["layered"]:
        return ["    single: made as one image"]
    f = plan["frame"]
    lines = [f"    layered, Frame {f['width']}x{f['height']}; Layers bottom to top:"]
    for i, layer in enumerate(plan["layers"], start=1):
        lines.append(f"    {i:2} {layer['id']}: {scene_state.norm(layer['entry'])}")
    return lines


# ---------------------------------------------------------------------- plan


def parse_frame(text: str) -> dict:
    m = re.fullmatch(r"(\d+)x(\d+)", text.strip().lower())
    if not m or not int(m.group(1)) or not int(m.group(2)):
        raise Fail(f"--frame {text!r}: give the Frame as WxH in pixels, e.g. 1536x1024")
    return {"width": int(m.group(1)), "height": int(m.group(2))}


def proposal_from(args, records: list[dict]) -> dict:
    if args.single:
        if args.layer:
            raise Fail("--single takes no --layer: a single plan states no Layers")
        return {"layered": False}
    if not args.frame:
        raise Fail("give --single, or --frame WxH with one --layer ID=TEXT per Layer")
    layers = []
    for spec in args.layer:
        lid, sep, text = spec.partition("=")
        if not sep:
            raise Fail(f"--layer {spec!r}: use ID=TEXT, or ID=@N to copy Layer ID's "
                       "Layer Entry from plan record N")
        m = re.fullmatch(r"@(\d+)", text.strip())
        entry = scene_state.entry_from(records, int(m.group(1)), lid) if m else text
        layers.append({"id": lid, "entry": entry})
    return {"layered": True, "frame": parse_frame(args.frame), "layers": layers}


def cmd_plan(args) -> int:
    if not args.dry_run and args.based_on is None:
        raise Fail("--based-on is required: the journal number the dry run printed, "
                   "so a decision is never recorded against a state the User wasn't shown")
    if not args.dry_run and not (args.confirmation or "").strip():
        raise Fail("--confirmation is required: the User's confirmation of this plan, "
                   "verbatim")
    scene = scene_dir(args)
    records = scene_state.read_journal(scene)                   # read
    proposal = proposal_from(args, records)
    changes = scene_state.check_plan(                           # check
        records, proposal, scene_state.generated(scene, gen.deleted_numbers))
    cur = scene_state.current_plan(records)
    based_on = scene_state.latest(records)

    print(f"  scene {args.scene}: proposed Layer Plan")
    print("\n".join(show_plan(proposal)))
    if cur is not None:
        print(f"  changes from plan record {cur['number']}: "
              + ("; ".join(changes) or "none"))

    if args.dry_run:
        print(f"  dry run: nothing written. Show the User this proposal; to record "
              f"their confirmation, pass --based-on {based_on} and --confirmation.")
        return 0
    scene_state.check_based_on(records, args.based_on)
    gen.writable_base(scene_state.journal_dir(scene))

    record = {"number": based_on + 1, "kind": "plan", "date": date.today().isoformat(),
              "words": args.confirmation, **proposal}
    if cur is not None:
        record |= {"previous": cur["number"], "changes": changes}
    dest = scene_state.publish(scene, record,                   # publish
                               fallback=not proposal["layered"])
    print(f"  wrote {dest}")
    return 0


# -------------------------------------------------------------------- status


def cmd_status(args) -> int:
    scene = scene_dir(args)
    if not scene.is_dir():
        print(f"  scene {args.scene}: no folder at {scene}; no Layer Plan, nothing "
              "generated. Propose a Layer Plan before generating.")
        return 0
    records = scene_state.read_journal(scene)
    plan = scene_state.current_plan(records)
    made = scene_state.generated(scene, gen.deleted_numbers)
    if plan is None:
        print(f"  scene {args.scene}: {scene_state.describe(plan)}")
        print("    " + ("made as one image, as before Layer Plans" if made else
                        "nothing generated yet: propose a Layer Plan before generating"))
    else:
        print(f"  scene {args.scene}: {scene_state.describe(plan)} "
              f"(current plan: journal/{plan['number']:03d}.json, {plan['date']})")
        print("\n".join(show_plan(plan)))
        print(f"    confirmed: {scene_state.norm(plan['words'])}")
    print(f"  journal: latest record {scene_state.latest(records)}; pass "
          f"--based-on {scene_state.latest(records)} to a command recording a decision "
          "the User makes on this state")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="command", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--package", required=True, metavar="PKG")
    common.add_argument("--output", required=True, metavar="OUT")
    common.add_argument("--scene", required=True)

    pl = sub.add_parser("plan", parents=[common],
                        help="record the Layer Plan the User confirmed")
    kind = pl.add_mutually_exclusive_group(required=True)
    kind.add_argument("--single", action="store_true", help="made as one image")
    kind.add_argument("--frame", metavar="WxH", help="a layered plan's Frame, in pixels")
    pl.add_argument("--layer", action="append", default=[], metavar="ID=TEXT",
                    help="one per Layer, bottom to top; ID=@N copies Layer ID's Layer "
                         "Entry verbatim from plan record N")
    pl.add_argument("--confirmation", metavar="WORDS",
                    help="the User's confirmation, verbatim (required unless --dry-run)")
    pl.add_argument("--based-on", type=int, metavar="N",
                    help="the journal number the dry run printed (required unless "
                         "--dry-run)")
    pl.add_argument("--dry-run", action="store_true",
                    help="print the proposal and what it changes; write nothing")
    pl.set_defaults(func=cmd_plan)

    st = sub.add_parser("status", parents=[common],
                        help="report the scene's state; writes nothing")
    st.set_defaults(func=cmd_status)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (Fail, scene_state.Fail) as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
