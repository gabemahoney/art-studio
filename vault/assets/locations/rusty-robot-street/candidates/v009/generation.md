# rusty-robot-street v009

User request verbatim: Use the v5 from the old batch as the reference we are trying to target in terms of scene composition and the size of the buildings. / Thats better but we need less garage style doors for the buildings. Its a pedestrian only city.
Mode: FRESH: old scene v005 (crew blacked out) attached for composition and building scale; pedestrian-only doors. Roll 1 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a103f1-b44b-7390-bb90-5cdf810b9589/exec-bc95bb8f-d28b-4292-9796-1f7f396a7511.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/locations/the-rusty-robot/reference.png; frozen assets/locations/the-rusty-robot/candidates/v023/image.png
- Image 3 IDENTITY: assets/locations/rusty-robot-street/sources/composition-from-scene-v005.png
- Image 4 IDENTITY: assets/locations/rusty-robot-street/sources/dome-from-scene-v005.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.26 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: FRESH with old scene v005 for composition. Matches its composition: low camera, cantina large at left-centre, street receding steeply right between tall wall-to-wall buildings, dome ribs and domed towers in the sky gap. Person-sized doors only. Sign per reference. Alley is a dark strip at the left edge, narrow.

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
Image 3 is IDENTITY: An earlier painting of this street. Copy its composition and building scale only.
Image 4 is IDENTITY: A painting showing the city dome's scale. Copy the dome's size only.

TASK: A single establishing illustration: the Rusty Robot cantina on its street inside the domed city of Kannan, at night.

SUBJECT DESIGN (description v6, restated so nothing is invented):
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
  alley's far side is not seen at all: the picture's left edge falls inside the alley.

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
  buildings with moderately varied heights: three to five storeys, each differing from
  its neighbour by about one storey, rooflines stepping gently up and down.
- Kannan is **pedestrian only**: every ground-floor opening is a person-sized door —
  single or double, arched or square, set up a step or two — or a shopfront window.
  No garage doors, roller shutters or vehicle bays anywhere.
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
with a few warm windows. No street lamps. The
alley to the left of the cantina is the darkest area in the picture.

ONE single illustration, a 3:2 horizontal rectangle, one and a half times as wide as it
is tall. No text other than the cantina's own sign; no labels, borders or frames; no
people anywhere.

Image 2 is the Rusty Robot cantina's approved reference sheet. Copy the building
EXACTLY as its large three-quarter view shows it: three storeys of brutalist concrete,
teal bands, two-tone fins, arched windows, the heavy canopy whose LEFT end face is a
trapezoid narrow at the top and wide at the bottom, the sign face tilting outward at
the bottom with the rusted board lying flat on it — lettering "THE RUSTY ROBOT" and the
robot emblem in the board's perspective — the lamp hood over the sign, the arched steel
door, the centred steps with matching side walls and handrails, the two slim door
lamps. Ignore the sheet's layout and grey background; draw the building once.

Image 3 is an earlier painting of this street. Copy ONLY its COMPOSITION and SCALE:
- the low camera close to the cantina, its entrance large in the left half of the
  picture with the canopy near the top third;
- the street receding steeply to the right, lined by tall buildings whose upper
  storeys run up and out of the top of the frame;
- a dark strip at the left edge;
- the dome's heavy ribs visible in the gap of sky above the far street, top right.
Ignore everything else in it: its buildings' designs and colours, its sign, door,
lamps, stairs and ground. The blacked-out area is not part of the composition.

Image 4 shows the scale of the city dome: heavy ribs sweeping in huge arcs, close
overhead.

COMPOSITION:
- The LEFT edge of the picture is inside a narrow, dark alley: a strip of deep
  shadow running straight back between the cantina's left side wall and the picture
  edge. No building on the alley's far side is visible. It is the darkest area.
- The Rusty Robot, large and close, fills the left-centre, its entrance and sign
  plainly visible.
- To its RIGHT the street recedes steeply. The buildings stand WALL TO WALL against
  the cantina and each other: one continuous frontage, no gaps, no other alleys.
  Brutalist concrete like the cantina, arched windows, faded painted colour bands —
  brick red, mustard, slate blue — a different colour on each. They are tall, their
  tops leaving the frame or stepping gently down in the distance.
- Kannan is PEDESTRIAN ONLY. Every ground-floor opening is a person-sized door —
  single or double, arched or square, up a step or two — or a small shop window. No
  garage doors, roller shutters or vehicle bays anywhere.

GROUND: smooth, matte, dry concrete paving slabs with straight joints — indoors. No
dirt, no rocks, no puddles, no reflections.

No street lamps. The cantina's entrance is the warmest, brightest light in the
picture; the rest of the street is cool night blue with a few lit windows.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
