# getting-sky-gunship-pose v004

User request verbatim: 53. (next: gunships behind the Antares)
Mode: Gunship pose for the upper-atmosphere scene: climbing to upper right, seen from left and below. Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10a5a-c902-7d82-835a-dfbaf69a4da7/exec-23cd90f4-9f81-46a0-9546-ac4e59f04bee.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/ships/hegemony-assault-ship/reference.png; frozen assets/ships/hegemony-assault-ship/candidates/v014/image.png
Date: 2026-10-04
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.78 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Only three pods visible (near-front pod missing); hull reads grey-brown, not black.

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
Image 2 is IDENTITY: The assault ship reference sheet. Copy its design exactly; ignore the sheet layout.

TASK: A single flight view of the Hegemony assault ship on plain grey.

ONE single view of the Hegemony assault ship (image 2) on a plain flat mid-grey
background, a 3:2 horizontal rectangle. No other objects, no text.

It is climbing steeply toward the UPPER RIGHT of the picture: its nose and twin chin
guns point to the upper right, its tail to the lower left. Seen from its left side
and slightly below.
- Exactly FOUR thruster pods, two on each side, all pointing straight back toward the
  lower left; the near pods drawn full size, the far pods smaller and partly hidden
  behind the hull, as perspective requires. No exhaust.
- Design exactly as image 2: black armour, red bands, the red line-built star.
- It fills about the middle half of the picture, plain grey all around.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
