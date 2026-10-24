#!/usr/bin/env python3
"""Record the post-generation assessment on a candidate's receipt.

A receipt is frozen history with exactly two exceptions, because both are known
only AFTER the run: `Status` (owned by bin/promote.py) and `Review` (owned by this
script). Everything else in generation.md is written once by bin/gen.py.

bin/gen.py cannot take the review — it runs before the image exists — so it leaves
a placeholder. Fill it here, once you have looked at the image:

  python3 bin/review.py outputs/antares-planet-beauty/v009 \
      --review "Near trail trimmed but now only modestly larger than the far one;
                hull definition and topside symmetry held from v007."

Stdlib only; no venv required.
"""

from __future__ import annotations

import sys

# A compiled copy of this file in __pycache__ is a copy that does not carry
# later changes — including the paid-call gate. Never leave one behind.
sys.dont_write_bytecode = True

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLACEHOLDERS = ("pending — record with bin/review.py", "TODO — fill in")


class Fail(Exception):
    pass


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("candidate", help="the vNNN directory whose receipt to annotate")
    p.add_argument("--review", required=True,
                   help="your honest assessment, including where it missed the brief")
    p.add_argument("--replace", action="store_true",
                   help="overwrite a review that has already been written")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    cand = (ROOT / args.candidate).resolve()
    if not re.fullmatch(r"v\d+", cand.name):
        raise Fail(f"{args.candidate} is not a vNNN candidate directory")
    receipt = cand / "generation.md"
    if not receipt.exists():
        raise Fail(f"{receipt.relative_to(ROOT)} does not exist")

    text = receipt.read_text()
    m = re.search(r"^Review:[ \t]*(.*)$", text, re.M)
    if not m:
        raise Fail(f"{receipt.relative_to(ROOT)} has no 'Review:' line. Hand-written "
                   "receipts predate bin/gen.py — add the line yourself, once.")
    existing = m.group(1).strip()
    if existing and not any(ph in existing for ph in PLACEHOLDERS) and not args.replace:
        raise Fail(f"{receipt.relative_to(ROOT)} already has a review:\n"
                   f"  {existing[:120]}\nPass --replace to overwrite it.")

    review = " ".join(args.review.split())
    if args.dry_run:
        print(f"  would set Review on {receipt.relative_to(ROOT)}:\n  {review[:150]}")
        return 0

    receipt.write_text(text[:m.start()] + f"Review: {review}" + text[m.end():])
    print(f"  updated {receipt.relative_to(ROOT)} Review line")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Fail as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
