# getting-sky v016

User request verbatim: the ship should be moving along the lines of the valley. it looks like it about to fly into a wall.
Mode: Layer 2 again: Antares flying along the gorge toward the viewer, nose forward. Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a1087b-5966-75d3-b8b4-14dadb55c4b3/exec-9686ede3-a2e7-40af-8a66-81f692a841b5.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: assets/locations/kalagra-storm-gorge/reference.png; frozen assets/locations/kalagra-storm-gorge/candidates/v001/image.png
- Image 3 IDENTITY: assets/ships/the_antares/sources/hero-crop-from-reference.png
Date: 2026-10-04
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.37 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: REJECTED by user: three engines, still oblique to the canyon, too big.

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

Reproduce image 2, the gorge, exactly as it is, and add the Antares (image 3).

She flies ALONG the gorge, following its floor: coming out of the distant bend at
upper left and racing straight toward us down the middle of the valley, her nose
pointing at the viewer and slightly to the lower right, her tail and engine exhaust
trailing back up the gorge toward the bend. The cliff walls run parallel to her on
both sides; open air all around her.
- In the lower-right part of the picture, about one fifth of the picture's width,
  high above the gorge floor, banked a little.
- Seen from in front: her cockpit nose and windscreen nearest us, both engine pods
  behind it at her rear, their fan intakes facing forward, flame trailing from their
  backs.
Nothing else is added.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
