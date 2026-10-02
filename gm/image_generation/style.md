# Rogue Frontier — Visual Style Guide

**Style version: v3** (2026-10-01)

This file defines what Rogue Frontier art LOOKS like — nothing else. How
generations run (input roles, prompt assembly, the One Rule) lives in `rules.md`,
including the versioning procedure for this file.

## Style anchor

`ref_images/style_references/canonical_style_reference.png` — the user-selected
authoritative rendering for all Rogue Frontier art — in the images tree, not the repo
(`rules.md` → *Where images live*). Copy its **rendering only**.
Never copy its subjects: not the gold waistcoat, not the clean-shaven faces, not
the cockpit layout.

## Style Block (paste verbatim into every prompt)

> Hand-painted flat angular matte gouache illustration in the manner of late-1970s
> TSR tabletop-RPG interior art (Star Frontiers, early Dungeons & Dragons) — poster
> paint, not digital illustration. Build every form from a few large flat opaque
> color planes with hard edges. Plane edges are straight or crisply angled —
> chiseled, polygonal shapes, never soft rounded blobs; shadow meets light in a
> straight angular seam. HARD LIMITS: a face is five to eight flat planes
> total; any surface gets at most three value steps; shadow is one darker flat
> plane, never a gradient or blend. Hair is one or two chunky painted masses —
> silhouette only, zero strands. Fabric folds are a few straight angular strokes.
> Equipment, trim, patterns and fasteners are simplified blocks of color — details
> suggested, never drawn. Muted palette: slate blue-gray, warm ochre, ivory,
> brick-red accents. Coarse dry-brush edges and broken pigment on large areas;
> large areas stay quiet and under-detailed. When in doubt, paint LESS: fewer
> shapes, fewer details, flatter.
>
> Forbidden: smooth gradients, airbrush or glossy digital shading, photographic
> detail or realistic skin, fine linework or fine hair strands, surface
> subdivisions or micro-detail, more than three values on any surface, neon or rim
> lighting, uniform granular noise, dense tiny facets or polygon mosaics, and the
> polished modern AI character-sheet look.

## Closing style line (last line of every prompt)

> Render everything in the exact brush scale of image 1, the style anchor: fewest
> possible flat shapes, no blending, no micro-detail.

("Image 1" = the style anchor, which `rules.md` requires to be the first image
attached — on every call except a masked API call, which is the sole exception and
uses the line below instead.)

## Closing style line for masked calls

A masked API call is the one case where the anchor is not image 1 (`rules.md` →
*Masked inpainting* for why), so an index would point at the image being repainted.
Those calls end with this line instead, which names the anchor by role:

> Render everything in the exact brush scale of the style anchor attached to this
> call: fewest possible flat shapes, no blending, no micro-detail.

## Note on the Forbidden list

**Every item on the Forbidden line names a rendering tell, not a subject** — including
"neon or rim lighting". It forbids the *look*: saturated glow, bloom, halo, soft falloff,
the lit-from-within sheen of modern digital art. It does **not** forbid lit signage,
lamps, glowing instruments or electric light as subject matter. The world can have neon
in it; the painting must not be rendered like neon.

So a lit sign is fine painted the way this style paints everything else: flat opaque
shapes with hard edges, a bright core and at most one darker band of the same hue, no
glow, no gradient, no rays. Recorded 2026-09-30 after the sign in
`outputs/the-rusty-robot/`, where reading the ban as a subject prohibition would have
blocked a legitimate art direction.

This note sits BELOW both closing-line sections deliberately — `style_block()` ships
anything between `## Style Block` and `## Closing style line` to the model, and `gen.py`
now fails closed on it. See the Changelog.

## Archived references

`ref_images/archive/` holds retired Elmore-era paintings (smooth realistic
rendering that conflicts with the Style Block). Never attach them as style inputs.
They may be reintroduced only if the user explicitly hands one in, and then only
as a composition or design reference — the anchor still governs rendering.

## Changelog

- **v3** (2026-10-01) — Adds the **closing style line for masked calls**, needed because a
  masked API call puts the EDIT TARGET in image 1, so "image 1, the style anchor" would
  point at the wrong image. **The Style Block is byte-identical to v2** and the anchor
  image is unchanged; this bump exists because One Rule #3 makes the closing line part of
  the prompt contract, and v2 was frozen without this line — a masked receipt stamped
  `Style: v2` would cite a line absent from frozen v2 and be unreproducible.

- **v2** (2026-09-11) — Style Block strengthened after v1 text failed to override the
  model's detail prior (graxo v014): countable hard limits (5–8 planes per face, ≤3
  values per surface), angular plane-edge geometry (chiseled polygonal shapes,
  straight shadow seams), "paint LESS" directive, closing style line added. Anchor
  image unchanged from v1. Generation procedure split out of this file into `rules.md`.

- **v1** (2026-09-11) — Initial versioned guide: canonical_style_reference.png as sole style
  anchor, Style Block codified, STYLE/IDENTITY roles defined, Elmore-era secondary
  references retired to `ref_images/archive/`.

### Incident, not a version

- **v2 over-delivery, 2026-09-30 to 2026-10-01.** The "Note on the Forbidden list" sat
  between `## Style Block` and `## Closing style line`, which is exactly what
  `style_block()` extracts — so 39 prompts shipped a **402-word** Block where v2 declares
  **214**, the extra 188 words being the Note, its own markdown heading, and a sentence
  claiming the note sat *outside* the Block while being shipped inside it. **Those 39
  receipts are the record of the figure, not this file**, which has changed since; 165 receipts
  carry a `Style: v2` stamp as of 2026-10-01, and 7 more mention it in prose. No version was bumped because their Block is a
  superset of v2, not a different style. The Note now sits below both closing-line
  sections and `gen.py` fails closed if the extract contains a heading.
