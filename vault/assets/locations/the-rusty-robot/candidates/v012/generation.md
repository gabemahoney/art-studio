# the-rusty-robot v012

User request verbatim: Make it look a litle dirty. Also, I think our buildings have some kind of color bands on them generall. Also, can we try a more brutalist architecture?
Mode: FRESH sheet, no candidate attached: description v9 — brutalist board-formed concrete, two-tone fins, faded teal band per floor line, grime streaks, four storeys, arched windows kept.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a1036f-015c-7953-aea2-7c454e83a50c/exec-ba719275-70c2-4d3e-8291-d9e1661c1679.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/locations/the-rusty-robot/sources/user-canopy-sketch-2026-10-02.png
- Image 3 IDENTITY: assets/locations/the-rusty-robot/sources/sign-board-flat-from-v082.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.05 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: FRESH (no candidate attached), description v9. LANDED: brutalist board-formed concrete massing with deep two-tone fins at the corners and flanking the entrance, heavy plinth and roof band; faded teal colour bands at the floor lines on front and side; grime and rust streaks down from every sill and ledge; arched windows with heavy sills; canopy with trapezoid ends and tilted sign face; arched steel door with no straps and nothing glowing; slim lamp pair; centred flight with matching walls and rails. MISSES: still three storeys in every view (asked four); robot emblem's two eyes merged into one heart-shaped blot in the three-quarter and front views.

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

TASK: An architectural reference sheet of the Rusty Robot cantina, a brutalist concrete building, ground to roof.

SUBJECT DESIGN (description v9, restated so nothing is invented):
A cantina in the domed city of Kannan: a four-storey brutalist concrete building whose street front
is a heavy entrance with a tilted sign canopy, an arched door at the top of a short
flight of steps, and a narrow alley running back along its left side. The entrance is
symmetrical about the door's centre line.

Design sources:
- `sources/user-canopy-sketch-2026-10-02.png` — the user's sketch of the canopy and massing.
- `sources/sign-board-flat-from-v082.png` — the sign's lettering and robot emblem.

Provisional details are marked *(provisional)*; everything else is established.

## Massing — brutalist

- Four storeys of **raw board-formed concrete**: massive, blocky, heavy, its front face
  square to the street. Forms are thick slabs and deep recesses; edges are square and
  blunt. The top storey is crowned by a deep, heavy concrete band projecting slightly
  over the wall below, like a lid.
- The ground storey holds the entrance and is topped by the canopy. Three storeys rise
  above the canopy, the same width as the front.
- The front-left corner is one clean vertical edge from the ground to the roof. The
  left side wall runs straight back from it and forms the right wall of a narrow
  alley, with windows on every storey.

## Surface and character

- **Two-tone fins.** Broad, deep concrete fins run the full height of the front, one
  at each corner and one each side of the entrance. Each fin projects from the wall:
  its front face catches the light, its side face is a darker cool tone — so the front
  reads as alternating light and dark vertical bands.
- **Colour bands.** Painted horizontal bands of muted teal run across the front and
  the side wall at each floor line — one broad band per storey, crossing the fins —
  the only colour on the grey-ochre concrete *(provisional hue)*.
- A heavy concrete **plinth** along the bottom of the front and side walls, slightly
  proud of the wall above, darker than the wall.
- **Dirty.** The concrete is grimy: dark soot and water stains streak down from every
  sill, ledge and band; grime darkens the plinth and the inner corners; the paint of
  the colour bands is faded and patchy. Rust streaks run down from the metal fixtures.
- Warm ochre where lit, cool slate blue-grey on faces turned away from the light.

## Windows

- **Every window on the building has a semicircular arched top**: a vertical opening
  whose head is a half circle, punched deep into the concrete, with a heavy projecting
  concrete sill.
  Dark glass, unlit.
- Front, above the canopy: three storeys, each with three evenly spaced arched windows
  between the fins *(provisional count)*.
- Left side wall: one arched window per storey per bay.

## The canopy

- A deep fascia band running the **full width of the front**, from corner to corner,
  between the ground storey and the storeys above.
- **From the front it is a plain rectangle**: top and bottom edges the same length.
- **From the side it is a trapezoid**: its back edge is the facade; its top edge runs
  out from the wall a short way; its bottom edge runs out about one and a half times as
  far; the front edge joining them slants forward as it goes down. The sign face
  therefore **tilts outward at the bottom**, angled down toward the street.
- Both end faces are the same trapezoid, raw concrete. The top is a flat strip; the
  underside is a plain flat plane with no lights in it.

## The sign

- A rusted metal board mounted flat on the canopy's tilted front face, centred on the
  door, with canopy face showing beyond it on all four sides. One flat plane: all its
  lettering and the emblem lie in it and share its perspective.
- Lettering: **THE RUSTY ROBOT** — "THE" small, upper left; "RUSTY ROBOT" large, in
  wide squared retro capitals, ivory paint. No other lettering anywhere on the building.
- At the board's right end, the **robot emblem**: a solid ivory silhouette of a butler
  robot — domed head with a small ball antenna, two round dark eyes, a bow tie, two
  round buttons down the chest, sloping shoulders — as tall as the large capitals.
- A small rectangular lamp hood on the canopy's top edge, centred over the sign,
  throwing warm light down onto it.

## The door

- A **brutalist** door with a **semicircular arched top**: a deep round-arched portal
  of raw board-formed concrete, a massive thick square-edged surround whose top is a
  full half circle, set well back into the facade.
- Two flat slab door leaves of raw dark steel fill the opening up into the arch,
  meeting at a plain vertical seam, each with one deep horizontal groove and a short
  vertical bar handle.
- **Nothing on or around the door glows.** The wall either side of the portal is plain
  concrete. No straps, rivets or studs on the leaves.

## The lamps

- Two slim vertical light fixtures, one each side of the door on the fins' inner
  faces, at the same height: a narrow metal housing mounted flat to the wall with one
  tall rectangular warm light panel. A matching pair. These are the entrance's light.

## The steps

- **Seven treads**, centred on the door: the flight's centre line is the door's centre
  line, and the flight is as wide as the portal.
- The flight runs straight out from the door, perpendicular to the facade.
- **Two side walls, mirror images**: the same thickness and height, sloping tops
  following the treads, and as long as the flight: each ends in the same plain square
  concrete block beside the bottom tread, so no tread runs past them.
- **Two handrails, mirror images**: dark metal pipe along the top of each side wall,
  from beside the door to a vertical post on the end block beside the bottom tread.

## Light

At night the entrance is lit warm amber by the two door lamps and the sign lamp; the
concrete around the door glows ochre and gold, falling off to cool slate blue away from
the light and on every face turned from it.

A single architectural reference sheet on a plain flat mid-grey background, a 3:2
horizontal rectangle, one and a half times as wide as it is tall. The entrance front
of the building only, ground to parapet. No street, no sky, no neighbouring buildings, no people. No text
other than the sign's own lettering; no labels, arrows, dimension lines or frames.

Image 2 is a rough line sketch by the user of the canopy and massing, drawn from in
front and to the left. Follow its GEOMETRY exactly: the canopy is a deep band across
the whole width of the front at the top of the ground storey, its left end face is a
trapezoid, and its front face (the
one carrying the word) slants outward as it goes down. Ignore the sketch's line-drawing
technique and its scribbled lettering.

Draw the WHOLE building, all FOUR storeys — the ground storey plus THREE rows of
windows above the canopy — in every view. Every window on the building has a
semicircular arched top. Brutalist raw concrete, two-tone fins, a faded teal colour
band at each floor line, and grime streaking down from every ledge.

THREE views of the same entrance, at one consistent scale, separated by empty grey:

- LEFT HALF, largest: a THREE-QUARTER VIEW of the whole building from in front and to the building's LEFT,
  at standing eye height, matching the sketch's viewpoint: the front face, the
  canopy's left end face, and the first stretch of the left side wall. The canopy's
  left end face is a trapezoid whose bottom edge is one and a half times its top
  edge, and the sign face visibly tilts outward at the bottom, so its lower edge
  overhangs the facade further than its upper edge — exactly as in the sketch. Night
  lighting as described.
- UPPER RIGHT: a FRONT ELEVATION, perfectly square to the facade, no perspective.
  This view is the authority on symmetry: the canopy band spans the whole front; the
  sign, door, lamps, flight, side walls and handrails are mirror images about the
  door's vertical centre line.
- LOWER RIGHT: a SIDE ELEVATION seen from the LEFT, perfectly square, the facade a
  vertical line at the RIGHT of the view and the street to the left. This view is the
  authority on profiles. The canopy is a trapezoid at the top of the facade: its top
  edge runs out from the wall a short distance, its bottom edge runs out one and a half
  times as far, and the front edge joining them leans forward as it goes down. The
  steps descend from the door to the left in seven equal treads; the side wall's
  sloping top and its handrail run the full length of the flight to a post on the end
  block beside the bottom tread. Draw the door lamp here only as a thin edge-on sliver
  on the facade line.

In EVERY view the side walls are as long as the flight: each ends in its square block
beside the bottom tread, and no tread runs past the walls.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
