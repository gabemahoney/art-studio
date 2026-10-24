# getting-sky v011

User request verbatim: Canyon looks good. Now render Antares zooming down it (bottom right corner)
Mode: Layer 2 on the approved gorge (v001): Antares only, bottom right. Roll 1 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a104ee-e808-7e33-8803-78a3f7b96d79/exec-7a500653-e2ea-4364-b6e0-3dfa60ba4883.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: assets/locations/kalagra-storm-gorge/reference.png; frozen assets/locations/kalagra-storm-gorge/candidates/v001/image.png
- Image 3 IDENTITY: assets/ships/the_antares/sources/hero-crop-from-reference.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.36 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: REJECTED by user: Antares too big and looks like it's crashing into the ground.  CORRECTION: my geometry call on v011/v012 was backwards — the reference front view shows the fans head-on, so fans are the INTAKE (front) faces; v011 was right, v012 wrong.

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

Image 1 is STYLE: Match this image's rendering technique only. Ignore its people, clothing, equipment, and setting.
Image 2 is EDIT TARGET: The approved gorge. Reproduce it exactly and add only the Antares.
Image 3 is IDENTITY: The Antares. Copy its design exactly.

TASK: Add the Antares to this storm gorge.

Reproduce image 2, the gorge, exactly as it is, and add the Antares (image 3) zooming
down it in the bottom-right corner of the picture: close to us, flying fast toward the
lower right out of the gorge, banked steeply into the turn, engines flaring behind
her. Her design exactly as image 3 — cockpit nose leading, both engine pods at her
rear. Lit cold by the lightning, with warm glow only from her engines.
Nothing else is added.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
