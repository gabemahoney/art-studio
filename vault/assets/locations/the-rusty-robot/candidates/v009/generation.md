# the-rusty-robot v009

User request verbatim: The door needs to remain half circular like it was in the first image
Mode: Edit off v008: brutalist portal given a semicircular arched top, steel leaves following it (description v7). Only the door regions will be kept; composite onto v008 follows.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a1006c-c9e4-7c52-8a49-c57636dfa174/exec-749c7b14-799b-45a9-b5c8-8639995e3c57.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: assets/locations/the-rusty-robot/candidates/v008/image.png
Date: 2026-10-02
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.89 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Arched brutalist door landed in the three-quarter and front views, nothing on it glows. Built off v008, so it carries v008's rejected warped sign; only its door regions are used, in v010. Grey plate beside the door still present.

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
Image 2 is EDIT TARGET: The reference sheet being revised. Preserve everything the spec does not change.

TASK: Revise this architectural reference sheet of the Rusty Robot cantina's entrance.

SUBJECT DESIGN (description v7, restated so nothing is invented):
A cantina in the domed city of Kannan. Its street front is a heavy stone entrance block
with a canopy carrying the sign, a round-arched door at the top of a short flight of
steps, and a narrow alley running back along its left side. Everything about the
entrance is symmetrical about the door's centre line.

Provisional details are marked *(provisional)*; everything else is established.

## Massing

- A stone building of warm sand-coloured plaster over grey concrete, its front face
  flat and square to the street. **Four storeys.** The ground storey holds the entrance
  and is topped by the canopy; three more storeys rise above the canopy, the same width
  as the front, in the same stone, each with a row of three evenly spaced deep-set
  rectangular windows *(provisional count)*, ending in a plain flat parapet.
- The front-left corner is one clean vertical edge from the ground to the roof. The
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
  strip; the underside is a plain flat plane over the door with **no lights in it**.
- No end caps, no bevelled pieces, no vents, no separate block over the door.
- Grey weathered stone with a few rust stains.

## The sign

- A rusted metal board mounted flat on the canopy's tilted front face, centred on the
  door, with a margin of canopy face beyond it on all four sides. The board is ONE flat
  plane: all its lettering and the emblem lie in that plane and share its perspective.
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

- A **brutalist** door with a **semicircular arched top**. A deep round-arched portal
  of raw board-formed concrete: a massive, thick, square-edged surround whose top is a
  full half circle, set well back into the facade. Within it, two flat slab door
  leaves of raw dark steel filling the opening up into the arch, meeting at a plain
  vertical seam, each with one deep horizontal recessed groove and a short vertical bar
  handle. Heavy and blunt; the only curve is the half-circle top.
- **Nothing on or around the door glows**: no light strips, no light bands, no lit
  panels or buttons. A plain unlit square steel plate on the wall beside the portal's
  right edge *(provisional)*.
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

Reproduce image 2, the reference sheet, and change ONE thing: the shape of the door
opening, in all three views. Everything else stays exactly as it is.

The door opening gets a SEMICIRCULAR ARCHED TOP. Today the concrete portal is a
rectangle with a flat slab lintel. Make its top a full half circle instead:

- The portal keeps its massive, thick, square-edged surround of raw board-formed
  concrete, set well back into the facade — only now the surround's top follows a
  half circle, like a round-arched doorway. The two straight sides rise to where the
  half circle begins.
- The two raw dark steel door leaves fill the opening up into the arch, each leaf's
  top following its half of the curve, meeting at a plain vertical seam. Keep their
  deep horizontal groove and short vertical bar handle.
- The opening stays the same width and sits in the same place.
- Nothing on or around the door glows: no light strips, bands or lit panels.

In the side elevation the door is not visible; leave that view unchanged.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
