# the-rusty-robot v074

User request verbatim: I want to go back to v5 and start from there. Make the following changes: 1. Make the alley more clearly and plausibly connected to the side of the Rusty Robot. 2. Fix the geometry of the marguee. The left and right sides should be the same shape. 3. Change the lamps to look more modern and sci fi 4. Make the stair case and handrails symmetrical. Do NOT change the crew or the lighting in the alley way itself.
Mode: Edit off v005 (user-designated): alley tied to the cantina's left side wall; canopy ends made mirror images; lantern lamps replaced with slim sci-fi wall fixtures; stairs and handrails made symmetrical. Crew and alley lighting frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10048-0eef-7702-b45c-de9970af558d/exec-66777ee6-726d-4eab-a68c-f8cb5ade6018.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v005/image.png
Date: 2026-10-02
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.13 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Off v005. LANDED: cantina's left side wall now runs back into the alley with windows, tying the alley to the building; canopy ends both angle back and read as near-mirror images; lanterns replaced by slim vertical panel fixtures, a matching pair; stair side walls and two handrails now a matching pair. MISSED: the flight is not centred on the door (sits ~90 px right of the door's centre line); the alley was brightened (far end 43 vs v005's 27) with a lit window and sky at its far end; crew brightened (ratio 0.329 vs 0.2975) and shifted ~15 px. Fixed by composite in v075.

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

Reproduce image 2 and change FOUR things. Everything else stays exactly as it is.

FIRST: CONNECT THE ALLEY TO THE CANTINA.

The three figures at the left stand in a narrow alley that runs back into the picture
along the cantina's LEFT side. Make that plain:

- The alley's right-hand wall IS the cantina's own left side wall: the same stone,
  running straight back from the cantina's front corner into the darkness, with its
  base meeting the alley floor in one continuous line.
- The cantina's front left corner is one clean vertical edge, from the ground up to
  the roof, where the front facade turns the corner into that side wall.
- The alley floor is the same ground as the street, continuing into the alley without
  a break.
- The alley's left-hand wall is the neighbouring building at the picture's left edge,
  as now.

SECOND: MAKE THE CANOPY SYMMETRICAL.

The heavy armoured canopy over the door, carrying the sign on its front face, has two
different ends: the left end is a large angled wedge, the right end is a different
shape. Make the two ends MIRROR IMAGES of each other:

- Both ends angle back toward the wall at the same slope, with the same depth and the
  same height.
- The canopy is centred on the door.
- The sign stays mounted on the canopy's front face, centred, wholly contained within
  it with a margin of canopy face beyond both ends. Its board, lettering "THE RUSTY
  ROBOT" and robot emblem are unchanged. No other lettering anywhere.
- The small lamp above the sign stays centred over it.

THIRD: MODERN SCIENCE-FICTION LAMPS.

Replace the two lantern-style lamps beside the door with modern science-fiction light
fixtures: each one a slim vertical metal housing mounted flat to the wall, with a
single tall rectangular light panel down its face. The two are identical and mirror
each other, one each side of the door at the same height. They give the same warm
light as now.

FOURTH: MAKE THE STAIRCASE AND HANDRAILS SYMMETRICAL.

- The flight is centred on the door: its left and right edges are equally far from
  the door's centre line.
- Two matching side walls, mirror images of each other: the same thickness, the same
  height, the same sloping top, each ending on the ground in the same square block.
- Exactly TWO handrails, a matching pair: one running down each side of the flight,
  each with the same shape, the same height and the same posts.
- Keep the flight's length and the number of treads as they are now.

FREEZE EVERYTHING ELSE:

- The three figures, their poses, faces, clothing and the robot arm.
- The lighting in the alley where the figures stand: they stay in deep shadow at the
  same brightness as now.
- The door, its arch and ironwork.
- The buildings down the right-hand side, the far lit archway, the distant figures,
  the domed skyline.
- The ground and the palette.

Render the picture as a 3:2 horizontal rectangle, one and a half times as wide as it
is tall.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
