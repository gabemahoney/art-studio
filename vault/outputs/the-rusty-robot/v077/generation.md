# the-rusty-robot v077

User request verbatim: Could you take the geometry of the leftside of the marquee in v5 and use that for the geometry instead?
Mode: Edit off v076: both canopy ends rebuilt as v005's left end (crop attached as IDENTITY), right end mirrored. Only the canopy region will be kept; composite onto v076 follows.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a1004d-b31e-7db2-a030-73ff5e1bfd43/exec-d9d18c3b-9312-42d4-8755-1a741636a744.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v076/image.png
- Image 3 IDENTITY: outputs/the-rusty-robot/sources/canopy-left-end-from-v005.png
Date: 2026-10-02
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.98 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: MISSED: canopy is essentially unchanged from v076 (mean abs difference 6/255 over the canopy box 760x420+330+20). Neither end took v005's left-end geometry: no larger projecting block, no visible top face sloping toward the end, no broad underside chamfer. Rest of frame repainted (whole-frame regeneration), so nothing here is worth compositing.

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
Image 3 is IDENTITY: A close-up of the canopy end shape to copy. Copy its shape only; ignore its framing.

TASK: A single scene illustration: the exterior of the Rusty Robot cantina at night in the domed city of Kannan.

Reproduce image 2 and change ONE thing: the shape of the two ends of the heavy armoured
canopy over the door. Everything else stays exactly as it is.

Image 3 is a close-up of how the canopy's LEFT end should look. Give the canopy that
end on the left, and its exact mirror image on the right:

- Each end is a massive armoured block, as deep from front to back as the canopy itself
  and the full height of the canopy.
- Its outer end face is one broad flat slab that leans INWARD toward the sign as it
  rises, so the canopy is wider at the bottom than at the top.
- Its underside is a broad chamfer: one sloping plane running from the bottom front
  edge back and up to the wall, catching the warm light from below.
- Its top face carries one louvred vent panel of five or six horizontal slats.
- Panel seams with a few rivets divide the end block from the canopy's front face.
- The right end is the same size, slope and depth as the left end, reflected left to
  right. The canopy is centred on the door.

KEEP UNCHANGED:

- The sign on the canopy's front face: the board, the lettering "THE RUSTY ROBOT",
  the robot emblem, and the small lamp centred above it. No other lettering anywhere.
- The two slim vertical light panels beside the door.
- The door, the stairs and the handrails.
- The three figures at the left and the dark alley they stand in.
- The buildings on the right, the far archway, the skyline, the ground, the palette.

Take only the SHAPE from image 3. Its colours and lighting already match image 2.

Render the picture as a 3:2 horizontal rectangle, one and a half times as wide as it
is tall.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
