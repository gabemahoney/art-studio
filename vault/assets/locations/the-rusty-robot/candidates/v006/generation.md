# the-rusty-robot v006

User request verbatim: Make it a multi story building. try a brutalist door. nothing on the door should glow.
Mode: Edit off v005: four storeys (three above the canopy); brutalist rectangular concrete portal with raw steel slab leaves; no glowing elements on the door; side-elevation underside light removed (description v6).
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10067-6b2b-70c0-a0ed-29e3625bd1b6/exec-1b42f32d-5c9f-4636-bf51-68493a1bc4fb.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: assets/locations/the-rusty-robot/candidates/v005/image.png
Date: 2026-10-02
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.95 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: LANDED: brutalist rectangular board-formed concrete portal with raw steel slab leaves; nothing on the door glows (lamps beside it still lit, as described); canopy underside plain in all views. MISSES: storey count differs between views — front elevation has four storeys, the three-quarter and side views three; in the three-quarter view the lettering and emblem are drawn level while the board slants (user: not on the same plane as the marquee).

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

SUBJECT DESIGN (description v6, restated so nothing is invented):
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

- A **brutalist** door. A deep rectangular portal of raw board-formed concrete: a
  massive square-edged frame, its lintel a single heavy slab, set well back into the
  facade. Within it, two flat slab door leaves of raw dark steel, meeting at a plain
  vertical seam, each with one deep horizontal recessed groove and a short vertical
  bar handle. Heavy, blunt, rectilinear. No arch.
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

Reproduce image 2, the reference sheet, and change THREE things. Everything else stays
exactly as it is: the three views, their layout, the canopy's shape in every view, the
sign with its lettering and robot emblem, the lamp hood on the canopy, the two slim
lamps beside the door, the stairs, side walls and handrails, the grey background.

FIRST: FOUR STOREYS.

The building rises THREE storeys above the canopy instead of one: four storeys in all.
Each upper storey is the same width as the front, in the same stone, with a row of
THREE evenly spaced deep-set dark rectangular windows; the top storey ends in a plain
flat parapet. In the three-quarter view the left side wall rises with them, with small
deep-set windows on each storey. In the side elevation the facade line runs straight
up past the canopy to the parapet. Fit the taller building into each view by drawing
every view a little smaller; keep the three views separate on the grey.

SECOND: A BRUTALIST DOOR, IN ALL THREE VIEWS.

Replace the arched metal door and its arched surround. The door is now a deep
RECTANGULAR portal of raw board-formed concrete: a massive square-edged frame whose
lintel is one heavy slab, set well back into the facade. Within it, two flat slab door
leaves of raw dark steel meeting at a plain vertical seam, each with one deep
horizontal groove and a short vertical bar handle. No arch anywhere.

THIRD: NOTHING ON THE DOOR GLOWS.

No light strip up the seam, no light band above the door, no lit control panel or
button. Beside the portal's right edge, one plain unlit square steel plate. Also: the
canopy's underside is plain stone with no light in it, in every view — including the
side elevation, where one small light is still set into it.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
