#!/usr/bin/env python3
"""Exercise every guard in gen.py, prompt.py, review.py, promote.py and layers.py
without generating anything.

  python3 -I scripts/selftest.py
  python3 -I scripts/selftest.py --exhaustive   # adds the exhaustive state-space
                                                # tests of the Scene Journal (slow)

Builds a throwaway package and output folder in a temp directory, so it needs no
real package and touches none. gen.py runs under --dry-run, fails before any
call is made, runs in-process with its backend and key stubbed, or runs against a
stub `codex` put first on PATH, which returns a fixture image; no image is
generated and nothing is billed. Run it after touching anything in scripts/.

Each case asserts that a specific invariant FAILS CLOSED. A guard that stops firing
is a guard that has silently been removed.
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import base64
import builtins
import collections
import contextlib
import errno
import functools
import io
import itertools
import json
import os
import re
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import gen  # noqa: E402
import layers  # noqa: E402
import scene_state  # noqa: E402

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


def install_stub_codex(root: Path) -> Path:
    """A stub `codex` first on PATH, mocking the one external service. It copies the
    image STUB_CODEX_IMAGE names to a generated_images path and prints that path, and
    logs each -i file it receives, keeping a copy (gen.py removes its temporary
    flattened copies). Without STUB_CODEX_IMAGE it fails: no run reaches a model.
    Returns the folder holding inputs.log."""
    bin_dir, logs = root / "bin", root / "stub-codex"
    bin_dir.mkdir()
    stub = bin_dir / "codex"
    stub.write_text(f"""#!{sys.executable} -I
import os, shutil, sys, uuid
from pathlib import Path
sys.stdin.read()
logs = Path({str(logs)!r})
(logs / "inputs").mkdir(parents=True, exist_ok=True)
args = sys.argv[1:]
with open(logs / "inputs.log", "a") as log:
    for i, a in enumerate(args[:-1]):
        if a == "-i":
            copy = logs / "inputs" / (uuid.uuid4().hex + ".png")
            shutil.copyfile(args[i + 1], copy)
            log.write(args[i + 1] + " " + str(copy) + "\\n")
src = os.environ.get("STUB_CODEX_IMAGE")
if not src:
    sys.exit("stub codex: no STUB_CODEX_IMAGE; selftest never calls a model")
dest = logs / "generated_images" / (uuid.uuid4().hex + ".png")
dest.parent.mkdir(exist_ok=True)
shutil.copyfile(src, dest)
print(dest)
""")
    stub.chmod(0o755)
    os.environ["PATH"] = f"{bin_dir}{os.pathsep}{os.environ.get('PATH', '')}"
    return logs


def main() -> int:
    if shutil.which("magick") is None:
        print("  skip: ImageMagick (magick) is not installed")
        return 1
    if sys.argv[1:] not in ([], ["--exhaustive"]):
        print(__doc__)
        return 2
    tmp, started = Path(tempfile.mkdtemp(prefix="art-studio-selftest-")), time.monotonic()
    try:
        return run_checks(tmp, exhaustive=sys.argv[1:] == ["--exhaustive"])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        print(f"  selftest wall time: {time.monotonic() - started:.1f} s")


def run_checks(tmp: Path, exhaustive: bool = False) -> int:
    pkg, out = build_fixture(tmp)
    stub_logs = install_stub_codex(tmp)
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

    # --- positive controls: correct calls are accepted, and touch nothing. A new
    # scene's first generation needs a Layer Plan, so the second output folder's
    # scene gets one first.
    code, msg = script("layers.py", "plan", *P, "--output", str(tmp / "out2"), *scene,
                       "--single", "--confirmation", "Yes, one image.", "--based-on", "0")
    report("a single plan is recorded for a scene in a second output folder",
           code == 0 and (tmp / "out2/scene-a/journal/001.json").exists(), msg)
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

    # --- vNNN numbering never reuses a number recorded in DELETED.md, even one logged
    # after main()'s pre-flight read (while the backend ran); only vNNN tokens count
    for name, asset, scene, folders, logged, expect in [
        ("asset numbering skips a deleted v003", "people/tester", None, (1, 2), "v003",
         "v004"),
        ("folders above every DELETED.md entry still count", None, "scene-b", (1, 3, 5),
         "v002 v004", "v006"),
        ("numbering skips every DELETED.md entry, across a gap", None, "scene-c", (1, 2),
         "v003 v007", "v008"),
        ("log token v12 is ignored, v010 counts", None, "scene-d", (1,), "v12 v010",
         "v011"),
    ]:
        gen.PKG = gen.OUT = None
        gen.set_locations(pkg, out if scene else None)
        base = gen.check_target(asset, scene)
        for n in folders:
            (base / f"v{n:03d}").mkdir(parents=True, exist_ok=True)
        (base / "DELETED.md").write_text("# Deleted attempts\n\n" + "".join(
            f"- {v}: deleted at the user's insistence\n" for v in logged.split()))
        got = gen.target_dir(base, set())   # empty pre-flight read: the log came later
        report(name, got.name == expect, f"allocated {got.name}, expected {expect}; "
               f"before: {sorted(c.name for c in base.iterdir() if c != got)}")
    gen.PKG = gen.OUT = None

    # --- a cast crop in the output folder's top-level sources/ is already frozen
    crop = out / "sources/tester-crop.png"
    crop.parent.mkdir()
    magick("-size", "300x600", "xc:#888888", str(crop))
    gen.set_locations(pkg, out)
    got = gen.frozen_equivalent(crop)
    gen.PKG = gen.OUT = None
    report("a crop under output:sources/ is recorded as already frozen",
           got == "already frozen", f"got {got!r}")

    # --- real main() runs into a scene, in-process, with the backend and key stubbed;
    # nothing is sent and nothing is billed
    png = (pkg / "assets/people/tester/candidates/v001/image.png").read_bytes()
    response = {"data": [{"b64_json": base64.b64encode(png).decode()}]}

    def no_codex(*_args, **_kw):
        raise AssertionError("selftest must never reach the codex backend")

    def stubbed_main(target: list[str], fake_generate) -> tuple[str, str]:
        """Run gen.main() on the api backend into target; return its result and stderr."""
        saved = (sys.argv, gen.api_key, gen.generate, gen.generate_codex)
        sys.argv = ["gen.py", *P, *target, "--prompt-file", str(prompt),
                    *A, *I, *API, "--approved-by", "test"]
        gen.api_key, gen.generate, gen.generate_codex = (lambda: "selftest-key"), \
            fake_generate, no_codex
        err = io.StringIO()
        try:
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
                result = f"exit {gen.main()}"
        except (Exception, SystemExit) as e:   # a stray exception is a failure, not a crash
            result = f"{type(e).__name__}: {e}"
        finally:
            sys.argv, gen.api_key, gen.generate, gen.generate_codex = saved
            gen.PKG = gen.OUT = None
        return result, err.getvalue()

    # the log becomes unreadable while the backend runs: the image is paid for, so
    # main() warns and numbers past its pre-flight read
    base = out / "scene-e"
    (base / "v001").mkdir(parents=True)
    (base / "DELETED.md").write_text("- v009: deleted at the user's insistence\n")

    def fake_generate(*_args, **_kw) -> dict:
        (base / "DELETED.md").unlink()
        (base / "DELETED.md").mkdir()
        return response

    result, err = stubbed_main(O + ["--scene", "scene-e"], fake_generate)
    got = sorted(c.name for c in base.iterdir())
    report("main() numbers past its pre-flight log read when the log turns unreadable",
           result == "exit 0" and got == ["DELETED.md", "v001", "v010"]
           and (base / "v010/image.png").exists()
           and "warn: could not re-read" in err
           and "rerun" not in err,   # the image is paid for: no rerun advice
           f"{result}; folders {got}, expected v010 beside v001; stderr: {err!r}")

    # a concurrent run claims v002 between this run's scan and its mkdir: this run
    # takes the next free number and keeps its paid-for image
    base = out / "scene-h"
    (base / "v001").mkdir(parents=True)
    real_mkdir = Path.mkdir

    def rival_claims_v002(self, *args, **kw):
        if self.name == "v002" and self.parent.name == "scene-h" and not self.exists():
            real_mkdir(self)
            (self / "image.png").write_bytes(b"rival image")
        return real_mkdir(self, *args, **kw)

    Path.mkdir = rival_claims_v002
    try:
        result, err = stubbed_main(O + ["--scene", "scene-h"], lambda *_args, **_kw: response)
    finally:
        Path.mkdir = real_mkdir
    got = sorted(c.name for c in base.iterdir())
    report("a run that loses its vNNN to a concurrent run takes the next and keeps its image",
           result == "exit 0" and got == ["v001", "v002", "v003"]
           and (base / "v002/image.png").read_bytes() == b"rival image"
           and (base / "v003/image.png").read_bytes() == png
           and (base / "v003/generation.md").exists(),
           f"{result}; folders {got}, expected v003 beside the other run's v002; "
           f"stderr: {err!r}")

    # --- an unreadable DELETED.md refuses the run pre-flight, before anything is billed
    base = out / "scene-f"
    (base / "DELETED.md").mkdir(parents=True)   # unreadable even under root, unlike chmod 000
    before = sorted(base.iterdir())
    code, msg = script("gen.py", *P, *O, "--scene", "scene-f", "--prompt-file", str(prompt),
                       *A, *I, *DRY)
    report("unreadable DELETED.md refuses a dry run pre-flight",
           code != 0 and "cannot read the deletion log" in msg
           and sorted(base.iterdir()) == before,
           f"exit {code}:\n{msg}")

    # --- the attempt folder, or a parent of it, is a file: not a permissions problem
    (pkg / "assets/people/spare").mkdir()
    (pkg / "assets/people/spare/candidates").write_text("")
    (out / "scene-g").write_text("")
    (tmp / "out-file").write_text("")
    for name, target in [
        ("an asset attempt folder that is a file", ["--asset", "people/spare"]),
        ("a scene attempt folder that is a file", O + ["--scene", "scene-g"]),
        ("a scene under an --output that is a file",
         ["--output", str(tmp / "out-file"), "--scene", "x"]),
    ]:
        before = sorted(tmp.rglob("*"))
        code, msg = script("gen.py", *P, *target, "--prompt-file", str(prompt), *A, *I, *DRY)
        report(f"{name} refuses a dry run",
               code != 0 and "not a directory" in msg and "chmod" not in msg
               and sorted(tmp.rglob("*")) == before, f"exit {code}:\n{msg}")

    # --- --refinish records its deliverable on the receipt itself, never by hand
    for name, receipt, expect in [
        ("--refinish writes the Delivered line after Output, and replaces it on a rerun",
         "Status: awaiting user evaluation\nOutput: image.png, 1536x1024\n"
         "Review: pending — record with review.py\n\n## Exact prompt\n\nx\n",
         "Output: image.png, 1536x1024\nDelivered: delivered-800x600.png"),
        ("--refinish adds the Delivered line to an older receipt without an Output line",
         "Status: approved\n\n## Exact prompt\n\nx\n",
         "Status: approved\nDelivered: delivered-800x600.png"),
    ]:
        vdir = out / f"refinish-{checks}/v001"
        vdir.mkdir(parents=True)
        magick("-size", "1536x1024", "xc:#336699", str(vdir / "image.png"))
        (vdir / "generation.md").write_text(f"# refinish v001\n\n{receipt}")
        runs = [script("gen.py", *P, "--refinish", str(vdir), "--final-size", "800x600")
                for _ in range(2)]
        text = (vdir / "generation.md").read_text()
        report(name, all(code == 0 for code, _ in runs) and expect in text
               and text.count("Delivered:") == 1 and text.index("Delivered:")
               < text.index("## Exact prompt"), f"{runs}\nreceipt:\n{text}")

    vdir = out / "refinish-dry/v001"
    vdir.mkdir(parents=True)
    magick("-size", "1536x1024", "xc:#336699", str(vdir / "image.png"))
    receipt = "# refinish v001\n\nStatus: approved\nOutput: image.png, 1536x1024\n"
    (vdir / "generation.md").write_text(receipt)
    code, msg = script("gen.py", *P, "--refinish", str(vdir), "--final-size", "800x600", *DRY)
    report("--refinish --dry-run says what it would write and writes nothing",
           code == 0 and "would write" in msg and "delivered-800x600.png" in msg
           and sorted(c.name for c in vdir.iterdir()) == ["generation.md", "image.png"]
           and (vdir / "generation.md").read_text() == receipt, f"exit {code}:\n{msg}")

    vdir = out / "refinish-none/v001"
    vdir.mkdir(parents=True)
    magick("-size", "1536x1024", "xc:#336699", str(vdir / "image.png"))
    code, msg = script("gen.py", *P, "--refinish", str(vdir), "--final-size", "800x600")
    report("--refinish without a receipt is refused and writes nothing",
           code != 0 and "no generation.md" in msg
           and sorted(c.name for c in vdir.iterdir()) == ["image.png"], f"exit {code}:\n{msg}")

    # --- an attempt folder, or the folder that must hold it, that cannot be written:
    # refused pre-flight in a dry run and a real run, before the backend is called
    calls = []

    def counted(*_args, **_kw) -> dict:
        calls.append(1)
        return response

    (pkg / "assets/people/linked").mkdir()
    (pkg / "assets/people/linked/candidates").symlink_to(tmp / "nowhere")
    (out / "scene-ro/v001").mkdir(parents=True)
    (out / "scene-link").symlink_to(tmp / "nowhere")
    (tmp / "ro-out").mkdir()
    read_only = [pkg / "assets/people/tester/candidates", out / "scene-ro", tmp / "ro-out"]
    root = os.geteuid() == 0   # root ignores permission bits: chmod cases cannot fail
    for p in read_only:
        p.chmod(0o555)
    try:
        for name, target, blocker, needs_chmod in [
            ("asset candidates/ read-only", ["--asset", "people/tester"],
             "people/tester/candidates", True),
            ("asset candidates/ broken symlink", ["--asset", "people/linked"],
             "people/linked/candidates", False),
            ("scene folder read-only", O + ["--scene", "scene-ro"], "out/scene-ro", True),
            ("scene folder broken symlink", O + ["--scene", "scene-link"], "out/scene-link",
             False),
            ("scene under a read-only --output",
             ["--output", str(tmp / "ro-out"), "--scene", "new"], "ro-out", True),
        ]:
            if needs_chmod and root:
                print(f"  skip: {name} (running as root)")
                continue
            before = sorted(tmp.rglob("*"))
            code, msg = script("gen.py", *P, *target, "--prompt-file", str(prompt),
                               *A, *I, *API, *DRY)
            calls.clear()
            result, err = stubbed_main(target, counted)
            report(f"unwritable target refused pre-flight: {name}",
                   code != 0 and "FAIL:" in msg and blocker in msg
                   and result.startswith("Fail: ") and blocker in result and not calls
                   and sorted(tmp.rglob("*")) == before,
                   f"expected a Fail naming {blocker}; backend called {len(calls)}x\n"
                   f"main(): {result}\ndry run exit {code}: {msg}")
    finally:
        for p in read_only:
            p.chmod(0o755)

    # --- the target turns unwritable while the backend runs: the image is paid for,
    # so main() saves it under the system temp dir, names it, and still fails
    base = out / "scene-i"
    (base / "v001").mkdir(parents=True)

    def target_breaks(*_args, **_kw) -> dict:
        shutil.rmtree(base)
        base.symlink_to(tmp / "nowhere")   # unwritable even under root, unlike chmod
        return response

    result, err = stubbed_main(O + ["--scene", "scene-i"], target_breaks)
    temp, ours = os.path.realpath(tempfile.gettempdir()), os.path.realpath(tmp)
    named = [Path(p) for m in re.findall(r"/[^\s'\"`,;()]+", result)
             if (p := os.path.realpath(m.rstrip(".:"))).startswith(temp + os.sep)
             and not p.startswith(ours + os.sep) and os.path.exists(p)]
    kept = [p for p in named if (k := p / "image.png" if p.is_dir() else p).is_file()
            and k.read_bytes() == png]
    report("an image whose target breaks after generating is saved to the temp dir",
           result.startswith("Fail: ") and kept,
           f"{result}; expected a Fail naming a file under {temp} holding the image; "
           f"stderr: {err!r}")
    for p in kept:   # outside tmp, so main()'s cleanup would miss it
        shutil.rmtree(p) if p.is_dir() else p.unlink()
        if str(p.parent) != temp:
            with contextlib.suppress(OSError):
                p.parent.rmdir()   # an emptied per-run fallback folder; never a full one

    # --- Layer Plans: layers.py plan and status, and gen.py's gate on a new scene
    def plan(scene_slug: str, *args: str) -> tuple[int, str]:
        return script("layers.py", "plan", *P, *O, "--scene", scene_slug, *args)

    def journal(scene_slug: str) -> list[str]:
        jdir = out / scene_slug / "journal"
        return sorted(p.name for p in jdir.iterdir()) if jdir.is_dir() else []

    def record(scene_slug: str, n: int) -> dict:
        return json.loads((out / scene_slug / f"journal/{n:03d}.json").read_text())

    F, YES = ["--frame", "1536x1024"], ["--confirmation", "Yes."]
    TWO = ["--layer", "sky=Sky and far hills", "--layer", "boats=The two boats"]
    # a layered scene and a single scene that already have generations
    for slug, kind in (("lay-gen", F + TWO), ("single-gen", ["--single"])):
        code, msg = plan(slug, *kind, *YES, "--based-on", "0")
        if code:
            raise SystemExit(f"  FAIL: could not plan {slug}:\n  {msg}")
    (out / "lay-gen/layers/sky/v001").mkdir(parents=True)
    (out / "single-gen/v001").mkdir()

    layer_cases = [
        ("a layered plan with one Layer refused",
         ["fresh", *F, "--layer", "sky=Sky", "--dry-run"], "two or more Layers"),
        ("a malformed Layer ID refused",
         ["fresh", *F, "--layer", "Sky=Sky", "--layer", "b=Boats", "--dry-run"],
         "Layer ID 'Sky'"),
        ("a duplicate Layer ID refused",
         ["fresh", *F, "--layer", "a=Sky", "--layer", "a=Boats", "--dry-run"], "given twice"),
        ("an empty Layer Entry refused",
         ["fresh", *F, "--layer", "a= \n ", "--layer", "b=Boats", "--dry-run"],
         "empty Layer Entry"),
        ("a --layer without ID= refused", ["fresh", *F, "--layer", "sky", "--dry-run"],
         "use ID=TEXT"),
        ("--single with --layer refused",
         ["fresh", "--single", "--layer", "a=Sky", "--dry-run"], "takes no --layer"),
        ("a malformed --frame refused",
         ["fresh", "--frame", "0x1024", *TWO, "--dry-run"], "give the Frame as WxH"),
        ("@N naming no plan record refused",
         ["lay-gen", *F, "--layer", "sky=@7", "--layer", "boats=@1", "--dry-run"],
         "holds no record 7"),
        ("@N on a Layer that plan record lacks refused",
         ["lay-gen", *F, "--layer", "sky=@1", "--layer", "fog=@1", "--dry-run"],
         "holds no Layer 'fog'"),
        ("a plan without --confirmation refused",
         ["fresh", "--single", "--based-on", "0"], "--confirmation is required"),
        ("a plan without --based-on refused", ["fresh", "--single", *YES],
         "--based-on is required"),
        ("a stale --based-on refused",
         ["lay-gen", *F, *TWO, "--layer", "fog=Fog", *YES, "--based-on", "0"],
         "show the User its new state"),
        ("layered to single after generation refused",
         ["lay-gen", "--single", *YES, "--based-on", "1"], "Offer the User a new scene"),
        ("single to layered after generation refused",
         ["single-gen", *F, *TWO, *YES, "--based-on", "1"], "Offer the User a new scene"),
        ("a scene made before Layer Plans can't become layered",
         ["scene-a", *F, *TWO, "--dry-run"], "Offer the User a new scene"),
        ("a Frame change after generation refused",
         ["lay-gen", "--frame", "1024x1024", *TWO, *YES, "--based-on", "1"],
         "Frame is locked"),
        ("removal from a two-Layer plan after generation refused",
         ["lay-gen", *F, "--layer", "sky=@1", *YES, "--based-on", "1"],
         "add the replacement Layer first"),
        ("layers.py refuses --output inside the package", None, "overlaps the package"),
        ("layers.py refuses a bad scene slug", ["Bad Scene", "--single", "--dry-run"],
         "scene slug"),
    ]
    for name, args, expect in layer_cases:
        before = sorted(tmp.rglob("*"))
        if args is None:
            code, msg = script("layers.py", "plan", *P, "--output", str(pkg / "renders"),
                               "--scene", "x", "--single", *YES, "--based-on", "0")
        else:
            code, msg = plan(*args)
        report(name, code != 0 and expect in msg and "Traceback" not in msg
               and sorted(tmp.rglob("*")) == before,
               f"expected {expect!r} and nothing written, exit {code}:\n{msg}")

    for name, slug, expect in [
        ("a new scene's first generation needs a Layer Plan", "fresh", "has no Layer Plan"),
        ("a layered scene refuses a one-image generation", "lay-gen", "is layered"),
    ]:
        code, msg = script("gen.py", *P, *O, "--scene", slug, "--prompt-file", str(prompt),
                           *A, *I, *DRY)
        report(name, code != 0 and expect in msg, f"expected {expect!r}, exit {code}:\n{msg}")
    code, msg = script("gen.py", *P, *O, "--scene", "single-gen", "--prompt-file",
                       str(prompt), *A, *I, *DRY)
    report("a planned Single-Layer Scene generates as before",
           code == 0 and "invariants OK" in msg, msg)

    (out / "deleted-only").mkdir()
    (out / "deleted-only/DELETED.md").write_text("- v001: deleted at the user's insistence\n")
    code, msg = script("gen.py", *P, *O, "--scene", "deleted-only", "--prompt-file",
                       str(prompt), *A, *I, *DRY)
    report("a scene whose only history is its deletion log generates as before",
           code == 0 and "invariants OK" in msg, msg)

    good = '{"number": 1, "kind": "plan", "date": "2026-01-01", "words": "Yes.", '
    for name, files, expect in [
        ("a journal record whose number doesn't match its name refused",
         {"001.json": '{"number": 2, "kind": "plan"}'}, "is not a journal record"),
        ("an unparseable journal record refused", {"001.json": '{"number": 1, '},
         "is not a readable journal record"),
        ("a journal holding one number twice refused",
         {"001.json": good + '"layered": false}', "0001.json": good + '"layered": false}'},
         "holds record 1 twice"),
        ("a plan record missing its fields refused",
         {"001.json": good + '"layered": true, "frame": {"width": 9}}'},
         "is not a whole plan record"),
    ]:
        jbad = out / f"bad-journal-{checks}/journal"
        jbad.mkdir(parents=True)
        for fname, text in files.items():
            (jbad / fname).write_text(text)
        code, msg = script("layers.py", "status", *P, *O, "--scene", jbad.parent.name)
        code2, msg2 = script("gen.py", *P, *O, "--scene", jbad.parent.name,
                             "--prompt-file", str(prompt), *A, *I, *DRY)
        report(name, code != 0 and expect in msg and code2 != 0 and expect in msg2,
               f"status exit {code}: {msg}\ngen.py exit {code2}: {msg2}")

    # positive controls after generation: adding a Layer, removing one with its
    # replacement in the same change, and putting a removed Layer back
    steps = [
        ("adding a Layer after generation is recorded",
         ["--layer", "sky=@1", "--layer", "boats=@1", "--layer", "fog=Fog"], "1",
         ["adds Layer fog"]),
        ("removing a Layer with its replacement in the same change is recorded",
         ["--layer", "sky=@1", "--layer", "fog=@2", "--layer", "ships=Ships"], "2",
         ["adds Layer ships", "removes Layer boats"]),
        ("a removed Layer put back with a new Layer Entry says so",
         ["--layer", "sky=@1", "--layer", "boats=Other boats", "--layer", "fog=@2",
          "--layer", "ships=@3", "--dry-run"], "3",
         ["puts back Layer boats, with a Layer Entry that differs from plan record 2's"]),
        ("a removed Layer put back with its Layer Entry says so",
         ["--layer", "sky=@1", "--layer", "fog=@2", "--layer", "ships=@3",
          "--layer", "boats=@2"], "3",
         ["puts back Layer boats, with its Layer Entry from plan record 2"]),
    ]
    for name, layer_args, based, expect in steps:
        dry = "--dry-run" in layer_args
        code, msg = plan("lay-gen", *F, *layer_args, *YES, "--based-on", based)
        n = int(based) + 1
        ok = code == 0 and all(e in msg for e in expect)
        if ok and not dry:
            ok = record("lay-gen", n).get("changes") == expect
        report(name, ok and len(journal("lay-gen")) == (n - 1 if dry else n), msg)

    # positive controls: dry runs print the proposal and the number to pass, and write
    # nothing; then a single plan, a change before generation, and an @N copy
    before = sorted(tmp.rglob("*"))
    code1, msg1 = plan("fresh", "--single", "--dry-run")
    code2, msg2 = plan("fresh", *F, *TWO, "--layer", "fog=Morning fog", "--dry-run")
    report("plan --dry-run prints single and layered proposals and writes nothing",
           code1 == code2 == 0 and "single" in msg1 and "--based-on 0" in msg1
           and all(s in msg2 for s in ("1536x1024", "sky: Sky and far hills",
                                       "3 fog: Morning fog", "--based-on 0"))
           and sorted(tmp.rglob("*")) == before, msg1 + msg2)

    words = "Yes,  one image.\nGo ahead."
    code, msg = plan("planned", "--single", "--confirmation", words, "--based-on", "0")
    rec = record("planned", 1) if code == 0 else {}
    report("a single plan writes journal/001.json with the words verbatim",
           code == 0 and journal("planned") == ["001.json"] and rec.get("words") == words
           and rec.get("kind") == "plan" and rec.get("layered") is False
           and rec.get("number") == 1 and "previous" not in rec, f"{msg}\n{rec}")
    umask = os.umask(0)
    os.umask(umask)
    mode = (out / "planned/journal/001.json").stat().st_mode & 0o777
    report("a journal record takes the umask's mode, not mkstemp's 0600",
           mode == 0o666 & ~umask, f"mode {mode:o}, umask {umask:o}")

    sky = "Sky,   far hills\nand the sun"
    code, msg = plan("planned", *F, "--layer", f"sky={sky}", "--layer", "boats=Boats",
                     *YES, "--based-on", "1")
    rec = record("planned", 2) if code == 0 else {}
    report("a change before generation switches single to layered",
           code == 0 and rec.get("previous") == 1 and rec.get("frame") ==
           {"width": 1536, "height": 1024} and [l["id"] for l in rec.get("layers", [])]
           == ["sky", "boats"] and rec.get("changes") == ["switches from single to layered"],
           f"{msg}\n{rec}")

    code, msg = plan("planned", "--frame", "1024x1024", "--layer", "boats=Boats",
                     "--layer", "sky=@2", "--layer", "fog=Fog", *YES, "--based-on", "2")
    rec = record("planned", 3) if code == 0 else {}
    changes = rec.get("changes", [])
    report("@N copies a Layer Entry verbatim, and the change says what it does",
           code == 0 and rec.get("layers", [{}, {}])[1].get("entry") == sky
           and "changes the Frame from 1536x1024 to 1024x1024" in changes
           and "adds Layer fog" in changes
           and "reorders Layers, bottom to top: boats, sky" in changes, f"{msg}\n{rec}")

    code, msg = plan("planned", "--frame", "1024x1024", "--layer", "boats=Boats",
                     "--layer", "sky=Clouds only", *YES, "--based-on", "3", "--dry-run")
    report("a dry run names a removed Layer and a changed Layer Entry",
           code == 0 and "removes Layer fog" in msg and "changes Layer sky's Layer Entry"
           in msg and journal("planned") == ["001.json", "002.json", "003.json"], msg)

    code, msg = script("layers.py", "status", *P, *O, "--scene", "planned")
    report("status prints the current plan bottom to top",
           code == 0 and "layered, Frame 1024x1024, 3 Layers" in msg
           and msg.index("boats:") < msg.index("sky:") < msg.index("fog:")
           and "journal/003.json" in msg and "--based-on 3" in msg, msg)
    code, msg = script("layers.py", "status", *P, *O, "--scene", "scene-a")
    report("status reports a scene made before Layer Plans as single",
           code == 0 and "single (no Layer Plan recorded)" in msg
           and "as before Layer Plans" in msg, msg)

    # the journal writer: a number taken at publish, and a filesystem without hard
    # links, injected in-process; nothing partial is ever left behind
    def layers_main(*argv: str) -> str:
        try:
            with contextlib.redirect_stdout(io.StringIO()), \
                    contextlib.redirect_stderr(io.StringIO()):
                return f"exit {layers.main(['plan', *P, *O, *argv])}"
        except (Exception, SystemExit) as e:
            return f"{type(e).__name__}: {e}"
        finally:
            gen.PKG = gen.OUT = None

    real_link = os.link

    def rival_link(src, dst, *a, **kw):
        Path(dst).write_text('{"number": 1, "kind": "plan", "rival": true}')
        return real_link(src, dst, *a, **kw)

    def no_links(*_a, **_kw):
        raise OSError(errno.ENOTSUP, "Operation not supported")

    def disk_full(*_a, **_kw):
        raise OSError(errno.ENOSPC, "No space left on device")

    real_open = builtins.open

    def open_then_fill(path, mode="r", *a, **kw):   # creates the file, then the disk fills
        f = real_open(path, mode, *a, **kw)
        f.write = disk_full
        return f

    for name, patches, args, expect, files in [
        ("a number taken at publish refuses and writes nothing", [(os, "link", rival_link)],
         ["race", *F, *TWO], "published by another writer", ["001.json"]),
        ("no hard links: a layered plan stops, naming the journal folder",
         [(os, "link", no_links)],
         ["nolink-l", *F, *TWO], f"{(out / 'nolink-l/journal').resolve()}", []),
        ("no hard links: a single plan falls back to exclusive create",
         [(os, "link", no_links)], ["nolink-s", "--single"], "exit 0", ["001.json"]),
        ("a full disk while writing the record refuses and leaves no file",
         [(os, "fchmod", disk_full)], ["full-l", *F, *TWO],
         "could not write in the Scene Journal", []),
        ("a full disk during the no-hard-link fallback leaves no partial record",
         [(os, "link", no_links), (builtins, "open", open_then_fill)],
         ["full-s", "--single"], "could not write in the Scene Journal", []),
    ]:
        saved = [(obj, attr, getattr(obj, attr)) for obj, attr, _ in patches]
        for obj, attr, value in patches:
            setattr(obj, attr, value)
        try:
            result = layers_main("--scene", args[0], *args[1:], *YES, "--based-on", "0")
        finally:
            for obj, attr, value in saved:
                setattr(obj, attr, value)
        got = journal(args[0])
        ok = expect in result and got == files
        if ok and args[0] == "race":
            ok = record("race", 1).get("rival") is True
        if ok and args[0] == "nolink-s":
            ok = record("nolink-s", 1).get("words") == "Yes."
        report(name, ok, f"{result}; journal holds {got}, expected {files}")

    # done: a new Single-Layer Scene plans, then generates (backend stubbed), reviews
    # and promotes exactly as before, leaving today's files plus its journal
    code, msg = plan("single-new", "--single", *YES, "--based-on", "0")
    result, err = stubbed_main(O + ["--scene", "single-new"], lambda *_a, **_kw: response)
    rv = script("review.py", str(out / "single-new/v001"), "--review", "Fine.")
    pr = script("promote.py", str(out / "single-new/v001"), "--approval", "Yes.")
    got = sorted(str(p.relative_to(out / "single-new")) for p in
                 (out / "single-new").rglob("*"))
    report("a planned Single-Layer Scene runs today's loop and keeps its journal",
           code == 0 and result == "exit 0" and rv[0] == pr[0] == 0
           and got == ["final.md", "final.png", "journal", "journal/001.json", "v001",
                       "v001/generation.md", "v001/image.png"],
           f"plan {msg}; gen {result} {err}; review {rv}; promote {pr}; files {got}")

    # --- Layered Scenes: real Layer and Draft generations against the stub codex, the
    # separation checks, combine, rebuild and status. Fixture frames are small.
    fxd = tmp / "fx"
    fxd.mkdir()

    def img(name: str, *draw: str, size: str = "192x108") -> Path:
        magick("-size", size, *draw, str(fxd / name))
        return fxd / name

    def disc(colour: str, x: int, y: int, r: int) -> list[str]:
        return ["-fill", colour, "-draw", f"circle {x},{y} {x},{y - r}"]

    ship = lambda x, y: ["-fill", "#cc2222", "-draw", f"polygon {x},{y + 10} {x + 40},{y} {x},{y - 10}",
                         *disc("rgba(255,160,40,0.5)", x - 6, y, 8)]
    draft_png = img("draft.png", "xc:#223355", *disc("#cc8844", 60, 54, 30))
    planet_png = img("planet.png", "gradient:#101830-#304070", *disc("#6688aa", 60, 60, 40),
                     size="200x112")
    rocks_png = img("rocks.png", "xc:none", *disc("#888070", 120, 40, 12),
                    *disc("#7a7060", 160, 80, 8), size="200x112")
    ships_png = img("ships.png", "xc:none", *ship(40, 60))
    ships2_png = img("ships2.png", "xc:none", *ship(100, 30))
    square_png = img("square.png", "xc:none", *disc("#cc2222", 75, 75, 40), size="150x150")
    glow_png = img("glow.png", "xc:none", *disc("#0f0804", 96, 54, 30), *disc("#ff9922", 96, 54, 12))
    flat_png = img("flat.png", "xc:#3366aa")
    user_png = img("user.png", "xc:#3366aa")

    def gen_run(image: Path | None, *args: str) -> tuple[int, str]:
        """gen.py for real against the stub codex, which returns image."""
        os.environ["STUB_CODEX_IMAGE"] = str(image or "")
        try:
            return script("gen.py", *P, *O, *args)
        finally:
            os.environ.pop("STUB_CODEX_IMAGE", None)

    def layers_cmd(command: str, slug: str, *args: str) -> tuple[int, str]:
        return script("layers.py", command, *P, *O, "--scene", slug, *args)

    def receipt(rel: str) -> dict:
        return scene_state.read_receipt(out / rel)

    def rgba(path: Path, depth: int = 8) -> bytes:
        return subprocess.run(["magick", str(path), "-depth", str(depth), "-endian", "MSB",
                               "rgba:-"],
                              capture_output=True, check=True).stdout

    def stub_inputs() -> list[list[str]]:
        log = stub_logs / "inputs.log"
        return [l.split() for l in log.read_text().splitlines()] if log.exists() else []

    LF = ["--frame", "192x108"]
    code, msg = plan("space", *LF, "--layer", "planet=The ringed planet and stars",
                     "--layer", "asteroids=The asteroid field",
                     "--layer", "ships=The two ships and their engine glow", *YES,
                     "--based-on", "0")
    if code:
        raise SystemExit(f"  FAIL: could not plan space:\n  {msg}")
    SP = ["--scene", "space"]
    lblock = build("layer.txt", "--role", "STYLE:", "--role", "PLACEMENT:",
                   "--layer-name", "ships", "--below", "the planet and asteroids",
                   "--opaque", "the ships' hulls", "--soft", "the engine flames and glow")
    text = " ".join(lblock.read_text().split())
    report("prompt.py emits the Layer statement and transparent-background block",
           "This image is ONE LAYER of a layered illustration: the ships layer only. "
           "Beneath it: the planet and asteroids." in text
           and gen.TRANSPARENT_LEAD in text
           and "Fully opaque, with a clean edge: the ships' hulls." in text
           and "fully transparent at its edges so whatever lies beneath shows through: "
               "the engine flames and glow." in text
           and "Image 2 is PLACEMENT: An image of this same scene. Use it only for "
               "placement, scale and light direction." in text
           and text.index("ONE LAYER") < text.index("single horizontal")
           < text.index("BACKGROUND: TRANSPARENT"), text)
    code, msg = script("prompt.py", *P, "--below", "x", "--opaque", "y")
    report("prompt.py refuses --below without --layer-name",
           code != 0 and "give --layer-name too" in msg, msg)

    PL = lambda rel: ["--attach", f"{rel}:PLACEMENT"]
    code, msg = gen_run(draft_png, *SP, "--draft", "--prompt-file", str(prompt), *A,
                        "--request", "a draft")
    r = receipt("space/drafts/v001")
    report("a Draft lands in drafts/v001 as returned, with its receipt fields",
           code == 0 and (out / "space/drafts/v001/image.png").read_bytes()
           == draft_png.read_bytes() and r.get("Kind") == "Draft"
           and r.get("Layer Plan") == "journal/001.json" and r.get("Frame") == "192x108"
           and r.get("md5") == gen.md5(draft_png), f"{msg}\n{r}")

    code, msg = gen_run(planet_png, *SP, "--layer", "planet", "--prompt-file", str(prompt),
                        *A, *PL("space/drafts/v001/image.png"))
    lv, r = out / "space/layers/planet/v001", receipt("space/layers/planet/v001")
    report("a Layer generation scales to the Frame, keeps raw.png and writes its fields",
           code == 0 and gen.identify(lv / "image.png") == (192, 108)
           and (lv / "raw.png").read_bytes() == planet_png.read_bytes()
           and r.get("Kind") == "Layer Version" and r.get("Layer") == "planet"
           and r.get("Layer Entry") == "The ringed planet and stars"
           and r.get("Layer Plan") == "journal/001.json" and r.get("Frame") == "192x108"
           and r.get("Raw size") == "200x112"
           and r.get("Scale") == "x 0.9600, y 0.9643 (-resize 192x108!)"
           and r.get("Starting version") == "none; generated fresh"
           and r.get("Flattened", "").startswith("none")
           and r.get("Checks", "").startswith("not run")
           and r.get("md5") == gen.md5(lv / "image.png")
           and f"output:space/drafts/v001/image.png md5={gen.md5(draft_png)}"
               in (lv / "generation.md").read_text()
           and "lacks the transparent-background block" not in msg, f"{msg}\n{r}")

    code, msg = gen_run(rocks_png, *SP, "--layer", "asteroids", "--prompt-file", str(lblock),
                        *A, *PL("space/layers/planet/v001/image.png"))
    r = receipt("space/layers/asteroids/v001")
    report("a Layer prompt with the block is checked, and a clean cut-out passes",
           code == 0 and r.get("Checks") == "round 1, raw output: pass"
           and (out / "space/layers/asteroids/v001/raw.png").exists()
           and gen.has_alpha(out / "space/layers/asteroids/v001/image.png"), f"{msg}\n{r}")

    code, msg = layers_cmd("combine", "space", "--request", "show me the step")
    report("combine stacks the Layers that have versions into the scene's v001",
           code == 0 and [s["layer"] for s in receipt("space/v001")["stack"]]
           == ["planet", "asteroids"] and "left out, with no counting version: ships" in msg,
           msg)

    logged = len(stub_inputs())
    code, msg = gen_run(ships_png, *SP, "--layer", "ships", "--prompt-file", str(lblock), *A,
                        *PL("space/v001/image.png"), *PL("space/drafts/v001/image.png"))
    r, sent = receipt("space/layers/ships/v001"), stub_inputs()[logged:]
    ci = out / "space/v001/image.png"
    magick(str(ci), "-background", "black", "-alpha", "remove", "-alpha", "off",
           str(tmp / "ci-flat.png"))
    copy = next((Path(c) for p, c in sent if p != str(ci) and "image2-" in p), None)
    report("an attachment with alpha reaches the model flattened onto black",
           code == 0 and len(sent) == 3 and str(ci) not in [p for p, _ in sent]
           and copy is not None and not gen.has_alpha(copy)
           and rgba(copy) == rgba(tmp / "ci-flat.png")
           and r.get("Flattened", "").startswith("image 2 output:space/v001/image.png onto black")
           and not any(Path(p).exists() for p, _ in sent if "gen-flat-" in p)
           and f"PLACEMENT: output:space/v001/image.png md5={gen.md5(ci)}"
               in (out / "space/layers/ships/v001/generation.md").read_text(),
           f"{msg}\nsent {sent}\n{r}")
    report("a Layer returned at the Frame's size is kept as is, with no raw.png",
           code == 0 and not (out / "space/layers/ships/v001/raw.png").exists()
           and r.get("Scale", "").startswith("none; already")
           and r.get("Checks") == "round 1, raw output: pass", f"{msg}\n{r}")

    code, msg = layers_cmd("combine", "space", "--preset", "page", "--request", "all three",
                           "--mode", "step's Combined Image")
    v2, r = out / "space/v002", receipt("space/v002")
    ok = code == 0 and [(s["layer"], s["path"], s["approved"], s["removed"]) for s in
                        r["stack"]] == [(l, f"output:space/layers/{l}/v001", "no", "no")
                                        for l in ("planet", "asteroids", "ships")]
    report("combine writes the Combined Image receipt and prints each Layer's version",
           ok and (v2 / "generation.md").read_text().startswith("# space v002\n\nNo image model")
           and r.get("Kind") == "Combined Image" and r.get("Frame") == "192x108"
           and r["stack"][2]["entry"] == "The two ships and their engine glow"
           and r["stack"][0]["md5"] == gen.md5(lv / "image.png")
           and r["stack"][0]["style"] == "v1" and r.get("md5") == gen.md5(v2 / "image.png")
           and r.get("Pixel signature") == layers.signature(v2 / "image.png")
           and r.get("ImageMagick", "unknown") != "unknown"
           and r.get("Command", "").startswith("magick -size 192x108 xc:none ")
           and "output:space/layers/ships/v001/image.png -compose Over" in r.get("Command", "")
           and r.get("User request verbatim") == "all three"
           and "3 ships v001  (its Default Version; not its Approved Layer Version)" in msg
           and "Warning" not in r, f"{msg}\n{r}")
    deliverable = v2 / "delivered-1200x800.png"
    report("combine --preset derives one flat deliverable showing the flatten colour",
           code == 0 and deliverable.exists() and not gen.has_alpha(deliverable)
           and gen.identify(deliverable) == (1200, 800)
           and r.get("Delivered", "").startswith("delivered-1200x800.png")
           and gen.magick(deliverable, "-format", "%[pixel:p{0,0}]", "info:").strip()
           in ("srgb(0,0,0)", "black", "srgb(0%,0%,0%)"), f"{msg}\n{r}")

    code, msg = layers_cmd("rebuild", "space", "--combined", "v002")
    report("rebuild matches the recorded pixel signature",
           code == 0 and "pixel signature matches" in msg and "note:" not in msg, msg)
    saved = (v2 / "generation.md").read_text()
    pwned = tmp / "pwned"
    (v2 / "generation.md").write_text(re.sub(r"^Command: .*$", f"Command: touch {pwned}",
                                             saved, flags=re.M))
    code, msg = layers_cmd("rebuild", "space", "--combined", "v002")
    report("rebuild builds its own command when the receipt's is edited, never running it",
           code == 0 and "pixel signature matches" in msg and "Command differs" in msg
           and f"touch {pwned}" in msg and not pwned.exists(), msg)
    (v2 / "generation.md").write_text(saved.replace("\n1. planet ", "\n1.  planet ", 1))
    code, msg = layers_cmd("rebuild", "space", "--combined", "v002")
    code2, msg2 = layers_cmd("status", "space")
    report("a Stack line that can't be read refuses rebuild and shows in status",
           code != 0 and "Stack line rebuild can't read" in msg and "Traceback" not in msg
           and "v002's receipt has a Stack line that can't be read" in msg2, msg + msg2)
    (v2 / "generation.md").write_text(re.sub(r"^Pixel signature: .*$",
                                             "Pixel signature: " + "0" * 64, saved, flags=re.M))
    code, msg = layers_cmd("rebuild", "space", "--combined", "v002")
    report("rebuild reports a pixel signature that doesn't match",
           code != 0 and "MISMATCH" in msg, msg)
    (v2 / "generation.md").write_text(saved.replace("output:space/layers/planet/v001",
                                                    "output:scene-a/v001", 1))
    code, msg = layers_cmd("rebuild", "space", "--combined", "v002")
    report("rebuild refuses a stack line outside the scene's Layer Versions",
           code != 0 and "not one of this scene's Layer Versions" in msg, msg)
    (v2 / "generation.md").write_text(saved)

    code, msg = layers_cmd("combine", "space")
    report("combining the same stack again is deterministic",
           code == 0 and receipt("space/v003").get("Pixel signature")
           == receipt("space/v002").get("Pixel signature")
           and gen.md5(out / "space/v003/image.png") == gen.md5(v2 / "image.png"), msg)

    code1, msg1 = gen_run(ships2_png, *SP, "--layer", "ships", "--prompt-file", str(lblock), *A)
    code2, msg2 = layers_cmd("combine", "space", "--mode", "the ship moved")
    a, b = rgba(out / "space/v003/image.png"), rgba(out / "space/v004/image.png")
    # the ship fixtures are 16-bit: an alpha below 1/255 is not fully transparent
    s1, s2 = (rgba(out / f"space/layers/ships/{v}/image.png", 16) for v in ("v001", "v002"))
    moved = [i for i in range(0, len(a), 4) if a[i:i + 4] != b[i:i + 4]]
    clear = lambda s, i: s[2 * i + 6:2 * i + 8] == b"\0\0"
    stray = [i // 4 for i in moved if clear(s1, i) and clear(s2, i)]
    report("a new version of one Layer changes the Combined Image only where it or the "
           "old version isn't transparent",
           code1 == code2 == 0 and moved and not stray
           and [s["path"].rsplit("/", 1)[-1] for s in receipt("space/v004")["stack"]]
           == ["v001", "v001", "v002"], f"{len(moved)} changed, stray {stray[:5]}; {msg2[-300:]}")

    code, msg = gen_run(square_png, *SP, "--layer", "ships", "--prompt-file", str(lblock), *A)
    r = receipt("space/layers/ships/v003")
    report("a Layer off the Frame's aspect ratio is kept unscaled and doesn't count",
           code == 0 and gen.identify(out / "space/layers/ships/v003/image.png") == (150, 150)
           and "Tell the User and show it to them on its own" in msg
           and "doesn't count" in r.get("Warning", "")
           and r.get("Scale", "").startswith("none; its aspect ratio"), f"{msg}\n{r}")
    code, msg = gen_run(square_png, *SP, "--draft", "--prompt-file", str(prompt), *A)
    report("a Draft off the Frame's aspect ratio is kept, and the Caller told",
           code == 0 and (out / "space/drafts/v002/image.png").exists()
           and "doesn't match the Frame's aspect ratio" in msg and "Tell the User" in msg
           and "Tell the User" in receipt("space/drafts/v002").get("Warning", ""), msg)

    code, msg = gen_run(ships_png, *SP, "--layer", "ships", "--prompt-file", str(lblock), *A,
                        "--attach", "space/v004/image.png:EDIT TARGET")
    report("a Layer edited from a Combined Image records the version it holds as its start",
           code == 0 and receipt("space/layers/ships/v004").get("Starting version")
           == "output:space/layers/ships/v002", msg)

    code, msg = layers_cmd("status", "space")
    lines = msg.splitlines()
    report("status lists versions, whether each counts, Default Versions, Drafts and "
           "Combined Images",
           code == 0 and "      v003  doesn't count: 150x150 doesn't match the Frame's "
           "aspect ratio" in lines
           and "      Default Version: v004 (its latest version); Approved Layer Version: none"
           in lines and "    v002  150x150, not the Frame's aspect ratio" in lines
           and "    v004  planet v001, asteroids v001, ships v002" in lines
           and "  integrity problems: none" in lines, msg)

    code, msg = layers_cmd("combine", "space")   # v005 holds ships v004; then delete it
    shutil.rmtree(out / "space/layers/ships/v004")
    (out / "space/layers/ships/DELETED.md").write_text(
        "- v004: deleted at the user's insistence\n")
    code, msg = layers_cmd("status", "space")
    report("status reports a deleted version, and a Combined Image that names it",
           code == 0 and "      v004  doesn't count: deleted" in msg.splitlines()
           and "v005's Stack line 3 names output:space/layers/ships/v004, which is deleted"
           in msg and "Default Version: v002" in msg, msg)
    code, msg = layers_cmd("rebuild", "space", "--combined", "v005")
    report("rebuild refuses a stack that names a deleted version",
           code != 0 and "is deleted" in msg, msg)

    rocks = out / "space/layers/asteroids/v001/image.png"
    saved_rocks = rocks.read_bytes()
    magick(str(rocks), "-fill", "#ffffff", "-draw", "point 1,1", str(rocks))
    code, msg = layers_cmd("status", "space")
    report("status reports an altered Layer Version as altered",
           code == 0 and "layers/asteroids/v001/image.png is altered" in msg
           and "v002's Stack line 2 names output:space/layers/asteroids/v001, which is altered"
           in msg, msg)

    # refusals: each writes nothing and prints no traceback
    lay = [*SP, "--prompt-file", str(lblock), *A]
    (out / "space/sources").mkdir()
    shutil.copyfile(user_png, out / "space/sources/bare.png")
    shutil.copyfile(out / "space/layers/ships/v002/image.png", out / "space/sources/stale.png")
    (out / "space/sources/stale.md").write_text(
        f"Derived from: output:space/layers/ships/v002/image.png md5={'0' * 32}\n"
        "Command: magick in.png -blur 0x2 out.png\n")
    for name, args, expect in [
        ("--layer on a Single-Layer Scene refused",
         ["--scene", "single-gen", "--layer", "sky", "--prompt-file", str(prompt), *A],
         "Single-Layer Scene"),
        ("--draft on a scene made before Layer Plans refused",
         ["--scene", "scene-a", "--draft", "--prompt-file", str(prompt), *A],
         "Single-Layer Scene"),
        ("a Layer the current plan doesn't hold refused", [*lay, "--layer", "moon"],
         "is not in scene space's current Layer Plan"),
        ("--layer with --draft refused", [*lay, "--layer", "ships", "--draft"], "not both"),
        ("--emissive without --layer refused", [*lay, "--draft", "--emissive"],
         "needs --layer"),
        ("a --size off the Frame's aspect ratio refused",
         [*lay, "--layer", "ships", "--size", "1536x1024"],
         "doesn't match the Frame's aspect ratio"),
        ("--preset on a Layer generation refused", [*lay, "--layer", "ships", "--preset", "page"],
         "only a Combined Image gets"),
        ("--final-size on a Draft refused", [*lay, "--draft", "--final-size", "800x450"],
         "only a Combined Image gets"),
        ("a masked Layer generation editing a Combined Image refused",
         [*SP, "--prompt-file", str(mprompt), "--layer", "ships", "--backend", "api",
          "--attach", "space/v004/image.png:EDIT TARGET", *A, "--mask", small,
          "--size", "192x108"], "repaints its starting version itself"),
        ("a Draft as a Layer's EDIT TARGET refused",
         [*lay, "--layer", "ships", "--attach", "space/drafts/v001/image.png:EDIT TARGET"],
         "a Draft is a reference for placement"),
        ("another scene's image as a Layer's EDIT TARGET refused",
         [*lay, "--layer", "ships", "--attach", "scene-a/v001/image.png:EDIT TARGET"],
         "import content"),
        ("a package asset's reference.png as a Layer's EDIT TARGET refused",
         [*lay, "--layer", "ships", "--attach", "assets/people/tester/reference.png:EDIT TARGET"],
         "import content"),
        ("a User's file as a Layer's EDIT TARGET refused",
         [*lay, "--layer", "ships", "--attach", f"{user_png}:EDIT TARGET"], "import content"),
        ("a sources/ image without a sidecar as EDIT TARGET refused",
         [*lay, "--layer", "ships", "--attach", "space/sources/bare.png:EDIT TARGET"],
         "import content"),
        ("an adjusted copy whose source isn't what its sidecar records refused",
         [*lay, "--layer", "ships", "--attach", "space/sources/stale.png:EDIT TARGET"],
         "not the image its sidecar records"),
        ("a second EDIT TARGET on a Layer generation refused",
         [*lay, "--layer", "ships", "--attach", "space/v003/image.png:EDIT TARGET",
          "--attach", "space/layers/ships/v002/image.png:EDIT TARGET"], "at most one EDIT TARGET"),
        ("a same-scene image as a Layer's IDENTITY refused, naming PLACEMENT",
         [*lay, "--layer", "ships", "--attach", "space/layers/planet/v001/image.png:IDENTITY"],
         "as PLACEMENT"),
        ("another scene's image as a Layer's IDENTITY refused",
         [*lay, "--layer", "ships", "--attach", "scene-a/v001/image.png:IDENTITY"],
         "never takes"),
        ("a Layer Version off the Frame's aspect ratio attached refused",
         [*lay, "--layer", "asteroids", *PL("space/layers/ships/v003/image.png")],
         "doesn't match the Frame's aspect ratio"),
        ("a Draft off the Frame's aspect ratio attached refused",
         [*lay, "--layer", "asteroids", *PL("space/drafts/v002/image.png")],
         "doesn't match the Frame's aspect ratio"),
        ("a package image as PLACEMENT refused",
         [*lay, "--layer", "ships", *PL("assets/people/tester/reference.png")],
         "can't be PLACEMENT"),
        ("PLACEMENT on a Draft generation refused",
         [*lay, "--draft", *PL("space/v003/image.png")], "for a Layer generation (--layer) only"),
        ("PLACEMENT on a Single-Layer Scene refused",
         ["--scene", "single-gen", "--prompt-file", str(prompt), *A,
          *PL("scene-a/v001/image.png")], "for a Layer generation (--layer) only"),
        ("an altered Layer Version attached refused, naming it",
         [*lay, "--layer", "ships", *PL("space/layers/asteroids/v001/image.png")],
         "output:space/layers/asteroids/v001/image.png is altered"),
    ]:
        before = sorted(tmp.rglob("*"))
        code, msg = gen_run(None, *args, *DRY)
        report(name, code != 0 and expect in msg and "Traceback" not in msg
               and sorted(tmp.rglob("*")) == before,
               f"expected {expect!r} and nothing written, exit {code}:\n{msg}")
    code, msg = gen_run(None, "--asset", "people/tester", "--layer", "x",
                        "--prompt-file", str(prompt), *A, *DRY)
    report("--layer with --asset refused", code != 0 and "no meaning with --asset" in msg, msg)

    for name, args, expect in [
        ("combine on a Single-Layer Scene refused", ["single-gen"], "not a Layered Scene"),
        ("combine with no counting version refused", ["empty-l"], "nothing to combine"),
        ("combine --use of a Layer not in the plan refused", ["space", "--use", "moon=v001"],
         "is not in the current Layer Plan"),
        ("combine --use of a version that doesn't exist refused",
         ["space", "--use", "ships=v009"], "has no such version"),
        ("a malformed combine --use refused", ["space", "--use", "ships"], "ID=vNNN"),
        ("combine --only naming a Layer not in the plan refused",
         ["space", "--only", "planet,moon"], "is not in the current Layer Plan"),
        ("combine --use of a Layer --only leaves out refused",
         ["space", "--only", "planet", "--use", "ships=v001"], "--only leaves out"),
        ("combine naming a version off the Frame's aspect ratio refused",
         ["space", "--only", "planet,ships", "--use", "ships=v003"],
         "ships's v003 is 150x150, which doesn't match the Frame's aspect ratio"),
        ("combine naming a deleted version refused",
         ["space", "--only", "planet,ships", "--use", "ships=v004"], "is deleted"),
        ("combine refuses an altered Layer Version, naming the file",
         ["space"], "output:space/layers/asteroids/v001/image.png is altered"),
        ("rebuild refuses a stack naming an altered version", None, "is altered"),
        ("rebuild refuses a folder with no Combined Image receipt", None,
         "no Combined Image receipt"),
    ]:
        if name.startswith("combine with no counting"):
            plan("empty-l", *LF, "--layer", "a=A", "--layer", "b=B", *YES, "--based-on", "0")
        before = sorted(tmp.rglob("*"))
        if args is None:
            code, msg = layers_cmd("rebuild", "space", "--combined",
                                   "v002" if "altered" in name else "v099")
        else:
            code, msg = layers_cmd("combine", *args)
        report(name, code != 0 and expect in msg and "Traceback" not in msg
               and sorted(tmp.rglob("*")) == before,
               f"expected {expect!r} and nothing written, exit {code}:\n{msg}")
    rocks.write_bytes(saved_rocks)

    # positive controls for the attachment rules, and the block warning
    (out / "space/sources/soft.png").write_bytes(
        (out / "space/layers/asteroids/v001/image.png").read_bytes())
    (out / "space/sources/soft.md").write_text(
        f"Derived from: output:space/layers/asteroids/v001/image.png "
        f"md5={gen.md5(rocks)}\nCommand: magick image.png -blur 0x1 soft.png\n")
    before = sorted(tmp.rglob("*"))
    for name, args, expect in [
        ("a same-scene Layer Version as EDIT TARGET is accepted",
         [*lay, "--layer", "ships", "--attach", "space/layers/ships/v002/image.png:EDIT TARGET"],
         "invariants OK"),
        ("an adjusted copy in sources/ with its sidecar as EDIT TARGET is accepted",
         [*lay, "--layer", "asteroids", "--attach", "space/sources/soft.png:EDIT TARGET"],
         "invariants OK"),
        ("an asset's reference.png and an output:sources/ crop as a Layer's IDENTITY are "
         "accepted",
         [*lay, "--layer", "ships", "--attach", "assets/people/tester/reference.png:IDENTITY",
          "--attach", "sources/tester-crop.png:IDENTITY"], "invariants OK"),
        ("an attachment with alpha is named as sent flattened in a dry run",
         [*lay, "--layer", "ships", *PL("space/v001/image.png")],
         "(has alpha: sent flattened onto black)"),
        ("a Layer above the bottom whose prompt lacks the block warns",
         [*SP, "--layer", "asteroids", "--prompt-file", str(prompt), *A],
         "lacks the transparent-background block"),
    ]:
        code, msg = gen_run(None, *args, *DRY)
        report(name, code == 0 and expect in msg and "invariants OK" in msg, msg)
    report("Layer dry runs wrote nothing", sorted(tmp.rglob("*")) == before)

    # the separation checks on synthetic outputs; an emissive repair and a failure,
    # each recorded on a real Layer generation
    S = "96x54"
    c = lambda colour, r: disc(colour, 48, 27, r)
    checks_cases = [
        ("no alpha", [S, "xc:#3366aa", *c("#cc2222", 15)], ["NO_ALPHA"]),
        ("opaque everywhere", [S, "xc:#3366aa", "-alpha", "set", "-define",
                               "png:color-type=6"], ["OPAQUE_EVERYWHERE"]),
        ("a painted checkerboard", [S, "pattern:checkerboard", *c("#cc2222", 10)],
         ["NO_ALPHA", "PAINTED_CHECKERBOARD_OR_FLAT_LIGHT_BACKDROP"]),
        ("a green backdrop left in", [S, "xc:#00ff00", *c("#cc2222", 15)],
         ["NO_ALPHA", "BACKDROP_LEFT_IN_GREEN"]),
        ("a magenta backdrop left in", [S, "xc:#ff00ff", *c("#cc2222", 15)],
         ["NO_ALPHA", "BACKDROP_LEFT_IN_MAGENTA"]),
        ("a black backdrop left in", [S, "xc:black", *c("#cc2222", 15)],
         ["NO_ALPHA", "BACKDROP_LEFT_IN_BLACK"]),
        ("a green fringe", [S, "xc:none", *c("#00ee00", 15), *c("#cc2222", 13)],
         ["GREEN_FRINGE"]),
        ("a dark fringe", [S, "xc:none", *c("#050505", 15), *c("#cc2222", 13)],
         ["DARK_FRINGE"]),
        ("a light fringe", [S, "xc:none", *c("#ffffff", 15), *c("#cc2222", 13)],
         ["LIGHT_FRINGE"]),
        ("a clean cut-out passes", [S, "xc:none", *c("#cc2222", 15)], []),
        ("a partly transparent full-frame haze passes",
         [S, "gradient:rgba(80,110,200,0.25)-rgba(120,90,200,0.6)"], []),
    ]
    for name, args, expect in checks_cases:
        p = img(f"check-{len(expect)}-{checks}.png", "-size", *args)
        got = gen.separation_checks(p, False)
        report(f"separation check: {name}", [g.split("(")[0] for g in got] == expect,
               f"got {got}, expected {expect}")
    p = img("check-glow.png", "-size", S, "xc:none", *c("#0f0804", 20), *c("#ff9922", 8))
    report("separation check: glow baked onto dark, only when emissive",
           any(g.startswith("GLOW_BAKED_ON_DARK") for g in gen.separation_checks(p, True))
           and not any(g.startswith("GLOW") for g in gen.separation_checks(p, False)))

    plan("glowy", *LF, "--layer", "base=Night sky", "--layer", "glow=The engine glow",
         *YES, "--based-on", "0")
    code, msg = gen_run(glow_png, "--scene", "glowy", "--layer", "glow", "--emissive",
                        "--prompt-file", str(lblock), *A)
    gv, r = out / "glowy/layers/glow/v001", receipt("glowy/layers/glow/v001")
    text = (gv / "generation.md").read_text() if (gv / "generation.md").exists() else ""
    report("an emissive Layer's glow baked onto dark is unmultiplied and checked again",
           code == 0 and "GLOW_BAKED_ON_DARK" in r.get("Checks", "")
           and "Checks: round 2, after repair: pass" in text
           and r.get("Repair", "").startswith("glow baked onto dark, unmultiplied")
           and (gv / "raw.png").read_bytes() == glow_png.read_bytes()
           and gen.md5(gv / "image.png") != gen.md5(gv / "raw.png")
           and gen.identify(gv / "image.png") == (192, 108)
           and "separation check failed" not in msg, f"{msg}\n{text}")
    code, msg = gen_run(flat_png, "--scene", "glowy", "--layer", "glow",
                        "--prompt-file", str(lblock), *A)
    r = receipt("glowy/layers/glow/v002")
    report("a Layer that fails the checks is recorded, its failure printed with advice",
           code == 0 and r.get("Checks") == "round 1, raw output: NO_ALPHA"
           and "separation check failed: NO_ALPHA" in msg and "regenerate it" in msg
           and "Repair" not in r, f"{msg}\n{r}")
    code, msg = layers_cmd("combine", "glowy", "--use", "glow=v001", "--final-size", "192x108",
                           "--flatten", "#ff00ff")
    ci, dv = out / "glowy/v001/image.png", out / "glowy/v001/delivered-192x108.png"
    report("areas no Layer covers stay transparent, and show the flatten colour delivered",
           code == 0 and rgba(ci)[3] == 0 and dv.exists() and not gen.has_alpha(dv)
           and rgba(dv)[:3] == b"\xff\x00\xff", msg)

    # combine on a two-Layer and a six-Layer scene: subsets, named versions, and the
    # style-version and opaque-everywhere warnings (a haze Layer doesn't warn)
    def fake_version(slug: str, lid: str, image: Path, entry: str, style: str = "v1") -> str:
        """A Layer Version made with ImageMagick, in the Layer's next vNNN folder."""
        base = out / slug / "layers" / lid
        d = base / f"v{1 + max((int(p.name[1:]) for p in base.glob('v[0-9]*')), default=0):03d}"
        d.mkdir(parents=True)
        shutil.copyfile(image, d / "image.png")
        (d / "generation.md").write_text(
            f"# {slug} {lid} {d.name}\n\nStyle: {style}\nKind: Layer Version\nLayer: {lid}\n"
            f"Layer Entry: {entry}\nmd5: {gen.md5(image)}\nStatus: awaiting user evaluation\n"
            "Review: pending — record with review.py\n")
        return d.name

    plan("duo", *LF, "--layer", "bg=Sky", "--layer", "top=A wall", *YES, "--based-on", "0")
    fake_version("duo", "bg", flat_png, "Sky")
    fake_version("duo", "top", img("wall.png", "xc:#884422"), "A wall", style="v2")
    code, msg = layers_cmd("combine", "duo")
    r = receipt("duo/v001")
    warns = (out / "duo/v001/generation.md").read_text().count("Warning:")
    report("a two-Layer scene combines, warning of mixed style versions and an opaque "
           "upper Layer",
           code == 0 and len(r["stack"]) == 2 and warns == 2
           and "different style versions: bg v1, top v2" in msg
           and "Layer top (v001) is opaque everywhere" in msg, msg)
    code, msg = layers_cmd("combine", "duo", "--only", "top", "--use", "top=v001", "--dry-run")
    report("combine --only and --use pick a subset; a dry run writes nothing",
           code == 0 and "1 top v001  (named with --use" in msg and "bg v001" not in msg
           and not (out / "duo/v002").exists(), msg)

    six = ["base", "l2", "l3", "haze", "l5", "l6"]
    plan("six", *LF, *[x for lid in six for x in ("--layer", f"{lid}=Part {lid}")], *YES,
         "--based-on", "0")
    for i, lid in enumerate(six):
        if lid == "base":
            image = img("six-base.png", "gradient:#101830-#304070")
        elif lid == "haze":
            image = img("haze.png", "gradient:rgba(80,110,200,0.25)-rgba(120,90,200,0.6)")
        else:
            image = img(f"six-{lid}.png", "xc:none", *disc("#aa3344", 30 * i, 54, 10))
        fake_version("six", lid, image, f"Part {lid}")
    code, msg = layers_cmd("combine", "six")
    report("a six-Layer scene combines in plan order, and a haze Layer doesn't warn",
           code == 0 and [s["layer"] for s in receipt("six/v001")["stack"]] == six
           and "warn" not in msg, msg)

    code, msg = layers_cmd("status", "space")
    report("status reports nothing wrong once the altered image is restored",
           code == 0 and "layers/asteroids/v001/image.png is altered" not in msg, msg)

    # review.py and gen.py --refinish on Layer Versions and Combined Images
    for rel in ("space/layers/ships/v002", "space/v004"):
        code, msg = script("review.py", str(out / rel), "--review", "Plumbing only.")
        report(f"review.py records a review on {rel}",
               code == 0 and receipt(rel).get("Review") == "Plumbing only.", msg)
    code, msg = script("gen.py", *P, "--refinish", str(out / "space/v004"), "--final-size",
                       "800x450")
    report("gen.py --refinish derives a deliverable from a Combined Image",
           code == 0 and (out / "space/v004/delivered-800x450.png").exists()
           and receipt("space/v004").get("Delivered", "").startswith("delivered-800x450.png"),
           msg)

    # review findings: a black-backdrop glow is repaired, deliverables stay on Combined
    # Images, a posing file or looping sidecar is refused cleanly, and every same-scene
    # input carries its md5
    black_glow = img("black-glow.png", "xc:black", *disc("#ff9922", 96, 54, 12),
                     *disc("rgba(255,153,34,0.3)", 96, 54, 24))
    code, msg = gen_run(black_glow, "--scene", "glowy", "--layer", "glow", "--emissive",
                        "--prompt-file", str(lblock), *A)
    r = receipt("glowy/layers/glow/v003")
    text = (out / "glowy/layers/glow/v003/generation.md").read_text() if code == 0 else ""
    report("an emissive Layer's glow on an opaque black backdrop is unmultiplied",
           code == 0 and "GLOW_BAKED_ON_DARK" in r.get("Checks", "")
           and "Checks: round 2, after repair: pass" in text and "Repair" in r
           and "separation check failed" not in msg, f"{msg}\n{text}")
    before = sorted(tmp.rglob("*"))
    code, msg = script("gen.py", *P, "--refinish", str(out / "space/layers/ships/v001"),
                       "--final-size", "800x450")
    code2, msg2 = script("gen.py", *P, "--refinish", str(out / "space/drafts/v001"),
                         "--final-size", "800x450")
    report("gen.py --refinish refuses a Layer Version and a Draft, writing nothing",
           code != 0 and code2 != 0 and "only a Combined Image gets deliverables" in msg
           and "only a Combined Image gets deliverables" in msg2
           and sorted(tmp.rglob("*")) == before, msg + msg2)

    plan("posing", *LF, "--layer", "a=A", "--layer", "b=B", *YES, "--based-on", "0")
    svg = fxd / "posing.svg"
    svg.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/'
                   f'1999/xlink" width="192" height="108"><image xlink:href="{user_png}" '
                   'width="192" height="108"/></svg>')
    fake_version("posing", "a", svg, "A")
    for name, args, expect in [
        ("combine refuses a Layer Version that isn't a PNG, writing nothing",
         ["posing"], "could not stack"),
        ("combine refuses --final-size 0x0 before writing anything",
         ["space", "--final-size", "0x0"], "give WxH in pixels"),
    ]:
        before = sorted(tmp.rglob("*"))
        code, msg = layers_cmd("combine", *args)
        report(name, code != 0 and expect in msg and "Traceback" not in msg
               and sorted(tmp.rglob("*")) == before, msg)
    (out / "space/sources/loop.png").write_bytes(user_png.read_bytes())
    (out / "space/sources/loop.md").write_text(
        f"Derived from: output:space/sources/loop.png md5={gen.md5(user_png)}\n")
    code, msg = gen_run(None, *lay, "--layer", "ships", "--attach",
                        "space/sources/loop.png:EDIT TARGET", *DRY)
    report("a sidecar naming another sources/ image is not followed",
           code != 0 and "import content" in msg and "Traceback" not in msg, msg)
    code, msg = gen_run(draft_png, "--scene", "space", "--draft", "--prompt-file", str(prompt),
                        *A, "--attach", "space/sources/bare.png:IDENTITY")
    report("every same-scene input of a Draft carries its md5",
           code == 0 and f"output:space/sources/bare.png md5={gen.md5(user_png)}"
           in (out / "space/drafts/v003/generation.md").read_text(), msg)

    # decision 5: an identical plan is a no-op, refused
    before = journal("space")
    same = ["--layer", "planet=@1", "--layer", "asteroids=@1", "--layer", "ships=@1"]
    code, msg = plan("space", *LF, *same, *YES, "--based-on", "1")
    code2, msg2 = plan("space", *LF, *same, "--dry-run")
    report("an identical plan is refused as a no-op, dry run or not",
           code != 0 and code2 != 0 and "plan unchanged; nothing recorded" in msg
           and "plan unchanged" in msg2 and journal("space") == before, msg + msg2)

    # --- keeps and approvals: a bluer planet, keeps ended by an
    # approval, a Layer Entry change and a removal, then a scene approval and its copies
    def approve(rel: str, *args: str) -> tuple[int, str]:
        return script("promote.py", str(out / rel), *args)

    def status_of(slug: str) -> str:
        return layers_cmd("status", slug)[1]

    BP = "bluer"
    PE, AE, SE = ("The ringed planet and stars", "The asteroid field",
                  "The two ships and their engine glow")
    plan(BP, *LF, "--layer", f"planet={PE}", "--layer", f"asteroids={AE}",
         "--layer", f"ships={SE}", *YES, "--based-on", "0")
    blues = [img(f"blue{i}.png", f"xc:#2030{c}", *disc(f"#55{c}cc", 60, 54, 30))
             for i, c in ((1, "60"), (2, "90"), (3, "c0"), (4, "f0"))]
    rocks_a = img("rocks-a.png", "xc:none", *disc("#888070", 120, 40, 12))
    rocks_b = img("rocks-b.png", "xc:none", *disc("#888070", 140, 70, 10))
    fake_version(BP, "planet", blues[0], PE)
    pv1 = out / BP / "layers/planet/v001"

    code, msg = approve(f"{BP}/layers/planet/v001", "--dry-run")
    report("promote.py --dry-run on a Layer Version names what it approves and the number "
           "to pass", code == 0 and "as Layer planet's Approved Layer Version" in msg
           and "--based-on 1" in msg and journal(BP) == ["001.json"], msg)
    words = "Planet v1 is right.\nLock it in."
    code, msg = approve(f"{BP}/layers/planet/v001", "--approval", words, "--based-on", "1")
    rec = record(BP, 2) if code == 0 else {}
    report("approving a Layer Version on its own writes one Layer approval record, words "
           "verbatim", code == 0 and rec.get("kind") == "layer-approval"
           and (rec.get("layer"), rec.get("version")) == ("planet", "v001")
           and rec.get("md5") == gen.md5(pv1 / "image.png") and rec.get("words") == words
           and rec.get("replaces") is None
           and "Status: approved as Layer planet's Approved Layer Version on " in
           (pv1 / "generation.md").read_text() and not (out / BP / "final.png").exists(),
           f"{msg}\n{rec}")

    fake_version(BP, "asteroids", rocks_a, AE)
    fake_version(BP, "ships", ships_png, SE)
    code, msg = layers_cmd("combine", BP)
    report("a Layer approved before the others had versions is in later Combined Images",
           code == 0 and [(s["layer"], s["path"][-4:], s["approved"]) for s in
                          receipt(f"{BP}/v001")["stack"]]
           == [("planet", "v001", "yes"), ("asteroids", "v001", "no"), ("ships", "v001", "no")]
           and "1 planet v001  (its Default Version; its Approved Layer Version)" in msg, msg)
    code, msg = approve(f"{BP}/layers/ships/v001", "--approval", "Those ships, yes.",
                        "--based-on", "2")
    fake_version(BP, "asteroids", rocks_b, AE)
    code2, msg2 = layers_cmd("combine", BP, "--use", "asteroids=v002", "--mode", "asteroid step")
    report("the next asteroid step's Combined Image holds the approved planet and ships",
           code == code2 == 0 and [(s["layer"], s["path"][-4:], s["approved"]) for s in
                                   receipt(f"{BP}/v002")["stack"]]
           == [("planet", "v001", "yes"), ("asteroids", "v002", "no"), ("ships", "v001", "yes")],
           msg + msg2)

    # the bluer planet: v2 kept, v3 shown but not kept, then v3 approved over v1
    fake_version(BP, "planet", blues[1], PE)
    layers_cmd("combine", BP, "--use", "planet=v002", "--mode", "bluer planet step")
    code, msg = layers_cmd("keep", BP, "--layer", "planet", "--version", "v002",
                           "--words", "Close, but bluer still.", "--dry-run")
    code2, msg2 = layers_cmd("keep", BP, "--layer", "planet", "--version", "v002",
                             "--words", "Close, but bluer still.", "--based-on", "3")
    rec = record(BP, 4) if code2 == 0 else {}
    st = status_of(BP)
    report("keeping planet v2 makes it the Default Version without approving it",
           code == code2 == 0 and "--based-on 3" in msg and journal(BP)[-1] == "004.json"
           and rec.get("kind") == "keep" and rec.get("version") == "v002"
           and rec.get("md5") == gen.md5(out / BP / "layers/planet/v002/image.png")
           and "      Default Version: v002 (kept); Approved Layer Version: v001" in st
           and "      kept: v002 in journal/004.json, " in st, msg + msg2 + st)
    fake_version(BP, "planet", blues[2], PE)
    st = status_of(BP)
    code, msg = layers_cmd("combine", BP, "--mode", "ships step")
    report("a newer planet v3 doesn't end the keep, and status says v3 isn't the Default "
           "Version", code == 0 and "      Default Version: v002 (kept); Approved Layer "
           "Version: v001" in st and "its newest counting version, v003, isn't its Default "
           "Version" in st and receipt(f"{BP}/v004")["stack"][0]["path"].endswith("planet/v002"),
           st + msg)
    code, msg = approve(f"{BP}/layers/planet/v003", "--approval", "That blue.", "--based-on", "4")
    report("approving planet v3 over v1 without --replace is refused, naming v1",
           code != 0 and "Approved Layer Version is v001 (journal/002.json" in msg
           and "--replace" in msg and journal(BP)[-1] == "004.json", msg)
    code, msg = approve(f"{BP}/layers/planet/v003", "--approval", "That blue. Approve it.",
                        "--based-on", "4", "--replace")
    rec, st = (record(BP, 5) if code == 0 else {}), status_of(BP)
    report("approving planet v3 with --replace replaces v1 and ends the keep",
           code == 0 and rec.get("replaces") == {"record": 2, "version": "v001"}
           and "it replaces v001 (journal/002.json)" in msg
           and "      Default Version: v003 (its Approved Layer Version); Approved Layer "
               "Version: v003" in st and "kept: v002" not in st, msg + st)

    # keeps end, for good, on a Layer Entry change and on a removal
    layers_cmd("keep", BP, "--layer", "asteroids", "--version", "v001", "--words", "Keep the "
               "first field.", "--based-on", "5")
    st = status_of(BP)
    report("a keep in force can name a version older than the Layer's latest",
           "      Default Version: v001 (kept); Approved Layer Version: none" in st
           and "its newest counting version, v002, isn't its Default Version" in st, st)
    keep_plan = ["--layer", "planet=@1", "--layer", "asteroids=The asteroid field and dust",
                 "--layer", "ships=@1"]
    code, msg = plan(BP, *LF, *keep_plan, *YES, "--based-on", "6")
    code2, msg2 = plan(BP, *LF, "--layer", "planet=@1", "--layer", "asteroids=@1",
                       "--layer", "ships=@1", *YES, "--based-on", "7")
    st = status_of(BP)
    report("a keep ends on a Layer Entry change, and changing it back doesn't restore it",
           code == code2 == 0 and "kept: v001 in journal/006.json" not in st
           and "      Default Version: v002 (its latest version); Approved Layer Version: none"
           in st, msg + msg2 + st)
    fake_version(BP, "ships", ships2_png, SE)
    layers_cmd("keep", BP, "--layer", "ships", "--version", "v002", "--words", "Use these.",
               "--based-on", "8")
    code, msg = plan(BP, *LF, "--layer", "planet=@1", "--layer", "asteroids=@1", *YES,
                     "--based-on", "9")
    st_removed = status_of(BP)
    code2, msg2 = plan(BP, *LF, "--layer", "planet=@1", "--layer", "asteroids=@1",
                       "--layer", "ships=@1", *YES, "--based-on", "10")
    st = status_of(BP)
    report("a keep ends on its Layer's removal; put back, the Layer's approval counts again "
           "and the keep doesn't", code == code2 == 0
           and "  removed Layers:" in st_removed and "kept: v002" not in st_removed
           and "      Approved Layer Version: v001" in st_removed
           and "      Default Version: v001 (its Approved Layer Version); Approved Layer "
               "Version: v001" in st and "kept: v002" not in st, st_removed + st)

    # Combined Images built by plan changes: the Layer Entry change built nothing (asteroids then had no
    # counting version), changing it back, the removal and the put-back each built one
    stacks = {v: [(s["layer"], s["path"][-4:]) for s in receipt(f"{BP}/{v}").get("stack", [])]
              for v in ("v005", "v006", "v007")}
    report("plan builds its Combined Image on a change back, a removal and a put-back, and "
           "none on a change whose Layer has no counting version",
           not (out / BP / "v008").exists() and stacks == {
               "v005": [("planet", "v003"), ("asteroids", "v002"), ("ships", "v001")],
               "v006": [("planet", "v003"), ("asteroids", "v002")],
               "v007": [("planet", "v003"), ("asteroids", "v002"), ("ships", "v001")]}
           and receipt(f"{BP}/v007").get("Mode") == "Layer Plan change, journal/011.json: puts "
               "back Layer ships, with its Layer Entry from plan record 8"
           and receipt(f"{BP}/v007").get("User request verbatim") == "Yes."
           and receipt(f"{BP}/v007").get("Layer Plan") == "journal/011.json",
           f"{stacks}\n{receipt(f'{BP}/v007')}")

    # the scene approval: one record, then final.png, final.md and final-layers/
    code = 0
    st = status_of(BP)
    code2, msg2 = approve(f"{BP}/v007", "--dry-run")
    code3, msg3 = approve(f"{BP}/v007", "--approval", "Approve the scene.", "--based-on", "11")
    rec = record(BP, 12) if code3 == 0 else {}
    held = [("planet", "v003"), ("asteroids", "v002"), ("ships", "v001")]
    files = sorted(p.name for p in (out / BP / "final-layers").iterdir()) \
        if (out / BP / "final-layers").is_dir() else []
    report("status lists the Combined Image as approvable, and the dry run names its Layers",
           code == code2 == 0 and re.search(r"^  can be approved now: .*\bv007$", st, re.M)
           and "planet v003, asteroids v002, ships v001" in msg2 and "--based-on 11" in msg2,
           st + msg2)
    report("approving a Combined Image writes one scene approval record, final.png, final.md "
           "and one byte-identical Layer file per Layer",
           code3 == 0 and journal(BP)[-1] == "012.json" and rec.get("kind") == "scene-approval"
           and rec.get("combined") == f"output:{BP}/v007"
           and [(l["layer"], l["version"]) for l in rec.get("layers", [])] == held
           and (out / BP / "final.png").read_bytes() == (out / BP / "v007/image.png").read_bytes()
           and (out / BP / "final.md").read_text() == scene_state.final_md(rec)
           and files == ["01-planet.png", "02-asteroids.png", "03-ships.png"]
           and all((out / BP / "final-layers" / f"{i:02d}-{l}.png").read_bytes()
                   == (out / BP / "layers" / l / v / "image.png").read_bytes()
                   for i, (l, v) in enumerate(held, start=1))
           and "approved and promoted to final.png" in receipt(f"{BP}/v007").get("Status", "")
           and "approved in Combined Image v007" in
               receipt(f"{BP}/layers/asteroids/v002").get("Status", ""), f"{msg3}\n{rec}")
    finals = {p: p.read_bytes() for p in [out / BP / "final.png", out / BP / "final.md",
                                         *(out / BP / "final-layers").iterdir()]}

    fake_version(BP, "ships", ships2_png, SE)
    code, msg = approve(f"{BP}/layers/ships/v003", "--approval", "Smaller ships, approved.",
                        "--based-on", "12", "--replace")
    report("approving a new ships version after the scene approval leaves the approved image "
           "and Layer files unchanged, and says so",
           code == 0 and "the scene's approved image, v007, holds ships v001" in msg
           and {p: p.read_bytes() for p in finals if p.exists()} == finals
           and sorted(p.name for p in (out / BP / "final-layers").iterdir()) == files, msg)

    shutil.rmtree(out / BP / "final-layers")
    st = status_of(BP)
    code, msg = approve(f"{BP}/v007")
    report("missing Layer files show in status; promote.py completes them from the record "
           "without writing another", "final-layers/ is missing: run promote.py on v007" in st
           and code == 0 and "completing the copies" in msg and journal(BP)[-1] == "013.json"
           and {p: p.read_bytes() for p in finals if p.exists()} == finals
           and "integrity problems: none" in status_of(BP), st + msg)
    code, msg = approve(f"{BP}/v007", "--approval", "Again.", "--based-on", "13")
    report("once the copies match, approving that Combined Image again is a new approval, "
           "naming what it replaces", code != 0 and "the approved image v007 (journal/012.json)"
           in msg and "Layer ships's Approved Layer Version v003 (journal/013.json" in msg, msg)
    code, msg = approve(f"{BP}/v007", "--based-on", "13")
    report("a new Combined Image approval without --approval refused",
           code != 0 and "--approval is required" in msg, msg)

    fake_version(BP, "planet", blues[3], PE)
    layers_cmd("keep", BP, "--layer", "planet", "--version", "v004", "--words", "Keep v4.",
               "--based-on", "13")
    st = status_of(BP)
    report("status reports approvals with their words, keeps, Default Versions, the "
           "approvable Combined Images and the approved one with its Layer files",
           "      approved in journal/012.json, " in st
           and "      approved in journal/013.json, " in st and ": Smaller ships, approved." in st
           and "      kept: v004 in journal/014.json, " in st
           and "      Default Version: v004 (kept); Approved Layer Version: v003" in st
           and "      Default Version: v003 (its Approved Layer Version); Approved Layer "
               "Version: v003" in st
           and "  can be approved now: " in st
           and "  approved image: v007, approved in journal/012.json" in st
           and "    final-layers/03-ships.png: ships v001" in st, st)

    # check-delete: approved and used versions never; others under today's rule
    for name, rel, ok, expect in [
        ("check-delete refuses a version approved on its own and in no Combined Image",
         f"{BP}/layers/ships/v003", False, "it is Layer ships's Approved Layer Version"),
        ("check-delete refuses a version a Combined Image uses, naming each",
         f"{BP}/layers/asteroids/v001", False, "Combined Images v001 name it"),
        ("check-delete refuses an approved version a Combined Image uses, naming both",
         f"{BP}/layers/planet/v003", False, "Approved Layer Version (journal/012.json"),
        ("check-delete refuses a folder that isn't a record folder", f"{BP}/journal", False,
         "is not one of scene bluer's"),
        ("check-delete allows an unused, unapproved version under today's rule",
         f"{BP}/layers/ships/v002", True, "may be deleted under today's rule"),
        ("check-delete says deleting a kept version ends its keep",
         f"{BP}/layers/planet/v004", True, "deleting it ends its keep (journal/014.json)"),
        ("check-delete refuses the scene's approved Combined Image, naming it",
         f"{BP}/v007", False, "it is the scene's approved image (journal/012.json)"),
        ("check-delete allows a Combined Image that isn't the approved one",
         f"{BP}/v004", True, "may be deleted under today's rule"),
    ]:
        before = sorted(tmp.rglob("*"))
        code, msg = layers_cmd("check-delete", BP, str(out / rel))
        report(name, (code == 0) == ok and expect in msg and "Traceback" not in msg
               and sorted(tmp.rglob("*")) == before, msg)
    code, msg = layers_cmd("check-delete", BP, str(out / BP / "layers/ships/v099"))
    report("check-delete refuses a folder that doesn't exist",
           code != 0 and "doesn't exist" in msg and "Traceback" not in msg, msg)
    (out / BP / "final-layers/.DS_Store").write_text("finder")
    shutil.rmtree(out / BP / "layers/planet/v004")   # by hand, with no deletion log
    st = status_of(BP)
    report("status ignores a dotfile in final-layers/ and names a kept folder that's gone",
           "final-layers/.DS_Store" not in st and "journal/014.json (keep) names planet v004, "
           "whose folder is gone" in st, st)
    code, msg = layers_cmd("check-delete", "single-gen", str(out / "single-gen/v001"))
    report("check-delete refuses a Single-Layer Scene", code != 0 and "not a Layered Scene"
           in msg, msg)

    # each refusal by name, on a scene whose plan changes under its Combined Images
    C = "cond"
    plan(C, *LF, "--layer", "a=Part a", "--layer", "b=Part b", "--layer", "c=Part c", *YES,
         "--based-on", "0")
    for lid, x in (("a", 40), ("b", 90), ("c", 140)):
        fake_version(C, lid, img(f"cond-{lid}.png", "xc:none", *disc("#aa3344", x, 54, 12)),
                     f"Part {lid}")
    fake_version(C, "a", square_png, "Part a")   # a v002, off the Frame's aspect ratio
    layers_cmd("combine", C)                      # v001: a, b, c
    layers_cmd("combine", C, "--only", "a,b")     # v002: c missing
    (out / C / "drafts/v001").mkdir(parents=True)
    shutil.copyfile(draft_png, out / C / "drafts/v001/image.png")
    (out / C / "drafts/v001/generation.md").write_text(
        f"# cond draft v001\n\nKind: Draft\nmd5: {gen.md5(draft_png)}\n")
    b1 = out / C / "layers/b/v001/image.png"
    saved_b1 = b1.read_bytes()

    def refusals(rows) -> None:
        for name, args, expect, prep in rows:
            if prep:
                prep()
            before = sorted(tmp.rglob("*"))
            code, msg = (approve(*args[1:]) if args[0] == "promote"
                         else layers_cmd(args[0], C, *args[1:]))
            report(name, code != 0 and expect in msg and "Traceback" not in msg
                   and sorted(tmp.rglob("*")) == before,
                   f"expected {expect!r} and nothing written, exit {code}:\n{msg}")
            b1.write_bytes(saved_b1)

    AP = ["--approval", "Yes."]
    refusals([
        ("a Draft approval refused", ["promote", f"{C}/drafts/v001", *AP, "--based-on", "1"],
         "is a Draft", None),
        ("a Layer Version approval without --approval refused",
         ["promote", f"{C}/layers/a/v001", "--based-on", "1"], "--approval is required", None),
        ("a Layer Version approval without --based-on refused",
         ["promote", f"{C}/layers/a/v001", *AP], "--based-on is required", None),
        ("a stale --based-on on promote.py refused",
         ["promote", f"{C}/layers/a/v001", *AP, "--based-on", "0"],
         "show the User its new state", None),
        ("a Layer Version approval at the wrong aspect ratio refused, naming it",
         ["promote", f"{C}/layers/a/v002", *AP, "--based-on", "1"],
         "Layer a's v002 can't be approved: 150x150 doesn't match the Frame's aspect ratio",
         None),
        ("a Combined Image missing a Layer refused, naming it",
         ["promote", f"{C}/v002", *AP, "--based-on", "1"],
         "c: missing from the Combined Image", None),
        ("a Combined Image holding an altered Layer Version refused, naming the file",
         ["promote", f"{C}/v001", *AP, "--based-on", "1"],
         "output:cond/layers/b/v001/image.png is altered",
         lambda: magick(str(b1), "-fill", "#ffffff", "-draw", "point 1,1", str(b1))),
        ("a keep of a version that doesn't count refused",
         ["keep", "--layer", "a", "--version", "v002", "--words", "Keep.", "--based-on", "1"],
         "Layer a's v002 doesn't count (150x150 doesn't match", None),
        ("a keep of a version that doesn't exist refused",
         ["keep", "--layer", "a", "--version", "v009", "--words", "Keep.", "--based-on", "1"],
         "has no version v009", None),
        ("a keep of a Layer not in the plan refused",
         ["keep", "--layer", "moon", "--version", "v001", "--words", "Keep.", "--based-on", "1"],
         "is not in the current Layer Plan", None),
        ("a keep without --based-on refused",
         ["keep", "--layer", "a", "--version", "v001", "--words", "Keep."],
         "--based-on is required", None),
        ("a stale --based-on on keep refused",
         ["keep", "--layer", "a", "--version", "v001", "--words", "Keep.", "--based-on", "0"],
         "show the User its new state", None),
        ("a keep of an altered version refused, naming the file",
         ["keep", "--layer", "b", "--version", "v001", "--words", "Keep.", "--based-on", "1"],
         "output:cond/layers/b/v001/image.png is altered",
         lambda: magick(str(b1), "-fill", "#ffffff", "-draw", "point 1,1", str(b1))),
    ])
    layers_cmd("keep", C, "--layer", "b", "--version", "v001", "--words", "Keep b.",
               "--based-on", "1")
    plan(C, *LF, "--layer", "b=@1", "--layer", "a=@1", "--layer", "c=@1", *YES,
         "--based-on", "2")                         # 3: reordered
    plan(C, *LF, "--layer", "b=@1", "--layer", "a=@1", *YES, "--based-on", "3")   # 4: no c
    layers_cmd("combine", C)                        # v003: b, a
    plan(C, *LF, "--layer", "b=@1", "--layer", "a=Part a, changed", *YES,
         "--based-on", "4")                         # 5: a's Layer Entry changed
    refusals([
        ("a keep already in force recorded again refused",
         ["keep", "--layer", "b", "--version", "v001", "--words", "Keep.", "--based-on", "5"],
         "already kept", None),
        ("a Combined Image in an old order refused, naming the Layers",
         ["promote", f"{C}/v001", *AP, "--based-on", "5"], "a: in an old order", None),
        ("a Combined Image holding a removed Layer refused, naming it",
         ["promote", f"{C}/v001", *AP, "--based-on", "5"], "c: removed", None),
        ("a Combined Image made under a different Layer Entry refused, naming the Layer",
         ["promote", f"{C}/v003", *AP, "--based-on", "5"],
         "a: v001 is made under a different Layer Entry", None),
        ("a removed Layer's version approval refused", ["promote", f"{C}/layers/c/v001", *AP,
                                                         "--based-on", "5"],
         "its Layer is removed", None),
        ("a Layer Version made under another Layer Entry refused",
         ["promote", f"{C}/layers/a/v001", *AP, "--based-on", "5"],
         "made under another Layer Entry", None),
    ])

    # a version replaced along with its receipt's md5 is still caught by the journal's md5
    b1_md = out / C / "layers/b/v001/generation.md"
    saved_md = b1_md.read_text()
    magick("-size", "192x108", "xc:none", *disc("#33aa44", 60, 54, 12), str(b1))
    b1_md.write_text(re.sub(r"^md5: .*$", f"md5: {gen.md5(b1)}", saved_md, flags=re.M))
    before = sorted(tmp.rglob("*"))
    code, msg = layers_cmd("combine", C)
    st = status_of(C)
    report("a kept version that isn't the md5 its keep record holds is refused by combine "
           "and named by status", code != 0 and "that journal/002.json records" in msg
           and "layers/b/v001/image.png is not the md5" in st and "Traceback" not in msg
           and sorted(tmp.rglob("*")) == before, msg + st)
    b1.write_bytes(saved_b1)
    b1_md.write_text(saved_md)

    # a two-Layer and a six-Layer scene each approved; folders named layers/ or drafts/ in a
    # scene that isn't layered promote as today
    for slug, n in (("duo", 2), ("six", 6)):
        code, msg = approve(f"{slug}/v001", "--approval", "Approved.", "--based-on", "1")
        report(f"a {n}-Layer scene's Combined Image is approved, with {n} Layer files",
               code == 0 and len(list((out / slug / "final-layers").iterdir())) == n
               and record(slug, 2).get("kind") == "scene-approval", msg)
    (out / "duo/final.png").chmod(0o444)
    before = sorted(tmp.rglob("*"))
    code, msg = approve("duo/v001", "--approval", "Again.", "--based-on", "2", "--replace")
    report("a scene approval whose final.png can't be replaced is refused before recording",
           code != 0 and "can't be replaced" in msg and "Traceback" not in msg
           and journal("duo") == ["001.json", "002.json"] and sorted(tmp.rglob("*")) == before,
           msg)
    (out / "duo/final.png").chmod(0o644)
    (out / "drafts/v001").mkdir(parents=True)
    magick("-size", "64x64", "xc:#445566", str(out / "drafts/v001/image.png"))
    (out / "drafts/v001/generation.md").write_text("# drafts v001\n\nStatus: awaiting user "
                                                   "evaluation\n")
    code, msg = approve("drafts/v001", "--approval", "Yes.")
    report("a scene named drafts, not layered, promotes as today",
           code == 0 and (out / "drafts/final.png").exists(), msg)

    # --- revising one Layer: starting versions, fixes recorded
    # with layers.py record, path 3 and a moved ship, and path 4's colour-only merge
    R = "rev"
    plan(R, *LF, "--layer", f"planet={PE}", "--layer", f"asteroids={AE}",
         "--layer", f"ships={SE}", *YES, "--based-on", "0")
    fake_version(R, "planet", blues[0], PE)
    fake_version(R, "asteroids", rocks_a, AE)
    fake_version(R, "ships", ships_png, SE)
    fake_version(R, "ships", ships2_png, SE)          # ships v002, the Default Version
    layers_cmd("combine", R, "--use", "ships=v001")   # v001 holds ships v001
    layers_cmd("combine", R)                          # v002 holds ships v002
    layers_cmd("combine", R, "--only", "planet,asteroids")   # v003 holds no ships
    (out / R / "sources").mkdir()
    shutil.copyfile(user_png, out / R / "sources/bare.png")
    shutil.copyfile(out / R / "v001/image.png", out / R / "sources/held.png")
    (out / R / "sources/held.md").write_text(
        f"Derived from: output:{R}/v001/image.png md5={gen.md5(out / R / 'v001/image.png')}\n"
        "Command: magick image.png -modulate 100,90 held.png\n")
    shutil.copyfile(out / R / "layers/ships/v002/image.png", out / R / "sources/ship-adj.png")
    (out / R / "sources/ship-adj.md").write_text(
        f"Derived from: output:{R}/layers/ships/v002/image.png "
        f"md5={gen.md5(out / R / 'layers/ships/v002/image.png')}\n"
        "Command: magick image.png -modulate 100,90 ship-adj.png\n")
    RS = ["--scene", R, "--prompt-file", str(lblock), *A, "--layer", "ships"]
    ET = lambda rel: ["--attach", f"{R}/{rel}:EDIT TARGET"]
    RP = lambda rel: PL(f"{R}/{rel}")
    for name, args, ok, expect in [
        ("a Layer generation starting from a version that isn't the Default Version warns, "
         "naming both", ET("layers/ships/v001/image.png"), True,
         "the starting version, ships v001, isn't Layer ships's Default Version (v002, latest)"),
        ("an edit attaching an image that holds another version of its Layer refused",
         ET("layers/ships/v002/image.png") + RP("v001/image.png"), False,
         "holds Layer ships's v001, but this generation starts from v002"),
        ("a fresh generation attaching a Combined Image holding a version of its Layer refused",
         RP("v001/image.png"), False, "holds Layer ships's v001, but this generation is fresh"),
        ("a fresh generation attaching an adjusted copy holding a version of its Layer refused",
         RP("sources/held.png"), False, "holds Layer ships's v001, but this generation is fresh"),
        ("an edit from the Default Version attaching a Combined Image holding it is accepted, "
         "without the warning", ET("layers/ships/v002/image.png") + RP("v002/image.png"), True,
         "invariants OK"),
        ("a fresh generation attaching a Combined Image without its Layer is accepted",
         RP("v003/image.png"), True, "invariants OK"),
    ]:
        before = sorted(tmp.rglob("*"))
        code, msg = gen_run(None, *RS, *args, *DRY)
        report(name, (code == 0) == ok and expect in msg and "Traceback" not in msg
               and (not ok or "isn't Layer ships's Default" not in msg or "warns" in name)
               and sorted(tmp.rglob("*")) == before, f"expected {expect!r}, exit {code}:\n{msg}")

    for name, args, expect in [
        ("a scene-folder copy (raw.png) attached to a Layer generation refused, in any role",
         ["--attach", "space/layers/planet/v001/raw.png:STYLE"], "lies in the scene's folder"),
        ("--emissive on a masked Layer generation refused",
         ["--emissive", "--backend", "api", "--mask", small], "no meaning on a masked Layer"),
    ]:
        before = sorted(tmp.rglob("*"))
        code, msg = gen_run(None, *lay, "--layer", "ships", *args, *DRY)
        report(name, code != 0 and expect in msg and "Traceback" not in msg
               and sorted(tmp.rglob("*")) == before, msg)

    def region_replace(start: Path, donor: Path, mask_png: Path, dest: Path) -> str:
        """Inside the mask, colour and alpha are the mask-weighted mix of the two
        images' premultiplied values; outside it nothing changes."""
        mix = lambda c: f"((1-wm)*u.{c}*u.a+wm*v.{c}*v.a)/max(aa,1e-9)"
        cmd = ["magick", "(", str(start), "-colorspace", "sRGB", ")", "(", str(donor),
               "-colorspace", "sRGB", ")", "(", str(mask_png), "-alpha", "off",
               "-colorspace", "Gray", ")", "-alpha", "set", "-fx",
               f"wm=u[2].r; aa=(1-wm)*u.a+wm*v.a; channel({mix('r')},{mix('g')},{mix('b')},0,aa)",
               "-define", "png:color-type=6", str(dest)]
        subprocess.run(cmd, check=True, capture_output=True)
        return " ".join(cmd)

    def differs_only_where(ci_a: Path, ci_b: Path, old: Path, new: Path) -> tuple[int, list]:
        a, b = rgba(ci_a), rgba(ci_b)
        o, n = rgba(old, 16), rgba(new, 16)
        moved = [i for i in range(0, len(a), 4) if a[i:i + 4] != b[i:i + 4]]
        clear = lambda s, i: s[2 * i + 6:2 * i + 8] == b"\0\0"
        return len(moved), [i // 4 for i in moved if clear(o, i) and clear(n, i)]

    # path 3 on the asteroid Layer: regenerate from its Default Version, take only the
    # fixed region and composite it onto that version, record it, then one Combined Image
    rocks_fix = img("rocks-fix.png", "xc:none", *disc("#a09080", 120, 40, 14),
                    *disc("#7a7060", 40, 80, 9))
    code, msg = gen_run(rocks_fix, "--scene", R, "--prompt-file", str(lblock), *A,
                        "--layer", "asteroids", *ET("layers/asteroids/v001/image.png"))
    fix_mask = img("fix-mask.png", "xc:black", "-fill", "white", "-draw",
                   "rectangle 100,20 140,60", "-blur", "0x3", "-alpha", "off")
    a1, a2 = (out / R / f"layers/asteroids/{v}/image.png" for v in ("v001", "v002"))
    composite = fxd / "rocks-composite.png"
    commands = region_replace(a1, a2, fix_mask, composite)
    code2, msg2 = layers_cmd("record", R, "--layer", "asteroids", "--image", str(composite),
                             "--start", "v001", "--donor", "asteroids=v002", "--mask",
                             str(fix_mask), "--commands", commands)
    r = receipt(f"{R}/layers/asteroids/v003")
    code3, msg3 = layers_cmd("combine", R, "--mode", "asteroid fix step")   # v004
    count, stray = differs_only_where(out / R / "v002/image.png", out / R / "v004/image.png",
                                      a1, out / R / "layers/asteroids/v003/image.png")
    report("path 3: a regeneration's fixed region composited onto the starting version is "
           "recorded, with no warning, and the step's one Combined Image differs only where "
           "the asteroid Layer's old or new version isn't fully transparent",
           code == code2 == code3 == 0 and "warn" not in msg2
           and (out / R / "layers/asteroids/v003/generation.md").read_text().startswith(
               f"# {R} asteroids v003\n\nNo image model was called")
           and r.get("Kind") == "Layer Version" and r.get("Layer Entry") == AE
           and r.get("Starting version") == f"output:{R}/layers/asteroids/v001 md5={gen.md5(a1)}"
           and r.get("Donors") == f"output:{R}/layers/asteroids/v002 md5={gen.md5(a2)}"
           and r.get("Mask", "").startswith(f"output:{R}/masks/asteroids-v003-fix-mask.png")
           and (out / R / "masks/asteroids-v003-fix-mask.png").read_bytes()
               == fix_mask.read_bytes()
           and r.get("Style") == "v1" and r.get("md5") == gen.md5(composite)
           and r.get("Commands", "").startswith("magick ") and "Status" in r
           and [(s["layer"], s["path"][-4:]) for s in receipt(f"{R}/v004").get("stack", [])]
           == [("planet", "v001"), ("asteroids", "v003"), ("ships", "v002")]
           and count > 0 and not stray, f"{msg2}\n{msg3}\n{r}\n{count} changed, stray {stray[:5]}")

    # a ship moved within its Layer with ImageMagick: the Layers beneath show where it was
    s2, moved_png = out / R / "layers/ships/v002/image.png", fxd / "ships-moved.png"
    magick(str(s2), "-roll", "+30+0", str(moved_png))
    code, msg = layers_cmd("record", R, "--layer", "ships", "--image", str(moved_png),
                           "--start", "v002", "--commands",
                           "magick ships/v002/image.png -roll +30+0 moved.png")
    code2, msg2 = layers_cmd("combine", R, "--mode", "moved ship step")   # v005
    s3 = out / R / "layers/ships/v003/image.png"
    count, stray = differs_only_where(out / R / "v004/image.png", out / R / "v005/image.png",
                                      s2, s3)
    lower = fxd / "rev-lower.png"
    magick(str(out / R / "layers/planet/v001/image.png"), str(out / R / "layers/asteroids/"
           "v003/image.png"), "-compose", "Over", "-composite", str(lower))
    at = lambda p, x, y: rgba(p)[4 * (y * 192 + x):4 * (y * 192 + x) + 4]
    report("a ship moved and recorded gives one Combined Image naming the same other "
           "versions, showing the Layers beneath where the ship was",
           code == code2 == 0 and "warn" not in msg
           and receipt(f"{R}/layers/ships/v003").get("Donors") == "none"
           and receipt(f"{R}/layers/ships/v003").get("Mask") == "none given"
           and [(s["layer"], s["path"][-4:]) for s in receipt(f"{R}/v005").get("stack", [])]
           == [("planet", "v001"), ("asteroids", "v003"), ("ships", "v003")]
           and count > 0 and not stray
           and at(out / R / "v005/image.png", 112, 30) == at(lower, 112, 30)
           != at(out / R / "v004/image.png", 112, 30), f"{msg}\n{msg2}\n{count} {stray[:5]}")

    # record's refusals, each writing nothing, and its warnings
    shutil.copyfile(out / R / "v001/image.png", out / R / "sources/ci-adj.png")
    (out / R / "sources/ci-adj.md").write_text(
        f"Derived from: output:{R}/v001 md5={gen.md5(out / R / 'v001/image.png')}\n")
    (out / R / "drafts/v001").mkdir(parents=True)
    shutil.copyfile(draft_png, out / R / "drafts/v001/image.png")
    (out / R / "drafts/v001/generation.md").write_text(f"Kind: Draft\nmd5: {gen.md5(draft_png)}\n")
    rec_args = lambda *extra, image=moved_png, start="v003", layer="ships": [
        "--layer", layer, "--image", str(image), "--start", start, "--commands", "magick x",
        *extra]
    s1_img = out / R / "layers/ships/v001/image.png"
    saved_s1 = s1_img.read_bytes()
    for name, args, expect, prep in [
        ("record refuses a Draft donor", rec_args("--donor", "drafts/v001/image.png"),
         "a Draft is never one", None),
        ("record refuses a Combined Image donor", rec_args("--donor", "v001/image.png"),
         "a Combined Image is never one", None),
        ("record refuses an adjusted copy of a Combined Image as donor",
         rec_args("--donor", "sources/ci-adj.png"), "an adjusted copy of a Combined Image", None),
        ("record refuses a donor from another scene",
         rec_args("--donor", str(out / BP / "layers/ships/v001/image.png")),
         "an image from outside the scene is never one", None),
        ("record refuses a donor file with no sidecar",
         rec_args("--donor", "sources/bare.png"), "a file with no sidecar", None),
        ("record refuses an image that isn't the Frame's pixel size",
         rec_args(image=square_png), "is 150x150, not the Frame's pixel size", None),
        ("record refuses an image that dropped the starting version's alpha channel",
         rec_args(image=flat_png), "has no alpha channel, but the starting version", None),
        ("record refuses a Layer not in the current plan", rec_args(layer="moon"),
         "is not in the current Layer Plan", None),
        ("record refuses a starting version that doesn't exist", rec_args(start="v009"),
         "has no such version", None),
        ("record refuses a file that isn't a PNG", rec_args(image=svg), "not a PNG file", None),
        ("record refuses a mask that isn't the Frame's size", rec_args("--mask", small),
         "not the Frame's pixel size", None),
        ("record refuses a donor that is altered, naming the file",
         rec_args("--donor", "ships=v001"), f"output:{R}/layers/ships/v001/image.png is altered",
         lambda: magick(str(s1_img), "-fill", "#ffffff", "-draw", "point 1,1", str(s1_img))),
        ("record refuses a donor file that doesn't exist",
         rec_args("--donor", "sources/none.png"), "no such file", None),
        ("record refuses a donor from a Layer no plan held",
         rec_args("--donor", "moon=v001"), "ever held a Layer 'moon'", None),
        ("record refuses a mask ImageMagick can't read, without a traceback",
         rec_args("--mask", str(spec)), "can't read it as an image", None),
        ("record refuses empty --commands",
         ["--layer", "ships", "--image", str(moved_png), "--start", "v003", "--commands", " "],
         "--commands is required", None),
    ]:
        if prep:
            prep()
        before = sorted(tmp.rglob("*"))
        code, msg = layers_cmd("record", R, *args)
        report(name, code != 0 and expect in msg and "Traceback" not in msg
               and sorted(tmp.rglob("*")) == before,
               f"expected {expect!r} and nothing written, exit {code}:\n{msg}")
        s1_img.write_bytes(saved_s1)
    code, msg = layers_cmd("record", "single-gen", *rec_args())
    report("record refuses a Single-Layer Scene", code != 0 and "not a Layered Scene" in msg, msg)

    odd = fxd / "ships-odd.png"
    magick(str(s3), "-fill", "#22cc22", "-draw", "rectangle 0,0 9,9", "-draw",
           "rectangle 180,90 191,107", str(odd))
    odd_mask = img("odd-mask.png", "xc:black", "-fill", "white", "-draw", "rectangle 0,0 9,9",
                   "-alpha", "off")
    # noise at 5/255 counts as outside the mask (decision 14); 6/255 counts as inside
    noisy_mask = img("noisy-mask.png", "xc:gray(5)", "-fill", "white", "-draw",
                     "rectangle 0,0 9,9", "-alpha", "off", "-depth", "8")
    edge_mask = img("edge-mask.png", "xc:black", "-fill", "white", "-draw", "rectangle 0,0 9,9",
                    "-fill", "gray(6)", "-draw", "rectangle 180,90 191,107", "-alpha", "off",
                    "-depth", "8")
    fake_version(R, "ships", ships_png, SE, style="v2")       # ships v004, another style
    for name, args, expect in [
        ("record warns, with the count, when pixels outside the mask changed",
         rec_args("--mask", str(odd_mask), image=odd),
         "216 pixels differ from the starting version outside the mask"),
        ("record counts a noisy mask's pixels at or below 5/255 as outside it",
         rec_args("--mask", str(noisy_mask), image=odd),
         "216 pixels differ from the starting version outside the mask"),
        ("record warns when the starting version is neither the Default Version nor a "
         "donor's start", rec_args(start="v001", image=s2), "the starting version, ships v001, "
         "isn't the Layer's Default Version (v004)"),
        ("record warns when a donor was made under another style version",
         rec_args("--donor", "ships=v004"), "was made under style v2"),
    ]:
        before = sorted(tmp.rglob("*"))
        code, msg = layers_cmd("record", R, *args, "--dry-run")
        report(name, code == 0 and expect in msg and sorted(tmp.rglob("*")) == before, msg)
    before = sorted(tmp.rglob("*"))
    code, msg = layers_cmd("record", R, *rec_args("--mask", str(edge_mask), image=odd),
                           "--dry-run")
    report("record counts mask pixels above 5/255 as inside, with no warning",
           code == 0 and "outside the mask" not in msg and sorted(tmp.rglob("*")) == before, msg)
    before = sorted(tmp.rglob("*"))
    code, msg = layers_cmd("record", R, *rec_args("--donor", "sources/ship-adj.png", "--mask",
                                                  str(odd_mask), start="v002", image=s2),
                           "--dry-run")
    report("record accepts an adjusted copy of a Layer Version as donor, and an unchanged "
           "outside, without the mask warning",
           code == 0 and "donor: output:rev/sources/ship-adj.png" in msg
           and "outside the mask" not in msg and sorted(tmp.rglob("*")) == before, msg)

    # path 4 on a Layer: the paid output's colour merged into the starting version,
    # keeping its alpha everywhere and every pixel outside the mask (the API stubbed)
    plan("p4", *LF, "--layer", "base=Night sky", "--layer", "top=The lantern", *YES,
         "--based-on", "0")
    start_png = img("p4-start.png", "xc:none", *disc("#cc3322", 60, 54, 30), "-fill",
                    "rgba(200,180,40,0.5)", "-draw", "rectangle 100,20 150,90")
    fake_version("p4", "top", start_png, "The lantern")
    p4_mask = img("p4-mask.png", "xc:black", "-fill", "white", "-draw",
                  "rectangle 70,30 140,80", "-blur", "0x4", "-alpha", "off")
    paid = img("p4-paid.png", "xc:rgb(60,120,200)")
    seen = {}

    def paid_generate(_prompt, attachments, *_a, **_kw) -> dict:
        seen["first"] = attachments[0][0]
        seen["alpha"] = gen.has_alpha(attachments[0][0])
        return {"data": [{"b64_json": base64.b64encode(seen["paid"].read_bytes()).decode()}]}

    def masked_layer_run(version: str, paid_png: Path) -> tuple[str, str]:
        """A real masked gen.py --layer run, in-process, its API call stubbed."""
        saved = (sys.argv, gen.api_key, gen.generate, gen.generate_codex)
        seen["paid"] = paid_png
        sys.argv = ["gen.py", *P, *O, "--scene", "p4", "--layer", "top", "--prompt-file",
                    str(mprompt), "--attach", f"p4/layers/top/{version}/image.png:EDIT TARGET",
                    *A, "--backend", "api", "--mask", str(p4_mask), "--approved-by",
                    "Yes, one call."]
        gen.api_key, gen.generate, gen.generate_codex = (lambda: "selftest-key"), \
            paid_generate, no_codex
        err = io.StringIO()
        try:
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
                result = f"exit {gen.main()}"
        except (Exception, SystemExit) as e:
            result = f"{type(e).__name__}: {e}"
        finally:
            sys.argv, gen.api_key, gen.generate, gen.generate_codex = saved
            gen.PKG = gen.OUT = None
        return result, err.getvalue()

    result, err = masked_layer_run("v001", paid)
    err = io.StringIO(err)
    v2d = out / "p4/layers/top/v002"
    r = receipt("p4/layers/top/v002")
    problems, partly, feathered = [], 0, 0
    if result == "exit 0":
        st, mg, mk, pd = (rgba(p, 16) for p in (start_png, v2d / "image.png", p4_mask, paid))
        q = lambda b, i: int.from_bytes(b[i:i + 2], "big") / 65535
        for px in range(192 * 108):
            i = 8 * px
            m, a = q(mk, i), q(st, i + 6)
            if q(mg, i + 6) != a:
                problems.append(f"pixel {px}: alpha {q(mg, i + 6)} is not the start's {a}")
            elif m == 0 and mg[i:i + 8] != st[i:i + 8]:
                problems.append(f"pixel {px}: changed outside the mask")
            elif m > 0 and a > 0:
                want = [(1 - m) * q(st, i + 2 * c) + m * min(1, q(pd, i + 2 * c) / a)
                        for c in range(3)]
                if any(abs(q(mg, i + 2 * c) - want[c]) > 2 / 255 for c in range(3)):
                    problems.append(f"pixel {px}: colour {[q(mg, i + 2 * c) for c in range(3)]}"
                                    f", want {want}")
                partly += m == 1 and 0 < a < 1
                feathered += 0 < m < 1
    report("path 4 on a Layer: the paid colour is merged inside the mask, divided by the "
           "starting alpha and mixed in the feathered edge; alpha and every pixel outside "
           "are kept, the paid output stays as raw.png",
           result == "exit 0" and not problems and partly > 0 and feathered > 0
           and seen.get("alpha") is False and seen["first"] != out / "p4/layers/top/v001/image.png"
           and (v2d / "raw.png").read_bytes() == paid.read_bytes()
           and r.get("Repair", "").startswith("masked repaint (path 4) merged as colour only")
           and r.get("Starting version") == "output:p4/layers/top/v001"
           and r.get("Checks") == "round 1, merged Layer Version: pass"
           and r.get("md5") == gen.md5(v2d / "image.png"),
           f"{result}; partly {partly}, feathered {feathered}; checks {r.get('Checks')}; "
           f"start {r.get('Starting version')}\n" + "\n".join(problems[:3]) + err.getvalue())
    grey = img("p4-grey.png", "xc:none", "-fill", "rgba(180,180,180,0.5)", "-draw",
               "rectangle 20,10 170,100")
    fake_version("p4", "top", grey, "The lantern")                          # top v003
    result, err = masked_layer_run("v003", img("p4-red.png", "xc:rgb(60,0,0)"))
    got = rgba(out / "p4/layers/top/v004/image.png")[4 * (55 * 192 + 105):4 * (55 * 192 + 106)] \
        if result == "exit 0" else b""
    report("path 4 on a grey starting version still merges the paid colour",
           result == "exit 0" and len(got) == 4 and abs(got[0] - 120) <= 2 and got[1] <= 2
           and got[2] <= 2 and got[3] in (127, 128), f"{result} {got.hex()} {err}")
    code, msg = gen_run(None, "--scene", "p4", "--layer", "top", "--prompt-file", str(mprompt),
                        "--attach", "p4/layers/top/v004/image.png:EDIT TARGET", *A,
                        "--backend", "api", "--mask", str(p4_mask), *DRY)
    report("a masked Layer generation from its Default Version is accepted in a dry run, "
           "without the missing-block warning",
           code == 0 and "invariants OK" in msg and "lacks the transparent" not in msg
           and "isn't Layer top's Default" not in msg, msg)

    # a plan change whose Combined Image can't be written records nothing; a damaged
    # version it would hold refuses the change, saying why
    plan("ro", *LF, "--layer", "a=Part a", "--layer", "b=Part b", *YES, "--based-on", "0")
    fake_version("ro", "a", rocks_a, "Part a")
    fake_version("ro", "b", ships_png, "Part b")
    (out / "ro").chmod(0o555)
    try:
        code, msg = plan("ro", *LF, "--layer", "b=@1", "--layer", "a=@1", *YES, "--based-on", "1")
    finally:
        (out / "ro").chmod(0o755)
    report("a plan change whose Combined Image can't be written is refused before recording",
           code != 0 and "not writable" in msg and journal("ro") == ["001.json"]
           and "Traceback" not in msg, msg)
    ra = out / "ro/layers/a/v001/image.png"
    saved_ra = ra.read_bytes()
    magick(str(ra), "-fill", "#ffffff", "-draw", "point 1,1", str(ra))
    code, msg = plan("ro", *LF, "--layer", "b=@1", "--layer", "a=@1", "--dry-run")
    ra.write_bytes(saved_ra)
    report("a plan change whose Combined Image would hold an altered version is refused, "
           "saying the plan isn't recorded", code != 0 and "plan not recorded" in msg
           and "is altered" in msg, msg)

    # --- changing the plan later: a moon Layer moved and back
    MO, PM = "moon", "The planet and its moon"
    plan(MO, *LF, "--layer", f"planet={PM}", "--layer", f"asteroids={AE}",
         "--layer", f"ships={SE}", *YES, "--based-on", "0")                          # 1
    for lid, image, entry in (("planet", blues[0], PM), ("asteroids", rocks_a, AE),
                              ("ships", ships_png, SE)):
        fake_version(MO, lid, image, entry)
    approve(f"{MO}/layers/planet/v001", "--approval", "That planet.", "--based-on", "1")   # 2
    approve(f"{MO}/layers/asteroids/v001", "--approval", "Those rocks.", "--based-on", "2")  # 3
    fake_version(MO, "planet", blues[1], PM)
    fake_version(MO, "planet", blues[2], PM)
    layers_cmd("keep", MO, "--layer", "planet", "--version", "v002", "--words", "Keep v2.",
               "--based-on", "3")                                                    # 4
    move = ["--layer", "planet=The planet", "--layer", "asteroids=The asteroid field and the "
            "moon", "--layer", "ships=@1"]
    code, msg = plan(MO, *LF, *move, "--dry-run")
    report("a proposal moving the moon names both approvals that would stop counting and the "
           "keep that would end, and builds nothing",
           code == 0 and "Layer planet's Approved Layer Version v001 (journal/002.json) would "
           "stop counting" in msg and "Layer asteroids's Approved Layer Version v001 "
           "(journal/003.json) would stop counting" in msg
           and "the keep of Layer planet's v002 (journal/004.json) would end, for good" in msg
           and "builds its Combined Image" not in msg, msg)
    code, msg = plan(MO, *LF, *move, *YES, "--based-on", "4")                       # 5
    rec = record(MO, 5) if code == 0 else {}
    report("the plan record states the approvals and the keep its change affects",
           code == 0 and any("would stop counting" in c for c in rec.get("changes", []))
           and any("would end, for good" in c for c in rec.get("changes", []))
           and not (out / MO / "v001").exists(), f"{msg}\n{rec}")
    fake_version(MO, "planet", blues[3], "The planet")                       # planet v004
    fake_version(MO, "asteroids", rocks_b, "The asteroid field and the moon")  # asteroids v002
    layers_cmd("combine", MO)                                                       # v001
    back = ["--layer", "planet=@1", "--layer", "asteroids=@1", "--layer", "ships=@1"]
    code, msg = plan(MO, *LF, *back, "--dry-run")
    code2, msg2 = plan(MO, *LF, *back, *YES, "--based-on", "5")                     # 6
    built = receipt(f"{MO}/v002")
    code3, msg3 = approve(f"{MO}/v002", "--approval", "Yes, that one.", "--based-on", "6")  # 7
    report("moving the moon back builds a Combined Image at once holding the original "
           "Approved Layer Versions, planet at v1 not v2, and promote.py accepts it",
           code == code2 == code3 == 0
           and "Layer planet's Approved Layer Version v001 (journal/002.json) would count "
           "again" in msg and "builds its Combined Image in the same run" in msg
           and [(s["layer"], s["path"][-4:], s["approved"]) for s in built.get("stack", [])]
           == [("planet", "v001", "yes"), ("asteroids", "v001", "yes"), ("ships", "v001", "no")]
           and record(MO, 7).get("kind") == "scene-approval", msg + msg2 + msg3)
    final_bytes = (out / MO / "final.png").read_bytes() if code3 == 0 else b""
    code, msg = plan(MO, *LF, *move, *YES, "--based-on", "7")                       # 8
    code2, msg2 = approve(f"{MO}/layers/planet/v004", "--approval", "Planet alone.",
                          "--based-on", "8")
    code3, msg3 = approve(f"{MO}/layers/planet/v004", "--approval", "Planet alone.",
                          "--based-on", "8", "--replace")                           # 9
    code4, msg4 = plan(MO, *LF, *back, *YES, "--based-on", "9")                     # 10
    st = status_of(MO)
    report("approving a new planet version after moving the moon out again names the earlier "
           "approval, though it no longer counts, and moving back doesn't restore it",
           code == code3 == code4 == 0 and code2 != 0
           and "Approved Layer Version is v001 (journal/007.json, counting or not)" in msg2
           and "Layer planet's Approved Layer Version v004 (journal/009.json) would stop "
           "counting" in msg4
           and "      Default Version: v003 (its latest version); Approved Layer Version: v004 "
           "(doesn't count)" in st, msg2 + msg4 + st)
    code, msg = plan(MO, *LF, *back, "--layer", "comet=A comet", *YES, "--based-on", "10")  # 11
    newest = max(int(p.name[1:]) for p in (out / MO).glob("v[0-9]*"))
    code2, msg2 = approve(f"{MO}/v{newest:03d}", "--approval", "Yes.", "--based-on", "11",
                          "--replace")
    report("adding a Layer builds nothing, and a Combined Image without it is refused",
           code == 0 and "builds its Combined Image" not in msg and newest == 4
           and code2 != 0 and "comet: missing from the Combined Image" in msg2, msg + msg2)
    code, msg = plan(MO, *LF, "--layer", "planet=@1", "--layer", "asteroids=@1",
                     "--layer", "comet=@11", *YES, "--based-on", "11")             # 12
    st = status_of(MO)
    report("removing a Layer builds its Combined Image at once; status lists the removed "
           "Layer with its versions and approval",
           code == 0 and [(s["layer"], s["path"][-4:]) for s in receipt(f"{MO}/v005").get("stack", [])]
           == [("planet", "v003"), ("asteroids", "v001")]
           and "  removed Layers:\n    ships:\n      v001  doesn't count: its Layer is removed"
           in st and "      Approved Layer Version: v001" in st, msg + st)
    code, msg = layers_cmd("combine", MO, "--insert", "ships=v001@3", "--mode", "one-off")
    r = receipt(f"{MO}/v006")
    code2, msg2 = approve(f"{MO}/v006", "--approval", "Yes.", "--based-on", "12", "--replace")
    report("combine --insert places a removed Layer at its position, warns and records it, "
           "and that Combined Image can't be approved",
           code == 0 and [(s["layer"], s["removed"]) for s in r.get("stack", [])]
           == [("planet", "no"), ("asteroids", "no"), ("ships", "yes")]
           and "Layer ships (v001) is removed from the current plan and included at position 3"
           in msg and "included at position 3" in r.get("Warning", "")
           and "3 ships v001  (removed; placed with --insert" in msg
           and code2 != 0 and "ships: removed" in msg2, msg + msg2)
    report("the approved Combined Image and final.png are unchanged by the plan changes",
           final_bytes and (out / MO / "final.png").read_bytes() == final_bytes
           and record(MO, 7).get("combined") == f"output:{MO}/v002")
    for name, args, expect in [
        ("combine --insert of a Layer in the current plan refused", ["--insert", "planet=v001@1"],
         "name its version with --use"),
        ("combine --insert of a Layer never planned refused", ["--insert", "moon=v001@1"],
         "ever held a Layer"),
        ("a malformed combine --insert refused", ["--insert", "ships=v001"], "ID=vNNN@POSITION"),
        ("combine --insert past the top of the stack refused", ["--insert", "ships=v001@4"],
         "its position is at most 3"),
        ("combine --insert of a version that doesn't exist refused",
         ["--insert", "ships=v009@1"], "has no such version"),
        ("combine --insert naming one position twice refused",
         ["--insert", "ships=v001@1", "--insert", "ships=v001@1"], "names position 1 twice"),
    ]:
        before = sorted(tmp.rglob("*"))
        code, msg = layers_cmd("combine", MO, *args)
        report(name, code != 0 and expect in msg and "Traceback" not in msg
               and sorted(tmp.rglob("*")) == before, msg)
    code, msg = plan("fresh-change", *LF, "--layer", "a=A", "--layer", "b=B", *YES,
                     "--based-on", "0")
    code2, msg2 = plan("fresh-change", *LF, "--layer", "b=@1", "--layer", "a=@1", *YES,
                       "--based-on", "1")
    report("before anything is generated, a plan change builds nothing",
           code == code2 == 0 and not list((out / "fresh-change").glob("v[0-9]*"))
           and "builds its Combined Image" not in msg2, msg2)

    if exhaustive:
        explore_scene_states(tmp, report)
    else:
        print("  (the exhaustive Scene Journal tests run with --exhaustive)")

    print(f"\n  {checks - failures}/{checks} checks passed")
    return 1 if failures else 0


# ------------------------------- Scene Journal state space: the bounded exhaustive test

# Three Layers: a has two Layer Entry texts, and is the one the plan changes remove,
# put back, change and change back; b and c have one each. Each Layer holds at most
# one version at the Frame's aspect ratio and one off it per Layer Entry, except b,
# which may hold two at it, so a counting version can differ from the Default Version.
X_ENTRIES = {"a": ("The moon", "The moon and the comet"), "b": ("The ships",),
             "c": ("The stars",)}
X_AT = {"a": 1, "b": 2, "c": 1}
X_IDS = ("a", "b", "c")
X_FRAME = {"width": 192, "height": 108}
X_SIZE = {True: (192, 108), False: (150, 150)}
X_TARGETS = (
    "Default Version: kept", "Default Version: approved", "Default Version: latest",
    "Default Version: none", "an approval of a Layer with a keep in force",
    "a removed Layer with an approval and a keep put back with its approved entry",
    "a removed Layer with an approval and a keep put back with another entry",
    "candidate: each Layer at its Default Version",
    "candidate: one Layer at a counting non-default version",
    "candidate: one Layer missing", "candidate: an old order",
    "candidate: a removed Layer", "candidate: a version that doesn't count",
    "a keep in force on a version older than the Layer's latest",
    "a new version while another Layer's Default Version is kept",
    "a new version while another Layer's Default Version is approved",
    "a new version while another Layer's Default Version is its latest")


def explore_scene_states(tmp: Path, report) -> None:
    """Drives the real scene_state over every state reachable from an empty
    scene, each distinct state once, and checks it against a small independent model
    of Layer state: after every event, the Layer state invariants; for every keep and approval tried,
    that the real check accepts exactly what the model allows. Then, from each state
    where a reachability target is first reached, runs every interleaving of two
    writers' read, check and publish steps on a real journal folder.

    A model state is (order, ever, versions, approved, kept, scene approved): order is
    ((Layer ID, Layer Entry), ...) bottom first; versions[i] is ((entry, at Frame
    ratio), ...) for X_IDS[i], numbered from 1; approved and kept hold version numbers
    (0 for none). Two states are the same when they agree on what the Layer state reads."""
    started, problems = time.monotonic(), []
    reached: dict[str, tuple] = {}

    def bad(what: str) -> None:
        if len(problems) < 8:
            problems.append(what)

    @functools.cache
    def entries(order):
        return dict(order)

    def entry(m, lid):
        return entries(m[0]).get(lid)

    def counts(m, i, n):
        e, fit = m[2][i][n - 1]
        return fit and e == entry(m, X_IDS[i])

    def default(m, i):
        if entry(m, X_IDS[i]) is None:
            return 0
        if m[4][i]:
            return m[4][i]
        if m[3][i] and counts(m, i, m[3][i]):
            return m[3][i]
        return max((n for n in range(1, len(m[2][i]) + 1) if counts(m, i, n)), default=0)

    @functools.cache
    def layer_key(vs, approved, kept):
        """What the Layer state reads of one Layer: its versions at the Frame's aspect ratio in
        order, the entries of those off it (which never count), and which of the
        former are approved and kept."""
        at = [n for n in range(1, len(vs) + 1) if vs[n - 1][1]]
        return (tuple(vs[n - 1][0] for n in at), frozenset(e for e, fit in vs if not fit),
                at.index(approved) if approved else None, at.index(kept) if kept else None)

    def key(m):
        return m[0], m[1], tuple(layer_key(m[2][i], m[3][i], m[4][i]) for i in range(3))

    def put(t, i, value):
        return t[:i] + (value,) + t[i + 1:]

    def record(records, kind, **fields):
        return records + ({"number": len(records) + 1, "kind": kind, "date": "2026-01-01",
                           "words": f"{kind} {len(records) + 1}", **fields},)

    def plan_record(records, order):
        return record(records, "plan", layered=True, frame=X_FRAME,
                      layers=[{"id": l, "entry": e} for l, e in order])

    def named(lid, n):
        return {"layer": lid, "version": f"v{n:03d}", "md5": "0" * 32}

    def derive(records, raw):
        view = scene_state.journal_view(records)
        if view["plan"] is None:
            return view, None, None
        assessed = {lid: scene_state.assess(raw[i], lid, view["plan"])
                    for i, lid in enumerate(X_IDS)}
        return view, assessed, {lid: scene_state.layer_state(view, lid, assessed[lid])
                                for lid in X_IDS}

    num = lambda v: v["number"] if v else 0

    def agrees(m, assessed, real, where):
        """The real implementation matches the model, and every Default Version counts."""
        for i, lid in enumerate(X_IDS):
            st = real[lid]
            if [v["counts"] for v in assessed[lid]] != [counts(m, i, n) for n in
                                                       range(1, len(m[2][i]) + 1)]:
                bad(f"{where}: Layer {lid}'s counting versions differ from the model")
            got = (num(st["default"]), num(st["approved"]), num(st["kept"]))
            if got != (default(m, i), m[3][i], m[4][i]):
                bad(f"{where}: Layer {lid} (default, approved, kept) is {got}, the model "
                    f"says {(default(m, i), m[3][i], m[4][i])}")
            if st["default"] is not None and not st["default"]["counts"]:
                bad(f"{where}: Layer {lid}'s Default Version doesn't count")

    def candidates(m):
        """The six kinds of Combined Image approval the test tries, as stacks."""
        order = [l for l, _ in m[0]]
        base = [(l, default(m, X_IDS.index(l))) for l in order]
        if not order or any(n == 0 for _, n in base):
            return
        yield "candidate: each Layer at its Default Version", base
        for k, (l, d) in enumerate(base):
            i, vs = X_IDS.index(l), m[2][X_IDS.index(l)]
            for n in range(1, len(vs) + 1):
                if n != d and counts(m, i, n):
                    yield "candidate: one Layer at a counting non-default version", put(
                        tuple(base), k, (l, n))
                elif not counts(m, i, n):
                    yield "candidate: a version that doesn't count", put(tuple(base), k, (l, n))
            if len(base) > 1:
                yield "candidate: one Layer missing", base[:k] + base[k + 1:]
        if len(base) > 1:
            yield "candidate: an old order", base[::-1]
        for l in m[1]:
            i = X_IDS.index(l)
            if l not in order and m[2][i]:
                yield "candidate: a removed Layer", base + [(l, 1)]

    def plan_changes(m):
        order, ids = m[0], [l for l, _ in m[0]]
        if not order:
            yield "plan", ((X_IDS[0], X_ENTRIES["a"][0]), ("b", "The ships"), ("c", "The stars"))
            yield "plan", (("b", "The ships"), ("c", "The stars"))
            return
        if "a" in ids:
            if len(ids) == 3:
                yield "remove", tuple(x for x in order if x[0] != "a")
            other = next(e for e in X_ENTRIES["a"] if e != entry(m, "a"))
            yield "change", tuple((l, other if l == "a" else e) for l, e in order)
        else:
            for e in X_ENTRIES["a"]:
                for pos in range(len(order) + 1):
                    yield ("put back" if "a" in m[1] else "add"), \
                        order[:pos] + (("a", e),) + order[pos:]
        for p in itertools.permutations(order):
            if p != order:
                yield "reorder", p

    def first(target, state):
        if target not in reached:
            reached[target] = state

    empty = ((), frozenset(), ((), (), ()), (0, 0, 0), (0, 0, 0), False)
    seen = {key(empty)}
    queue = collections.deque([(empty, (), ((), (), ()))])
    states = events = 0
    while queue:
        m, records, raw = queue.popleft()
        states += 1
        view, assessed, real = derive(records, raw)
        if real is not None:
            agrees(m, assessed, real, f"state {states}")
            for lid in (l for l, _ in m[0]):
                first(f"Default Version: {real[lid]['default_why'] or 'none'}", (m, records, raw))
                st = real[lid]
                if st["kept"] and st["latest"] and st["kept"]["number"] < st["latest"]["number"]:
                    first("a keep in force on a version older than the Layer's latest",
                          (m, records, raw))
        children = []
        present = [l for l, _ in m[0]]
        # new versions, at and off the Frame's aspect ratio
        for lid in present:
            i, e = X_IDS.index(lid), entry(m, lid)
            vs = m[2][i]
            for fit in (True, False):
                if sum(1 for x in vs if x == (e, fit)) >= (X_AT[lid] if fit else 1):
                    continue
                n = len(vs) + 1
                raw2 = put(raw, i, raw[i] + ({"number": n, "name": f"v{n:03d}", "layer": lid,
                                               "entry": e, "size": X_SIZE[fit],
                                               "deleted": False},))
                child = (m[0], m[1], put(m[2], i, vs + ((e, fit),)), m[3], m[4], m[5])
                for other in present:
                    if other == lid:
                        continue
                    before = real[other]
                    why = before["default_why"]
                    if why:
                        first(f"a new version while another Layer's Default Version is "
                              + {"kept": "kept", "approved": "approved", "latest": "its latest"}[why],
                              (child, records, raw2))
                    j = X_IDS.index(other)
                    after = scene_state.layer_state(
                        view, other, scene_state.assess(raw2[j], other, view["plan"]))
                    if num(after["default"]) != num(before["default"]):
                        bad(f"a new {lid} version changed {other}'s Default Version")
                children.append((child, records, raw2))
        # keeps and Layer approvals of every recorded version, counting or not
        for i, lid in enumerate(X_IDS):
            for n in range(1, len(m[2][i]) + 1):
                ok, name = lid in present and counts(m, i, n), f"v{n:03d}"
                vs = assessed[lid] if assessed else []
                for kind in ("keep", "layer-approval"):
                    events += 1
                    try:
                        if kind == "keep":
                            scene_state.check_keep(view, lid, vs, name)
                        else:
                            scene_state.check_layer_approval(view, lid, vs, name, True)
                        took = True
                    except scene_state.Fail:
                        took = False
                    if took != ok:
                        bad(f"state {states}: {kind} of {lid} {name} "
                            + ("accepted" if took else "refused") + " against the model")
                    if not ok:
                        continue
                    if kind == "keep":
                        child = (m[0], m[1], m[2], m[3], put(m[4], i, n), m[5])
                    else:
                        if real[lid]["keep"]:
                            first("an approval of a Layer with a keep in force",
                                  (m, records, raw))
                        try:
                            scene_state.check_layer_approval(view, lid, vs, name, False)
                            alone = True
                        except scene_state.Fail:
                            alone = False
                        if alone != (m[3][i] in (0, n)):
                            bad(f"state {states}: approving {lid} {name} without --replace "
                                + ("accepted" if alone else "refused") + " against the model")
                        child = (m[0], m[1], m[2], put(m[3], i, n), put(m[4], i, 0), m[5])
                    recs = record(records, kind, **named(lid, n))
                    if kind == "layer-approval" and scene_state.journal_view(recs)["keep"].get(lid):
                        bad(f"a keep of {lid} is in force after its approval")
                    children.append((child, recs, raw))
        # Combined Image approvals of the six kinds of candidate
        for target, stack in candidates(m):
            events += 1
            first(target, (m, records, raw))
            order = [l for l, _ in m[0]]
            ok = [l for l, _ in stack] == order and all(
                counts(m, X_IDS.index(l), n) for l, n in stack)
            alone = ok and not m[5] and all(m[3][X_IDS.index(l)] in (0, n) for l, n in stack)
            for replace, want in ((True, ok), (False, alone)):
                try:
                    scene_state.check_scene_approval(
                        view, assessed, [{"layer": l, "version": f"v{n:03d}"} for l, n in stack],
                        replace)
                    took = True
                except scene_state.Fail:
                    took = False
                if took != want:
                    bad(f"state {states}: {target} {stack} "
                        + ("accepted" if took else "refused") + f" with replace={replace}")
            if not ok:
                continue
            if any(real[l]["keep"] for l, _ in stack):
                first("an approval of a Layer with a keep in force", (m, records, raw))
            approved, kept = m[3], m[4]
            for l, n in stack:
                approved, kept = put(approved, X_IDS.index(l), n), put(kept, X_IDS.index(l), 0)
            recs = record(records, "scene-approval", combined="output:x/v001", md5="0" * 32,
                          layers=[named(l, n) for l, n in stack])
            if any(scene_state.journal_view(recs)["keep"].get(l) for l, _ in stack):
                bad("a keep is in force after a scene approval of its Layer")
            children.append(((m[0], m[1], m[2], approved, kept, True), recs, raw))
        # Layer Plan changes
        for change, order in plan_changes(m):
            events += 1
            kept = tuple(0 if m[4][i] and entry(m, lid) != dict(order).get(lid) else m[4][i]
                         for i, lid in enumerate(X_IDS))
            child = (order, m[1] | {l for l, _ in order}, m[2], m[3], kept, m[5])
            if key(child) not in seen:   # the real plan check, on each first visit
                proposal = {"layered": True, "frame": X_FRAME,
                            "layers": [{"id": l, "entry": e} for l, e in order]}
                try:
                    scene_state.check_plan(list(records), proposal, any(raw))
                except scene_state.Fail as e:
                    bad(f"state {states}: a valid plan change ({change}) refused: {e}")
                    continue
            recs = plan_record(records, order)
            if any(m[4]):
                # a plan change can end keeps; the state it reaches may have been seen
                # by a path without them, so check this path's keeps here
                now = scene_state.journal_view(recs)["keep"]
                if tuple(int(now[l]["version"][1:]) if l in now else 0 for l in X_IDS) != kept:
                    bad(f"state {states}: after a plan change ({change}) the keeps in "
                        f"force are {sorted(now)}, the model says {kept}")
            if change == "remove" and m[3][0] and m[4][0]:
                # a removed Layer holding an approval and a keep, put back both ways
                for e in X_ENTRIES["a"]:
                    back = plan_record(recs, order + (("a", e),))
                    same = e == m[2][0][m[3][0] - 1][0]
                    first("a removed Layer with an approval and a keep put back with "
                          + ("its approved entry" if same else "another entry"),
                          (child, recs, raw))
                    check_put_back(back, raw, e, same, bad)
            if change == "put back":
                e = dict(order)["a"]
                check_put_back(recs, raw, e, e == m[2][0][m[3][0] - 1][0] if m[3][0] else None,
                               bad)
            children.append((child, recs, raw))
        for child in children:
            k = key(child[0])
            if k not in seen:
                seen.add(k)
                queue.append(child)
    elapsed = time.monotonic() - started
    report(f"Scene Journal state space: {states} distinct states and {events} tried decisions explored in "
           f"{elapsed:.1f} s; the real scene_state agrees with the model, and the Layer "
           "state invariants hold after every event", not problems, "\n".join(problems))
    missed = [t for t in X_TARGETS if t not in reached]
    report(f"Scene Journal state space: all {len(X_TARGETS)} reachability targets reached", not missed,
           "missed: " + "; ".join(missed))
    interleave_writers(tmp, reached, report)


def check_put_back(records, raw, put_entry: str, approved_same: bool | None, bad) -> None:
    """On a plan record that puts Layer a back: its Approved Layer Version
    counts again exactly when the entry it is put back with says the same as the one
    that version was made under, and no keep recorded before the removal is in force."""
    view = scene_state.journal_view(records)
    st = scene_state.layer_state(view, "a", scene_state.assess(raw[0], "a", view["plan"]))
    if st["keep"] is not None:
        bad("a keep recorded before Layer a's removal is in force after it is put back")
    if approved_same is not None and (st["approved"] is not None
                                      and st["approved"]["counts"]) != approved_same:
        bad(f"Layer a put back with {put_entry!r}: its Approved Layer Version "
            + ("doesn't count" if approved_same else "counts"))


def interleave_writers(tmp: Path, reached: dict, report) -> None:
    """From each state where a target was first reached, for every pair of
    record kinds (two of one kind included), every interleaving of two writers' read,
    check and publish steps on a real journal folder. Both writers decided on the
    starting state. Each published record must pass its check against the journal as
    it stood just before it, and a writer whose journal moved past its based-on number
    must publish nothing."""
    started, problems, runs = time.monotonic(), [], 0
    kinds = ("plan", "keep", "layer-approval", "scene-approval")
    steps = [p for p in itertools.permutations([0, 0, 0, 1, 1, 1])]
    orders = sorted(set(steps))   # the 20 interleavings of two three-step writers
    scene = tmp / "two-writers"

    def decide(kind, view, assessed):
        """A decision of this kind the journal allows, or None."""
        plan = view["plan"]
        ids = [l["id"] for l in plan["layers"]]
        if kind == "plan":
            layers = plan["layers"][1::-1] + plan["layers"][2:]
            return {"layered": True, "frame": X_FRAME, "layers": layers}
        counting = [(lid, v) for lid in ids for v in assessed[lid] if v["counts"]]
        if kind in ("keep", "layer-approval"):
            return ({"layer": counting[0][0], "version": counting[0][1]["name"]}
                    if counting else None)
        stack = []
        for lid in ids:
            d = scene_state.layer_state(view, lid, assessed[lid])["default"]
            if d is None:
                return None
            stack.append({"layer": lid, "version": d["name"]})
        return stack

    def check(kind, decision, records):
        view = scene_state.journal_view(records)
        assessed = {lid: scene_state.assess(raws[lid], lid, view["plan"]) for lid in X_IDS}
        if kind == "plan":
            scene_state.check_plan(records, decision, True)
        elif kind == "keep":
            scene_state.check_keep(view, decision["layer"], assessed[decision["layer"]],
                                   decision["version"])
        elif kind == "layer-approval":
            scene_state.check_layer_approval(view, decision["layer"],
                                             assessed[decision["layer"]], decision["version"],
                                             True)
        else:
            scene_state.check_scene_approval(view, assessed, decision, True)

    def as_record(kind, decision, n):
        fields = ({**decision} if kind == "plan" else
                  {"combined": "output:x/v001", "md5": "0" * 32,
                   "layers": [{**s, "md5": "0" * 32} for s in decision]}
                  if kind == "scene-approval" else {**decision, "md5": "0" * 32})
        return {"number": n, "kind": kind, "date": "2026-01-01", "words": f"writer {kind}",
                **fields}

    for target, (m, records, raw) in reached.items():
        if not records:
            continue
        raws = dict(zip(X_IDS, raw))
        base = len(records)
        shutil.rmtree(scene, ignore_errors=True)
        (scene / "journal").mkdir(parents=True)
        for r in records:
            scene_state.publish(scene, dict(r))
        view = scene_state.journal_view(list(records))
        assessed = {lid: scene_state.assess(raws[lid], lid, view["plan"]) for lid in X_IDS}
        decisions = {k: decide(k, view, assessed) for k in kinds}
        for a, b in itertools.combinations_with_replacement(kinds, 2):
            if decisions[a] is None or decisions[b] is None:
                continue
            for order in orders:
                runs += 1
                writers = [{"kind": a, "based_on": base, "step": 0, "done": None},
                           {"kind": b, "based_on": base, "step": 0, "done": None}]
                for w in order:
                    wr = writers[w]
                    if wr["done"] is not None:
                        continue
                    try:
                        if wr["step"] == 0:
                            wr["records"] = scene_state.read_journal(scene)
                        elif wr["step"] == 1:
                            scene_state.check_based_on(wr["records"], wr["based_on"])
                            check(wr["kind"], decisions[wr["kind"]], wr["records"])
                        else:
                            n = scene_state.latest(wr["records"]) + 1
                            scene_state.publish(scene, as_record(wr["kind"],
                                                                 decisions[wr["kind"]], n))
                            wr["done"] = n
                        wr["step"] += 1
                    except scene_state.Fail:
                        wr["done"] = 0
                now = scene_state.read_journal(scene)
                for w, wr in enumerate(writers):
                    if wr["done"]:
                        before = now[:wr["done"] - 1]
                        if scene_state.latest(before) != wr["based_on"]:
                            problems.append(f"{target}: writer {w + 1} ({wr['kind']}) "
                                            "published past its based-on number")
                        try:
                            check(wr["kind"], decisions[wr["kind"]], before)
                        except scene_state.Fail as e:
                            problems.append(f"{target}: writer {w + 1}'s {wr['kind']} fails "
                                            f"its check against the journal before it: {e}")
                if len(now) != base + 1 or sum(1 for wr in writers if wr["done"]) != 1:
                    problems.append(f"{target}: {a} and {b} in order {order} left "
                                    f"{len(now) - base} records")
                leftovers = [p.name for p in (scene / "journal").iterdir()
                             if not scene_state.RECORD.fullmatch(p.name)]
                if leftovers:
                    problems.append(f"{target}: temporary files left: {leftovers}")
                for p in (scene / "journal").iterdir():
                    if (mm := scene_state.RECORD.fullmatch(p.name)) and int(mm.group(1)) > base:
                        p.unlink()
    shutil.rmtree(scene, ignore_errors=True)
    report(f"Scene Journal writers: {runs} two-writer interleavings from {len(reached)} target states, in "
           f"{time.monotonic() - started:.1f} s: every published record passes its check "
           "against the journal before it, and a moved journal publishes nothing",
           runs > 0 and not problems, "\n".join(problems[:8]))


if __name__ == "__main__":
    sys.exit(main())
