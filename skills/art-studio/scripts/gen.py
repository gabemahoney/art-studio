#!/usr/bin/env python3
"""Generate one candidate image (Codex image_gen by default, OpenAI Images API with
--backend api).

Two locations, always given explicitly:
  --package PKG   the style, its anchor, and the assets (people, places, things).
                  Asset work (--asset) writes its candidate here.
  --output OUT    where a scene render (--scene) lands: OUT/<scene>/vNNN/ holds the
                  image and its generation.md. A scene render never writes to PKG.
                  A Layered Scene is made one Layer (--layer, into
                  OUT/<scene>/layers/<id>/vNNN/) or Draft (--draft, into
                  OUT/<scene>/drafts/vNNN/) at a time, at the scene's Frame.

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
import shutil
import tempfile
import time
import urllib.error
import urllib.request
import uuid
from datetime import date
from pathlib import Path, PurePosixPath

# python3 -I leaves this script's folder off sys.path; scene_state lives beside it.
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
import scene_state  # noqa: E402
from prompt import TRANSPARENT_LEAD  # noqa: E402

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
ROLES = ("STYLE", "IDENTITY", "EDIT TARGET", "PLACEMENT")
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
    if not re.fullmatch(scene_state.SLUG, scene):
        raise Fail(f"scene slug {scene!r}: use lowercase letters, digits, . _ -")
    return writable_base(OUT / scene)


def writable_base(base: Path) -> Path:
    """base, refused pre-flight if it or its nearest existing ancestor is not a
    writable directory, or a broken symlink stands in the way: the run could not
    create its vNNN folder there after billing."""
    for p in (base, *base.parents):
        if p.is_symlink() and not p.exists():
            raise Fail(f"{p} is a broken symlink, so {base} cannot hold attempt "
                       "folders. Fix or remove the link and rerun.")
        if p.exists():
            if not p.is_dir():
                raise Fail(f"{p} is not a directory, so {base} cannot hold attempt "
                           "folders. Move it aside and rerun.")
            if not os.access(p, os.W_OK | os.X_OK):
                raise Fail(f"{p} is not writable, so {base} cannot hold attempt "
                           "folders. Fix its permissions (e.g. chmod u+wx) and rerun.")
            break
    return base


def check_layer_plan(scene_dir: Path, layer: str | None, draft: bool) -> dict | None:
    """A scene's first generation needs a Layer Plan the User confirmed, recorded with
    layers.py plan. A scene with attempts and no plan (made before Layer Plans) and a
    Single-Layer Scene generate as before; a Layered Scene is made one Layer (--layer)
    or Draft (--draft) at a time. Returns the current plan."""
    try:
        records = scene_state.read_journal(scene_dir)
    except scene_state.Fail as e:
        raise Fail(str(e)) from None
    plan = scene_state.current_plan(records)
    if plan is None and not scene_state.generated(scene_dir, deleted_numbers):
        raise Fail(f"scene {scene_dir.name} has no Layer Plan and nothing generated yet. "
                   "Propose a Layer Plan (single or layered) to the User and record their "
                   "confirmation with layers.py plan before generating.")
    if plan is None or not plan["layered"]:
        if layer or draft:
            raise Fail(f"scene {scene_dir.name} is a Single-Layer Scene, so it has no "
                       "Layers or Drafts: drop --layer/--draft and generate it as one image.")
        return plan
    where = f"journal/{plan['number']:03d}.json"
    if not (layer or draft):
        raise Fail(f"scene {scene_dir.name} is layered ({where}), so it is made one Layer "
                   "or Draft at a time, never as one image: pass --layer <layer-id> or "
                   "--draft.")
    ids = [l["id"] for l in plan["layers"]]
    if layer and layer not in ids:
        raise Fail(f"Layer {layer!r} is not in scene {scene_dir.name}'s current Layer Plan "
                   f"({where}), which holds, bottom to top: {', '.join(ids)}.")
    return plan


def layer_or_draft(folder: Path) -> bool:
    """Whether folder is a Layer Version (<scene>/layers/<id>/vNNN) or Draft
    (<scene>/drafts/vNNN) of a scene whose current plan is layered; a folder that only
    happens to sit under one named layers/ or drafts/ is not."""
    parts = Path(folder).resolve().parts
    if len(parts) > 3 and parts[-3] == "layers":
        scene = Path(*parts[:-3])
    elif len(parts) > 2 and parts[-2] == "drafts":
        scene = Path(*parts[:-2])
    else:
        return False
    try:
        return scene_state.is_layered(scene_state.read_journal(scene))
    except scene_state.Fail:
        return False


def in_scene_folder(path: Path) -> bool:
    """Whether path lies in a scene folder of the output folder (OUT/<scene>/...), as
    opposed to OUT/sources/, where single-view cast crops live."""
    if OUT is None or not Path(path).resolve().is_relative_to(OUT):
        return False
    parts = Path(path).resolve().relative_to(OUT).parts
    return len(parts) > 1 and parts[0] != "sources"


def check_layer_inputs(attachments: list[tuple[Path, str]], scene_dir: Path, plan: dict,
                       layer: str | None) -> tuple[dict, Path | None]:
    """The attachment rules for a Layer (layer given) or Draft (layer None) generation,
    on top of check_inputs: a Layer's EDIT TARGET, PLACEMENT and IDENTITY come only from
    where the SRD allows, every same-scene image is unaltered, and a Layer never takes
    a Layer Version, adjusted copy of one or Draft off the Frame's aspect ratio.

    Returns the md5 of each same-scene attachment, for its Inputs line, and the
    starting version: the version of this Layer the EDIT TARGET holds, if any."""
    targets = [p for p, r in attachments if r == "EDIT TARGET"]
    if layer and len(targets) > 1:
        raise Fail("a Layer generation attaches at most one EDIT TARGET; got "
                   + ", ".join(rel_of(p) for p in targets))
    allowed = ("this scene's Layer Versions and Combined Images, and adjusted copies of "
               "them saved in its sources/ with a sidecar")
    md5s = {}
    for path, role in attachments:
        if is_anchor(path):
            continue
        rel, what = rel_of(path), scene_state.classify(scene_dir, path)
        kind = what and what["kind"]
        if layer and role == "EDIT TARGET" and kind in (None, "draft", "other"):
            raise Fail(f"{rel} can't be a Layer generation's EDIT TARGET: "
                       + ("a Draft is a reference for placement, scale and light only"
                          if kind == "draft" else "editing it would import content into "
                          "the Layer from outside the scene")
                       + f". A Layer's EDIT TARGET is one of {allowed}.")
        if role == "PLACEMENT" and kind in (None, "other"):
            raise Fail(f"{rel} can't be PLACEMENT, which takes only {allowed}, and its "
                       "Drafts.")
        if layer and role == "IDENTITY" and in_scene_folder(path):
            raise Fail(f"{rel} is a scene's image, which a Layer generation never takes "
                       "as IDENTITY: attach this scene's images as PLACEMENT (placement, "
                       "scale and light only). Another scene's images can't be attached.")
        if kind == "other":
            md5s[path] = md5(path)
        if kind in (None, "other"):
            continue
        record = (path.with_suffix(".md") if kind == "adjusted"
                  else what["dir"] / "generation.md")
        trouble = scene_state.problem(what["dir"], deleted_numbers)
        if trouble is None and kind == "adjusted" and \
                md5(what["dir"] / "image.png") != what["source_md5"]:
            trouble = f"not the image its sidecar records (md5 {what['source_md5']})"
        if trouble:
            raise Fail(f"can't attach {rel}: {rel_of(what['dir'] / 'image.png')} is "
                       f"{trouble}; {rel_of(record)} names it.")
        made = what["source"]["kind"] if kind == "adjusted" else kind
        if layer and made in ("layer", "draft") and \
                not scene_state.ratio_matches(identify(path), plan["frame"]):
            w, h = identify(path)
            raise Fail(f"{rel} is {w}x{h}, which doesn't match the Frame's aspect ratio "
                       f"({scene_state.frame_text(plan['frame'])}), so it is never "
                       "attached to a Layer generation (its pixels can still be "
                       "transplanted).")
        md5s[path] = md5(path)
    start = (scene_state.holds(scene_state.classify(scene_dir, targets[0]), layer)
             if layer and targets else None)
    # SR-5.5: no image holding another version of this Layer, so a version the User
    # may have rejected never feeds the next one; a fresh generation attaches none
    for path, _ in attachments if layer else []:
        what = scene_state.classify(scene_dir, path)
        if what and what["kind"] == "other":
            raise Fail(f"{rel_of(path)} lies in the scene's folder but isn't one of its Layer "
                       "Versions, Combined Images, Drafts or adjusted copies with a sidecar "
                       "(final.png, final-layers/ and raw.png are copies), so which Layer "
                       "versions it holds can't be checked: attach the record it copies.")
        held = scene_state.holds(what, layer)
        if held is not None and (start is None or held.resolve() != start.resolve()):
            raise Fail(f"{rel_of(path)} holds Layer {layer}'s {held.name}, but this generation "
                       + (f"starts from {start.name}" if start else "is fresh (no EDIT TARGET "
                          "holds a version of it)")
                       + f": a Layer generation attaches no image holding another version of "
                       "its Layer. Attach a Combined Image or Draft without it, or edit "
                       "from that version.")
    return md5s, start


def check_starting_version(scene_dir: Path, plan: dict, layer: str, start: Path) -> str | None:
    """SR-5.4: a warning, naming both, when the starting version isn't the Layer's
    Default Version. A warning, not a refusal: a retry within one step reuses the
    step's starting version after a failed generation became the Layer's latest."""
    try:
        records = scene_state.read_journal(scene_dir)
    except scene_state.Fail as e:
        raise Fail(str(e)) from None
    versions = scene_state.layer_versions(scene_dir, layer, plan, deleted_numbers, identify)
    st = scene_state.layer_state(scene_state.journal_view(records), layer, versions)
    if st["default"] is not None and st["default"]["dir"].resolve() == start.resolve():
        return None
    return (f"the starting version, {layer} {start.name}, isn't Layer {layer}'s Default "
            "Version (" + (f"{st['default']['name']}, {st['default_why']}" if st["default"]
                           else "none") + "): revise from the Default Version, unless this "
            "retries a step that started from it")


# ------------------------------------------------------------- Layer outputs


def magick(*args) -> str:
    import subprocess

    return subprocess.run(["magick", *map(str, args)], check=True, capture_output=True,
                          text=True).stdout


def fx(path: Path, expr: str, *pre: str) -> float:
    return float(magick(path, *pre, "-format", f"%[fx:{expr}]", "info:"))


def separation_checks(img: Path, emissive: bool) -> list[str]:
    """The SR-4.3 checks on a Layer generation's output, with the rules and starting
    thresholds of Research b.gr7's `layerlab.py check` (calibration, not limits).
    Returns failure codes; an empty list passes.

    The backdrop checks read colour only when alpha is absent or unused (fewer than
    0.1% of pixels below alpha 0.02); otherwise they would read whatever RGB lies
    hidden under alpha 0. Unused alpha alone is not a failure."""
    ext = ("-alpha", "extract")
    codes = []
    if not has_alpha(img):
        codes.append("NO_ALPHA")
        unused = True
    else:
        if fx(img, "minima", *ext) >= 0.98:     # no pixel below the solid level
            codes.append("OPAQUE_EVERYWHERE")
        unused = fx(img, "mean", *ext, "-threshold", "2%", "-negate") < 0.001
    if unused:
        flat = lambda expr: fx(img, "mean", "-alpha", "off", "-fx", f"{expr}?1:0")
        neutral = flat("(max(r,max(g,b))-min(r,min(g,b)))<0.04 && "
                       "(0.2126*r+0.7152*g+0.0722*b)>0.55")
        if neutral >= 0.20:
            codes.append(f"PAINTED_CHECKERBOARD_OR_FLAT_LIGHT_BACKDROP(neutral={neutral:.2f})")
        for name, expr in (("GREEN", "(g-max(r,b))>0.5"), ("MAGENTA", "(min(r,b)-g)>0.5"),
                           ("BLACK", "max(r,max(g,b))<0.04")):
            frac = flat(expr)
            if frac >= 0.20:
                codes.append(f"BACKDROP_LEFT_IN_{name}({frac:.2f})")
                # light-only content on an opaque black backdrop is glow baked onto
                # dark too, in the form unmultiplying repairs exactly
                if name == "BLACK" and emissive:
                    codes.append(f"GLOW_BAKED_ON_DARK(black_backdrop={frac:.2f})")
        return codes

    # the edge ring: solid pixels (alpha >= 0.5) within 3 px of a clear one (< 0.02),
    # whose colour shows a backdrop left in; the interior is the rest of the solid
    with tempfile.TemporaryDirectory(prefix="gen-checks-") as tmp:
        ring, inner = Path(tmp) / "ring.png", Path(tmp) / "inner.png"
        magick(img, *ext, "(", "+clone", "-threshold", "2%", "-negate", "-morphology",
               "Dilate", "Disk:3", ")", "(", "-clone", "0", "-threshold", "50%", ")",
               "-delete", "0", "-compose", "multiply", "-composite", ring)
        magick(img, *ext, "-threshold", "50%", ring, "-compose", "minus_src", "-composite",
               inner)
        stats = {}
        for where, mask in (("ring", ring), ("inner", inner)):
            area = fx(mask, "mean")
            stats[where] = {"area": area}
            for name, expr in (("dark", "(0.2126*r+0.7152*g+0.0722*b)<0.08"),
                               ("green", "(g-max(r,b))>0.12"),
                               ("white", "min(r,min(g,b))>0.92")):
                hit = float(magick(img, "-alpha", "off", "-fx", f"{expr}?1:0", mask,
                                   "-compose", "multiply", "-composite",
                                   "-format", "%[fx:mean]", "info:"))
                stats[where][name] = round(hit / max(area, 1e-9), 3)
    ring, inner = stats["ring"], stats["inner"]
    if ring["area"] > 0:
        if ring["green"] > 0.05:
            codes.append(f"GREEN_FRINGE(ring={ring['green']})")
        if ring["dark"] - inner["dark"] > 0.15:
            codes.append(f"DARK_FRINGE(ring={ring['dark']},inner={inner['dark']})")
        if ring["white"] - inner["white"] > 0.15:
            codes.append(f"LIGHT_FRINGE(ring={ring['white']},inner={inner['white']})")
    if emissive and inner["dark"] > 0.10:
        codes.append(f"GLOW_BAKED_ON_DARK(dark_solid={inner['dark']})")
    return codes


def unmultiply(src: Path, dest: Path) -> None:
    """SR-4.4: light painted onto dark, made transparent. Flattened onto black,
    alpha = max(R,G,B), colour = RGB / alpha. Exact for light added over black; never
    for opaque content, which it would make partly transparent."""
    with tempfile.TemporaryDirectory(prefix="gen-unmult-") as tmp:
        onblack, a, c = (Path(tmp) / n for n in ("onblack.png", "a.png", "c.png"))
        magick(src, "-background", "black", "-alpha", "remove", "-alpha", "off", onblack)
        magick(onblack, "-alpha", "off", "-separate", "-evaluate-sequence", "max", a)
        magick(onblack, a, "-channel", "RGB", "-fx", "v<=0.004?0:min(1,u/v)", "+channel", c)
        magick(c, a, "-alpha", "off", "-compose", "CopyOpacity", "-composite",
               "-define", "png:color-type=6", dest)


def make_layer_version(out: Path, frame: dict, checked: bool,
                       emissive: bool) -> tuple[list[str], list[str], bool]:
    """Turn out/raw.png, a Layer generation's output, into out/image.png, the Layer
    Version: checked (when the prompt carries the transparent-background block),
    repaired when an emissive output shows glow baked onto dark, checked again, then
    scaled to the Frame when its aspect ratio matches. raw.png stays only when
    image.png differs from it. Returns the receipt lines, the final failures, and
    whether the version is at the Frame."""
    raw, image = out / "raw.png", out / "image.png"
    rw, rh = identify(raw)
    fw, fh = frame["width"], frame["height"]
    lines, failures = [f"Raw size: {rw}x{rh}"], []
    with tempfile.TemporaryDirectory(prefix="gen-layer-") as tmp:
        src, repair = raw, None
        if checked:
            failures = separation_checks(raw, emissive)
            lines.append(f"Checks: round 1, raw output: {' '.join(failures) or 'pass'}")
            if emissive and any(f.startswith("GLOW_BAKED_ON_DARK") for f in failures):
                src = Path(tmp) / "repaired.png"
                unmultiply(raw, src)
                repair = ("glow baked onto dark, unmultiplied: flattened onto black, alpha "
                          "= max(R,G,B), colour = RGB / alpha; raw output kept as raw.png")
                failures = separation_checks(src, emissive)
                lines.append(f"Checks: round 2, after repair: {' '.join(failures) or 'pass'}")
        else:
            lines.append("Checks: not run; the prompt lacks the transparent-background block")
        fits = scene_state.ratio_matches((rw, rh), frame)
        if fits and (rw, rh) != (fw, fh):
            magick(src, "-resize", f"{fw}x{fh}!", image)
            lines.append(f"Scale: x {fw / rw:.4f}, y {fh / rh:.4f} (-resize {fw}x{fh}!)")
        else:
            lines.append("Scale: none; " + ("already the Frame's size" if fits else
                         "its aspect ratio doesn't match the Frame's, so it is kept "
                         "unscaled and doesn't count"))
            if src == raw:
                raw.rename(image)
            else:
                shutil.copyfile(src, image)
        if repair:
            lines.append(f"Repair: {repair}")
    return lines, failures, fits


def merge_masked(out: Path, start: Path, mask: Path, frame: dict,
                 checked: bool) -> tuple[list[str], list[str], bool]:
    """SR-6.5: turn out/raw.png, a masked Layer generation's paid output, into
    out/image.png: the starting version with new colour inside the mask, keeping its
    alpha everywhere and every pixel outside the mask. The API saw the starting
    version premultiplied onto black, so the new colour is the paid colour divided by
    the starting alpha where that is above 0, clamped to 1; in a feathered edge it is
    mixed with the starting colour by the mask's value. Returns what
    make_layer_version returns."""
    raw, image = out / "raw.png", out / "image.png"
    (rw, rh), (sw, sh) = identify(raw), identify(start)
    if not scene_state.ratio_matches((rw, rh), {"width": sw, "height": sh}):
        lines, failures, fits = make_layer_version(out, frame, checked, False)
        return lines + ["Repair: none; the paid output's aspect ratio doesn't match the "
                        "starting version's, so it wasn't merged"], failures, fits
    lines, failures = [f"Raw size: {rw}x{rh}"], []
    with tempfile.TemporaryDirectory(prefix="gen-merge-") as tmp:
        paid, merged = raw, Path(tmp) / "merged.png"
        if (rw, rh) != (sw, sh):
            paid = Path(tmp) / "paid.png"
            magick(raw, "-resize", f"{sw}x{sh}!", paid)
            lines.append(f"Scale: x {sw / rw:.4f}, y {sh / rh:.4f} (-resize {sw}x{sh}!), "
                         "the paid output to the starting version's size")
        else:
            lines.append("Scale: none; already the starting version's size")
        # -fx reads a missing alpha channel wrongly, so every input gets one first; a
        # grey start would leave -fx one colour channel, so it is read as sRGB
        magick("(", start, "-colorspace", "sRGB", ")", "(", paid, "-alpha", "off", ")",
               "(", mask, "-alpha", "off", "-colorspace", "Gray", ")", "-alpha", "set",
               "-channel", "RGB", "-fx", "wm=u[2].r; u.a>0 ? (1-wm)*u+wm*min(1,v/u.a) : u",
               "+channel", "-define", "png:color-type=6", merged)
        if checked:
            failures = separation_checks(merged, False)
            lines.append(f"Checks: round 1, merged Layer Version: {' '.join(failures) or 'pass'}")
        else:
            lines.append("Checks: not run; the bottom Layer's prompt lacks the "
                         "transparent-background block")
        shutil.copyfile(merged, image)
    lines.append(f"Repair: masked repaint (path 4) merged as colour only: inside the mask, "
                 f"the paid colour divided by the starting version's alpha where above 0, "
                 "clamped to 1, mixed with the starting colour by the mask's value; the "
                 f"starting version's alpha kept everywhere, and every pixel outside the "
                 f"mask; paid output kept as raw.png")
    return lines, failures, scene_state.ratio_matches((sw, sh), frame)


def flatten_onto_black(src: Path, dest: Path) -> None:
    """SR-4.5: the model ignores alpha and sees whatever colour lies under it."""
    magick(src, "-background", "black", "-alpha", "remove", "-alpha", "off", dest)


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


def finish(raw: Path, final_size: str, flatten: str, max_mb: float,
           dry_run: bool = False) -> tuple[Path, str]:
    """Deliverable derived from the raw output: exact px, flattened, sRGB, no alpha.

    Scales to FIT inside the target and pads onto the flatten color, so a raw
    output whose aspect differs from the target is never stretched or cropped —
    no hull is ever cut off to satisfy the box. With dry_run, writes nothing and
    returns the path and note it would have; the note then has no size in MB.
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
    if not dry_run:
        subprocess.run(cmd, check=True, capture_output=True)
    mb = 0.0 if dry_run else dest.stat().st_size / 1_000_000
    note = (f"{dest.name}, {final_size}, sRGB 8-bit PNG-24 no alpha, "
            f"flattened onto {flatten}"
            + ("" if dry_run else f", {mb:.2f} MB")
            + f"; scaled to fit from raw {rw}x{rh}")
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
                  raw_size: str = "", layered: list[str] | None = None,
                  md5s: dict | None = None, output: str | None = None):
    """layered: a Layer Version's or Draft's labelled lines (SRD SR-17.2), whose free
    text, and the request and mode, are written with whitespace collapsed; md5s: each
    same-scene attachment's md5, ending its Inputs line; output: the Output line."""
    label = (args.asset or args.scene).split("/")[-1]
    free = norm if layered is not None else (lambda text: text)
    lines = [
        f"# {label} {out.name}" if not args.layer else f"# {label} {args.layer} {out.name}",
        "",
        f"User request verbatim: {free(args.request or 'TODO — fill in')}",
        f"Mode: {free(args.mode or 'TODO — fill in')}",
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
        *(layered or []),
        "Inputs:",
    ]
    for i, (path, role) in enumerate(attachments, start=1):
        rel = rel_of(path)
        frozen = frozen_equivalent(path)
        suffix = f"; frozen {frozen}" if frozen not in ("n/a", "already frozen") else ""
        if path in (md5s or {}):
            suffix += f" md5={md5s[path]}"
        lines.append(f"- Image {i} {role}: {rel}{suffix}")
    if usage:
        lines.append(f"Token usage: {json.dumps(usage, sort_keys=True)}")
    lines += [
        f"Date: {date.today().isoformat()}",
        "Status: awaiting user evaluation",
        output or f"Output: image.png, {raw_size or args.size} (raw model output, frozen)",
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
    p.add_argument("--layer", metavar="LAYER-ID",
                   help="a Layered Scene: generate a version of this Layer into the next "
                        "OUT/<scene>/layers/<layer-id>/vNNN/, at the Frame")
    p.add_argument("--draft", action="store_true",
                   help="a Layered Scene: generate a Draft (a whole-scene reference for "
                        "placement, scale and light) into the next OUT/<scene>/drafts/vNNN/")
    p.add_argument("--emissive", action="store_true",
                   help="with --layer: the Layer's content is light only (glow, flames, "
                        "glowing haze), so glow baked onto dark is unmultiplied")
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
                   help="validate invariants and exit without calling the API "
                        "(with --refinish: without writing anything)")
    args = p.parse_args()
    check_no_stale_bytecode()
    set_locations(args.package, args.output)
    layered = bool(args.layer or args.draft)
    if args.layer and args.draft:
        raise Fail("pass --layer or --draft, not both")
    if (layered or args.emissive) and (args.asset or args.refinish):
        raise Fail("--layer, --draft and --emissive belong to a Layered Scene's "
                   "generation (--scene); they have no meaning with --asset or --refinish")
    if args.emissive and not args.layer:
        raise Fail("--emissive marks a Layer generation whose content is light only; "
                   "it needs --layer")
    if args.emissive and args.mask:
        raise Fail("--emissive has no meaning on a masked Layer generation (path 4): it keeps "
                   "the starting version's alpha and repaints colour only, so nothing is "
                   "unmultiplied.")
    size_given = args.size

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
        if layer_or_draft(raw.parent):
            raise Fail(f"{args.refinish} is a Layered Scene's Layer Version or Draft; only "
                       "a Combined Image gets deliverables (layers.py combine).")
        require_binary("magick", "install ImageMagick (brew install imagemagick)")
        dest, note = finish(raw, args.final_size, args.flatten, args.max_mb, args.dry_run)
        if args.dry_run:
            verb = "would write" if dest != raw else "deliverable would be"
            print(f"  {verb} {dest}\n  {note}")
            print(f"  would update {receipt} Delivered line to: {note}")
            print("  dry run: invariants OK, nothing written")
            return 0
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
    plan = check_layer_plan(base, args.layer, args.draft) if args.scene else None
    scene_dir = base
    if layered:
        # A Layer or Draft is made at the scene's Frame; only Combined Images get
        # deliverables, so the delivery options belong to layers.py combine.
        frame = scene_state.frame_text(plan["frame"])
        if args.preset or args.final_size:
            raise Fail("--preset and --final-size derive deliverables, which only a "
                       "Combined Image gets (layers.py combine takes them). A Layer or "
                       f"Draft is generated at the Frame, {frame}: drop them.")
        if size_given:
            m = re.fullmatch(r"(\d+)x(\d+)", size_given.strip().lower())
            if not m or not int(m.group(2)) or not scene_state.ratio_matches(
                    (int(m.group(1)), int(m.group(2))), plan["frame"]):
                raise Fail(f"--size {size_given} doesn't match the Frame's aspect ratio "
                           f"({frame}). A Layer or Draft is generated at the Frame: drop "
                           "--size.")
        else:
            args.size = frame
        base = writable_base(scene_dir / "layers" / args.layer if args.layer
                             else scene_dir / "drafts")
        deleted = deleted_numbers(base)
    require_binary("magick", "install ImageMagick (brew install imagemagick)")
    if args.backend == "codex":
        require_binary("codex", "install the Codex CLI, or use --backend api")
    attachments = [parse_attach(s) for s in args.attach]
    check_inputs(attachments, masked=bool(args.mask and args.backend == "api"))
    if not args.layer and any(role == "PLACEMENT" for _, role in attachments):
        raise Fail("PLACEMENT is a role for a Layer generation (--layer) only: the same "
                   "scene's image, used for placement, scale and light.")
    md5s, start = (check_layer_inputs(attachments, scene_dir, plan, args.layer)
                   if layered else ({}, None))
    masked_layer = bool(args.layer and args.mask and args.backend == "api")
    target = masked_layer and attachments and scene_state.classify(scene_dir, attachments[0][0])
    if masked_layer and not (target and target["kind"] == "layer"
                             and target["layer"] == args.layer):
        raise Fail(f"a masked Layer generation (path 4) repaints its starting version itself: "
                   f"attach a version of Layer {args.layer} (layers/{args.layer}/vNNN/image.png) "
                   "as image 1, EDIT TARGET, not a Combined Image or adjusted copy.")
    check_style_frozen()
    warnings = check_prompt(prompt, masked=bool(args.mask and args.backend == "api"))
    if args.layer and start is not None and \
            (w := check_starting_version(scene_dir, plan, args.layer, start)):
        warnings.append(w)
    checked = norm(TRANSPARENT_LEAD) in norm(prompt)
    bottom = layered and args.layer == plan["layers"][0]["id"]
    if masked_layer:
        # checked on its merged Layer Version, which keeps the starting version's
        # alpha, so it needs no block; a bottom Layer filling the Frame isn't checked
        checked = checked or not bottom
    elif args.layer and not checked and not bottom:
        warnings.append(f"the prompt lacks the transparent-background block (prompt.py "
                        f"--opaque/--soft), and {args.layer} isn't the scene's bottom "
                        "Layer: it may come back opaque and hide every Layer beneath it, "
                        "and the separation checks won't run.")
    for path, _ in attachments:
        frozen_equivalent(path)  # raises on any provenance failure
    for w in warnings:
        print(f"  warn: {w}", file=sys.stderr)
    to_flatten = [i for i, (path, _) in enumerate(attachments)
                  if args.layer and has_alpha(path)]

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
        print(f"  image {i} {role:11} {rel_of(path)}"
              + ("  (has alpha: sent flattened onto black)" if i - 1 in to_flatten else ""))
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

    # A Layer generation sends each attachment with alpha as a temporary copy
    # flattened onto black; the receipt names the frozen original.
    sent = list(attachments)
    flat_dir = Path(tempfile.mkdtemp(prefix="gen-flat-")) if to_flatten else None
    try:
        for i in to_flatten:
            path, role = attachments[i]
            sent[i] = (flat_dir / f"image{i + 1}-{path.name}", role)
            flatten_onto_black(path, sent[i][0])
        if args.backend == "codex":
            blob, provenance = generate_codex(prompt, sent, model, args.size)
            usage = None
        else:
            data = generate(prompt, sent, model, args.size, args.quality,
                            api_key_for_call, api_mask)
            payload = data["data"][0]
            if "b64_json" not in payload:
                raise Fail(f"no image in response: {json.dumps(data)[:400]}")
            import base64

            blob = base64.b64decode(payload["b64_json"])
            usage, provenance = data.get("usage"), "OpenAI Images API, exact prompt bytes sent"
    finally:
        if flat_dir is not None:
            shutil.rmtree(flat_dir, ignore_errors=True)

    if api_mask is not None:
        api_mask.unlink(missing_ok=True)   # converted copy; the user mask is the record

    try:
        out = target_dir(base, deleted)
        raw = out / ("raw.png" if args.layer else "image.png")
        raw.write_bytes(blob)
    except OSError as e:
        # Pre-flight passed but the target broke while the backend ran. The image is
        # paid for: keep it in the system temp dir rather than lose it.
        fd, kept = tempfile.mkstemp(prefix="gen-unsaved-", suffix=".png")
        with os.fdopen(fd, "wb") as f:
            f.write(blob)
        raise Fail(f"could not save the generated image under {base} "
                   f"({e.strerror or e}). It was saved to {kept} instead; no receipt "
                   "was written. Fix the target before the next run.") from None
    if not args.layer:
        print(f"  wrote {raw}")

    delivered = None
    if args.final_size:
        dest, delivered = finish(raw, args.final_size, args.flatten, args.max_mb)
        verb = "wrote" if dest != raw else "deliverable ="
        print(f"  {verb} {dest}  ({delivered})")

    rw, rh = identify(raw)
    head, output = (layer_receipt(out, args, plan, checked, start, to_flatten, attachments,
                                  warnings, resolve(args.mask) if masked_layer else None)
                    if layered else (None, None))
    write_receipt(out, args, prompt, attachments, model, usage, warnings,
                  delivered, provenance, f"{rw}x{rh}", head, md5s, output)
    print(f"  wrote {out / 'generation.md'}")
    return 0


def layer_receipt(out: Path, args, plan: dict, checked: bool, start: Path | None,
                  flattened: list[int], attachments, warnings: list[str],
                  mask: Path | None = None):
    """Finish a Layer Version or Draft in out/ and return its receipt lines (SRD
    SR-3.8, SR-17.2) and Output line. Prints what the Caller must tell the User."""
    frame = scene_state.frame_text(plan["frame"])
    head = [f"Kind: {'Layer Version' if args.layer else 'Draft'}"]
    if args.layer:
        entry = next(l["entry"] for l in plan["layers"] if l["id"] == args.layer)
        head += [f"Layer: {args.layer}", f"Layer Entry: {norm(entry)}"]
    head += [f"Layer Plan: journal/{plan['number']:03d}.json", f"Frame: {frame}"]
    image = out / "image.png"
    if not args.layer:
        rw, rh = identify(image)
        if not scene_state.ratio_matches((rw, rh), plan["frame"]):
            warnings.append(f"this Draft is {rw}x{rh}, which doesn't match the Frame's "
                            f"aspect ratio ({frame}); it is kept like any attempt. Tell "
                            "the User.")
            print(f"  NOTE: {warnings[-1]}")
        head.append(f"md5: {md5(image)}")
        return head, None

    got, failures, fits = (merge_masked(out, start / "image.png", mask, plan["frame"], checked)
                           if mask is not None else
                           make_layer_version(out, plan["frame"], checked, args.emissive))
    pick = lambda label: [l for l in got if l.startswith(f"{label}:")]
    head += pick("Raw size") + pick("Scale") + [
        "Starting version: " + (rel_of(start) if start else "none; generated fresh"),
        "Flattened: " + ("; ".join(f"image {i + 1} {rel_of(attachments[i][0])}"
                                   for i in flattened)
                         + " onto black (#000000); the originals are unchanged"
                         if flattened else "none; no attachment has an alpha channel"),
    ] + pick("Checks") + pick("Repair") + [f"md5: {md5(image)}"]
    w, h = identify(image)
    kept = (out / "raw.png").exists()
    print(f"  wrote {image}  (the Layer Version" + ("; the raw output stays as raw.png)"
                                                     if kept else ")"))
    if not fits:
        warnings.append(f"the raw output, {w}x{h}, doesn't match the Frame's aspect ratio "
                        f"({frame}): it is kept unscaled, so this Layer Version doesn't "
                        "count. Tell the User and show it to them on its own.")
        print(f"  NOTE: {warnings[-1]}")
    for f in failures:
        print(f"  separation check failed: {f}", file=sys.stderr)
    if failures:
        print("  The Layer Version fails the separation checks above: regenerate it, "
              "restating the transparent-background block.", file=sys.stderr)
    return head, (f"Output: image.png, {w}x{h} (the Layer Version, frozen)"
                  + ("; raw.png (the raw output, frozen)" if kept else ""))


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Fail as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
