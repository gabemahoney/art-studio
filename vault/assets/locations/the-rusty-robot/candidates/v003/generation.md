# the-rusty-robot v003

User request verbatim: this is what I want the margue to look like [sketch: sources/user-canopy-sketch-2026-10-02.png]
Mode: Fresh sheet from description v3: full-width fascia canopy with trapezoid side profile and outward-tilted sign face per the user's sketch; side walls and rails run to the bottom tread.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10061-fa2f-79f0-ace2-8be315f82d3e/exec-fba7eea4-8e7e-4663-9531-97bb4d89f812.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/locations/the-rusty-robot/sources/user-canopy-sketch-2026-10-02.png
- Image 3 IDENTITY: assets/locations/the-rusty-robot/sources/sign-board-flat-from-v082.png
Date: 2026-10-02
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.05 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: NOTE: generated with description v3 and the sketch attached, but with the OLD layout spec (my prompt.md update failed to write before the call; the receipt's Exact prompt is what ran). LANDED: canopy band spans the entrance front; side elevation canopy is a trapezoid leaning forward at the bottom (user confirmed correct); side walls and rails reach the bottom tread in all three views. MISSED: in the three-quarter view the sign face reads vertical, not tilted outward at the bottom (user confirmed wrong). Door is the medieval wheel design; user asked for sci-fi.

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
Image 2 is IDENTITY: The user's sketch of the canopy and massing. Copy its geometry only; ignore its line technique and lettering.
Image 3 is IDENTITY: The sign board, flattened: copy its lettering and its robot emblem only.

TASK: An architectural reference sheet of the Rusty Robot cantina's entrance.

SUBJECT DESIGN (description v3, restated so nothing is invented):
A cantina in the domed city of Kannan. Its street front is a heavy stone entrance block
with a canopy carrying the sign, a round-arched door at the top of a short flight of
steps, and a narrow alley running back along its left side. Everything about the
entrance is symmetrical about the door's centre line.

Provisional details are marked *(provisional)*; everything else is established.

## Massing

- A stone building of warm sand-coloured plaster over grey concrete, its front face
  flat and square to the street. The entrance front is one tall storey, topped by the
  canopy; nothing rises above the canopy's top edge at the front *(provisional)*.
- The front-left corner is one clean vertical edge from the ground to the canopy. The
  building's left side wall runs straight back from that corner and forms the right
  wall of a narrow alley. The side wall carries a few small deep-set windows, unlit.

## The canopy

Design source: `sources/user-canopy-sketch-2026-10-02.png` (the user's sketch).

- A deep fascia band running the **FULL WIDTH of the front**, from the front-left
  corner to the front-right corner, across the top of the facade. It is the top of
  the entrance front, about a third of the front's height.
- **From the front it is a plain rectangle**: top edge and bottom edge the same
  length, both ends flush with the building's corners.
- **From the side it is a trapezoid**: its back edge is the vertical facade line; its
  top edge runs out from the wall a short way; its bottom edge runs out further —
  about one and a half times as far; the front edge joining them slants forward as it
  goes down. So the sign face **tilts outward at the bottom**, angled down toward the
  street.
- Both end faces are the same trapezoid, plain flat stone. The top is a flat roof
  strip; the underside is a flat plane over the door.
- No end caps, no bevelled pieces, no vents, no separate block over the door.
- Grey weathered stone with a few rust stains.

## The sign

- A rusted metal board mounted flat on the canopy's tilted front face, centred on the
  door, with a margin of canopy face beyond it on all four sides.
- Lettering: **THE RUSTY ROBOT** — "THE" small, upper left; "RUSTY ROBOT" large, in
  wide squared retro capitals, ivory paint. No other lettering anywhere on the
  building.
- At the board's right end, the **robot emblem**: a solid ivory silhouette of a
  butler robot — domed head with a small ball antenna, two round dark eyes, a bow tie,
  two round buttons down the chest, sloping shoulders — as tall as the large capitals.
- A small rectangular lamp hood sits on the canopy's top edge, centred over the sign,
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
  sloping top following the treads, and **as long as the flight**: each ends in the
  same plain square stone block standing beside the BOTTOM tread, so no tread extends
  past the walls. No ledges, steps or extra blocks on one side that the other lacks.
- **Two handrails, mirror images**: dark metal pipe, one along the top of each side
  wall, running the full length of the flight from beside the door to a vertical post
  on the end block beside the bottom tread.

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
