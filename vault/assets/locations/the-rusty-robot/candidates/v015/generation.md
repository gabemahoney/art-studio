# the-rusty-robot v015

User request verbatim: Except...the right side of the bottom of the marquee looks weird. Its not a straight line nere the right columns
Mode: Edit off v014: straighten the canopy underside's back edge past the right fin in the three-quarter view. Only that region will be kept; composite onto v014 follows.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10378-4a23-74c2-89f7-fe365a0f9f0c/exec-94ed5f3d-1f9a-41fa-8826-1136cb414b70.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: assets/locations/the-rusty-robot/candidates/v014/image.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.96 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Canopy underside's right end fixed: back edge runs straight past the right fin, fin cut off cleanly by it, bottom corner a single point. Rest of frame lightly repainted; only the canopy's right end is used, in v016.

## Exact prompt

Hand-painted flat angular matte gouache illustration in the manner of late-1970s
TSR tabletop-RPG interior art (Star Frontiers, early Dungeons & Dragons) — poster
paint, not digital illustration. Build every form from a few large flat opaque
color planes with hard edges. Plane edges are straight or crisply angled —
chiseled, polygonal shapes, never soft rounded blobs; shadow meets light in a
straight angular seam. HARD LIMITS: a face is five to eight flat planes
total; any surface gets at most three value steps; shadow is one darker flat
plane, never a gradient or blend. Hair is one or two chunky painted masses —
silhouette only, zero strands. Fabric folds are a few straight angular strokes.
Equipment, trim, patterns and fasteners are simplified blocks of color — details
suggested, never drawn. Muted palette: slate blue-gray, warm ochre, ivory,
brick-red accents. Coarse dry-brush edges and broken pigment on large areas;
large areas stay quiet and under-detailed. When in doubt, paint LESS: fewer
shapes, fewer details, flatter.

Forbidden: smooth gradients, airbrush or glossy digital shading, photographic
detail or realistic skin, fine linework or fine hair strands, surface
subdivisions or micro-detail, more than three values on any surface, neon or rim
lighting, uniform granular noise, dense tiny facets or polygon mosaics, and the
polished modern AI character-sheet look.

Image 1 is STYLE: Match its hand-painted matte rendering only. Ignore its subjects.
Image 2 is EDIT TARGET: The reference sheet being revised. Preserve everything the spec does not change.

TASK: Revise this architectural reference sheet of the Rusty Robot cantina.

Reproduce image 2, the reference sheet, and change ONE thing: the right-hand end of
the canopy's underside in the large THREE-QUARTER VIEW. Everything else stays exactly
as it is.

The canopy's underside is one flat rectangular plane. Its two long edges are STRAIGHT
lines running the full width of the building, parallel to each other:

- The FRONT edge, where the underside meets the bottom of the tilted sign face, is one
  straight line from the canopy's left end to its right end.
- The BACK edge, where the underside meets the building's front wall, is one straight
  line from the left end to the right end, parallel to the front edge.

At the right-hand end, beside the right fin, the back edge currently bends and steps
down around the top of the fin. Instead, the back edge continues straight past the
fin: the fin simply stops at the underside, its top cut off by that straight line.
The right end of the canopy is the same trapezoid as the left end, its bottom corner
a single clean point.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
