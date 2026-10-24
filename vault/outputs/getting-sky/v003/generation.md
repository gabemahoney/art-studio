# getting-sky v003

User request verbatim: Just try a whole new prompt
Mode: Fresh, new concept: dark night storm gorge, ships small mid-distance coming toward camera; no ride-out sky reference. Roll 1 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a104df-fb30-7ca0-ab9d-29c6c12ca4ab/exec-e38757d5-5ae5-4650-9a42-29da378bc28e.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/ships/the_antares/sources/hero-crop-from-reference.png
- Image 3 IDENTITY: assets/ships/hegemony-assault-ship/sources/hero-crop-from-reference.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.50 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: New concept: dark storm gorge, lightning, sand curtains, slate palette; Antares banking mid-frame, two assault ships behind firing red bolts. Ships larger than asked; Antares flies across the gorge rather than toward the camera.

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
Image 2 is IDENTITY: The Antares. Copy its design exactly.
Image 3 is IDENTITY: The Hegemony assault ship. Copy its design exactly.

TASK: A single scene illustration: the Antares fleeing two Hegemony assault ships through a storm gorge at night.

ONE single continuous scene illustration, a 3:2 horizontal rectangle. No panels,
borders or text.

Night, in the heart of a planet-wide storm. A narrow, twisting gorge between towering
black cliffs, seen from low down inside it. Wind-driven sand fills the air in grey
curtains; a jagged fork of lightning splits the strip of sky above, throwing the cliff
faces into cold blue-white light. The palette is dark slate, storm blue and black,
with warm light only from engines and laser fire.

The Antares (image 2) comes toward us down the gorge, mid-distance, tilted in a hard
bank around a bend, engines flaring. Close behind and above her, two Hegemony assault
ships (image 3) swing round the same bend in pursuit, red laser bolts from their chin
guns slashing past her. The ships are small against the vast cliffs: the gorge and the
storm dominate the picture.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
