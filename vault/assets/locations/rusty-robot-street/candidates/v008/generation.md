# rusty-robot-street v008

User request verbatim: I think we need to do fresh ones from a new prompt rather than mask and edit.
Mode: FRESH, no candidate attached: everything settled so far in one prompt (alley left edge, wall-to-wall moderate heights, heavy dome, no lamps, matte paving, sign per reference). Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a103ef-fadf-7b30-8193-337fcff45424/exec-a6285eb6-1e56-4bcf-a312-95b69f8ee157.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/locations/the-rusty-robot/reference.png; frozen assets/locations/the-rusty-robot/candidates/v023/image.png
- Image 3 IDENTITY: assets/locations/rusty-robot-street/sources/dome-from-scene-v005.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.23 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: FRESH roll 2. Same strengths as v007; a strip of a far-side building shows at the left edge; garage-style doors on the right.

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

SUBJECT DESIGN (description v5, restated so nothing is invented):
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

Image 3 shows the scale of the city dome: copy its heavy ribs sweeping in huge arcs
across the whole sky, close overhead, and the domed towers beyond. Ignore its
foreground.

VIEW: standing in the street at eye height, looking at the Rusty Robot from in front
and slightly to its left, matching the reference sheet's three-quarter view.

COMPOSITION, left to right:
- The LEFT fifth of the picture is a narrow, dark alley running straight back into the
  block. The picture's left edge cuts through the alley, so no building on the alley's
  far side is visible. The Rusty Robot's left side wall forms the alley's right side:
  one flat wall running straight back, in deep cool shadow, far darker than the lit
  front. The alley floor is the street paving, fading to near black a few metres in.
  It is the darkest area of the picture.
- The Rusty Robot fills the centre, its entrance and sign plainly visible.
- To its RIGHT the street recedes. The buildings stand WALL TO WALL against the cantina
  and each other: one continuous frontage, no gaps, no other alleys. Brutalist concrete
  like the cantina, arched windows, faded painted colour bands — brick red, mustard,
  slate blue, teal — a different colour on each. Heights three to five storeys, each
  differing from its neighbour by about one storey; plain flat parapets; no towers.
  A few windows lit warm amber.

GROUND: smooth, matte, dry concrete paving slabs with straight joints — indoors. No
dirt, no rocks, no puddles, no reflections.

No street lamps anywhere. The cantina's entrance is the warmest, brightest light in the
picture; the rest of the street is cool night blue.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
