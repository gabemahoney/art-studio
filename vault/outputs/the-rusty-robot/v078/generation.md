# the-rusty-robot v078

User request verbatim: Hmmm...that geometry might be too hard for the renderer. How about we make it a more simple rhomboid-like. But thinner at the top and fatter at the bottom if you know what i mean.
Mode: Edit off v076: canopy rebuilt as one simple trapezoid block (top edge ~4/5 of bottom, both ends slanting outward ~20 deg, mirror images, no end caps or vents). Only the canopy region will be kept; composite onto v076 follows.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10050-c8ae-7363-8c6a-e1ac59d265e0/exec-6a21f8f2-0f1b-4f3f-ace8-e63d60940289.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v076/image.png
Date: 2026-10-02
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.03 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Canopy rebuilt as one simple block whose FRONT outline is a trapezoid (narrow top, wide bottom), ends slanting outward. User clarified this is the wrong reading: top and bottom should be equal length, with the trapezoid in the SIDE profile. Rest of frame close to v076 (mean diff ~3/255 along y 460-540).

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
Image 2 is EDIT TARGET: Reproduce this picture and change only what the spec names.

TASK: A single scene illustration: the exterior of the Rusty Robot cantina at night in the domed city of Kannan.

Reproduce image 2 and change ONE thing: the shape of the heavy canopy over the door.
Everything else stays exactly as it is.

In image 2 each end of the canopy is a separate bevelled cap with a vent panel on it,
so the canopy reads as three pieces. Replace it with ONE SIMPLE SOLID BLOCK:

- Seen from the front, its outline is a TRAPEZOID: a straight top edge, a straight
  bottom edge, and two straight slanted ends.
- The top edge is SHORTER than the bottom edge — about four fifths of its length — so
  the block is narrow at the top and wide at the bottom.
- Each end is ONE straight edge slanting outward as it goes down, both at the same
  angle, about twenty degrees from vertical. The left end and the right end are mirror
  images.
- The front face is one flat plane. No separate end pieces, no bevelled caps, and no
  vent panels on the ends.
- The underside is one flat plane catching the warm light from below.
- The block is centred on the door, the same height as the canopy is now.

KEEP UNCHANGED:

- The sign on the canopy's front face: the board, the lettering "THE RUSTY ROBOT",
  the robot emblem, and the small lamp centred above it. No other lettering anywhere.
- The two slim vertical light panels beside the door.
- The door, the stairs and the handrails.
- The three figures at the left and the dark alley they stand in.
- The buildings on the right, the far archway, the skyline, the ground, the palette.

Render the picture as a 3:2 horizontal rectangle, one and a half times as wide as it
is tall.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
