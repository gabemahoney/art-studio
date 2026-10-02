# Rogue Frontier — Visual Style Guide

**Style version: v2** (2026-09-11)

This file defines what Rogue Frontier art LOOKS like — nothing else. How
generations run (input roles, prompt assembly, the One Rule) lives in `rules.md`,
including the versioning procedure for this file.

## Style anchor

`ref_images/style_references/canonical_style_reference.png` — the user-selected
authoritative rendering for all Rogue Frontier art. Copy its **rendering only**.
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

("Image 1" = the style anchor, which `rules.md` requires to be the FIRST image
attached to every call.)

## Archived references

`ref_images/archive/` holds retired Elmore-era paintings (smooth realistic
rendering that conflicts with the Style Block). Never attach them as style inputs.
They may be reintroduced only if the user explicitly hands one in, and then only
as a composition or design reference — the anchor still governs rendering.

## Changelog

- **v1** (2026-09-11) — Initial versioned guide: canonical_style_reference.png as sole style
  anchor, Style Block codified, STYLE/IDENTITY roles defined, Elmore-era secondary
  references retired to `ref_images/archive/`.
- **v2** (2026-09-11) — Style Block strengthened after v1 text failed to override the
  model's detail prior (graxo v014): countable hard limits (5–8 planes per face, ≤3
  values per surface), angular plane-edge geometry (chiseled polygonal shapes,
  straight shadow seams), "paint LESS" directive, closing style line added. Anchor
  image unchanged from v1. Generation procedure split out of this file into `rules.md`.
