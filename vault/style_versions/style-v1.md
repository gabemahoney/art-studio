# Rogue Frontier — Visual Style Guide

**Style version: v1** (2026-09-11)

This file is the single source of truth for how every Rogue Frontier image is rendered.
Read it before ANY image generation, and follow **The One Rule** below without exception.

Versioning: this file is always the mutable head revision — the current version,
edited in place. Before any change to the Style
Block, the style anchor image, or the input-role rules: (1) confirm the current
version is snapshotted as `style_versions/style-v<N>.md` (copy it there if not),
(2) make the change here, bump the version number above, and add a changelog line,
(3) snapshot the new version to `style_versions/` as well. `style_versions/` is
read-only history — never edit or attach files from it. Every `generation.md`
records the style version it ran under ("Style: v1") and embeds the exact prompt
text, so any past image can be traced and replicated even as this file evolves.

## The One Rule (prevents style drift)

Every image-generation call — new artwork, revisions, and *especially* tiny edits like
"add a mustache" — must do BOTH of these:

1. **Attach the style anchor image** `ref_images/style_references/canonical_style_reference.png`
   as a style-only input, labeled as such in the prompt.
2. **Include the full Style Block below, verbatim**, in the prompt text.

Style is never inherited from a previous output. Edit operations silently pull the
rendering back toward generic digital illustration; re-asserting the style anchor and
Style Block on every call is what keeps it locked. If a call skips either one, the
result is invalid — regenerate.

## Style anchor

`ref_images/style_references/canonical_style_reference.png` — the user-selected authoritative
rendering for all Rogue Frontier art. Copy its **rendering only**. Never copy its
subjects: not the gold waistcoat, not the clean-shaven faces, not the cockpit layout.

The anchor is versioned with the style: the copy in force under style vN is frozen
as `style_versions/canonical_style_reference-vN.png`. Replacing the anchor image is a style
change — bump the style version and snapshot both the new `style.md` and the new
anchor. Generations always attach the mutable head revision
`canonical_style_reference.png`; the snapshot exists so past calls can be replayed
with the anchor they actually used.

## Style Block (paste verbatim into every prompt)

> Flat angular matte gouache illustration in the style of late-1970s/1980s tabletop
> RPG art (Star Frontiers, early Dungeons & Dragons paperbacks). Broad opaque
> interlocking color planes with hard edges and limited value steps. Warm ochre and
> umber facial planes with dark slate shadow masses; faces built from a few large
> angular shapes. Chunky simplified hair masses with no individual strands. Muted
> palette of slate blue-gray, warm ochre, ivory, and brick-red accents. Coarse
> dry-brush texture and broken pigment on large surfaces; large quiet color masses;
> simplified fabric folds and equipment surfaces.
>
> Do NOT render as: smooth gradients, airbrush or glossy digital shading,
> photographic detail or realistic skin, fine linework or fine hair strands, neon or
> rim lighting, uniform granular noise, dense tiny facets or polygon mosaics, or
> generic modern AI character-illustration style.

## Image input roles

Label every attached image with exactly one role in the prompt:

- **STYLE** — `canonical_style_reference.png`. "Match this image's rendering technique only.
  Ignore its people, clothing, equipment, and setting."
- **IDENTITY** — the asset's approved `assets/<type>/<slug>/reference.png`
  (or `sources/` originals for a new asset). "Copy this asset's design: face,
  build, clothing, equipment, colors. Ignore this image's rendering."

Rules:

- Attach one STYLE image + one IDENTITY image per asset in the shot. Never attach
  a whole folder.
- IDENTITY inputs are always **approved** `reference.png` files — never an
  unapproved candidate, never a previous revision attempt. Chaining candidate
  outputs compounds drift.
- Ignore borders, captions, signatures, and screenshot chrome in any reference.

## Archived references

`ref_images/archive/` holds retired Elmore-era paintings (smooth realistic rendering
that conflicts with the Style Block). Never attach them as style inputs. They may be
reintroduced only if the user explicitly hands one in, and then only as a
composition or design reference — the anchor still governs rendering. Ship scenes
need no extra style reference: rendering comes from the anchor, ship design from the
ship's own `reference.png`.

## Changelog

- **v1** (2026-09-11) — Initial versioned guide: canonical_style_reference.png as sole style
  anchor, Style Block codified, STYLE/IDENTITY roles defined, Elmore-era secondary
  references retired to `ref_images/archive/`.
