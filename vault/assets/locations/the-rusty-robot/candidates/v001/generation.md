# the-rusty-robot v001

User request verbatim: Let's rebuild the Rusty robot as an asset. And lets make some reference buildings as well for the street scene. Then we can do some passes places the crew into a scene. / also the rusty robot sheet needs to have the logo and image from this last one
Mode: New asset, sheet v1: three-quarter view, front elevation, left side elevation. Sign from scene v082 attached as IDENTITY.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a1005d-219d-7150-89e4-f8cf62b247ed/exec-4733ce2d-d816-4c81-8aa3-d8c03e4948b8.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/locations/the-rusty-robot/sources/sign-from-scene-v082.png
Date: 2026-10-02
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.98 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: SUPERSEDED: its sign source (sources/sign-from-scene-v082.png) included v082's canopy and lamp hood; user asked that only the lettering and robot carry over. Regenerated in v002 from the flattened board.

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
Image 2 is IDENTITY: The sign to reproduce: board, lettering and robot emblem. Copy its design; ignore its cropping and surroundings.

TASK: An architectural reference sheet of the Rusty Robot cantina's entrance.

SUBJECT DESIGN (description v1, restated so nothing is invented):
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
- Design source: `sources/sign-from-scene-v082.png`.

## The door and lamps

- A round-arched double door of dark wood, each leaf with a wheel-spoke pattern of
  heavy battens, two vertical metal pull handles at the centre. Set in a deep
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
  first stretch of the left side wall. Night lighting as described.
- UPPER RIGHT: a FRONT ELEVATION, perfectly square to the facade, no perspective.
  This view is the authority on symmetry: the canopy, sign, door, lamps, flight, side
  walls and handrails are all mirror images about the door's vertical centre line.
- LOWER RIGHT: a SIDE ELEVATION seen from the LEFT, perfectly square, the facade a
  vertical line at the RIGHT of the view and the street to the left. This view is the
  authority on profiles: the canopy is a trapezoid, narrow at the top and about twice
  as deep at the bottom; the steps descend from the door to the left in seven equal
  treads; the side wall's sloping top and handrail run the full length of the flight
  to a post at the bottom tread.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
