# the-rusty-robot-crew-pose v002

User request verbatim: Ok. Now try this with the characters at the cantina
Mode: Layered rebuild step B: crew alone on grey, lineup likeness, v091 pose. Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10cea-f26b-7e22-8457-6d13a919d82f/exec-6610fb4a-8345-4021-9603-33ab08c6161d.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
- Image 3 IDENTITY: outputs/the-rusty-robot/crew-pose-from-v091.png
Date: 2026-10-05
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.78 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Faces checked at 200% against the lineup: Graxo long face, mustache, silver temples; Daxus glasses; Sion goggles, steel left arm. Used.

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
Image 2 is IDENTITY: The approved crew lineup. Copy their faces, builds, hair, clothing and equipment exactly.
Image 3 is IDENTITY: The crew's approved pose and lighting. Copy their arrangement, poses and light; ignore its background.

TASK: The three crew, alone on plain grey.

ONE single image on a plain flat mid-grey background, a 3:2 horizontal rectangle. No
other objects, no text.

The three crew (image 2) standing together in a tight conspiratorial huddle, full
length, head to boots, posed exactly as in image 3: DAXUS at the left leaning in,
GRAXO behind in the middle, SION at the front right turned to her left facing the two
men and gesturing with her natural right hand.
Their faces, builds, hair, clothing and equipment exactly as image 2 — Graxo's long
weathered face, rounded nose and neat dark mustache with silver temples; Daxus's thin
glasses and full cheeks; Sion's large ruby-red goggles, teal scarf and steel LEFT arm.
Lit as in image 3: in deep shadow, dim and muted, with warm light from the right
catching only the sides of their faces and bodies turned toward it.
They fill the middle half of the picture's height; plain grey all around them.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
