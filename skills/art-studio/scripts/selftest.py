#!/usr/bin/env python3
"""Exercise every guard in gen.py, prompt.py, review.py and promote.py without
generating anything.

  python3 -I scripts/selftest.py

Builds a throwaway package and output folder in a temp directory, so it needs no
real package and touches none. gen.py runs under --dry-run, or fails before any
call is made; no image is generated and nothing is billed. Run it after touching
anything in scripts/.

Each case asserts that a specific invariant FAILS CLOSED. A guard that stops firing
is a guard that has silently been removed.
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import os
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ANCHOR = "ref_images/style_references/canonical_style_reference.png"

STYLE_MD = """# Selftest style

**Style version: v1** (2026-01-01)

## Style Block (paste verbatim into every prompt)

> Flat test paint. Three values per surface.

## Closing style line (last line of every prompt)

> Render everything in image 1's test brush.

## Closing style line for masked calls

> Render the repainted region in the STYLE image's test brush.

## Legacy closing style lines

> Old wording of the test closing line.
"""


def sh(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def script(name: str, *args: str, stdin: str | None = None) -> tuple[int, str]:
    env = {k: v for k, v in os.environ.items() if k != "OPENAI_API_KEY"}
    p = subprocess.run([sys.executable, "-I", str(HERE / name), *args], input=stdin,
                       capture_output=True, text=True, env=env)
    return p.returncode, p.stdout + p.stderr


def magick(*args: str) -> None:
    subprocess.run(["magick", *args], check=True, capture_output=True)


def build_fixture(root: Path) -> tuple[Path, Path]:
    """A minimal valid package (anchor, one approved asset) and an output folder
    holding one scene version to edit."""
    pkg, out = root / "pkg", root / "out"
    (pkg / "ref_images/style_references").mkdir(parents=True)
    (pkg / "style_versions").mkdir()
    (pkg / "style.md").write_text(STYLE_MD)
    (pkg / "presets.json").write_text(
        '{"page": {"final_size": "1200x800", "flatten": "#000000", "max_mb": 2}}')
    magick("-size", "1536x1024", "xc:#557799", str(pkg / ANCHOR))
    shutil.copy(pkg / ANCHOR, pkg / "style_versions/canonical_style_reference-v1.png")
    shutil.copy(pkg / "style.md", pkg / "style_versions/style-v1.md")

    asset = pkg / "assets/people/tester"
    cand = asset / "candidates/v001"
    cand.mkdir(parents=True)
    (asset / "description.md").write_text(
        "# Tester\n\n**Description version: v1**\n\n## Look\n\nA plain grey figure.\n")
    magick("-size", "1024x1024", "xc:#888888", str(cand / "image.png"))
    (cand / "generation.md").write_text("# tester v001\n\nStatus: awaiting user evaluation\n"
                                        "Review: pending — record with review.py\n")
    shutil.copy(cand / "image.png", asset / "reference.png")
    (asset / "reference.md").write_text("Promoted from candidates/v001\n")

    scene = out / "scene-a/v001"
    scene.mkdir(parents=True)
    magick("-size", "1536x1024", "xc:#aa6633", str(scene / "image.png"))
    (scene / "generation.md").write_text("# scene-a v001\n\nStatus: awaiting user evaluation\n"
                                         "Review: pending — record with review.py\n")
    magick("-size", "1536x1024", "xc:#ab6633", str(out / "scene-a/v002.png"))
    return pkg, out


def main() -> int:
    if shutil.which("magick") is None:
        print("  skip: ImageMagick (magick) is not installed")
        return 1
    tmp = Path(tempfile.mkdtemp(prefix="art-studio-selftest-"))
    try:
        return run_checks(tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def run_checks(tmp: Path) -> int:
    pkg, out = build_fixture(tmp)
    P, O = ["--package", str(pkg)], ["--output", str(out)]
    spec = tmp / "spec.txt"
    spec.write_text("A single horizontal test frame.\n")

    def build(name: str, *args: str) -> Path:
        dest = tmp / name
        code, msg = script("prompt.py", *P, *args, "--spec-file", str(spec), "-o", str(dest))
        if code:
            raise SystemExit(f"  FAIL: could not build {name} with prompt.py:\n  {msg}")
        return dest

    prompt = build("p.txt", "--role", "STYLE:", "--role", "IDENTITY:",
                   "--design-from", "assets/people/tester/description.md")
    mprompt = build("pm.txt", "--masked", "--role", "EDIT TARGET:", "--role", "STYLE:")
    lprompt = tmp / "pl.txt"
    lines = prompt.read_text().rstrip().splitlines()
    lprompt.write_text("\n".join(lines[:-1] + ["Old wording of the test closing line."]) + "\n")
    noblock = tmp / "nb.txt"
    noblock.write_text("Just paint something.\nRender everything in image 1's test brush.\n")

    def mask(name: str, *draw: str, size: str = "1536x1024", alpha: bool = False) -> str:
        p = tmp / name
        magick("-size", size, "xc:black", "-fill", "white", *draw,
               *([] if alpha else ["-alpha", "off"]), str(p))
        if alpha:
            magick(str(p), "-alpha", "set", "-channel", "A", "-evaluate", "set", "50%",
                   str(p))
        return str(p)

    small = mask("small.png", "-draw", "rectangle 60,430 390,930")
    black = mask("black.png")
    big = mask("big.png", "-draw", "rectangle 0,0 1536,700")
    alpha = mask("alpha.png", "-draw", "rectangle 60,430 390,930", alpha=True)
    wrong = mask("wrong.png", size="800x600")

    scene = ["--scene", "scene-a"]
    base = P + O + scene + ["--prompt-file", str(prompt)]
    mbase = P + O + scene + ["--prompt-file", str(mprompt)]
    A = ["--attach", f"{ANCHOR}:STYLE"]
    I = ["--attach", "assets/people/tester/reference.png:IDENTITY"]
    T = ["--attach", "scene-a/v001/image.png:EDIT TARGET"]
    T2 = ["--attach", f"{out}/scene-a/v002.png:EDIT TARGET"]
    API, M, DRY = ["--backend", "api"], ["--mask", small], ["--dry-run"]

    cases = [
        # --- locations
        ("--package is required", ["--scene", "x", "--prompt-file", str(prompt)] + DRY,
         "--package"),
        ("a folder without style.md is not a package",
         ["--package", str(tmp)] + O + scene + ["--prompt-file", str(prompt)] + DRY,
         "not a package"),
        ("--scene needs --output", P + scene + ["--prompt-file", str(prompt)] + A + DRY,
         "needs --output"),
        ("--output inside the package refused",
         P + ["--output", str(pkg / "renders")] + scene + ["--prompt-file", str(prompt)]
         + A + DRY, "overlaps the package"),
        ("--output with --asset refused",
         P + O + ["--asset", "people/tester", "--prompt-file", str(prompt)] + A + DRY,
         "no meaning with --asset"),
        ("unknown asset refused",
         P + ["--asset", "people/nobody", "--prompt-file", str(prompt)] + A + DRY,
         "no such asset"),
        ("unknown preset refused", base + A + ["--preset", "nope"] + DRY, "no preset"),
        # --- One Rule
        ("anchor must be image 1 when unmasked", base + I + A + DRY, "One Rule #1"),
        ("no attachments refused", base + DRY, "anchor is mandatory"),
        ("Style Block must be in the prompt",
         P + O + scene + ["--prompt-file", str(noblock)] + A + DRY, "Style Block verbatim"),
        ("anchor may not be attached twice", base + A + A + DRY, "anchor attached twice"),
        ("more than five attachments refused",
         base + A + [x for _ in range(5) for x in I] + DRY, "at most FIVE"),
        ("dead codex model caught by --dry-run", base + A + ["--model", "gpt-5.6-terra"]
         + DRY, "cannot generate images"),
        # --- provenance
        ("tampered reference.png refused", None, "silent overwrite"),
        ("drifted anchor refused", None, "without a style version bump"),
        ("edited Style Block without a version bump refused", None, "without a version bump"),
        # --- masked calls
        ("anchor may not be image 1 of a masked call", mbase + A + T + API + M + DRY,
         "repaint the anchor"),
        ("anchor relabelled EDIT TARGET still refused",
         mbase + ["--attach", f"{ANCHOR}:EDIT TARGET"] + API + M + DRY, "repaint the anchor"),
        ("image 1 must carry role EDIT TARGET when masked",
         mbase + ["--attach", "scene-a/v001/image.png:IDENTITY"] + A + API + M + DRY,
         "EDIT TARGET as image 1"),
        ("only one EDIT TARGET on a masked call", mbase + T + T2 + A + API + M + DRY,
         "more than one EDIT TARGET"),
        ("anchor still required on a masked call", mbase + T + API + M + DRY,
         "must still attach the style anchor"),
        ("--size must match the masked image",
         mbase + T + A + API + ["--size", "1200x1500"] + M + DRY,
         "does not match the image being masked"),
        ("mask rejected on the codex backend", base + A + T + M + DRY,
         "only applies to --backend api"),
        ("mask with an alpha channel rejected", mbase + T + A + API + ["--mask", alpha] + DRY,
         "carries an alpha channel"),
        ("missing mask rejected", mbase + T + A + API + ["--mask", "/nonexistent.png"] + DRY,
         "no such mask"),
        ("all-black mask rejected", mbase + T + A + API + ["--mask", black] + DRY,
         "entirely black"),
        ("mask dimensions must match", mbase + T + A + API + ["--mask", wrong] + DRY,
         "they must match"),
        ("ordinary closing line refused on a masked call", base + T + A + API + M + DRY,
         "image being repainted"),
        ("masked closing line refused on an unmasked call", mbase + A + DRY, "not masked"),
        ("legacy closing line refused on a masked call",
         P + O + scene + ["--prompt-file", str(lprompt)] + T + A + API + M + DRY,
         "legacy closing style line"),
        # --- paid calls
        ("paid call needs --approved-by", mbase + T + A + API + M, "--approved-by"),
        ("large mask does not crash on scientific notation",
         mbase + T + A + API + ["--mask", big], "--approved-by"),
        ("--mask meaningless with --refinish",
         P + O + ["--refinish", str(out / "scene-a/v001"), "--final-size", "800x600"] + M,
         "no meaning with --refinish"),
    ]

    failures = checks = 0

    def report(name: str, ok: bool, detail: str = "") -> None:
        nonlocal failures, checks
        checks += 1
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")
        if not ok:
            failures += 1
            print("         " + detail.strip().replace("\n", "\n         ")[:400])

    ref = pkg / "assets/people/tester/reference.png"
    frozen = pkg / "style_versions/canonical_style_reference-v1.png"
    for name, args, expect in cases:
        if name == "tampered reference.png refused":
            saved = ref.read_bytes()
            magick("-size", "1024x1024", "xc:#898989", str(ref))
            code, msg = script("gen.py", *(base + A + I + DRY))
            ref.write_bytes(saved)
        elif name == "drifted anchor refused":
            saved = frozen.read_bytes()
            magick("-size", "1536x1024", "xc:#557798", str(frozen))
            code, msg = script("gen.py", *(base + A + DRY))
            frozen.write_bytes(saved)
        elif name.startswith("edited Style Block"):
            style = pkg / "style.md"
            saved = style.read_text()
            style.write_text(saved.replace("Three values", "Four values"))
            code, msg = script("gen.py", *(base + A + DRY))
            style.write_text(saved)
        else:
            code, msg = script("gen.py", *args)
        report(name, code != 0 and expect in msg, f"expected {expect!r}, exit {code}:\n{msg}")

    # --- positive controls: correct calls are accepted, and touch nothing
    before = sorted(p for p in tmp.rglob("*"))
    for name, args in [
        ("a correct scene render is accepted", base + A + I + ["--preset", "page"] + DRY),
        ("the same render into a second output folder is accepted",
         P + ["--output", str(tmp / "out2")] + scene + ["--prompt-file", str(prompt)]
         + A + I + DRY),
        ("a correct asset render is accepted",
         P + ["--asset", "people/tester", "--prompt-file", str(prompt)] + A + I + DRY),
        ("a correct masked call is accepted", mbase + T + A + API + M + DRY),
        ("a legacy closing line is accepted, with a warning, when unmasked",
         P + O + scene + ["--prompt-file", str(lprompt)] + A + I + DRY),
    ]:
        code, msg = script("gen.py", *args)
        report(name, code == 0 and "invariants OK" in msg, msg)
    report("dry runs created nothing", sorted(p for p in tmp.rglob("*")) == before)

    # --- prompt.py
    code, msg = script("prompt.py", *P, "--role", "EDIT TARGET:x", "--role", "STYLE:y")
    report("prompt.py demands STYLE first without --masked", code != 0 and "One Rule #1" in msg, msg)
    code, msg = script("prompt.py", "--role", "STYLE:")
    report("prompt.py requires --package", code != 0 and "--package" in msg, msg)

    # --- review.py and promote.py work on any vNNN path, in either location
    code, msg = script("review.py", str(out / "scene-a/v001"), "--review", "Looks right.")
    report("review.py records a review in the output folder", code == 0
           and "Review: Looks right." in (out / "scene-a/v001/generation.md").read_text(), msg)
    code, msg = script("review.py", str(out / "scene-a/v001"), "--review", "Again.")
    report("review.py refuses to overwrite without --replace", code != 0, msg)
    code, msg = script("promote.py", str(out / "scene-a/v001"), "--approval", "Yes.")
    report("promote.py writes final.png beside the scene", code == 0
           and (out / "scene-a/final.png").exists() and (out / "scene-a/final.md").exists(), msg)
    code, msg = script("promote.py", str(out / "scene-a/v001"))
    report("promote.py refuses to replace without --replace", code != 0
           and "already exists" in msg, msg)
    code, msg = script("promote.py", str(pkg / "assets/people/tester/candidates/v001"),
                       "--replace", "--dry-run")
    report("promote.py targets reference.png for an asset candidate", code == 0
           and "reference.png" in msg, msg)

    print(f"\n  {checks - failures}/{checks} checks passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
