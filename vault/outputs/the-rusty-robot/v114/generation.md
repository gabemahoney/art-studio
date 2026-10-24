# the-rusty-robot v114

User request verbatim: Can you try one where she is doing the pointing pose again? Like in v5?
Mode: Blend off v113, lineup attached; only alley+crew region kept. Roll 1 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10cfd-10ca-70e3-9aee-55d09990c8fb/exec-0f174129-79a2-4bc6-a6a7-408737fb2754.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v113/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-10-05
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.01 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Blend off v113, lineup attached: crew shadowed, Sion pointing; faces held at 150%. Only alley+crew region used (v116).

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
Image 2 is EDIT TARGET: This is the image being modified. Preserve everything the prompt does not change.
Image 3 is IDENTITY: The approved crew lineup. Keep every face matching it exactly.

TASK: Blend the crew into the alley's shadow.

Reproduce image 2 exactly. Do not change the three people's faces, poses, sizes,
positions or clothing, or anything outside the alley. Only blend them into the dark
alley: they stand in its shadow — dim and muted, nearly the tone of the alley wall
behind them — with warm light from the cantina entrance on the right catching only
the sides of their faces and bodies turned toward it, and soft shadows at their feet.
Their faces stay exactly as they are and match image 3.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
