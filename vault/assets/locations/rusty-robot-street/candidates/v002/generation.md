# rusty-robot-street v002

User request verbatim: Also the dome looks too small. Take a look at v5 from the old images for an idea. Also, the buildings to the right of the Robot should all be pressed against it, like a real city. The alley on the left is the only visible alley. Also, have it so the left frame of the picture is in the alley. I dont want to see so much of the building to the elft of the alley at all
Mode: Fresh v2 (composition change): left edge inside the alley, right-hand buildings wall to wall, dome at v005 scale, matte dry paving.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a103dc-a6a1-78d3-9b1e-f3cc8bd790bc/exec-1540931d-2e7a-4167-a150-2e1891341809.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/locations/the-rusty-robot/reference.png; frozen assets/locations/the-rusty-robot/candidates/v023/image.png
- Image 3 IDENTITY: assets/locations/rusty-robot-street/sources/dome-from-scene-v005.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.31 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: LANDED: left edge is the alley's far wall in deep shadow, no building facade left of the alley; right-hand buildings stand wall to wall in one continuous frontage, varied heights and band colours; dome ribs larger, sweeping arcs across the whole sky; paving matte and dry. MISSES: the alley reads wide and lit — the cantina's long left side wall is lit as brightly as the street, so the alley is not the darkest area; dome ribs thinner than v005's.

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
Image 2 is IDENTITY: The Rusty Robot's approved reference sheet. Copy the building's design exactly; ignore the sheet layout.
Image 3 is IDENTITY: A painting showing the city dome's scale. Copy the dome's size and the distant towers only.

TASK: A single establishing illustration: the Rusty Robot cantina on its street inside the domed city of Kannan, at night.

SUBJECT DESIGN (description v2, restated so nothing is invented):
The street outside the Rusty Robot cantina, inside the domed city of Kannan, at night.
The establishing setting for scenes at the cantina.

Design sources:
- `assets/locations/the-rusty-robot/reference.png` — the cantina itself (approved).
- `sources/dome-from-scene-v005.png` — the city dome's scale and the skyline.

Provisional details are marked *(provisional)*; everything else is established.

## Layout

- **The Rusty Robot** stands on the street exactly as its reference shows: three
  storeys of brutalist concrete, the tilted sign canopy, the arched steel door at the
  top of its centred flight of steps, the two slim door lamps and the sign spotlight.
- **A dark alley** runs back into the block immediately to the LEFT of the Rusty
  Robot, between its left side wall and the neighbouring building. It is narrow —
  about as wide as the cantina's flight of steps *(provisional)* — deep, and dark: no
  lamps in it, lit only by faint spill from the street at its mouth. Its floor is the
  same paving as the street. This is where the crew will stand in the final scenes,
  so its mouth is clearly visible and unobstructed.
- **The street** runs past the cantina's front and recedes to the right. The buildings
  to the right of the Rusty Robot stand **wall to wall against it and against each
  other**, a continuous street frontage like a real city — no gaps, no other alleys.
- **The alley to the cantina's left is the only alley in view.** The building on the
  alley's far side is barely seen: only the alley wall it presents.

## The street surface

- The street is **indoors, under the dome**: a smooth, level paved surface of large
  rectangular concrete slabs with straight joints, swept and dry. No dirt, no rocks,
  no rubble, no puddles. Grime collects only along the building bases and in the
  joints.

## The neighbouring buildings

- The same **brutalist** language as the Rusty Robot: raw board-formed concrete,
  massive blocky forms, deep projecting fins, heavy sills and roof bands, arched
  windows, soot and rust streaks running down from every ledge.
- Each carries **painted horizontal colour bands** at its floor lines, faded and
  patchy; each building's band colour differs — muted teal, brick red, mustard, slate
  blue *(provisional)*.
- Varied in width, height and roofline, so the street reads as many separate
  buildings: some three storeys, some five or six, some with stepped tops.
- A few windows lit warm amber; most dark.

## The dome and sky

- Above the street, the **city dome** fills the sky: a vast curved lattice of heavy
  structural ribs, close overhead and **huge** — individual ribs are thick bands
  sweeping in long arcs across the whole sky, the lattice cells larger than the
  buildings below them — against deep night blue.
- Beyond the street's far end, a skyline of domed and towered buildings with scattered
  lit windows.

## Light

Night. The Rusty Robot's entrance is the brightest, warmest place on the street —
amber from its door lamps and sign spotlight. The street elsewhere is cool slate blue,
with a few warm windows and a street lamp or two farther down *(provisional)*. The
alley to the left of the cantina is the darkest area in the picture.

ONE single illustration, a 3:2 horizontal rectangle, one and a half times as wide as it
is tall. No text other than the cantina's own sign; no labels, borders or frames; no
people anywhere.

Image 2 is the Rusty Robot cantina's approved reference sheet: copy the building's
design exactly from it — its massing, fins, colour bands, arched windows, tilted sign
canopy, sign lettering and robot emblem, arched steel door, centred steps and
handrails, lamps. Ignore the sheet's layout and grey background; draw the building
once, standing in the street.

Image 3 shows how BIG the city dome is: copy its scale — heavy ribs sweeping in huge
arcs across the sky, close overhead — and the domed towers beyond. Ignore its
foreground buildings and its painting of the street.

COMPOSITION, from left to right:

- THE LEFT EDGE OF THE PICTURE IS INSIDE THE ALLEY. The left fifth of the picture is
  the dark alley: its far wall runs along the picture's left edge, plain and in deep
  shadow, and the alley floor recedes into darkness. No building facade is visible to
  the left of the alley — only that dark alley wall.
- The Rusty Robot occupies the centre, seen from in front and slightly to its left,
  its left side wall forming the alley's right-hand wall. Its entrance and sign are
  plainly visible.
- To the RIGHT of the cantina, the street recedes into the distance. Every building
  on this side stands WALL TO WALL: the first building's left wall touches the
  cantina's right wall, the next touches that one, and so on — one continuous
  frontage with no gaps, no alleys, no space between buildings. They are brutalist
  concrete like the cantina, each with faded painted colour bands of a different
  colour, varied in height and roofline.

The alley on the left is the only alley in the picture and the darkest area in it.

ABOVE: the city dome's ribs fill the sky — thick bands sweeping in vast arcs, each
lattice cell larger than a building — against deep night blue.

GROUND: smooth, matte, dry concrete paving slabs with straight joints, indoors. No
dirt, no rocks, no puddles, no reflections or sheen.

The cantina's entrance is the warmest, brightest light in the picture.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
