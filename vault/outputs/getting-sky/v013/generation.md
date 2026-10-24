# getting-sky v013

User request verbatim: Its too bug an looks like it crashinginto the ground
Mode: Layer 2 again on the approved gorge: Antares ~1/5 frame width, high in open air, lower right. Roll 1 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10877-bff4-7751-b3de-66ae7ffdd103/exec-324ab8e4-d253-4232-803a-c7f23c636fc1.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: assets/locations/kalagra-storm-gorge/reference.png; frozen assets/locations/kalagra-storm-gorge/candidates/v001/image.png
- Image 3 IDENTITY: assets/ships/the_antares/sources/hero-crop-from-reference.png
Date: 2026-10-04
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.35 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: REJECTED by user: heading across the gorge, looks about to fly into the wall; must fly along the valley's line.

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

Reproduce image 2, the gorge, exactly as it is, and add the Antares (image 3) flying
fast down the gorge in the lower-right part of the picture.
- She is SMALL against the cliffs: about one fifth of the picture's width.
- She flies HIGH in open air, level, well above the gorge floor — clear sand-filled
  air between her and the rocks below. Banked a little into the turn.
- Her design exactly as image 3: cockpit nose leading, both engine pods at her rear,
  their round rear faces glowing with exhaust.
Nothing else is added.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
