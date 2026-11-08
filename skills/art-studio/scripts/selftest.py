#!/usr/bin/env python3
"""Exercise every guard in gen.py, prompt.py, review.py and promote.py without
generating anything.

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
import contextlib
import io
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import gen  # noqa: E402

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

    print(f"\n  {checks - failures}/{checks} checks passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
