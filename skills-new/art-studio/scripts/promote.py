#!/usr/bin/env python3
"""Promote an approved candidate to the head revision, with provenance.

Approval is the one step where the vault's invariants are easiest to break by
hand: copy the wrong file, forget the sidecar, or edit reference.png in place and
silently orphan its provenance. So do it here.

  assets/<type>/<slug>/candidates/vNNN/image.png  ->  reference.png + reference.md
  outputs/<scene>/vNNN/image.png                  ->  final.png    + final.md

Refuses to overwrite an existing head revision unless --replace is given, and
verifies byte-identity afterwards — the same check rules.md requires before any
reference may be attached to a generation.

  python3 bin/promote.py outputs/market-scene/v002 \
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
import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class Fail(Exception):
    pass


def md5(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def _gen():
    """gen.py owns the images-root config; import it rather than re-deriving it, so the
    two can never disagree about where an image lives."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("_gen_cfg", Path(__file__).resolve().parent / "gen.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


_G = _gen()
IMAGES, vpath, rel_of = _G.IMAGES, _G.vpath, _G.rel_of


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("candidate", help="the vNNN directory to promote")
    p.add_argument("--approval", help="the user's approval, verbatim, for the sidecar")
    p.add_argument("--replace", action="store_true",
                   help="allow overwriting an existing reference.png / final.png")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    rel = Path(args.candidate)
    if rel.is_absolute():
        rel = rel_of(rel)
    cand = ROOT / rel
    if not re.fullmatch(r"v\d+", rel.name):
        raise Fail(f"{args.candidate} is not a vNNN candidate directory")
    image, receipt = vpath(rel / "image.png"), ROOT / rel / "generation.md"
    for f in (image, receipt):
        if not f.exists():
            raise Fail(f"{rel_of(f)} is missing — candidate is incomplete"
                       + ("" if IMAGES == ROOT or f == receipt
                          else f" (images live in {IMAGES})"))
    if rel.parts[0] == "assets":
        if cand.parent.name != "candidates":
            raise Fail(f"expected assets/<type>/<slug>/candidates/vNNN, got {rel}")
        head_dir, head_name, sidecar_name = rel.parent.parent, "reference.png", "reference.md"
    elif rel.parts[0] == "outputs":
        head_dir, head_name, sidecar_name = rel.parent, "final.png", "final.md"
    else:
        raise Fail(f"{rel} is under neither assets/ nor outputs/")

    head, sidecar = vpath(head_dir / head_name), ROOT / head_dir / sidecar_name
    if head.exists() and not args.replace:
        prior = ""
        if sidecar.exists():
            m = re.search(r"candidates/(v\d+)|(?:^|/)(v\d+)", sidecar.read_text())
            prior = f" (currently from {m.group(0)})" if m else ""
        raise Fail(f"{rel_of(head)} already exists{prior}. "
                   "Pass --replace if the user approved superseding it.")

    # The candidate's own path, relative to where the sidecar will live, is what
    # rules.md's validation walks back down.
    provenance = str(rel.relative_to(head_dir))
    body = [
        f"Promoted from {provenance}",
        "",
        f"Date: {date.today().isoformat()}",
        f"md5: {md5(image)}",
    ]
    if args.approval:
        body.insert(1, f"User approval, verbatim: {args.approval}")

    if args.dry_run:
        print(f"  would write {rel_of(head)} from {rel}/image.png")
        print(f"  would write {rel_of(sidecar)}: Promoted from {provenance}")
        return 0

    shutil.copy2(image, head)
    sidecar.write_text("\n".join(body) + "\n")

    if md5(head) != md5(image):
        raise Fail("post-copy byte check FAILED — head revision does not match "
                   "the candidate. Do not attach this reference.")
    print(f"  wrote {rel_of(head)}  (byte-identical to {rel}/image.png)")
    print(f"  wrote {rel_of(sidecar)}")

    # Reflect approval back into the frozen receipt so status lives in one place.
    text = receipt.read_text()
    if "Status: awaiting user evaluation" in text:
        status = (f"Status: approved and promoted to {head_name} on "
                  f"{date.today().isoformat()}")
        if args.approval:
            status += f'. User approval: "{args.approval}"'
        receipt.write_text(text.replace("Status: awaiting user evaluation", status))
        print(f"  updated {rel_of(cand / 'generation.md')} status line")
    else:
        # Receipts written by hand (everything before bin/gen.py existed) use their
        # own wording, so there is nothing to rewrite. Say so — silently leaving a
        # promoted candidate reading as unapproved is worse than the extra line.
        print(f"  note: {rel_of(cand / 'generation.md')} has no "
              "'Status: awaiting user evaluation' line, so its status was NOT "
              "updated. Edit it by hand to record the approval.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Fail as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
