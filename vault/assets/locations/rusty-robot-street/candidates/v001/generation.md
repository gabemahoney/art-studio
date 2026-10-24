# rusty-robot-street v001

User request verbatim: lets make a reference image of it situatied in the city itself. I liked the dome of the city visible in the skybox from the last images. Also, the buildings should be a similar style. The road should not be dirt with rocks, its inside. Also, there is a required dark alley to the left of the Rusty Robot.
Mode: New asset v1: fresh establishing view from the approved Rusty Robot reference and the v082 dome crop.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a103d9-7fe9-7f53-a7bf-070e48f9cfa5/exec-b711d5f3-1813-47f7-ae4e-1ce5c5208897.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/locations/the-rusty-robot/reference.png; frozen assets/locations/the-rusty-robot/candidates/v023/image.png
- Image 3 IDENTITY: assets/locations/rusty-robot-street/sources/dome-skyline-from-scene-v082.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.21 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: LANDED: the Rusty Robot as its reference (three storeys, teal bands, fins, tilted sign canopy with emblem, arched steel door, centred steps and rails, lamp pair); dark alley immediately left of it, open mouth, darkest area; neighbours in the same brutalist language with red, mustard and teal bands, varied heights; dome ribs across the sky and domed towers beyond; smooth concrete slab paving, no dirt or rocks. MISSES: paving has a glossy reflective sheen that reads slightly wet; the cantina's left side wall and the alley's far wall are hard to tell apart.

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
Image 3 is IDENTITY: The city dome and skyline. Copy the dome and distant towers only.

TASK: A single establishing illustration: the Rusty Robot cantina on its street inside the domed city of Kannan, at night.

SUBJECT DESIGN (description v1, restated so nothing is invented):
The street outside the Rusty Robot cantina, inside the domed city of Kannan, at night.
The establishing setting for scenes at the cantina.

Design sources:
- `assets/locations/the-rusty-robot/reference.png` — the cantina itself (approved).
- `sources/dome-skyline-from-scene-v082.png` — the city dome and skyline.

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
- **The street** runs past the cantina's front. Neighbouring buildings line it on both
  sides, receding into the distance.

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
  structural ribs crossing overhead against deep night blue.
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

Image 3 shows the city's dome and skyline: copy the dome — the vast lattice of heavy
curved ribs overhead against night blue — and the domed towers beyond. Ignore its
buildings in the foreground.

VIEW: standing in the street at eye height, looking at the Rusty Robot from in front
and slightly to its left, as in the reference sheet's three-quarter view. The cantina
fills the centre-right of the picture, its entrance and sign plainly visible.

IMMEDIATELY LEFT of the cantina, a narrow dark alley runs straight back into the block
between the cantina's left side wall and the next building. Its mouth is in the left
third of the picture, open and unobstructed, its floor the same paving as the street,
fading into darkness within a few metres. It is the darkest area of the picture.

The street runs across the foreground and recedes to the right, lined with brutalist
concrete buildings in the same style as the cantina, each with faded painted colour
bands of a different colour, varied in height and roofline. Above them the dome's
ribs cross the night sky. The street surface is smooth, dry concrete paving slabs with
straight joints — indoors, no dirt, no rocks.

The cantina's entrance is the warmest, brightest light in the picture.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
