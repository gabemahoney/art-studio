#!/usr/bin/env python3
"""Exercise every guard in gen.py, prompt.py, review.py, promote.py and layers.py
without generating anything.

  python3 -I scripts/selftest.py

Builds a throwaway package and output folder in a temp directory, so it needs no
real package and touches none. gen.py runs under --dry-run, fails before any
call is made, or runs in-process with its backend and key stubbed; no image is
generated and nothing is billed. Run it after touching
anything in scripts/.

Each case asserts that a specific invariant FAILS CLOSED. A guard that stops firing
is a guard that has silently been removed.
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import base64
import builtins
import contextlib
import errno
import io
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import gen  # noqa: E402
import layers  # noqa: E402

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

    print(f"\n  {checks - failures}/{checks} checks passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
