#!/usr/bin/env python3
"""Generate one candidate image (Codex image_gen by default, OpenAI Images API with
--backend api).

Two locations, always given explicitly:
  --package PKG   the style, its anchor, and the assets (people, places, things).
                  Asset work (--asset) writes its candidate here.
  --output OUT    where a scene render (--scene) lands: OUT/<scene>/vNNN/ holds the
                  image and its generation.md. A scene render never writes to PKG.

Enforces the package invariants in code instead of by good intentions:
  - the One Rule (anchor attached FIRST as STYLE, Style Block verbatim at top,
    closing style line last)
  - reference validation (hard stop) for every attached reference.png
  - frozen-revision resolution for every mutable head revision used
  - a complete generation.md receipt, including the pinned model snapshot

Stdlib only, no venv — but two external binaries are required: ImageMagick
(`magick`) always, and the `codex` CLI for the default backend.

  python3 scripts/gen.py --package ~/my-art --output ~/book/art --scene cover \
      --prompt-file /tmp/prompt.txt \
      --attach ref_images/style_references/canonical_style_reference.png:STYLE \
      --attach assets/people/alice/reference.png:IDENTITY

Relative --attach and --mask paths resolve against the package, then the output
folder; a path found in both is refused as ambiguous. Absolute paths are taken as is.
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
import tempfile
import time
import urllib.error
import urllib.request
import uuid
from datetime import date
from pathlib import Path, PurePosixPath

ANCHOR = Path("ref_images/style_references/canonical_style_reference.png")

# The two locations every command works against. Both are given on the command line --
# no config file, no environment override, no fallback: a silent default is how renders
# end up scattered somewhere nobody meant. set_locations() fills them in once, from
# main(); scripts that import this module call it themselves.
PKG: Path | None = None
OUT: Path | None = None


def set_locations(package: str | Path, output: str | Path | None = None) -> None:
    global PKG, OUT
    pkg = Path(package).expanduser().resolve()
    if not pkg.is_dir():
        raise Fail(f"no such package directory: {pkg}")
    if not (pkg / "style.md").exists():
        raise Fail(f"{pkg} has no style.md, so it is not a package "
                   "(see the art-studio skill's templates/style.md)")
    PKG = pkg
    if output is not None:
        out = Path(output).expanduser().resolve()
        if out == pkg or out.is_relative_to(pkg) or pkg.is_relative_to(out):
            raise Fail(f"--output {out} overlaps the package {pkg}. Scene renders must "
                       "land outside the package, which stays read-only while rendering.")
        OUT = out


def rel_of(path: Path) -> str:
    """How a path is written in a receipt: package:<rel>, output:<rel>, or absolute."""
    p = Path(path).resolve()
    for label, base in (("package", PKG), ("output", OUT)):
        if base is not None and p.is_relative_to(base):
            return f"{label}:{p.relative_to(base)}"
    return str(p)


def resolve(raw: str | Path) -> Path:
    """An --attach/--mask path: absolute as is; relative against PKG, then OUT."""
    q = Path(raw).expanduser()
    if q.is_absolute():
        return q.resolve()
    hits = [(b / q).resolve() for b in (PKG, OUT) if b is not None and (b / q).exists()]
    if len(hits) > 1:
        raise Fail(f"{raw} exists in both the package and the output folder; "
                   "give an absolute path")
    return hits[0] if hits else (PKG / q).resolve()


def is_anchor(path: Path) -> bool:
    return Path(path).resolve() == (PKG / ANCHOR).resolve()


API = "https://api.openai.com/v1/images/edits"
DEFAULT_MODEL = "gpt-image-2.5-sunburst-2026-09-08"
CODEX_MODEL = "gpt-6-astra"
DEFAULT_SIZE = "1536x1024"
DEFAULT_FLATTEN = "#ffffff"
DEFAULT_MAX_MB = 2.5
ROLES = ("STYLE", "IDENTITY", "EDIT TARGET")
# --backend api reads its key from OPENAI_API_KEY, or from this file (outside every
# repo, so it can never be committed with a package). Every real paid call must carry
# --approved-by: the user's own words approving that specific call.
API_KEY_FILE = Path("~/.config/art-studio/openai.key").expanduser()

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


def presets() -> dict:
    """Delivery specs, named once in the package's optional presets.json:
    {"book-float": {"final_size": "1536x1024", "flatten": "#1b1e26", "max_mb": 2.5}}"""
    f = PKG / "presets.json"
    if not f.exists():
        return {}
    try:
        data = json.loads(f.read_text())
    except json.JSONDecodeError as e:
        raise Fail(f"{f}: not valid JSON ({e})")
    for name, spec in data.items():
        if "final_size" not in spec:
            raise Fail(f"{f}: preset {name!r} has no final_size")
    return data


def legacy_closing_lines() -> list[str]:
    """Older wordings of the closing style line, accepted with a warning so prompts
    from older receipts can be replayed. Listed in style.md under '## Legacy closing
    style lines', one '> ' quote each. The CURRENT line is never hardcoded anywhere."""
    text = (PKG / "style.md").read_text()
    m = re.search(r"^## Legacy closing style lines.*?\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        return []
    return [" ".join(q.split()) for q in re.findall(r"^>\s?(.+)$", m.group(1), re.M)]


class Fail(Exception):
    """An invariant was violated. Nothing is written and nothing is spent."""


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def md5(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


# ---------------------------------------------------------------- style/version


def style_version() -> str:
    head = (PKG / "style.md").read_text()
    m = re.search(r"\*\*Style version:\s*v(\d+)\*\*", head)
    if not m:
        raise Fail("style.md has no '**Style version: vN**' header")
    return m.group(1)


def style_block(src: Path | None = None) -> str:
    """The Style Block, de-blockquoted, as it must appear in every prompt."""
    text = (src or PKG / "style.md").read_text()
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
    # Block. That has happened (a prose note rode along on 39 generations). A heading
    # in the extract means the regex over-ran.
    if re.search(r"^#{1,6}\s", block, re.M):
        raise Fail(
            "the extracted Style Block contains a markdown heading, so something "
            "has been inserted between '## Style Block' and '## Closing style line' "
            "in style.md and is being shipped to the model as part of the Block.\n"
            "  Move that section BELOW the closing-line sections."
        )
    return block


def closing_line(src: Path | None = None) -> str:
    """The current closing style line, read from style.md (the sole authority)."""
    text = (src or PKG / "style.md").read_text()
    m = re.search(r"## Closing style line.*?\n\n(.*?)\n\n", text, re.S)
    if not m:
        raise Fail("style.md is missing its '## Closing style line' section")
    unquoted = "\n".join(re.sub(r"^>\s?", "", l) for l in m.group(1).splitlines())
    return " ".join(unquoted.split())


def masked_closing_line(src: Path | None = None) -> str:
    """The closing line for masked calls, where the anchor is not image 1."""
    text = (src or PKG / "style.md").read_text()
    m = re.search(r"## Closing style line for masked calls.*?\n\n>(.*?)\n\n", text, re.S)
    if not m:
        raise Fail("style.md is missing its masked-call closing style line")
    unquoted = "\n".join(re.sub(r"^>\s?", "", l) for l in (">" + m.group(1)).splitlines())
    return " ".join(unquoted.split())


def check_style_frozen() -> None:
    """The versioned parts of style.md must equal the frozen style-vN.md. Prose may
    differ; the Style Block and both closing lines may not, or every receipt stamped
    "Style: vN" would be lying about what was sent."""
    frozen = PKG / "style_versions" / f"style-v{style_version()}.md"
    if not frozen.exists():
        raise Fail(f"style not frozen: {rel_of(frozen)} missing (rules.md -> Style "
                   "versioning procedure)")
    for name, part in (("Style Block", style_block), ("closing style line", closing_line),
                       ("masked closing style line", masked_closing_line)):
        if norm(part()) != norm(part(frozen)):
            raise Fail(f"style.md's {name} differs from {rel_of(frozen)} — the style "
                       "changed without a version bump (rules.md -> Style versioning).")


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
            "  Rebuild with: prompt.py --masked"
        )
    elif not masked and norm(tail) == norm(masked_closing_line()):
        raise Fail(
            "this prompt ends with the masked-call closing line but the call is not "
            "masked. Rebuild with prompt.py without --masked."
        )
    elif any(norm(tail) == norm(legacy) for legacy in legacy_closing_lines()):
        if masked:
            # Every legacy wording points at IMAGE 1 by index, which on a masked
            # call is the picture being repainted. Tolerated on ordinary calls,
            # never here.
            raise Fail(
                "prompt ends with a legacy closing style line, which names image 1 "
                "by index. On a masked call image 1 is the image being repainted, "
                "so that line would tell the model to match the rendering it is "
                "meant to fix.\n"
                "  Rebuild with: prompt.py --masked"
            )
        warnings.append(
            "prompt ends with a legacy wording of the closing style line, not "
            "style.md's current one. Accepted; rebuild with prompt.py."
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

    reference.png, reference.md and candidates/vNNN/{image.png,generation.md} are
    siblings in the asset's directory."""
    rel = rel_of(ref)                        # e.g. package:assets/ships/x/reference.png
    asset = ref.parent                       # .../assets/ships/x
    sidecar = asset / "reference.md"
    if not sidecar.exists():
        raise Fail(f"{rel}: no reference.md sidecar — asset is unapproved")
    m = re.search(r"candidates/(v\d+)", sidecar.read_text())
    if not m:
        raise Fail(f"{rel_of(sidecar)}: no 'candidates/vNNN' provenance")
    cand = asset / "candidates" / m.group(1)
    image, receipt = cand / "image.png", cand / "generation.md"
    if not image.exists():
        raise Fail(f"{rel}: {rel_of(image)} is missing")
    if not receipt.exists():
        raise Fail(f"{rel}: {rel_of(receipt)} is missing")
    if md5(ref) != md5(image):
        raise Fail(
            f"{rel}: bytes differ from {rel_of(image)} — silent overwrite. "
            "Re-promote or pick a newer candidate."
        )
    return image


def frozen_equivalent(path: Path) -> str:
    """Resolve a mutable head revision to its frozen history counterpart."""
    rel = rel_of(path)
    if is_anchor(path):
        frozen = PKG / "style_versions" / f"canonical_style_reference-v{style_version()}.png"
        if not frozen.exists():
            raise Fail(f"anchor not frozen: {rel_of(frozen)} missing")
        if md5(path) != md5(frozen):
            raise Fail(
                f"{rel} differs from {rel_of(frozen)} — the anchor changed "
                "without a style version bump (see rules.md style versioning)."
            )
        return rel_of(frozen)
    if path.name == "reference.png":
        return rel_of(validate_reference(path))
    parts = Path(rel.split(":", 1)[-1]).parts   # output:sources/x.png has no leading /
    return "already frozen" if "candidates" in parts or "sources" in parts else "n/a"


def parse_attach(spec: str) -> tuple[Path, str]:
    if ":" not in spec:
        raise Fail(f"--attach needs path:ROLE, got {spec!r}")
    raw, role = spec.rsplit(":", 1)
    role = role.strip().upper()
    if role not in ROLES:
        raise Fail(f"unknown role {role!r}; use one of {', '.join(ROLES)}")
    path = resolve(raw)
    if not path.exists():
        raise Fail(f"attachment not found: {raw}")
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
            "A scene attaches one single-view crop per cast member, never a "
            "multi-view sheet; carry anyone beyond the cap in text."
        )
    rels = [rel_of(p) for p, _ in attachments]
    anchors = [is_anchor(p) for p, _ in attachments]
    first, role = attachments[0]

    if anchors.count(True) > 1:
        raise Fail("anchor attached twice")

    if masked:
        # NARROW, DELIBERATE EXCEPTION TO ONE RULE #1, and the only one.
        # /v1/images/edits masks the FIRST image in image[]. With the anchor first
        # the call returns the anchor with a hole repainted in it — billed, and
        # silently wrong, since the anchor and a scene candidate are both 1536x1024
        # so no dimension check catches it. So the EDIT TARGET takes image 1. The
        # Style Block still reaches the model verbatim in the prompt, and only
        # masked pixels regenerate, so the target's own pixels carry the rendering.
        if anchors[0]:
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
        if not any(anchors[1:]):
            raise Fail(
                "a masked call must still attach the style anchor, as image 2 or "
                "later with role STYLE (One Rule #1 is relaxed in ORDER only, not "
                "waived).\n"
                "  Add: --attach ref_images/style_references/"
                "canonical_style_reference.png:STYLE"
            )
    elif not anchors[0] or role != "STYLE":
        raise Fail(
            "image 1 must be the style anchor with role STYLE (One Rule #1); "
            f"got {rels[0]}:{role}"
        )

    for path, role in attachments[1:]:
        rel = rel_of(path)
        if is_anchor(path):
            continue
        if "/candidates/" in rel and role == "IDENTITY":
            print(
                f"  warn: {rel} is an unapproved candidate used as "
                "IDENTITY — valid only as a user-designated baseline (rules.md)",
                file=sys.stderr,
            )


# ------------------------------------------------------------------ allocation


def check_target(asset: str | None, scene: str | None) -> Path:
    """Validate --asset/--scene and return the absolute directory whose next vNNN
    the run will fill. Creates nothing.

    Asset work writes into the package (it is changing the package); a scene render
    writes into the output folder and never touches the package. Runs pre-flight, so
    --dry-run catches a typo'd slug and a real run never gets as far as paying for an
    image it then has nowhere to put.
    """
    if bool(asset) == bool(scene):
        raise Fail("pass exactly one of --asset <type>/<slug> or --scene <slug>")
    if asset:
        if OUT is not None:
            raise Fail("--output has no meaning with --asset: asset candidates are "
                       "written into the package. Drop --output.")
        if not (PKG / "assets" / asset).is_dir():
            raise Fail(f"no such asset: {PKG / 'assets' / asset}")
        return writable_base(PKG / "assets" / asset / "candidates")
    if OUT is None:
        raise Fail("--scene needs --output: the folder this render is delivered to")
    if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", scene):
        raise Fail(f"scene slug {scene!r}: use lowercase letters, digits, . _ -")
    return writable_base(OUT / scene)


def writable_base(base: Path) -> Path:
    """base, refused pre-flight if it or its nearest existing ancestor is not a
    directory: the run could not create its vNNN folder there after billing."""
    for p in (base, *base.parents):
        if p.exists():
            if not p.is_dir():
                raise Fail(f"{p} is not a directory, so {base} cannot hold attempt "
                           "folders. Move it aside and rerun.")
            break
    return base


def deleted_numbers(base: Path) -> set[int]:
    """The attempt numbers base/DELETED.md records as vNNN tokens (empty if no log).

    Numbers are never reused: an attempt deleted at the user's insistence is logged
    there, and numbering continues past it. Read pre-flight, so a log the run cannot
    read refuses the run before anything is billed rather than after.
    """
    log = base / "DELETED.md"
    try:
        text = log.read_text(errors="replace")
    except FileNotFoundError:
        return set()
    except OSError as e:
        fail = Fail(f"cannot read the deletion log {log} ({e.strerror or e}). It must be "
                    "a readable file listing removed attempts as vNNN; fix it (e.g. "
                    "chmod u+r) and rerun.")
        fail.reason = e.strerror or str(e)
        raise fail from None
    return {int(n) for n in re.findall(r"\bv(\d{3,})\b", text)}


def target_dir(base: Path, deleted: set[int]) -> Path:
    """Allocate and create the next vNNN under base, past every folder on disk and
    every number in base/DELETED.md.

    `deleted` is the log as read pre-flight. The log is read again here, so a
    deletion logged while the backend ran still counts; if that re-read fails, the
    image is already paid for, so warn and number from `deleted` rather than fail.
    For the same reason, a concurrent run that creates the chosen vNNN between the
    scan and the mkdir does not fail this one: it takes the next free number.
    """
    try:
        logged = deleted_numbers(base)
    except Fail as e:
        print(f"  warn: could not re-read {base / 'DELETED.md'} after generating "
              f"({e.reason}); numbering from the log as read before generating. Fix "
              "the log before the next run.", file=sys.stderr)
        logged = set()
    base.mkdir(parents=True, exist_ok=True)
    used = {int(m.group(1)) for c in base.iterdir()
            if c.is_dir() and (m := re.fullmatch(r"v(\d+)", c.name))}
    used |= logged | deleted
    n = max(used, default=0) + 1   # above every logged number, so counting up skips them
    while True:
        out = base / f"v{n:03d}"
        try:
            out.mkdir()
            return out
        except FileExistsError:   # claimed by a concurrent run since the scan
            n += 1


# --------------------------------------------------------------------- request


def build_api_mask(src: Path, user_mask: Path,
                   out: Path | None = None) -> tuple[int, int]:
    """Convert a user mask to the shape the Images edits endpoint wants.

    Masks here are greyscale with WHITE = the region to change, the convention
    every composite in this project uses. The API wants the opposite, expressed in
    alpha: TRANSPARENT pixels are repainted, opaque ones are kept. Getting this
    backwards repaints the whole frame EXCEPT the part you meant and bills you for
    it, so the conversion happens here rather than in the caller's head.

    Returns (changed_px, total_px) so the caller can report what it is paying to
    repaint."""
    import subprocess

    if has_alpha(user_mask):
        raise Fail(
            f"{user_mask.name} carries an alpha channel. The convention is a "
            "plain greyscale mask, WHITE = repaint; with alpha present the coverage "
            "is measured from the wrong channel and the call can silently repaint "
            "the whole frame.\n"
            "  Rebuild it ending in  -alpha off  (every recipe in reference/imagemagick.md does)."
        )
    sw, sh = identify(src)
    mw, mh = identify(user_mask)
    if (sw, sh) != (mw, mh):
        raise Fail(f"mask is {mw}x{mh} but the image is {sw}x{sh} — they must match")
    if out is not None:
        subprocess.run(
            ["magick", str(src), "(", str(user_mask), "-negate", ")",
             "-alpha", "off", "-compose", "CopyOpacity", "-composite", str(out)],
            check=True, capture_output=True,
        )
    changed = subprocess.run(
        ["magick", str(user_mask), "-colorspace", "Gray", "-threshold", "50%",
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


def record_delivered(receipt: Path, delivered: str) -> None:
    """Set the receipt's Delivered line after --refinish, as promote.py sets Status.

    Replaces an existing Delivered line; otherwise inserts one after the Output line,
    or, on a receipt without one, before its first '## ' section."""
    text = receipt.read_text()
    line = f"Delivered: {delivered}"
    for pattern, repl in ((r"^Delivered:.*$", lambda m: line),
                          (r"^Output:.*$", lambda m: f"{m.group(0)}\n{line}"),
                          (r"\n+(?=^## )", lambda m: f"\n{line}\n\n")):
        new, n = re.subn(pattern, repl, text, count=1, flags=re.M)
        if n:
            break
    else:
        new = text.rstrip("\n") + f"\n{line}\n"
    receipt.write_text(new)


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
        f"Tool: art-studio gen.py, backend={args.backend}"
        + (" (Codex CLI built-in image_gen; underlying image model not exposed)"
           if args.backend == "codex" else " (OpenAI Images API /v1/images/edits)"),
        f"Model: {model}"
        + (" — orchestrator only; the image model it calls is not exposed"
           if args.backend == "codex" else " (pinned snapshot)"),
        f"Parameters: size requested {args.size}"
        + (f", actual {raw_size}" if raw_size and raw_size != args.size else "")
        + (f", quality={args.quality}, n=1" if args.backend == "api" else ""),
        f"Prompt integrity: {provenance}",
        *([f"Mask: {rel_of(resolve(args.mask))} (white = repainted; only those pixels regenerate)"]
          if getattr(args, "mask", None) else []),
        *([f"API approval, verbatim: {args.approved_by}"]
          if args.backend == "api" and args.approved_by else []),
        f"Style: v{style_version()}",
        f"Package: {PKG}",
        *([f"Output folder: {OUT}"] if OUT is not None else []),
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
        "Review: pending — record with review.py once you have seen it",
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
    p.add_argument("--package", required=True, metavar="PKG",
                   help="the package: style.md, anchor, assets")
    p.add_argument("--output", metavar="OUT",
                   help="where a --scene render lands (OUT/<scene>/vNNN/)")
    p.add_argument("--asset", help="<type>/<slug> under PKG/assets; the candidate is "
                                   "written into the package")
    p.add_argument("--scene", help="scene slug; needs --output")
    p.add_argument("--prompt-file", help="assembled prompt; - for stdin "
                                         "(build one with prompt.py)")
    p.add_argument("--refinish", metavar="VDIR",
                   help="re-derive the deliverable from an existing candidate's "
                        "image.png (a vNNN directory), record it on the receipt's "
                        "Delivered line, and exit — no generation, no new vNNN, "
                        "nothing billed")
    p.add_argument("--attach", action="append", default=[], metavar="PATH:ROLE",
                   help="repeatable, in order; image 1 must be the anchor as STYLE")
    p.add_argument("--preset", metavar="NAME",
                   help="a delivery spec named in the package's presets.json")
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
    set_locations(args.package, args.output)

    # --size, --flatten and --max-mb default to None so that "the user passed this"
    # is simply "it is not None". A preset fills whatever was left unset; an
    # explicit flag always wins. Resolved here, once, before anything reads them.
    spec = {}
    if args.preset:
        known = presets()
        if args.preset not in known:
            raise Fail(f"no preset {args.preset!r} in {PKG / 'presets.json'}; "
                       f"known: {', '.join(sorted(known)) or 'none'}")
        spec = known[args.preset]
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
        raw = (Path(args.refinish).expanduser() / "image.png").resolve()
        receipt = raw.parent / "generation.md"
        if not raw.exists():
            raise Fail(f"no image.png in {args.refinish}")
        if not receipt.exists():
            raise Fail(f"no generation.md in {args.refinish}, so the deliverable could "
                       "not be recorded. Every vNNN needs its receipt.")
        if not args.final_size:
            raise Fail("--refinish needs --final-size or --preset")
        require_binary("magick", "install ImageMagick (brew install imagemagick)")
        dest, note = finish(raw, args.final_size, args.flatten, args.max_mb)
        verb = "wrote" if dest != raw else "deliverable ="
        print(f"  {verb} {dest}\n  {note}")
        record_delivered(receipt, note)
        print(f"  updated {receipt} Delivered line")
        return 0

    if not args.prompt_file:
        raise Fail("--prompt-file is required (or use --refinish)")
    if args.prompt_file == "-":
        prompt = sys.stdin.read()
    else:
        pf = Path(args.prompt_file)
        if not pf.exists():
            raise Fail(f"no such prompt file: {args.prompt_file} "
                       "(build one with prompt.py)")
        prompt = pf.read_text()

    # Everything that can fail must fail here, before anything is billed.
    base = check_target(args.asset, args.scene)
    deleted = deleted_numbers(base)
    require_binary("magick", "install ImageMagick (brew install imagemagick)")
    if args.backend == "codex":
        require_binary("codex", "install the Codex CLI, or use --backend api")
    attachments = [parse_attach(s) for s in args.attach]
    check_inputs(attachments, masked=bool(args.mask and args.backend == "api"))
    check_style_frozen()
    warnings = check_prompt(prompt, masked=bool(args.mask and args.backend == "api"))
    for path, _ in attachments:
        frozen_equivalent(path)  # raises on any provenance failure
    for w in warnings:
        print(f"  warn: {w}", file=sys.stderr)

    model = args.model or (CODEX_MODEL if args.backend == "codex" else DEFAULT_MODEL)
    if args.backend == "codex":
        # Checked HERE, not inside generate_codex(), so --dry-run covers it too.
        # A dead model is the failure that broke image generation three times in one day;
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
        user_mask = resolve(args.mask)
        if not user_mask.exists():
            raise Fail(f"no such mask: {args.mask}")
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
        changed, total = build_api_mask(masked_image, user_mask)
        print(f"  mask applies to image 1: {rel_of(masked_image)}")
        mask_pct = 100.0 * changed / total
        print(f"  mask {args.mask}: repainting {mask_pct:.1f}% of the frame "
              f"({changed:,} of {total:,} px)")
        if changed == 0:
            raise Fail("that mask is entirely black — nothing would be repainted. "
                       "The convention is WHITE = the region to change.")
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
            api_mask = Path(tempfile.gettempdir()) / f"api-mask-{uuid.uuid4().hex}.png"
            build_api_mask(attachments[0][0], resolve(args.mask), api_mask)

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
        api_mask.unlink(missing_ok=True)   # converted copy; the user mask is the record

    out = target_dir(base, deleted)
    raw = out / "image.png"
    raw.write_bytes(blob)
    print(f"  wrote {raw}")

    delivered = None
    if args.final_size:
        dest, delivered = finish(raw, args.final_size, args.flatten, args.max_mb)
        verb = "wrote" if dest != raw else "deliverable ="
        print(f"  {verb} {dest}  ({delivered})")

    rw, rh = identify(raw)
    write_receipt(out, args, prompt, attachments, model, usage, warnings,
                  delivered, provenance, f"{rw}x{rh}")
    print(f"  wrote {out / 'generation.md'}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Fail as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
