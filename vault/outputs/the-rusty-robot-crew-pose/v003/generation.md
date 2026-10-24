# the-rusty-robot-crew-pose v003

User request verbatim: Can you try one where she is doing the pointing pose again? Like in v5?
Mode: Edit off crew-pose v002: Sion pointing as in scene v005. Roll 1 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10cf6-9072-72b3-9db8-600fa8397e0a/exec-4123bfaf-408e-4c48-a1df-11efc9321a0c.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot-crew-pose/v002/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
- Image 4 IDENTITY: outputs/the-rusty-robot/crew-pose-from-v005b.png
Date: 2026-10-05
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.74 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Sion pointing as in v005; faces checked at 200% (Graxo mustache/temples, Daxus glasses, Sion goggles). Used.

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
Image 4 is IDENTITY: An earlier painting. Copy only Sion's pointing pose from it.

TASK: Change one character's pose on this sheet.

Reproduce image 2 exactly — the same three people, the same faces, clothing, sizes and
positions, the plain grey background. Change only SION's pose (the woman at the right
with the ruby goggles and steel arm), to match her pose in image 4: she holds her
natural right hand up in front of her chest, index finger extended, pointing toward
Daxus and Graxo as she makes her point; her steel left arm hangs relaxed at her side.
She still faces the two men. Daxus and Graxo do not change at all.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
