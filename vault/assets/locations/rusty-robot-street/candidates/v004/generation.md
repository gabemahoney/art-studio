# rusty-robot-street v004

User request verbatim: also remove the streetlamps. They dont look sci fi
Mode: Edit off v003: streetlamps removed; alley mouth opened across the left fifth; cantina's left side wall straightened and shadowed.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a103e7-c9c8-7b40-8e21-6a7f3971825e/exec-b07a6b8d-68e3-4666-b902-1147fcd45447.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: assets/locations/rusty-robot-street/candidates/v003/image.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.08 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: LANDED: both streetlamps gone; cantina's left side wall now straight, receding in shadow; no far alley wall visible; neighbour heights and heavy dome ribs held from v003. MISS: with no far wall the left side reads as the cantina's flank on an open space rather than a narrow alley; alley floor at bottom-left is small.

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
Image 2 is EDIT TARGET: The street view being revised. Preserve everything the spec does not change.

TASK: Revise this establishing illustration of the Rusty Robot's street inside the domed city of Kannan, at night.

SUBJECT DESIGN (description v4, restated so nothing is invented):
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
  buildings with strongly varied heights: a two-storey block beside a six-storey one,
  a low one, then a tall tower with a stepped top — no two neighbours the same height.
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

Reproduce image 2 and change THREE things. Keep everything else exactly as it is: the
Rusty Robot, the buildings to its right and their heights, the dome's ribs, the
skyline, the paving, the painting style and the night palette.

FIRST: REMOVE BOTH STREET LAMPS. The two curved-arm lamp posts on the pavement to the
right of the cantina are gone, and so are the pools of light they cast. Plain wall
and paving where they stood.

SECOND: OPEN UP THE ALLEY. The left fifth of the picture is the alley mouth: its dark
paved floor running from the bottom-left corner straight back into darkness, wide
enough for three people to stand side by side. The picture's left edge cuts through
the alley, so no wall on the alley's far side is visible. The Rusty Robot's left side
wall forms the alley's right side.

THIRD: STRAIGHTEN THE CANTINA'S LEFT SIDE WALL. It is one flat vertical wall running
STRAIGHT back from the cantina's front-left corner into the alley, its top edge and
base both straight lines receding toward the same vanishing point as the rest of the
building — not curved or bowed. It is in deep cool shadow, far darker than the
cantina's lit front, with a few small dark arched windows.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
