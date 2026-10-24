# the-rusty-robot v073

User request verbatim: Put the Rusty Robot sign back on the margue like it was in v5 / also make the stairs right. they are too long and not symmetrical. this is for v072
Mode: Edit off v072 (user-designated): sign moved down onto the canopy's front face as in v005, covering the louvres; staircase shortened to ~7 treads, centred on the door, with matching side walls.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10044-3208-7472-b4ca-f464d278effd/exec-33050f9a-ddc7-48c7-99e5-34055ddc1432.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v072/image.png
Date: 2026-10-02
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.05 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: STAIRS LANDED: about six treads, centred on the door, two matching side walls ending in matching square blocks on the pavement, open pavement in front; no handrails. SIGN MISSED: the deep louvred canopy block was removed entirely rather than covered; the canopy is now a thin slab and the sign board stands on top of it against the wall, not mounted on the canopy's face as in v005. Lettering and emblem intact, no other text. Crew, door, right-hand buildings, far archway and ground read unchanged by eye.

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

Reproduce image 2 and change TWO things. Everything else stays exactly as it is.

FIRST: MOVE THE SIGN ONTO THE CANOPY.

In image 2 the sign board hangs on the wall ABOVE the canopy. Move it DOWN so it is
mounted flat on the canopy's own front face — the deep horizontal block above the
door that currently carries four louvred vents.

- The sign board now covers the canopy's front face, centred on it, and is wholly
  contained within it: a strip of the canopy's stone face shows beyond both ends of
  the board, and above and below it. Nothing overhangs the canopy.
- The four louvred vents on that face are gone, hidden behind the board.
- The board itself is unchanged: rusted metal, the same lettering "THE RUSTY ROBOT" in
  the same wide squared capitals, the same robot emblem at its right end. No other
  lettering anywhere.
- The small lamp that lit the sign from above now sits on the top edge of the canopy,
  centred over the board, shining down onto it.
- The wall where the sign used to hang, above the canopy, is now plain wall in the
  same stone as the rest of the building, continuing the windows and banding around it.
- The two downlights under the canopy stay where they are.

SECOND: MAKE THE STAIRCASE SHORTER AND SYMMETRICAL.

In image 2 the flight is too long — about eleven treads spilling far into the street —
and lopsided: a massive block on the left, a thin sloping parapet on the right.

- About SEVEN treads, ending roughly halfway between the door sill and the bottom
  edge of the picture, so open pavement shows in front of the bottom tread.
- The flight is centred on the door: its left and right edges are equally far from
  the door's centre line.
- The two side walls are a MATCHING PAIR, mirror images of each other: the same
  thickness, the same height, the same sloping top, each ending on the pavement in the
  same square block.
- Every tread is contained between the two side walls. No handrails.

FREEZE EVERYTHING ELSE:

- The three figures at the left, their poses, faces, clothing and the robot arm, and
  the deep shadow they stand in.
- The alley corner wall at the left, the pipe, the near wall.
- The door, its arch and ironwork; the two dark windows, one each side of the door.
- The buildings down the right-hand side, the far lit archway, the distant figures,
  the domed skyline.
- The ground and the palette.

Render the picture as a 3:2 horizontal rectangle, one and a half times as wide as it
is tall.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
