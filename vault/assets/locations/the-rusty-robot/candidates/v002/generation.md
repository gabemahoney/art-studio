# the-rusty-robot v002

User request verbatim: dont let the bad margue leak into the reference though. just the robot image and the font
Mode: Fresh sheet from description v2: sign source is now the flattened board only (no canopy); canopy side profile stated as bottom edge twice the top; wheel-spoke door; edge-on lamp in side elevation.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a1005f-8473-72e1-b9b7-cbc6e841eebe/exec-8fbbd06a-d8a1-4349-b809-44687e9d5d26.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/locations/the-rusty-robot/sources/sign-board-flat-from-v082.png
Date: 2026-10-02
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.12 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: LANDED: sign from the flattened board only — lettering and robot emblem, no canopy leak; wheel-spoke door with iron straps; slim lamp pair; flight centred on the door with mirror-image side walls in the three-quarter and front views; side elevation shows the canopy trapezoid with the bottom about twice the top, and its handrail runs to a post at the bottom. MISSED: in the three-quarter and front views the side walls and handrails stop about three treads short — the lower treads run on past the end blocks. PARTIAL: in the three-quarter view the canopy end face is only moderately wider at the bottom.

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
Image 2 is IDENTITY: The sign board, flattened: copy its lettering and its robot emblem only.

TASK: An architectural reference sheet of the Rusty Robot cantina's entrance.

SUBJECT DESIGN (description v2, restated so nothing is invented):
A cantina in the domed city of Kannan. Its street front is a heavy stone entrance block
with a canopy carrying the sign, a round-arched door at the top of a short flight of
steps, and a narrow alley running back along its left side. Everything about the
entrance is symmetrical about the door's centre line.

Provisional details are marked *(provisional)*; everything else is established.

## Massing

- A stone building of warm sand-coloured plaster over grey concrete, about three
  storeys tall *(provisional)*, its front face flat and square to the street.
- The front-left corner is one clean vertical edge from the ground to the roof. The
  building's left side wall runs straight back from that corner and forms the right
  wall of a narrow alley. The side wall carries a few small deep-set windows, unlit.
- Upper storeys: deep-set windows in plain stone *(provisional)*.

## The canopy

- One simple solid block projecting from the facade above the door, centred on it,
  wider than the door's stone arch surround.
- **From the front it is a plain rectangle**: top edge and bottom edge the same
  length, both ends vertical.
- **From the side it is a trapezoid**: shallow at the top, where it projects only a
  little from the wall, and deep at the bottom, where it projects about twice as far.
  Its front face therefore leans forward as it descends. Its top is a narrow strip; its
  underside is a broad flat plane.
- Both end faces are the same trapezoid. No end caps, no bevelled pieces, no vents.
- Grey weathered stone with a few rust stains.

## The sign

- A rusted metal board mounted flat on the canopy's front face, centred, with a
  margin of canopy face beyond it on all four sides.
- Lettering: **THE RUSTY ROBOT** — "THE" small, upper left; "RUSTY ROBOT" large, in
  wide squared retro capitals, ivory paint. No other lettering anywhere on the
  building.
- At the board's right end, the **robot emblem**: a solid ivory silhouette of a
  butler robot — domed head with a small ball antenna, two round dark eyes, a bow tie,
  two round buttons down the chest, sloping shoulders — as tall as the large capitals.
- A small rectangular lamp hood sits on top of the canopy, centred over the sign,
  throwing warm light down onto it.
- Design source for the lettering and emblem only: `sources/sign-board-flat-from-v082.png`
  (the board alone, flattened; the canopy in that scene is not a design source).

## The door and lamps

- A round-arched double door of dark wood. Each leaf carries half of one large wheel: a
  semicircular rim of heavy battens with spokes radiating from the centre seam — the
  two leaves together read as one spoked wheel. Not an X, not plain planks. Heavy
  iron straps; two vertical metal pull handles at the centre. Set in a deep
  stone arch surround.
- Two **slim vertical light fixtures**, one each side of the door at the same height:
  a narrow metal housing mounted flat to the wall with one tall rectangular warm light
  panel down its face. A matching pair.

## The steps

- **Seven treads** *(provisional count)*, centred on the door: the flight's centre
  line is the door's centre line, and the flight is as wide as the door's arch
  surround.
- The flight runs straight out from the door, perpendicular to the facade.
- **Two side walls, mirror images**: the same thickness, the same height, the same
  sloping top following the treads, each ending at the bottom in the same plain square
  stone block. No ledges, steps or extra blocks on one side that the other lacks.
- **Two handrails, mirror images**: dark metal pipe, one along the top of each side
  wall, running the full length of the flight from beside the door to a vertical post
  at the bottom tread.

## Colour and light

- At night the entrance is lit warm amber by the door fixtures and the sign lamp; the
  stone around the door glows ochre and gold, falling to cool slate blue away from
  the light.
- Palette: sand plaster, grey stone, rust brown, dark wood, ivory lettering, black
  metal.

A single architectural reference sheet on a plain flat mid-grey background, a 3:2
horizontal rectangle, one and a half times as wide as it is tall. The building's
ground floor and entrance only, cut off cleanly above the canopy's top edge plus one
storey of facade. No street, no sky, no neighbouring buildings, no people. No text
other than the sign's own lettering; no labels, arrows, dimension lines or frames.

THREE views of the same entrance, at one consistent scale, separated by empty grey:

- LEFT HALF, largest: a THREE-QUARTER VIEW from in front and to the building's LEFT,
  at standing eye height, showing the front face, the canopy's left end face and the
  first stretch of the left side wall. The canopy's left end face is plainly a
  trapezoid: its bottom edge is TWICE as long as its top edge. Night lighting as
  described.
- UPPER RIGHT: a FRONT ELEVATION, perfectly square to the facade, no perspective.
  This view is the authority on symmetry: the canopy, sign, door, lamps, flight, side
  walls and handrails are all mirror images about the door's vertical centre line.
- LOWER RIGHT: a SIDE ELEVATION seen from the LEFT, perfectly square, the facade a
  vertical line at the RIGHT of the view and the street to the left. This view is the
  authority on profiles. The canopy is a trapezoid: its top edge runs out from the
  wall a short distance, its bottom edge runs out TWICE as far, and the front edge
  joining them leans forward as it goes down. Draw the door lamp here only as a thin
  edge-on sliver on the facade line; the steps descend from the door to the left in seven equal
  treads; the side wall's sloping top and handrail run the full length of the flight
  to a post at the bottom tread.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
