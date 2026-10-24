# getting-sky v080

User request verbatim: Lets try some red laser-like projectiles though. they MUST come out from the exact angle of the Hegemony forward facing turrets and MUST go straight
Mode: Blend pass off v078: paint the laser bolts, positions locked. Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10a9e-0823-7ed0-95e5-c1ecc45bae37/exec-090bc71b-9f7a-43cb-bdb0-e84a9bc79663.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/getting-sky/v078/image.png
Date: 2026-10-04
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.16 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: REJECTED by user: 'awful. they look cartoonish.' Thick flat bars read as cartoon.

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

TASK: Paint the laser bolts in this scene.

Reproduce image 2 exactly. Do not move, rotate, lengthen or shorten anything — every
red bolt stays exactly where it is, along exactly the same straight line. Only paint
the red bolts as glowing laser projectiles in the picture's style: each a bright
red-orange core with a soft crimson edge and a short faint streak trailing behind it,
plus a small red muzzle flash at the tip of each gun barrel. Everything else —
ships, trails, gorge — stays exactly as it is.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
