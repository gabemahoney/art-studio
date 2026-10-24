# the-rusty-robot v004

User request verbatim: Lets make the door look less medieval. more sci fi. / Youve got the marguee correct on the side view. Just not the 3/4 view
Mode: Edit off v003 (user-designated by confirming its side view): three-quarter canopy made to match the side elevation (sketch attached); door replaced with sci-fi sliding metal panels in all views (description v4).
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10063-990d-7863-8431-9dbf858a3f58/exec-d3ecf26d-f561-424a-a6ae-88dd07081ae4.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: assets/locations/the-rusty-robot/candidates/v003/image.png
- Image 3 IDENTITY: assets/locations/the-rusty-robot/sources/user-canopy-sketch-2026-10-02.png
Date: 2026-10-02
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.01 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: User: 'Better.' LANDED: three-quarter canopy now reads as the tilted trapezoid; metal sliding door with seam light, transom light band and control panel. MISSES (user): the word ROBOT and emblem are not in the same plane as the rest of the board in the three-quarter view; small downlights on the canopy underside unwanted; door reads too dark to be clearly metal. User also asks for a second storey.

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
Image 3 is IDENTITY: The user's sketch of the canopy from the three-quarter angle. Copy its geometry only; ignore its line technique and lettering.

TASK: Revise this architectural reference sheet of the Rusty Robot cantina's entrance.

SUBJECT DESIGN (description v4, restated so nothing is invented):
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

- A science-fiction door set in a deep round-arched stone surround. Within the arch,
  a pair of heavy sliding metal door panels of dark gunmetal, worn and lightly rusted,
  meeting at a vertical centre seam. Each panel carries a few broad horizontal ribs and
  one flush rectangular inset; a thin strip of warm light runs up the centre seam. The
  arched top above the panels is a fixed metal transom with a single horizontal light
  band. A small square control panel with a lit button sits on the wall beside the
  right edge of the arch *(provisional)*. No wooden planks, no battens, no iron straps,
  no studs, no ring handles.
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

Reproduce image 2, the reference sheet, and change TWO things. Everything else stays
exactly as it is: the three views, their layout and scale, the sign and its lettering
and robot emblem, the lamps, the stairs, side walls and handrails, the grey background.

FIRST: FIX THE CANOPY IN THE LARGE THREE-QUARTER VIEW ON THE LEFT.

The SIDE ELEVATION at lower right is already correct: there the canopy's end is a
trapezoid, short at the top and longer at the bottom, and its front edge leans forward
as it goes down. The three-quarter view must show that SAME shape. Image 3 is the
user's sketch of how it should look from this angle:

- The canopy's left end face is a trapezoid: its top edge runs back to the wall a short
  way; its bottom edge runs back one and a half times as far.
- The sign face tilts OUTWARD at the bottom: its lower edge hangs further out from the
  facade than its upper edge, so we see the face angled down toward the street.
- The canopy spans the whole front of the building, from the left corner to the right
  corner.

SECOND: MAKE THE DOOR SCIENCE FICTION, IN ALL THREE VIEWS.

Replace the wooden door with a metal one. Keep the round-arched stone surround. Within
it: a pair of heavy sliding metal door panels of dark gunmetal, worn and lightly
rusted, meeting at a vertical centre seam, each carrying a few broad horizontal ribs
and one flush rectangular inset, with a thin strip of warm light running up the seam.
The arched top above the panels is a fixed metal transom with one horizontal light
band. A small square control panel with a lit button on the wall beside the arch's
right edge. No wooden planks, no battens, no wheel, no iron straps, no studs.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
