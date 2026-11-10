#!/usr/bin/env python3
"""Plan a scene as single or layered, combine its Layers, and report its state. Calls
no image model.

Every scene starts with a Layer Plan the User confirmed: single (made as one image,
as before) or layered (a Frame and two or more Layers, bottom to top). The plan is a
record in the scene's Scene Journal, OUT/<scene>/journal/NNN.json, so any later
session reads it from the output folder alone. gen.py --layer makes each Layer's
versions; combine stacks them into the scene's next vNNN/, a Combined Image, and
rebuild checks one against its receipt.

  python3 scripts/layers.py plan --package ~/my-art --output ~/book/art \
      --scene harbour --frame 1536x1024 \
      --layer sky="Sky and distant hills" --layer boats="The two fishing boats" \
      --dry-run
  python3 scripts/layers.py plan ... --confirmation "Yes, those two layers." --based-on 0
  python3 scripts/layers.py combine --package ~/my-art --output ~/book/art \
      --scene harbour --use boats=v002 --preset book-float
  python3 scripts/layers.py rebuild ... --scene harbour --combined v003
  python3 scripts/layers.py keep ... --scene harbour --layer boats --version v002 \
      --words "Close. Keep that one, but bluer." --based-on 4
  python3 scripts/layers.py check-delete ... --scene harbour ~/book/art/harbour/layers/boats/v001
  python3 scripts/layers.py status --package ~/my-art --output ~/book/art --scene harbour

promote.py approves a Layer Version or a Combined Image; it, keep and plan are the
commands that write the Scene Journal.

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
import shlex
import shutil
import subprocess
import tempfile
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
    if cur is not None and not changes:
        raise Fail(f"plan unchanged; nothing recorded: the proposal says the same as the "
                   f"current plan, journal/{cur['number']:03d}.json.")

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


# ---------------------------------------------------------- keep, check-delete


def cmd_keep(args) -> int:
    """SR-8.3: record that the User keeps a Layer Version, making it the Layer's
    Default Version (SR-8.5) without approving it."""
    if not args.dry_run and args.based_on is None:
        raise Fail("--based-on is required: the journal number the dry run printed, "
                   "so a decision is never recorded against a state the User wasn't shown")
    if not args.words.strip():
        raise Fail("--words is required: the User's words keeping this version, verbatim")
    scene = scene_dir(args)
    records = scene_state.read_journal(scene)                   # read
    view = scene_state.layered_view(records)
    versions = scene_layers(scene, view["plan"], [args.layer])[args.layer]
    v = scene_state.check_keep(view, args.layer, versions, args.version)   # check
    if trouble := scene_state.problem(v["dir"], gen.deleted_numbers):
        raise Fail(f"Layer {args.layer}'s {v['name']} can't be kept: "
                   f"{gen.rel_of(v['dir'] / 'image.png')} is {trouble}; "
                   f"{gen.rel_of(v['dir'] / 'generation.md')} names it.")
    if trouble := scene_state.journal_problem(records, args.layer, v["dir"]):
        raise Fail(f"Layer {args.layer}'s {v['name']} can't be kept: "
                   f"{gen.rel_of(v['dir'] / 'image.png')} is {trouble}.")
    st = scene_state.layer_state(view, args.layer, versions)
    if st["kept"] is not None and st["kept"]["number"] == v["number"]:
        raise Fail(f"Layer {args.layer}'s {v['name']} is already kept "
                   f"(journal/{st['keep']['number']:03d}.json); nothing recorded.")

    print(f"  scene {args.scene}: keep Layer {args.layer}'s {v['name']}. It becomes the "
          "Layer's Default Version, without approving it, until a version of the Layer is "
          "approved, another is kept, its Layer Entry changes or the Layer is removed.")
    if st["keep"]:
        print(f"  this ends the keep of {st['keep']['version']} "
              f"(journal/{st['keep']['number']:03d}.json)")
    if args.dry_run:
        print(f"  dry run: nothing written. To record the User's words, pass --based-on "
              f"{view['latest']}.")
        return 0
    scene_state.check_based_on(records, args.based_on)
    gen.writable_base(scene_state.journal_dir(scene))
    dest = scene_state.publish(scene, {                         # publish
        "number": view["latest"] + 1, "kind": "keep", "date": date.today().isoformat(),
        "words": args.words, "layer": args.layer, "version": v["name"],
        "md5": scene_state.md5(v["dir"] / "image.png")})
    print(f"  wrote {dest}")
    return 0


def cmd_check_delete(args) -> int:
    """SR-11.1: whether a Layer Version, Draft or Combined Image folder may be deleted.
    A Layer's Approved Layer Version, a version any Combined Image's receipt names, and
    the scene's approved Combined Image never may, even if the User insists."""
    scene = scene_dir(args)
    records, plan = layered_plan(scene, "check")
    folder = Path(args.folder).expanduser().resolve()
    what = scene_state.classify(scene, folder / "image.png")
    if not what or what["kind"] not in ("layer", "draft", "combined") or what["dir"] != folder:
        raise Fail(f"{args.folder} is not one of scene {args.scene}'s Layer Version, Draft or "
                   "Combined Image folders.")
    view, notes = scene_state.journal_view(records), []
    if int(folder.name[1:]) in gen.deleted_numbers(folder.parent):
        print(f"  {gen.rel_of(folder)} is already deleted (its deletion log records it)")
        return 0
    if not folder.is_dir():
        raise Fail(f"{gen.rel_of(folder)} doesn't exist, so there is nothing to delete.")
    if what["kind"] == "layer":
        lid = what["layer"]
        st = scene_state.layer_state(view, lid, scene_layers(scene, plan, [lid])[lid])
        why = []
        if st["approval"] and scene_state.named_versions(st["approval"])[lid] == folder.name:
            why.append(f"it is Layer {lid}'s Approved Layer Version (journal/"
                       f"{st['approval']['number']:03d}.json; counting or not)")
        users = [c["name"] for c in scene_state.folders(scene, gen.deleted_numbers)
                 if not c["deleted"] and any(
                     s["path"] == gen.rel_of(folder)
                     for s in scene_state.read_receipt(c["dir"]).get("stack", []))]
        if users:
            why.append("the receipts of Combined Images " + ", ".join(users) + " name it")
        if why:
            raise Fail(f"{gen.rel_of(folder)} may not be deleted, even if the User insists: "
                       + "; and ".join(why) + ".")
        if st["keep"] and st["keep"]["version"] == folder.name:
            notes.append(f"deleting it ends its keep (journal/{st['keep']['number']:03d}.json)")
    elif what["kind"] == "combined" and view["scene_approval"] and \
            view["scene_approval"]["combined"] == gen.rel_of(folder):
        raise Fail(f"{gen.rel_of(folder)} may not be deleted, even if the User insists: it is "
                   f"the scene's approved image (journal/"
                   f"{view['scene_approval']['number']:03d}.json), from which final.png and "
                   "final-layers/ are completed.")
    print(f"  {gen.rel_of(folder)} may be deleted under today's rule, only if the User insists "
          f"after being warned: log it as {folder.name} in {gen.rel_of(folder.parent)}/DELETED.md")
    for n in notes:
        print(f"  note: {n}")
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
        if plan["layered"]:
            print("\n".join(layered_status(scene, records, plan)))
    print(f"  journal: latest record {scene_state.latest(records)}; pass "
          f"--based-on {scene_state.latest(records)} to a command recording a decision "
          "the User makes on this state")
    return 0


WHY = {"kept": "kept", "approved": "its Approved Layer Version",
       "latest": "its latest version"}


def journal_ref(rec: dict) -> str:
    return f"journal/{rec['number']:03d}.json, {rec['date']}: {scene_state.norm(rec['words'])}"


def layered_status(scene: Path, records: list[dict], plan: dict) -> list[str]:
    """SR-12.1: each Layer's versions, whether each counts and why not, its approval,
    keep and Default Version; removed Layers; the Drafts; the Combined Images, which
    can be approved, and the approved one; and every integrity problem."""
    lines, problems = ["  Layers, bottom to top:"], []
    rel = lambda p: str(Path(p).relative_to(scene))
    view = scene_state.journal_view(records)
    current = [l["id"] for l in plan["layers"]]
    gone = [lid for lid in view["ever"] if lid not in current]
    layers = scene_layers(scene, plan, current + gone)
    for lid, versions in layers.items():
        removed = lid in gone
        if gone and lid == gone[0]:
            lines.append("  removed Layers:")
        lines.append(f"    {lid}:" + ("" if versions else " no versions yet"))
        for v in versions:
            lines.append(f"      {v['name']}  " + ("counts" if v["counts"] else
                         "doesn't count: " + "; ".join(v["why_not"])))
            if not v["deleted"] and (trouble := scene_state.problem(v["dir"], gen.deleted_numbers)
                                     or scene_state.journal_problem(records, lid, v["dir"])):
                problems.append(f"{rel(v['dir'] / 'image.png')} is {trouble}")
        st = scene_state.layer_state(view, lid, versions)
        for what, rec, there in (("approval", st["approval"], st["approved"]),
                                 ("keep", st["keep"], st["kept"])):
            if rec and there is None:
                problems.append(f"journal/{rec['number']:03d}.json ({what}) names {lid} "
                                f"{scene_state.named_versions(rec)[lid]}, whose folder is gone")
        if st["approval"]:
            name = scene_state.named_versions(st["approval"])[lid]
            approved = name + ("" if st["approved"] is None or st["approved"]["counts"]
                               else " (doesn't count)") + (" (its folder is gone)"
                                                           if st["approved"] is None else "")
        else:
            approved = "none"
        if not removed and versions:
            d = st["default"]
            lines.append("      Default Version: " + (f"{d['name']} ({WHY[st['default_why']]})"
                         if d else "none (no counting version)")
                         + f"; Approved Layer Version: {approved}")
        elif removed:
            lines.append(f"      Approved Layer Version: {approved}")
        if st["approval"]:
            lines.append(f"      approved in {journal_ref(st['approval'])}")
        if st["keep"]:
            lines.append(f"      kept: {st['keep']['version']} in {journal_ref(st['keep'])}")
        if not removed and st["latest"] and st["default"] is not st["latest"]:
            lines.append(f"      its newest counting version, {st['latest']['name']}, isn't its "
                         "Default Version: before a step that doesn't revise this Layer, ask "
                         "the User whether to keep it")
    drafts = scene_state.folders(scene / "drafts", gen.deleted_numbers)
    lines.append("  Drafts:" + (" none" if not drafts else ""))
    for d in drafts:
        size = None if d["deleted"] else scene_state.sized(d["dir"], gen.identify)
        lines.append(f"    {d['name']}  " + (
            "deleted" if d["deleted"] else "image.png missing or unreadable" if size is None
            else f"{size[0]}x{size[1]}" + ("" if scene_state.ratio_matches(size, plan["frame"])
                                            else ", not the Frame's aspect ratio")))
        if not d["deleted"] and (trouble := scene_state.problem(d["dir"], gen.deleted_numbers)):
            problems.append(f"{rel(d['dir'] / 'image.png')} is {trouble}")
    combined = scene_state.folders(scene, gen.deleted_numbers)
    lines.append("  Combined Images:" + (" none" if not combined else ""))
    approvable = []
    for c in combined:
        if c["deleted"]:
            lines.append(f"    {c['name']}  deleted")
            continue
        rec = scene_state.read_receipt(c["dir"])
        stack = rec.get("stack", [])
        problems += [f"{c['name']}'s receipt has a Stack line that can't be read: {bad!r}"
                     for bad in rec.get("stack_errors", [])]
        lines.append(f"    {c['name']}  " + (", ".join(
            f"{s['layer']} {s['path'].rsplit('/', 1)[-1]}" for s in stack) or "no Stack recorded"))
        sound = not rec.get("stack_errors") and rec.get("Kind") == "Combined Image"
        if trouble := scene_state.problem(c["dir"], gen.deleted_numbers):
            problems.append(f"{rel(c['dir'] / 'image.png')} is {trouble}")
            sound = False
        for s in stack:
            if trouble := stack_problem(scene, s):
                problems.append(f"{c['name']}'s Stack line {s['position']} names "
                                f"{s['path']}, which {trouble}")
                sound = False
        if sound and stack:
            try:
                replaces = scene_state.check_scene_approval(view, layers, scene_state.stack_of(rec),
                                                               True)
            except scene_state.Fail:
                continue
            named = ([f"the approved image {replaces['scene']['combined'].rsplit('/', 1)[-1]}"]
                     if replaces["scene"] else []) + [
                f"{l['layer']} {l['version']}" for l in replaces["layers"]]
            approvable.append(c["name"] + (f" (with --replace: replaces {', '.join(named)})"
                                           if named else ""))
    lines.append("  can be approved now: " + (", ".join(approvable) or "none"))
    sa = view["scene_approval"]
    if sa is None:
        lines.append("  approved image: none")
    else:
        lines.append(f"  approved image: {sa['combined'].rsplit('/', 1)[-1]}, approved in "
                     f"{journal_ref(sa)}")
        lines += [f"    final-layers/{name}: {l['layer']} {l['version']}"
                  for name, l in scene_state.layer_files(sa)]
        problems += [f"{m}: run promote.py on {sa['combined'].rsplit('/', 1)[-1]} to complete "
                     f"the copies from journal/{sa['number']:03d}.json"
                     for m in scene_state.copies_mismatch(scene, sa)]
    lines.append("  integrity problems:" + (" none" if not problems else ""))
    lines += [f"    {p}" for p in problems]
    return lines


def stack_problem(scene: Path, s: dict) -> str | None:
    """Why a Combined Image's stack line can't be rebuilt from (SR-1.8), or None."""
    vdir = (gen.OUT / s["path"].removeprefix("output:")).resolve()
    what = scene_state.classify(scene, vdir / "image.png")
    if not s["path"].startswith("output:") or not what or what["kind"] != "layer":
        return "is not one of this scene's Layer Versions"
    if int(vdir.name[1:]) in gen.deleted_numbers(vdir.parent):
        return "is deleted (its deletion log records it)"
    if not (vdir / "image.png").is_file():
        return "is missing (image.png is gone)"
    if scene_state.md5(vdir / "image.png") != s["md5"]:
        return f"is altered (its image.png's md5 isn't the {s['md5']} the Stack records)"
    return None


# ------------------------------------------------------------------- combine


def scene_layers(scene: Path, plan: dict, ids: list[str] | None = None) -> dict[str, list[dict]]:
    """Each Layer's assessed versions: the current plan's Layers, or the ids given."""
    return {lid: scene_state.layer_versions(scene, lid, plan, gen.deleted_numbers, gen.identify)
            for lid in (ids if ids is not None else [l["id"] for l in plan["layers"]])}


def layered_plan(scene: Path, command: str) -> tuple[list[dict], dict]:
    records = scene_state.read_journal(scene)
    plan = scene_state.current_plan(records)
    if not (plan and plan["layered"]):
        raise Fail(f"scene {scene.name} is not a Layered Scene ({scene_state.describe(plan)}), "
                   f"so it has no Layers to {command}.")
    return records, plan


def stack_command(frame: dict, images: list[Path], dest: Path) -> list[str]:
    """SR-7.5: a fully transparent canvas of the Frame's pixel size, with each Layer
    Version composited over it from the bottom with Over and nothing else. The PNG
    leaves out its date chunks, so the same stack writes the same bytes. Each input is
    read as PNG only (png:), so a file posing as one can't make ImageMagick read
    another format, such as an SVG that pulls in files from elsewhere."""
    cmd = ["magick", "-size", scene_state.frame_text(frame), "xc:none"]
    for image in images:
        cmd += [f"png:{image}", "-compose", "Over", "-composite"]
    return cmd + ["-depth", "8", "-define", "png:color-type=6",
                  "-define", "png:exclude-chunks=date,time", str(dest)]


def shown(cmd: list[str], dest: Path, final: Path) -> str:
    """The command as a receipt records it: paths written as output:<rel>."""
    return shlex.join(gen.rel_of(final) if a == str(dest) else
                      "png:" + gen.rel_of(Path(a[4:])) if a.startswith("png:/") else a
                      for a in cmd)


def run_stack(cmd: list[str]) -> None:
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)   # no shell
    except subprocess.CalledProcessError as e:
        raise Fail("ImageMagick could not stack the Layer Versions, so nothing was "
                   f"written: {e.stderr.strip()[-300:]}") from None


def imagemagick_version() -> str:
    m = re.search(r"ImageMagick (\S+ \S+)", gen.magick("-version"))
    return m.group(1) if m else "unknown"


def signature(image: Path) -> str:
    return gen.magick("identify", "-format", "%#", image).strip()


def opaque_everywhere(image: Path) -> bool:
    """SR-7.7: no pixel's alpha is below 0.98, so a haze Layer that is partly
    transparent everywhere doesn't count."""
    return not gen.has_alpha(image) or gen.fx(image, "minima", "-alpha", "extract") >= 0.98


def cmd_combine(args) -> int:
    scene = scene_dir(args)
    records, plan = layered_plan(scene, "combine")
    ids, frame = [l["id"] for l in plan["layers"]], plan["frame"]
    current = {l["id"]: l["entry"] for l in plan["layers"]}

    def in_plan(lid: str, flag: str) -> str:
        if lid not in ids:
            raise Fail(f"{flag}: Layer {lid!r} is not in the current Layer Plan "
                       f"(journal/{plan['number']:03d}.json), which holds, bottom to top: "
                       f"{', '.join(ids)}.")
        return lid

    use = {}
    for spec in args.use:
        m = re.fullmatch(r"([^=\s]+)=v(\d+)", spec.strip())
        if not m:
            raise Fail(f"--use {spec!r}: name a version as ID=vNNN, e.g. planet=v002")
        if in_plan(m.group(1), "--use") in use:
            raise Fail(f"--use names Layer {m.group(1)} twice")
        use[m.group(1)] = int(m.group(2))
    only = None
    if args.only is not None:
        only = [in_plan(lid.strip(), "--only") for lid in args.only.split(",") if lid.strip()]
        if not only:
            raise Fail("--only names no Layer; give a comma-separated list of Layer IDs")
        if outside := [lid for lid in use if lid not in only]:
            raise Fail(f"--use names {', '.join(outside)}, which --only leaves out")

    spec = {}
    if args.preset:
        known = gen.presets()
        if args.preset not in known:
            raise Fail(f"no preset {args.preset!r} in {gen.PKG / 'presets.json'}; "
                       f"known: {', '.join(sorted(known)) or 'none'}")
        spec = known[args.preset]
    final_size = args.final_size or spec.get("final_size")
    m = final_size and re.fullmatch(r"(\d+)x(\d+)", final_size.strip().lower())
    if final_size and not (m and int(m.group(1)) and int(m.group(2))):
        raise Fail(f"--final-size {final_size!r}: give WxH in pixels, e.g. 1536x1024")
    flatten = args.flatten or spec.get("flatten") or gen.DEFAULT_FLATTEN
    max_mb = args.max_mb if args.max_mb is not None else spec.get("max_mb", gen.DEFAULT_MAX_MB)

    # the stack: each chosen current Layer in the current order, at its named version
    # or its Default Version; a Layer with no counting version is left out
    layers, stack, left_out = scene_layers(scene, plan), [], []
    view, approved = scene_state.journal_view(records), {}
    for lid in ids:
        if only is not None and lid not in only:
            continue
        st = scene_state.layer_state(view, lid, layers[lid])
        approved[lid] = st["approved"]
        if lid in use:
            v = next((v for v in layers[lid] if v["number"] == use[lid]), None)
            if v is None:
                raise Fail(f"--use {lid}=v{use[lid]:03d}: Layer {lid} has no such version "
                           "(layers.py status lists them)")
        else:
            v = st["default"]
            if v is None:
                left_out.append(lid)
                continue
        stack.append(v)
    is_approved = lambda v: (approved[v["layer"]] is not None
                             and approved[v["layer"]]["number"] == v["number"])
    if not stack:
        raise Fail("no Layer " + ("--only names" if only else "of the current plan")
                   + " has a counting version, so there is nothing to combine. Generate "
                   "the Layers first (gen.py --layer).")
    for v in stack:
        image = v["dir"] / "image.png"
        if trouble := scene_state.problem(v["dir"], gen.deleted_numbers):
            raise Fail(f"Layer {v['layer']}'s {v['name']} can't be combined: "
                       f"{gen.rel_of(image)} is {trouble}; "
                       f"{gen.rel_of(v['dir'] / 'generation.md')} names it.")
        if trouble := scene_state.journal_problem(records, v["layer"], v["dir"]):
            raise Fail(f"Layer {v['layer']}'s {v['name']} can't be combined: "
                       f"{gen.rel_of(image)} is {trouble}.")
        if v["size"] != (frame["width"], frame["height"]):
            w, h = v["size"]
            raise Fail(f"Layer {v['layer']}'s {v['name']} is {w}x{h}, which "
                       + ("doesn't match the Frame's aspect ratio" if not
                          scene_state.ratio_matches(v["size"], frame) else
                          "isn't the Frame's pixel size")
                       + f" ({scene_state.frame_text(frame)}); it can't be combined.")

    styles = {v["layer"]: scene_state.read_receipt(v["dir"]).get("Style", "unknown")
              for v in stack}
    warnings = []
    if len(set(styles.values())) > 1:
        warnings.append("the Layers were made under different style versions: "
                        + ", ".join(f"{lid} {s}" for lid, s in styles.items()))
    for v in stack[1:]:
        if opaque_everywhere(v["dir"] / "image.png"):
            warnings.append(f"Layer {v['layer']} ({v['name']}) is opaque everywhere, so it "
                            "hides every Layer beneath it")

    print(f"  scene {args.scene}: Combined Image, Frame {scene_state.frame_text(frame)}, "
          "bottom to top:")
    for i, v in enumerate(stack, start=1):
        how = ("named with --use" if v["layer"] in use else "its Default Version")
        print(f"    {i:2} {v['layer']} {v['name']}  ({how}; "
              + ("its" if is_approved(v) else "not its") + " Approved Layer Version"
              + ("" if v["counts"] else "; doesn't count: " + "; ".join(v["why_not"])) + ")")
    if left_out:
        print(f"    left out, with no counting version: {', '.join(left_out)}")
    for w in warnings:
        print(f"  warn: {w}", file=sys.stderr)
    if args.dry_run:
        print("  dry run: nothing built or written")
        return 0

    gen.require_binary("magick", "install ImageMagick (brew install imagemagick)")
    gen.writable_base(scene)
    deleted = gen.deleted_numbers(scene)
    with tempfile.TemporaryDirectory(prefix="layers-combine-") as tmp:
        built = Path(tmp) / "image.png"
        cmd = stack_command(frame, [v["dir"] / "image.png" for v in stack], built)
        run_stack(cmd)
        out = gen.target_dir(scene, deleted)
        image = out / "image.png"
        shutil.copyfile(built, image)
    print(f"  wrote {image}")

    # the receipt first, so a Combined Image never stands without one; the
    # deliverable is then recorded on it as gen.py --refinish records one
    free = lambda text: scene_state.norm(text or "TODO — fill in")
    lines = [
        f"# {args.scene} {out.name}",
        "",
        "No image model was called: layers.py combine stacked recorded Layer Versions "
        "with ImageMagick.",
        f"User request verbatim: {free(args.request)}",
        f"Mode: {free(args.mode)}",
        "Tool: art-studio layers.py combine (ImageMagick only)",
        f"Package: {gen.PKG}",
        f"Output folder: {gen.OUT}",
        "Kind: Combined Image",
        f"Layer Plan: journal/{plan['number']:03d}.json",
        f"Frame: {scene_state.frame_text(frame)}",
        "Stack:",
        *(f"{i}. {v['layer']} {gen.rel_of(v['dir'])} "
          f"md5={scene_state.md5(v['dir'] / 'image.png')} style={styles[v['layer']]} "
          f"approved={'yes' if is_approved(v) else 'no'} removed=no "
          f"entry={scene_state.norm(v['entry'] or '')}"
          for i, v in enumerate(stack, start=1)),
        f"ImageMagick: {imagemagick_version()}",
        f"Command: {shown(cmd, built, image)}",
        f"Pixel signature: {signature(image)}",
        f"md5: {scene_state.md5(image)}",
        f"Date: {date.today().isoformat()}",
        "Status: awaiting user evaluation",
        f"Output: image.png, {scene_state.frame_text(frame)} (the Combined Image, frozen)",
        "Review: pending — record with review.py once you have seen it",
        *(f"Warning: {w}" for w in warnings),
        "",
    ]
    (out / "generation.md").write_text("\n".join(lines))
    print(f"  wrote {out / 'generation.md'}")
    if final_size:
        dest, delivered = gen.finish(image, final_size, flatten, max_mb)
        gen.record_delivered(out / "generation.md", delivered)
        print(f"  wrote {dest}  ({delivered})")
    return 0


# ------------------------------------------------------------------- rebuild


def cmd_rebuild(args) -> int:
    scene = scene_dir(args)
    layered_plan(scene, "rebuild")
    if not re.fullmatch(r"v\d+", args.combined):
        raise Fail(f"--combined {args.combined!r}: name the Combined Image's folder, e.g. v003")
    folder = scene / args.combined
    receipt = scene_state.read_receipt(folder)
    if receipt.get("Kind") != "Combined Image":
        raise Fail(f"{gen.rel_of(folder)} holds no Combined Image receipt "
                   "(Kind: Combined Image), so there is nothing to rebuild from.")
    named = gen.rel_of(folder / "generation.md")
    if not re.fullmatch(r"\d+x\d+", receipt.get("Frame", "")):
        raise Fail(f"{named} records no Frame as WxH, so there is nothing to rebuild from")
    frame = parse_frame(receipt["Frame"])
    if receipt["stack_errors"]:
        raise Fail(f"{named} has a Stack line rebuild can't read: "
                   f"{receipt['stack_errors'][0]!r}")
    if not receipt["stack"]:
        raise Fail(f"{named} records no Stack lines")
    images = []
    for s in receipt["stack"]:
        if trouble := stack_problem(scene, s):
            raise Fail(f"{gen.rel_of(folder / 'generation.md')}'s Stack line {s['position']} "
                       f"names {s['path']}, which {trouble}; rebuild reads only this scene's "
                       "unaltered Layer Versions.")
        images.append(gen.OUT / s["path"].removeprefix("output:") / "image.png")

    gen.require_binary("magick", "install ImageMagick (brew install imagemagick)")
    tmp = Path(tempfile.mkdtemp(prefix="layers-rebuild-")).resolve()
    try:
        if any(tmp.is_relative_to(p) for p in (gen.PKG, gen.OUT)):
            raise Fail(f"the scratch folder {tmp} lies inside the package or output folder; "
                       "set TMPDIR elsewhere")
        built = tmp / "image.png"
        cmd = stack_command(frame, images, built)   # built from checked fields only
        run_stack(cmd)
        got = signature(built)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print(f"  rebuilt {gen.rel_of(folder)} from its Frame and Stack in a scratch file:")
    for s in receipt["stack"]:
        print(f"    {s['position']:>2} {s['layer']} {s['path'].rsplit('/', 1)[-1]}")
    version, own = imagemagick_version(), shown(cmd, built, folder / "image.png")
    if version != receipt.get("ImageMagick"):
        print(f"  note: ImageMagick is {version}; the receipt records "
              f"{receipt.get('ImageMagick', 'none')}")
    if own != receipt.get("Command"):
        print("  note: the receipt's Command differs from the command rebuild built and ran "
              f"(rebuild never runs recorded text):\n    recorded: "
              f"{receipt.get('Command', 'none')}\n    built:    {own}")
    recorded = receipt.get("Pixel signature")
    if got == recorded:
        print(f"  pixel signature matches: {got}")
        return 0
    print(f"  MISMATCH: the rebuilt pixel signature is {got}; the receipt records "
          f"{recorded or 'none'}")
    return 1


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

    co = sub.add_parser("combine", parents=[common],
                        help="stack Layer Versions into the next Combined Image; calls no "
                             "image model")
    co.add_argument("--use", action="append", default=[], metavar="ID=vNNN",
                    help="this version of a Layer instead of its Default Version")
    co.add_argument("--only", metavar="ID,...", help="combine only these Layers")
    co.add_argument("--request", help="the User's request verbatim, for the receipt")
    co.add_argument("--mode", help="what this Combined Image shows, for the receipt")
    co.add_argument("--preset", metavar="NAME",
                    help="a delivery spec named in the package's presets.json")
    co.add_argument("--final-size", metavar="WxH", help="derive a deliverable of this size")
    co.add_argument("--flatten", help="the colour a deliverable is flattened onto "
                                      f"(default {gen.DEFAULT_FLATTEN})")
    co.add_argument("--max-mb", type=float,
                    help=f"warn if the deliverable exceeds this (default {gen.DEFAULT_MAX_MB})")
    co.add_argument("--dry-run", action="store_true",
                    help="print the stack and its warnings; build and write nothing")
    co.set_defaults(func=cmd_combine)

    kp = sub.add_parser("keep", parents=[common],
                        help="record that the User keeps a Layer Version: it becomes the "
                             "Layer's Default Version, not approved")
    kp.add_argument("--layer", required=True, metavar="ID")
    kp.add_argument("--version", required=True, metavar="vNNN")
    kp.add_argument("--words", required=True, metavar="WORDS",
                    help="the User's words keeping it, verbatim")
    kp.add_argument("--based-on", type=int, metavar="N",
                    help="the journal number the dry run printed (required unless --dry-run)")
    kp.add_argument("--dry-run", action="store_true", help="say what keeping does; write nothing")
    kp.set_defaults(func=cmd_keep)

    cd = sub.add_parser("check-delete", parents=[common],
                        help="report whether a Layer Version, Draft or Combined Image folder "
                             "may be deleted; writes nothing")
    cd.add_argument("folder", help="the vNNN folder")
    cd.set_defaults(func=cmd_check_delete)

    rb = sub.add_parser("rebuild", parents=[common],
                        help="rebuild a Combined Image from its receipt into a scratch file "
                             "and compare pixel signatures; writes nothing")
    rb.add_argument("--combined", required=True, metavar="vNNN")
    rb.set_defaults(func=cmd_rebuild)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (Fail, scene_state.Fail) as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
