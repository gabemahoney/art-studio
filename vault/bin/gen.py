#!/usr/bin/env python3
"""Generate one candidate image (Codex image_gen by default, OpenAI Images API with
--backend api).

Enforces the vault invariants in code instead of by good intentions:
  - the One Rule (anchor attached FIRST as STYLE, Style Block verbatim at top,
    closing style line last)
  - reference validation (hard stop) for every attached reference.png
  - frozen-revision resolution for every mutable head revision used
  - a complete generation.md receipt, including the pinned model snapshot

Stdlib only, no venv — but two external binaries are required: ImageMagick
(`magick`) always, and the `codex` CLI for the default backend.

  python3 bin/gen.py --asset ships/the_antares \
      --prompt-file /tmp/prompt.txt \
      --attach ref_images/style_references/canonical_style_reference.png:STYLE \
      --attach assets/ships/the_antares/reference.png:IDENTITY
"""

from __future__ import annotations

import sys

# A compiled copy of this file in __pycache__ is a copy that does not carry
# later changes — including the paid-call gate. Never leave one behind.
sys.dont_write_bytecode = True

import argparse
import hashlib
import json
import mimetypes
import os
import re
import time
import urllib.error
import urllib.request
import uuid
from datetime import date
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
ANCHOR = Path("ref_images/style_references/canonical_style_reference.png")

# Images live OUTSIDE the repo: they are large, numerous, and regenerate, so git is the
# wrong store for them. Text -- receipts, descriptions, sidecars -- stays in the repo and
# remains the provenance record. Both trees use the SAME vault-relative paths, so
# outputs/<scene>/vNNN/ has its generation.md here and its image.png under IMAGES.
#
# ONE source of truth: the `image-root` file beside rules.md. No environment override and
# no fallback -- three ways to answer "where are the images" is three ways to disagree,
# and a silent fallback would scatter renders into the repo the first time the file went
# missing. Absent or wrong, every command stops and says so.
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".tif", ".tiff", ".bmp"}
IMAGE_ROOT_FILE = ROOT / "image-root"


def _images_root() -> Path:
    def stop(why: str) -> None:
        raise SystemExit(
            f"FAIL: {why}\n"
            f"  {IMAGE_ROOT_FILE} must hold one line: the directory this vault's images\n"
            f"  live in. See rules.md -> Where images live."
        )

    if not IMAGE_ROOT_FILE.exists():
        stop(f"no {IMAGE_ROOT_FILE.name} file, so there is nowhere to read or write images.")
    raw = next((l.strip() for l in IMAGE_ROOT_FILE.read_text().splitlines()
                if l.strip() and not l.lstrip().startswith("#")), "")
    if not raw:
        stop(f"{IMAGE_ROOT_FILE.name} has no path in it (only blanks or comments).")
    q = Path(raw).expanduser()
    q = q if q.is_absolute() else (ROOT / q).resolve()
    # Require the tree itself to exist: a typo must fail here, not silently build a new
    # image tree under a path nobody meant.
    if not q.is_dir():
        stop(f"the images tree {q} does not exist (from {IMAGE_ROOT_FILE.name}).")
    return q


IMAGES = _images_root()


def rel_of(path: Path) -> Path:
    """Vault-relative form of an absolute path under either root."""
    p = Path(path).resolve()
    for base in (IMAGES, ROOT):
        try:
            return p.relative_to(base)
        except ValueError:
            continue
    return p


def vpath(rel) -> Path:
    """Resolve a vault-relative path to disk: images under IMAGES, text under ROOT."""
    rel = Path(rel)
    if rel.is_absolute():
        rel = rel_of(rel)
    # tmp/ is scratch: local to the vault, gitignored, and where intermediates belong.
    # It is NOT part of the vault's image tree, so it never follows IMAGES.
    if rel.parts and rel.parts[0] == "tmp":
        return ROOT / rel
    base = IMAGES if rel.suffix.lower() in IMAGE_SUFFIXES else ROOT
    return base / rel
API = "https://api.openai.com/v1/images/edits"
DEFAULT_MODEL = "gpt-image-2.5-sunburst-2026-09-08"
CODEX_MODEL = "gpt-6-astra"
DEFAULT_SIZE = "1536x1024"
DEFAULT_FLATTEN = "#1b1e26"
DEFAULT_MAX_MB = 2.5
ROLES = ("STYLE", "IDENTITY", "EDIT TARGET")
# --backend api reads its key from OPENAI_API_KEY, or from openai.key in the project
# folder (gitignored). Every real paid call must carry --approved-by: the user's own
# words approving that specific call.
API_KEY_FILE = ROOT / "openai.key"

# Verified 2026-09-28 by running each one. image_gen is reachable only from some
# Codex models; the rest burn credits and return no image. Credit rates per 1M
# tokens (input/output): astra 250/1250, sol 100/500, terra 62.5/375 with cached
# input at 6.25. Terra was the cheap default until 2026-09-30, when it, luna and
# sol all stopped being served to ChatGPT-account Codex within a few hours of each
# other. Astra is the only model left that reaches image_gen, so it is the default
# despite being the dearest — there is no cheaper working option to shop for.
CODEX_MODELS_OK = ("gpt-6-astra",)
CODEX_MODELS_BROKEN = {
    "gpt-5.6-terra": "HTTP 400, not supported on a ChatGPT account (broke 2026-09-30)",
    "gpt-5.6-luna": "HTTP 400, not supported on a ChatGPT account (broke 2026-09-30)",
    "gpt-6-sol": "HTTP 400, not supported on a ChatGPT account (broke 2026-09-30)",
    "gpt-6-luna": "image_gen returns no image (verified 2026-09-28)",
    "gpt-reserve": "image_gen returns no image (verified 2026-09-28)",
}

# Delivery specs, so a layout target is named once instead of retyped per call.
PRESETS = {
    # 55 mm right-hand float in the book, 3:2 landscape = 708 dpi, no resize.
    "book-float": {"final_size": "1536x1024", "flatten": "#1b1e26", "max_mb": 2.5},
    # Same float, 4:5 portrait = 554 dpi.
    "book-float-portrait": {"final_size": "1200x1500", "flatten": "#1b1e26",
                            "max_mb": 2.5},
}

# Legacy wordings of the closing style line, accepted with a warning so prompts
# from older receipts can be replayed. The CURRENT line is never hardcoded — it is
# read from style.md, which rules.md declares the sole authority. Hardcoding it
# here would mean a style version bump that rewords the line silently makes gen.py
# reject every prompt bin/prompt.py produces.
LEGACY_CLOSING_LINES = (
    "Render everything in image 1's exact brush scale: fewest possible flat "
    "shapes, no blending, no micro-detail.",
)


class Fail(Exception):
    """An invariant was violated. Nothing is written and nothing is spent."""


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def md5(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


# ---------------------------------------------------------------- style/version


def style_version() -> str:
    head = (ROOT / "style.md").read_text()
    m = re.search(r"\*\*Style version:\s*v(\d+)\*\*", head)
    if not m:
        raise Fail("style.md has no '**Style version: vN**' header")
    return m.group(1)


def style_block() -> str:
    """The Style Block, de-blockquoted, as it must appear in every prompt."""
    text = (ROOT / "style.md").read_text()
    m = re.search(
        r"## Style Block.*?\n\n(.*?)\n\n## Closing style line", text, re.S
    )
    if not m:
        raise Fail("could not locate the Style Block in style.md")
    block = "\n".join(
        re.sub(r"^>\s?", "", line) for line in m.group(1).splitlines()
    )
    # The regex spans Style Block -> Closing style line, so ANY section placed
    # between those two headings is silently shipped to the model as part of the
    # Block. That happened: a prose note sat there and added 188 words -- including
    # its own markdown heading and a dated vault anecdote -- to every prompt for 39
    # generations, all stamped "Style: v2" and all shipping a 402-word Block where v2
    # declares 214. A heading in the extract means the regex over-ran.
    if re.search(r"^#{1,6}\s", block, re.M):
        raise Fail(
            "the extracted Style Block contains a markdown heading, so something "
            "has been inserted between '## Style Block' and '## Closing style line' "
            "in style.md and is being shipped to the model as part of the Block.\n"
            "  Move that section BELOW the closing-line sections."
        )
    return block


def closing_line() -> str:
    """The current closing style line, read from style.md (the sole authority)."""
    text = (ROOT / "style.md").read_text()
    m = re.search(r"## Closing style line.*?\n\n(.*?)\n\n", text, re.S)
    if not m:
        raise Fail("style.md is missing its '## Closing style line' section")
    unquoted = "\n".join(re.sub(r"^>\s?", "", l) for l in m.group(1).splitlines())
    return " ".join(unquoted.split())


def masked_closing_line() -> str:
    """The closing line for masked calls, where the anchor is not image 1."""
    text = (ROOT / "style.md").read_text()
    m = re.search(r"## Closing style line for masked calls.*?\n\n>(.*?)\n\n", text, re.S)
    if not m:
        raise Fail("style.md is missing its masked-call closing style line")
    unquoted = "\n".join(re.sub(r"^>\s?", "", l) for l in (">" + m.group(1)).splitlines())
    return " ".join(unquoted.split())


def check_prompt(prompt: str, masked: bool = False) -> list[str]:
    warnings: list[str] = []
    if norm(style_block()) not in norm(prompt):
        raise Fail(
            "prompt does not contain the style.md Style Block verbatim "
            "(One Rule #2). Paste it at the TOP of the prompt."
        )
    current = masked_closing_line() if masked else closing_line()
    tail = [ln for ln in prompt.strip().splitlines() if ln.strip()][-1]
    if norm(tail) == norm(current):
        pass
    elif masked and norm(tail) == norm(closing_line()):
        raise Fail(
            "this is a masked call, so the EDIT TARGET is image 1 — but the prompt "
            "ends with the ordinary closing line, which tells the model to match "
            "the brush scale of IMAGE 1. That is the image being repainted, and on "
            "an inpaint its rendering is usually the fault being fixed.\n"
            "  Rebuild with: bin/prompt.py --masked"
        )
    elif not masked and norm(tail) == norm(masked_closing_line()):
        raise Fail(
            "this prompt ends with the masked-call closing line but the call is not "
            "masked. Rebuild with bin/prompt.py without --masked."
        )
    elif any(norm(tail) == norm(legacy) for legacy in LEGACY_CLOSING_LINES):
        if masked:
            # Every legacy wording points at IMAGE 1 by index, which on a masked
            # call is the picture being repainted. Tolerated on ordinary calls,
            # never here.
            raise Fail(
                "prompt ends with a legacy closing style line, which names image 1 "
                "by index. On a masked call image 1 is the image being repainted, "
                "so that line would tell the model to match the rendering it is "
                "meant to fix.\n"
                "  Rebuild with: bin/prompt.py --masked"
            )
        warnings.append(
            "prompt ends with a legacy wording of the closing style line, not "
            "style.md's current one. Accepted; rebuild with bin/prompt.py."
        )
    else:
        raise Fail(
            "prompt does not end with the closing style line (One Rule #3).\n"
            f"  last line: {tail[:90]}\n  expected : {current[:90]}"
        )
    return warnings


# ------------------------------------------------------------------- inputs


def validate_reference(ref: Path) -> Path:
    """Reference validation (hard stop). Returns the frozen candidate image.

    Crosses both roots deliberately: `reference.png` and the candidate `image.png` are
    images (under IMAGES), while `reference.md` and `generation.md` are the written
    record (under ROOT). Resolve each by kind rather than as siblings on disk -- they
    are siblings in the vault's layout, not necessarily in one directory.
    """
    rel = rel_of(ref)                        # e.g. assets/ships/x/reference.png
    asset = rel.parent                       # assets/ships/x
    sidecar = ROOT / asset / "reference.md"
    if not sidecar.exists():
        raise Fail(f"{rel}: no reference.md sidecar — asset is unapproved")
    m = re.search(r"candidates/(v\d+)", sidecar.read_text())
    if not m:
        raise Fail(f"{rel_of(sidecar)}: no 'candidates/vNNN' provenance")
    cand = asset / "candidates" / m.group(1)
    image = vpath(cand / "image.png")
    receipt = ROOT / cand / "generation.md"
    if not image.exists():
        raise Fail(f"{rel}: {cand}/image.png is missing"
                   + ("" if IMAGES == ROOT else f" (looked in {IMAGES})"))
    if not receipt.exists():
        raise Fail(f"{rel}: {cand}/generation.md is missing")
    if md5(ref) != md5(image):
        raise Fail(
            f"{rel}: bytes differ from {cand}/image.png — silent overwrite. "
            "Re-promote or pick a newer candidate."
        )
    return image


def frozen_equivalent(path: Path) -> str:
    """Resolve a mutable head revision to its frozen history counterpart."""
    rel = rel_of(path)
    if rel == ANCHOR:
        frozen = vpath(Path("style_versions") /
                       f"canonical_style_reference-v{style_version()}.png")
        if not frozen.exists():
            raise Fail(f"anchor not frozen: {rel_of(frozen)} missing")
        if md5(path) != md5(frozen):
            raise Fail(
                f"{rel} differs from {rel_of(frozen)} — the anchor changed "
                "without a style version bump (see rules.md style versioning)."
            )
        return str(rel_of(frozen))
    if path.name == "reference.png":
        return str(rel_of(validate_reference(path)))
    return "already frozen" if "/candidates/" in str(rel) or "/sources/" in str(rel) else "n/a"


def parse_attach(spec: str) -> tuple[Path, str]:
    if ":" not in spec:
        raise Fail(f"--attach needs path:ROLE, got {spec!r}")
    raw, role = spec.rsplit(":", 1)
    role = role.strip().upper()
    if role not in ROLES:
        raise Fail(f"unknown role {role!r}; use one of {', '.join(ROLES)}")
    path = vpath(raw).resolve()
    if not path.exists():
        raise Fail(f"attachment not found: {raw}")
    if not (path.is_relative_to(ROOT) or path.is_relative_to(IMAGES)):
        raise Fail(f"attachment is outside the vault: {path}")
    return path, role


def check_inputs(attachments: list[tuple[Path, str]], masked: bool = False) -> None:
    """Validate the attachment list by IDENTITY and POSITION, never by label alone.

    A role string is a claim the caller makes; the path is the fact. Checking only
    the role let an anchor attached as "EDIT TARGET" pass every guard and reach a
    billed call that would have repainted the anchor."""
    if not attachments:
        raise Fail("no attachments; the anchor is mandatory (One Rule #1)")
    if len(attachments) > 5:
        raise Fail(
            f"{len(attachments)} attachments; image_gen accepts at most FIVE. "
            "Refusing here rather than letting the backend reject it, which "
            "consumes an orchestration turn first.\n"
            "  Budget the slots: anchor + baseline + identities must total five. "
            "A single group lineup beats several individual sheets."
        )
    rels = [rel_of(p) for p, _ in attachments]
    first, role = attachments[0]

    if rels.count(ANCHOR) > 1:
        raise Fail("anchor attached twice")

    if masked:
        # NARROW, DELIBERATE EXCEPTION TO ONE RULE #1, and the only one.
        # /v1/images/edits masks the FIRST image in image[]. With the anchor first
        # the call returns the anchor with a hole repainted in it — billed, and
        # silently wrong, since the anchor and a scene candidate are both 1536x1024
        # so no dimension check catches it. So the EDIT TARGET takes image 1. The
        # Style Block still reaches the model verbatim in the prompt, and only
        # masked pixels regenerate, so the target's own pixels carry the rendering.
        if rels[0] == ANCHOR:
            raise Fail(
                "image 1 of a masked call is the style anchor — the mask repaints "
                "image 1, so this would repaint the anchor.\n"
                "  Attach the image being edited first, whatever role it is given."
            )
        if role != "EDIT TARGET":
            raise Fail(
                "a masked call must attach the EDIT TARGET as image 1 — got "
                f"{rels[0]}:{role}.\n"
                "  Put --attach <the image being edited>:\"EDIT TARGET\" first; the "
                "anchor follows."
            )
        if sum(1 for _, r in attachments if r == "EDIT TARGET") > 1:
            raise Fail(
                "more than one EDIT TARGET on a masked call. Only image 1 is "
                "masked, so the others would be silently unmasked references.\n"
                "  Attach exactly one EDIT TARGET."
            )
        # The inversion moves the anchor; it does not excuse it. Keeping it attached
        # preserves the Style Block's partner image and keeps the anchor-drift check
        # alive, which only runs on attachments that ARE the anchor.
        if not any(r == ANCHOR for r in rels[1:]):
            raise Fail(
                "a masked call must still attach the style anchor, as image 2 or "
                "later with role STYLE (One Rule #1 is relaxed in ORDER only, not "
                "waived).\n"
                "  Add: --attach ref_images/style_references/"
                "canonical_style_reference.png:STYLE"
            )
    elif rels[0] != ANCHOR or role != "STYLE":
        raise Fail(
            "image 1 must be the style anchor with role STYLE (One Rule #1); "
            f"got {rels[0]}:{role}"
        )

    for path, role in attachments[1:]:
        rel = rel_of(path)
        if rel == ANCHOR:
            continue
        if "/candidates/" in str(rel) and role == "IDENTITY":
            print(
                f"  warn: {rel} is an unapproved candidate used as "
                "IDENTITY — valid only as a user-designated baseline (rules.md)",
                file=sys.stderr,
            )


# ------------------------------------------------------------------ allocation


def check_target(asset: str | None, scene: str | None) -> Path:
    """Validate --asset/--scene and return the candidates dir. Creates nothing.

    Runs pre-flight, so --dry-run catches a typo'd slug and a real run never gets
    as far as paying for an image it then has nowhere to put.
    """
    if bool(asset) == bool(scene):
        raise Fail("pass exactly one of --asset <type>/<slug> or --scene <slug>")
    base = Path("assets/" + asset + "/candidates" if asset else "outputs/" + scene)
    if asset and not (ROOT / base).parent.exists():
        raise Fail(f"no such asset: assets/{asset}")
    return base


def target_dir(base: Path) -> Path:
    """Allocate the next vNNN and create it under BOTH roots, returning it
    vault-relative. The highest vNNN is the max across both trees: numbering them
    independently would let a receipt and an unrelated image share a folder name."""
    used = set()
    for root in {ROOT, IMAGES}:
        d = root / base
        d.mkdir(parents=True, exist_ok=True)
        used |= {int(m.group(1)) for c in d.iterdir()
                 if c.is_dir() and (m := re.fullmatch(r"v(\d+)", c.name))}
    out = base / f"v{max(used, default=0) + 1:03d}"
    for root in {ROOT, IMAGES}:
        (root / out).mkdir(parents=True, exist_ok=True)
    return out


# --------------------------------------------------------------------- request


def build_api_mask(src: Path, vault_mask: Path,
                   out: Path | None = None) -> tuple[int, int]:
    """Convert a vault mask to the shape the Images edits endpoint wants.

    The vault's masks are greyscale with WHITE = the region to change, the convention
    every composite in this project uses. The API wants the opposite, expressed in
    alpha: TRANSPARENT pixels are repainted, opaque ones are kept. Getting this
    backwards repaints the whole frame EXCEPT the part you meant and bills you for
    it, so the conversion happens here rather than in the caller's head.

    Returns (changed_px, total_px) so the caller can report what it is paying to
    repaint."""
    import subprocess

    if has_alpha(vault_mask):
        raise Fail(
            f"{vault_mask.name} carries an alpha channel. The vault convention is a "
            "plain greyscale mask, WHITE = repaint; with alpha present the coverage "
            "is measured from the wrong channel and the call can silently repaint "
            "the whole frame.\n"
            "  Rebuild it ending in  -alpha off  (every recipe in image-surgery does)."
        )
    sw, sh = identify(src)
    mw, mh = identify(vault_mask)
    if (sw, sh) != (mw, mh):
        raise Fail(f"mask is {mw}x{mh} but the image is {sw}x{sh} — they must match")
    if out is not None:
        subprocess.run(
            ["magick", str(src), "(", str(vault_mask), "-negate", ")",
             "-alpha", "off", "-compose", "CopyOpacity", "-composite", str(out)],
            check=True, capture_output=True,
        )
    changed = subprocess.run(
        ["magick", str(vault_mask), "-colorspace", "Gray", "-threshold", "50%",
         "-precision", "10", "-format", "%[fx:round(mean*w*h)]", "info:"],
        capture_output=True, text=True, check=True).stdout.strip()
    # %[fx:...] switches to scientific notation above 1e6 — i.e. above 63.6% of a
    # 1536x1024 frame — so int() would raise on exactly the large masks that most
    # need the coverage warning. Parse as float.
    return round(float(changed)), sw * sh


def api_key() -> str:
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key and API_KEY_FILE.exists():
        key = API_KEY_FILE.read_text().strip()
    if not key:
        raise Fail(f"no API key: set OPENAI_API_KEY or put the key in {API_KEY_FILE.name}")
    return key


def multipart(fields: list[tuple[str, str]], files: list[tuple[str, Path]]):
    boundary = uuid.uuid4().hex
    body = bytearray()
    for name, value in fields:
        body += (
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"\r\n\r\n"
            f"{value}\r\n"
        ).encode()
    for name, path in files:
        ctype = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        body += (
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"; "
            f"filename=\"{path.name}\"\r\nContent-Type: {ctype}\r\n\r\n"
        ).encode()
        body += path.read_bytes() + b"\r\n"
    body += f"--{boundary}--\r\n".encode()
    return bytes(body), f"multipart/form-data; boundary={boundary}"


def generate(prompt: str, attachments, model: str, size: str, quality: str,
             key: str, mask: Path | None = None) -> dict:
    """Post to the Images edits endpoint. With a mask, only the masked pixels are
    repainted — true inpainting, which no other backend here can do."""
    fields = [("model", model), ("prompt", prompt), ("size", size),
              ("quality", quality), ("n", "1")]
    files = [("image[]", p) for p, _ in attachments]
    if mask is not None:
        files.append(("mask", mask))
    body, ctype = multipart(fields, files)
    req = urllib.request.Request(
        API, data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": ctype},
    )
    try:
        with urllib.request.urlopen(req, timeout=900) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        try:
            detail = json.loads(detail)["error"]["message"]
        except Exception:
            pass
        raise Fail(f"API {e.code}: {detail}") from None


# --------------------------------------------------------------------- receipt


def require_binary(name: str, hint: str) -> None:
    """Fail pre-flight rather than mid-run, after an image has been paid for."""
    import shutil

    if shutil.which(name) is None:
        raise Fail(f"{name} not found on PATH — {hint}")


def identify(path: Path) -> tuple[int, int]:
    import subprocess

    out = subprocess.run(["magick", "identify", "-format", "%w %h", str(path)],
                         check=True, capture_output=True, text=True).stdout
    w, h = out.split()
    return int(w), int(h)


def has_alpha(path: Path) -> bool:
    import subprocess

    out = subprocess.run(["magick", "identify", "-format", "%A", str(path)],
                         check=True, capture_output=True, text=True).stdout
    return out.strip().lower() in ("true", "blend", "on", "activate")


def finish(raw: Path, final_size: str, flatten: str, max_mb: float) -> tuple[Path, str]:
    """Deliverable derived from the raw output: exact px, flattened, sRGB, no alpha.

    Scales to FIT inside the target and pads onto the flatten color, so a raw
    output whose aspect differs from the target is never stretched or cropped —
    no hull is ever cut off to satisfy the box.
    """
    import subprocess

    w, h = (int(v) for v in final_size.lower().split("x"))
    rw, rh = identify(raw)

    # When the raw output already IS the delivery spec, a second file is a
    # byte-for-byte duplicate of a multi-MB PNG. Say so instead of writing it.
    if (rw, rh) == (w, h) and not has_alpha(raw):
        mb = raw.stat().st_size / 1_000_000
        note = (f"image.png itself, {final_size}, sRGB 8-bit no alpha, {mb:.2f} MB "
                f"— raw output already meets the delivery spec, so no separate "
                f"deliverable was written. Place image.png.")
        if mb > max_mb:
            note += f"  [OVER the {max_mb} MB budget — needs recompression]"
        return raw, note

    dest = raw.parent / f"delivered-{final_size}.png"
    cmd = ["magick", str(raw), "-colorspace", "sRGB",
           "-resize", f"{w}x{h}", "-background", flatten,
           "-gravity", "center", "-extent", f"{w}x{h}",
           "-alpha", "remove", "-alpha", "off", "-depth", "8",
           "-define", "png:color-type=2", "-strip", str(dest)]
    subprocess.run(cmd, check=True, capture_output=True)
    mb = dest.stat().st_size / 1_000_000
    note = (f"{dest.name}, {final_size}, sRGB 8-bit PNG-24 no alpha, "
            f"flattened onto {flatten}, {mb:.2f} MB; scaled to fit from raw {rw}x{rh}")
    if abs((rw / rh) - (w / h)) > 0.01:
        note += (f"  [raw aspect {rw}:{rh} != target {w}:{h} — padded, not cropped; "
                 "regenerate at the target aspect for a full-bleed image]")
    if mb > max_mb:
        note += f"  [OVER the {max_mb} MB budget — needs recompression]"
    return dest, note


def generate_codex(prompt: str, attachments, model: str, size: str) -> tuple[bytes, str]:
    """Pixel backend: Codex CLI's built-in image_gen, billed to the ChatGPT plan."""
    import subprocess

    if model in CODEX_MODELS_BROKEN:
        raise Fail(f"{model} cannot generate images: {CODEX_MODELS_BROKEN[model]}. "
                   f"Use one of {', '.join(CODEX_MODELS_OK)}.")
    if model not in CODEX_MODELS_OK:
        print(f"  warn: {model} is not in the verified-working list "
              f"({', '.join(CODEX_MODELS_OK)}); it may burn credits and return "
              "no image", file=sys.stderr)
    w, h = (int(v) for v in size.lower().split("x"))
    orientation = "landscape" if w > h else "portrait" if h > w else "square"
    prompt_file = Path(os.environ.get("TMPDIR", "/tmp")) / f"gen-prompt-{uuid.uuid4().hex}.txt"
    prompt_file.write_text(prompt)
    # The prompt is relayed disk -> shell -> tool argument so it CANNOT be
    # paraphrased. The imagegen skill's step 9 tells the model to "normalize"
    # prompts into its own spec; that would silently rewrite the Style Block and
    # break the One Rule. Never let the prompt text pass through model tokens.
    instruction = (
        "Do this mechanically. Do not read this skill's reference docs.\n\n"
        "In ONE code-mode exec block:\n"
        f"1. Read the file {prompt_file} from disk with node's fs.readFileSync.\n"
        "2. Pass those exact bytes as the 'prompt' argument to "
        "tools.image_gen__imagegen, together with the attached images already in "
        "conversation context, in their attached order.\n"
        f"3. Request a single {orientation} image, {w} wide by {h} high.\n\n"
        "Do NOT retype, quote, summarize, normalize, expand or rewrite the prompt "
        "text — read it from disk and pass it through unchanged. The attached images "
        "carry the roles the prompt text assigns them by number. Do not write files, "
        "do not edit the repo, do not move the output.\n\n"
        "Reply with ONLY the absolute path of the generated PNG."
    )
    # --image is variadic, so a positional prompt after it gets swallowed as
    # another filename. Feed the instruction through stdin instead.
    cmd = ["codex", "exec", "-m", model, "-s", "read-only",
           "-c", 'model_reasoning_effort="low"']
    for path, _ in attachments:
        cmd += ["-i", str(path)]
    proc = subprocess.run(cmd, input=instruction, capture_output=True,
                          text=True, timeout=1800)
    if proc.returncode != 0:
        raise Fail(f"codex exec failed ({proc.returncode}): {proc.stderr[-500:]}")
    paths = re.findall(r"/\S+/generated_images/\S+\.png", proc.stdout)
    if not paths:
        raise Fail(f"codex produced no image; tail of output:\n{proc.stdout[-700:]}")
    src = Path(paths[-1])
    if not src.exists():
        raise Fail(f"codex reported {src} but it does not exist")
    tokens = re.search(r"tokens used\s*\n?([\d,]+)", proc.stdout)
    prompt_file.unlink(missing_ok=True)
    return src.read_bytes(), (
        f"codex source {src}"
        + (f"; tokens used {tokens.group(1)}" if tokens else "")
        + "; prompt relayed from disk via fs.readFileSync into the tool argument "
          "(never through model tokens), so the Style Block reached image_gen verbatim"
    )


def write_receipt(out: Path, args, prompt, attachments, model, usage, warnings,
                  delivered: str | None = None, provenance: str = "",
                  raw_size: str = ""):
    label = (args.asset or args.scene).split("/")[-1]
    lines = [
        f"# {label} {out.name}",
        "",
        f"User request verbatim: {args.request or 'TODO — fill in'}",
        f"Mode: {args.mode or 'TODO — fill in'}",
        f"Tool: bin/gen.py, backend={args.backend}"
        + (" (Codex CLI built-in image_gen; underlying image model not exposed)"
           if args.backend == "codex" else " (OpenAI Images API /v1/images/edits)"),
        f"Model: {model}"
        + (" — orchestrator only; the image model it calls is not exposed"
           if args.backend == "codex" else " (pinned snapshot)"),
        f"Parameters: size requested {args.size}"
        + (f", actual {raw_size}" if raw_size and raw_size != args.size else "")
        + (f", quality={args.quality}, n=1" if args.backend == "api" else ""),
        f"Prompt integrity: {provenance}",
        *([f"Mask: {args.mask} (white = repainted; only those pixels regenerate)"]
          if getattr(args, "mask", None) else []),
        *([f"API approval, verbatim: {args.approved_by}"]
          if args.backend == "api" and args.approved_by else []),
        f"Style: v{style_version()}",
        "Inputs:",
    ]
    for i, (path, role) in enumerate(attachments, start=1):
        rel = rel_of(path)
        frozen = frozen_equivalent(path)
        suffix = f"; frozen {frozen}" if frozen not in ("n/a", "already frozen") else ""
        lines.append(f"- Image {i} {role}: {rel}{suffix}")
    if usage:
        lines.append(f"Token usage: {json.dumps(usage, sort_keys=True)}")
    lines += [
        f"Date: {date.today().isoformat()}",
        "Status: awaiting user evaluation",
        f"Output: image.png, {raw_size or args.size} (raw model output, frozen)",
    ]
    if delivered:
        lines.append(f"Delivered: {delivered}")
    lines += [
        "Review: pending — record with bin/review.py once you have seen it",
    ]
    for w in warnings:
        lines.append(f"Warning: {w}")
    lines += ["", "## Exact prompt", "", prompt.rstrip(), ""]
    (out / "generation.md").write_text("\n".join(lines))


# ------------------------------------------------------------------------ main


def check_no_stale_bytecode() -> None:
    """A pre-gate gen.pyc in __pycache__ is a fully runnable copy of this script
    WITHOUT the paid-call gate — found on 2026-09-30 dated a day before the gate
    existed, and gitignored, so invisible in `git status`. Refuse to run beside one."""
    cache = Path(__file__).resolve().parent / "__pycache__"
    if not cache.is_dir():
        return
    # Bytecode here is a pure cache with no value, and `sys.dont_write_bytecode` in
    # this file cannot stop a DIFFERENT process from importing these modules and
    # writing it. So remove it rather than refusing to run — a stale gen*.pyc is a
    # runnable pre-gate copy of this script, and leaving one lying around is the
    # whole problem.
    for pyc in sorted(cache.glob("*.pyc")):
        try:
            pyc.unlink()
            print(f"  removed stale bytecode {pyc.name} (ungated copy risk)",
                  file=sys.stderr)
        except OSError as e:
            raise Fail(
                f"ungated bytecode present and undeletable: {pyc} ({e})\n"
                "  It is a runnable copy of an older gen.py that may bypass the "
                f"paid-call gate. Remove it by hand:  rm -rf {cache}"
            )
    try:
        cache.rmdir()
    except OSError:
        pass


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--asset", help="<type>/<slug>, e.g. ships/the_antares")
    p.add_argument("--scene", help="scene slug under outputs/")
    p.add_argument("--prompt-file", help="assembled prompt; - for stdin "
                                         "(build one with bin/prompt.py)")
    p.add_argument("--refinish", metavar="VDIR",
                   help="re-derive the deliverable from an existing candidate's "
                        "image.png (e.g. outputs/scene/v002) and exit — no "
                        "generation, no new vNNN, nothing billed")
    p.add_argument("--attach", action="append", default=[], metavar="PATH:ROLE",
                   help="repeatable, in order; image 1 must be the anchor as STYLE")
    p.add_argument("--preset", choices=sorted(PRESETS),
                   help="delivery spec: " + "; ".join(
                       f"{k} = {v['final_size']} on {v['flatten']} under "
                       f"{v['max_mb']}MB" for k, v in sorted(PRESETS.items())))
    p.add_argument("--backend", default="codex", choices=["api", "codex"],
                   help="api = OpenAI Images API (needs credits, pins the model); "
                        "codex = Codex CLI image_gen (billed to the ChatGPT plan)")
    p.add_argument("--model", default=None,
                   help=f"default {DEFAULT_MODEL} for api, {CODEX_MODEL} for codex")
    p.add_argument("--size", default=None,
                   help=f"raw size to request (default {DEFAULT_SIZE}, or the "
                        "preset's aspect when --preset is given)")
    p.add_argument("--quality", default="high",
                   choices=["low", "medium", "high", "xhigh", "max", "auto"])
    p.add_argument("--mask", metavar="PATH",
                   help="greyscale mask, WHITE = the region to repaint, same "
                        "dimensions as the EDIT TARGET. --backend api only: only "
                        "the white pixels are regenerated.")
    p.add_argument("--approved-by", metavar="WORDS",
                   help="required for a real --backend api call: the user's verbatim "
                        "words approving this specific paid call; recorded in the receipt")
    p.add_argument("--request", help="user request verbatim, for the receipt")
    p.add_argument("--mode", help="what this attempt changes, for the receipt")
    p.add_argument("--final-size", metavar="WxH",
                   help="post-process to exactly these pixels (needs ImageMagick)")
    p.add_argument("--flatten", default=None,
                   help=f"background color the deliverable is flattened onto "
                        f"(default {DEFAULT_FLATTEN})")
    p.add_argument("--max-mb", type=float, default=None,
                   help=f"warn if the deliverable exceeds this size "
                        f"(default {DEFAULT_MAX_MB})")
    p.add_argument("--dry-run", action="store_true",
                   help="validate invariants and exit without calling the API")
    args = p.parse_args()
    check_no_stale_bytecode()

    # --size, --flatten and --max-mb default to None so that "the user passed this"
    # is simply "it is not None". A preset fills whatever was left unset; an
    # explicit flag always wins. Resolved here, once, before anything reads them.
    spec = PRESETS[args.preset] if args.preset else {}
    if spec:
        args.final_size = args.final_size or spec["final_size"]
    # A preset names the delivery box, so an unspecified raw size matches its
    # aspect and the deliverable comes out full-bleed instead of padded.
    args.size = args.size or spec.get("final_size") or DEFAULT_SIZE
    args.flatten = args.flatten or spec.get("flatten") or DEFAULT_FLATTEN
    args.max_mb = args.max_mb if args.max_mb is not None else spec.get(
        "max_mb", DEFAULT_MAX_MB)

    if args.refinish:
        if args.mask:
            raise Fail("--mask has no meaning with --refinish; --refinish only "
                       "re-derives a deliverable and calls no model.")
        raw = vpath(Path(args.refinish) / "image.png").resolve()
        if not raw.exists():
            raise Fail(f"no image.png in {args.refinish}")
        if not args.final_size:
            raise Fail("--refinish needs --final-size or --preset")
        require_binary("magick", "install ImageMagick (brew install imagemagick)")
        dest, note = finish(raw, args.final_size, args.flatten, args.max_mb)
        verb = "wrote" if dest != raw else "deliverable ="
        print(f"  {verb} {rel_of(dest)}\n  {note}")
        print("  note: update the candidate's generation.md Delivered line by hand")
        return 0

    if not args.prompt_file:
        raise Fail("--prompt-file is required (or use --refinish)")
    if args.prompt_file == "-":
        prompt = sys.stdin.read()
    else:
        pf = Path(args.prompt_file)
        if not pf.exists():
            raise Fail(f"no such prompt file: {args.prompt_file} "
                       "(build one with bin/prompt.py)")
        prompt = pf.read_text()

    # Everything that can fail must fail here, before anything is billed.
    base = check_target(args.asset, args.scene)
    require_binary("magick", "install ImageMagick (brew install imagemagick)")
    if args.backend == "codex":
        require_binary("codex", "install the Codex CLI, or use --backend api")
    attachments = [parse_attach(s) for s in args.attach]
    check_inputs(attachments, masked=bool(args.mask and args.backend == "api"))
    warnings = check_prompt(prompt, masked=bool(args.mask and args.backend == "api"))
    for path, _ in attachments:
        frozen_equivalent(path)  # raises on any provenance failure
    for w in warnings:
        print(f"  warn: {w}", file=sys.stderr)

    model = args.model or (CODEX_MODEL if args.backend == "codex" else DEFAULT_MODEL)
    if args.backend == "codex":
        # Checked HERE, not inside generate_codex(), so --dry-run covers it too.
        # A dead model is the failure that broke this vault three times in one day;
        # a pre-flight that passes a dead model is worse than no pre-flight.
        if model in CODEX_MODELS_BROKEN:
            raise Fail(f"{model} cannot generate images: {CODEX_MODELS_BROKEN[model]}. "
                       f"Use one of {', '.join(CODEX_MODELS_OK)}.")
        if model not in CODEX_MODELS_OK:
            print(f"  warn: {model} is not in the verified-working list "
                  f"({', '.join(CODEX_MODELS_OK)}); it may burn a turn and return "
                  "no image", file=sys.stderr)
    print(f"  backend {args.backend}  model {model}  size {args.size}"
          + (f"  quality {args.quality}" if args.backend == "api" else ""))
    for i, (path, role) in enumerate(attachments, start=1):
        print(f"  image {i} {role:11} {rel_of(path)}")
    api_mask, mask_pct = None, None
    if args.mask:
        if args.backend != "api":
            raise Fail("--mask only applies to --backend api; the codex backend "
                       "cannot inpaint. Use Path 3 (generate-and-composite) instead.")
        vault_mask = vpath(args.mask).resolve()
        if not vault_mask.exists():
            raise Fail(f"no such mask: {args.mask}")
        if not (vault_mask.is_relative_to(ROOT) or vault_mask.is_relative_to(IMAGES)):
            raise Fail(
                f"mask is outside the vault: {vault_mask}. Attachments are confined "
                "to it and the mask must be too — it is recorded in the receipt as "
                "the record of what was repainted, and a path outside the vault "
                "cannot be resolved later."
            )
        masked_image = attachments[0][0]   # the API masks image[0]; the exception
                                           # in check_inputs guarantees this is the
                                           # EDIT TARGET
        tw, th = identify(masked_image)
        if f"{tw}x{th}" != args.size:
            raise Fail(
                f"--size {args.size} does not match the image being masked "
                f"({tw}x{th}). The mask is aligned to that image, so a different "
                "output size would misplace every masked pixel.\n"
                f"  Use --size {tw}x{th}, or mask an image of the size you want."
            )
        changed, total = build_api_mask(masked_image, vault_mask)
        print(f"  mask applies to image 1: {rel_of(masked_image)}")
        mask_pct = 100.0 * changed / total
        print(f"  mask {args.mask}: repainting {mask_pct:.1f}% of the frame "
              f"({changed:,} of {total:,} px)")
        if changed == 0:
            raise Fail("that mask is entirely black — nothing would be repainted. "
                       "The vault convention is WHITE = the region to change.")
        if mask_pct > 90:
            print("  warn: that mask covers almost the whole frame; this is barely "
                  "inpainting and will drift like a full repaint", file=sys.stderr)

    api_key_for_call = None
    if args.backend == "api" and not args.dry_run:
        if not (args.approved_by or "").strip():
            raise Fail(
                "--backend api spends prepaid credits. Ask the user first, then pass "
                "their approval verbatim with --approved-by."
            )
        api_key_for_call = api_key()
        if args.mask:
            api_mask = ROOT / "tmp" / f"api-mask-{uuid.uuid4().hex}.png"
            api_mask.parent.mkdir(exist_ok=True)
            build_api_mask(attachments[0][0], vpath(args.mask).resolve(), api_mask)

    if args.dry_run:
        print("  dry run: invariants OK, nothing sent, nothing allocated")
        if args.backend == "api":
            print("  note: a real run needs --approved-by with the user's approval")
        return 0

    if args.backend == "codex":
        blob, provenance = generate_codex(prompt, attachments, model, args.size)
        usage = None
    else:
        data = generate(prompt, attachments, model, args.size, args.quality,
                        api_key_for_call, api_mask)
        payload = data["data"][0]
        if "b64_json" not in payload:
            raise Fail(f"no image in response: {json.dumps(data)[:400]}")
        import base64

        blob = base64.b64decode(payload["b64_json"])
        usage, provenance = data.get("usage"), "OpenAI Images API, exact prompt bytes sent"

    if api_mask is not None:
        api_mask.unlink(missing_ok=True)   # converted copy; the vault mask is the record

    out = target_dir(base)                 # vault-relative
    raw = vpath(out / "image.png")          # under IMAGES
    raw.write_bytes(blob)
    print(f"  wrote {out}/image.png" + ("" if IMAGES == ROOT else f"  (in {IMAGES})"))

    delivered = None
    if args.final_size:
        dest, delivered = finish(raw, args.final_size, args.flatten, args.max_mb)
        verb = "wrote" if dest != raw else "deliverable ="
        print(f"  {verb} {rel_of(dest)}  ({delivered})")

    rw, rh = identify(raw)
    write_receipt(ROOT / out, args, prompt, attachments, model, usage, warnings,
                  delivered, provenance, f"{rw}x{rh}")
    print(f"  wrote {rel_of(out / 'generation.md')}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Fail as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
