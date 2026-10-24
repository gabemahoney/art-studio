# the-rusty-robot v081

User request verbatim: also we still need to fix that shadow on the crew AND make the staircase symmetrical AND extend the hand rails all the way down the stairs. / can you bring back the robot logo from v27 as well
Mode: Edit off v080: stairs centred on the door with matching side walls; two handrails running the full flight to posts on the bottom tread; v027's solid butler-robot emblem (crop attached as IDENTITY) replaces the outline robot. Only the stairs and emblem regions will be kept; composite onto v080 follows.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10056-e642-7e21-970e-882b7744e950/exec-d70848c0-358d-41c3-8934-d95209edcce6.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v080/image.png
- Image 3 IDENTITY: outputs/the-rusty-robot/sources/robot-logo-from-v027.png
Date: 2026-10-02
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.06 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: LANDED: v027's solid butler-robot emblem (antenna, round eyes, bow tie, buttons) replaces the outline robot; side walls now a matching pair of plain blocks; two matching handrails. PARTIAL: flight still sits right of the door's centre (door ~x660, flight centre ~x740) and both handrails end at a post about three treads above the bottom rather than on the bottom tread. Door repainted larger. Crew drifted brighter (41.2 vs 39.3) - left strip replaced from v080 in v082.

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
Image 3 is IDENTITY: The robot emblem to paint on the sign. Copy its design only; ignore the surrounding sign.

TASK: A single scene illustration: the exterior of the Rusty Robot cantina at night in the domed city of Kannan.

Reproduce image 2 and change THREE things. Everything else stays exactly as it is.

FIRST: CENTRE THE STAIRCASE ON THE DOOR AND MAKE IT SYMMETRICAL.

In image 2 the flight sits to the RIGHT of the door: the door is near its left edge.
Move and rebuild it so it is centred on the door:

- The flight's centre line is the door's centre line, the vertical line between the
  two door leaves.
- The flight is as wide as the stone arch around the door: its left edge lies directly
  below the arch's outer left edge, its right edge directly below the arch's outer
  right edge.
- Two side walls, a MATCHING PAIR: the same thickness, the same height, the same
  sloping top, each ending on the ground in the same plain square block. The tall
  stepped block on the left of image 2 becomes the same as the right side wall.
- Keep the same number of treads and the same overall length into the street.

SECOND: RUN THE HANDRAILS ALL THE WAY DOWN.

Exactly two handrails, a matching pair, one along each side wall. Each starts beside
the door and runs down the full length of the flight, parallel to the treads' slope,
ending in a vertical post standing on the bottom tread.

THIRD: THE ROBOT EMBLEM ON THE SIGN.

Image 3 shows the robot emblem the sign should carry. At the right end of the sign
board, replace the current outline robot with this one: a solid ivory painted
silhouette of a butler robot — a domed head with a small ball antenna, two round dark
eyes, a bow tie, two round buttons down the chest, sloping shoulders — the same height
as the lettering's capitals.

KEEP UNCHANGED:

- The canopy over the door: one simple block, rectangular from the front, its end
  faces wider at the bottom than at the top. The sign board and the lettering "THE
  RUSTY ROBOT", and the small lamp above. No other lettering anywhere.
- The door, its arch, and the two slim vertical light panels beside it.
- The three figures at the left and the dark alley they stand in.
- The buildings on the right, the far archway, the skyline, the ground, the palette.

Render the picture as a 3:2 horizontal rectangle, one and a half times as wide as it
is tall.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
