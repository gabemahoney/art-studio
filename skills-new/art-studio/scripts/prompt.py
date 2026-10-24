#!/usr/bin/env python3
"""Assemble a generation prompt in the order rules.md mandates.

Style must dominate, so the order is fixed and not up to whoever is typing:

  1. Style Block, verbatim from style.md      (One Rule #2)
  2. image role declarations, by NUMBER       (rules.md, image input roles)
  3. design text — what the subject IS
  4. scene / layout / framing spec
  5. closing style line, verbatim             (One Rule #3)

Writing prompts by hand is how the Style Block drifts and how the closing line
gets paraphrased. Build them here instead; bin/gen.py then re-validates the
result and refuses anything malformed.

  python3 bin/prompt.py \
      --role STYLE:"Match its hand-painted matte rendering technique only." \
      --role IDENTITY:"Copy this subject's design exactly. Ignore its sheet layout." \
      --design-from assets/people/alice/description.md \
      --spec-file /tmp/framing.txt \
      -o /tmp/prompt.txt

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
ROLE_HINTS = {
    "STYLE": "Match this image's rendering technique only. Ignore its people, "
             "clothing, equipment, and setting.",
    "IDENTITY": "Copy this asset's design: face, build, clothing, equipment, "
                "colors. Ignore this image's rendering.",
    "EDIT TARGET": "This is the image being modified. Preserve everything the "
                   "prompt does not change.",
}


class Fail(Exception):
    pass


def read_or_fail(path: Path, flag: str) -> str:
    if not path.exists():
        raise Fail(f"{flag}: no such file: {path}")
    return path.read_text().strip()


def style_parts(masked: bool = False) -> tuple[str, str]:
    """(Style Block, closing style line) — style.md is the single authority.

    A masked call puts the EDIT TARGET in image 1, so its closing line names the
    anchor by ROLE instead of by index; an index would point at the image being
    repainted."""
    text = (ROOT / "style.md").read_text()
    block = re.search(r"## Style Block.*?\n\n(.*?)\n\n## Closing style line",
                      text, re.S)
    if masked:
        closing = re.search(
            r"## Closing style line for masked calls.*?\n\n(>.*?)\n\n", text, re.S)
        missing = "masked-call closing style line"
    else:
        closing = re.search(r"## Closing style line.*?\n\n(.*?)\n\n", text, re.S)
        missing = "Style Block or closing style line"
    if not block or not closing:
        raise Fail(f"style.md is missing its {missing}")
    unquote = lambda s: "\n".join(re.sub(r"^>\s?", "", l) for l in s.splitlines())
    return unquote(block.group(1)).strip(), " ".join(
        unquote(closing.group(1)).split()
    )


def design_text(path: Path, section: str | None) -> tuple[str, str]:
    """(design prose, version) from an asset's description.md, optionally one section."""
    if not path.exists():
        raise Fail(f"no such description: {path}")
    text = path.read_text()
    version = re.search(r"\*\*Description version:\s*(v\d+)\*\*", text)
    if section:
        m = re.search(rf"^##\s+{re.escape(section)}\s*$(.*?)(?=^##\s|\Z)",
                      text, re.S | re.M)
        if not m:
            raise Fail(f"{path.name} has no '## {section}' section")
        body = m.group(1)
    else:
        body = re.sub(r"^#.*$", "", text, count=1, flags=re.M)
    body = re.sub(r"^\*\*Description version.*$", "", body, flags=re.M).strip()
    return body, (version.group(1) if version else "unversioned")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--role", action="append", default=[], metavar="ROLE:TEXT",
                   help="repeatable, IN ATTACHMENT ORDER; becomes 'Image N is "
                        "ROLE: TEXT'. Image 1 must be STYLE. Omit TEXT for the "
                        "standard wording from rules.md")
    p.add_argument("--task", help="one line stating what to produce")
    p.add_argument("--design-from", metavar="PATH",
                   help="an asset description.md to quote design text from")
    p.add_argument("--design-section", metavar="NAME",
                   help="only this '## section' of the description")
    p.add_argument("--design-file", metavar="PATH",
                   help="design text from an arbitrary file instead")
    p.add_argument("--spec-file", metavar="PATH",
                   help="scene / layout / framing spec (the variable part)")
    p.add_argument("--masked", action="store_true",
                   help="build a prompt for a masked API call: image 1 must be the "
                        "EDIT TARGET, and the closing style line names the anchor by "
                        "role rather than by index")
    p.add_argument("-o", "--out", metavar="PATH", help="write here instead of stdout")
    args = p.parse_args()

    block, closing = style_parts(args.masked)
    chunks = [block]

    if args.role:
        roles = []
        for i, spec in enumerate(args.role, start=1):
            role, _, text = spec.partition(":")
            role = role.strip().upper()
            if role not in ROLE_HINTS:
                raise Fail(f"unknown role {role!r}; use "
                           f"{', '.join(ROLE_HINTS)}")
            if i == 1 and role != ("EDIT TARGET" if args.masked else "STYLE"):
                raise Fail(
                    "image 1 must be EDIT TARGET for a --masked prompt (the API "
                    "repaints image 1)" if args.masked else
                    "image 1 must be STYLE (One Rule #1)")
            roles.append(f"Image {i} is {role}: {text.strip() or ROLE_HINTS[role]}")
        chunks.append("\n".join(roles))

    if args.task:
        chunks.append(f"TASK: {args.task.strip()}")

    if args.design_from and args.design_file:
        raise Fail("pass --design-from or --design-file, not both")
    if args.design_from:
        body, version = design_text(ROOT / args.design_from, args.design_section)
        chunks.append(f"SUBJECT DESIGN (description {version}, restated so "
                      f"nothing is invented):\n{body}")
    elif args.design_file:
        chunks.append(read_or_fail(Path(args.design_file), "--design-file"))

    if args.spec_file:
        chunks.append(read_or_fail(Path(args.spec_file), "--spec-file"))

    chunks.append(closing)
    out = "\n\n".join(c.strip() for c in chunks if c.strip()) + "\n"

    if args.out:
        Path(args.out).write_text(out)
        print(f"  wrote {args.out}  ({len(out.split())} words)", file=sys.stderr)
    else:
        sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Fail as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
