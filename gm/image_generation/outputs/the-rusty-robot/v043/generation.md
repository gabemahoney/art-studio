# the-rusty-robot v043

User request verbatim: Thats good but we need to tuck them in even further. They alley should be narrower and they themselves closers to the Rusty Robots walls
Mode: Narrow the slot to ~1/8 frame width and move the group right against the cantina's side wall, deeper into shadow. Countable: nearest figure within a hand's breadth of the wall; the open band of shadow sits BEHIND them.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f60b-52cd-7b01-bc7d-5108aa3f3590/exec-98c3e41f-229b-4fbc-b125-e4763e45882f.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v042/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.02 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: pending — record with bin/review.py once you have seen it

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

## Note on the Forbidden list

Every item in the Style Block's "Forbidden" line names a **rendering tell**, not a
subject: smooth gradients, airbrush, photographic detail, fine linework,
micro-detail, more than three values, granular noise, polygon mosaics, the polished
modern AI look — and, in that same company, **"neon or rim lighting."**

So "neon" there forbids the *look*: saturated glow, bloom, halo, soft falloff, the
lit-from-within sheen of modern digital art. It does **not** forbid lit signage,
lamps, glowing instruments or electric light as subject matter. The world can have
neon in it; the painting must not be rendered like neon.

A lit sign is therefore fine when it is painted the way this style paints
everything else: flat opaque shapes with hard edges, a bright core and at most one
darker band of the same hue, no glow, no gradient, no rays. Recorded 2026-09-30
after the electric sign in `outputs/the-rusty-robot/`, where reading the ban as a
subject prohibition would have blocked a legitimate art direction.

This note sits outside the Style Block and changes none of its text, so it does not
require a style version bump.

Image 1 is STYLE: Match its hand-painted matte rendering only. Ignore its subjects.
Image 2 is EDIT TARGET: Reproduce this picture and change only what the spec names.

TASK: A single scene illustration: the exterior of the Rusty Robot cantina at night in the domed city of Kannan.

Reproduce image 2 and change TWO things about the alley at the left. Everything else
in the picture — the cantina's front, its sign, canopy, staircase, the street and the
city beyond — stays exactly as it is.

CHANGE ONE — THE ALLEY IS NARROWER.

In image 2 the gap between the cantina and the building to its left is too wide. Close
it up. The neighbouring building's corner moves RIGHT, toward the cantina, until the
visible gap between the two is about ONE EIGHTH of the picture's width — roughly half
as wide as it is now. It is a slot barely wider than the group standing in it.

The cantina's side wall still turns back and to the left from its front corner as a
receding trapezoid, and a short way past the crew the alley still falls to flat
darkness: no far wall, no back door, no receding floor, no lit surfaces deeper in,
no light at the far end.

CHANGE TWO — THE CREW PRESS UP AGAINST THE CANTINA'S WALL.

In image 2 the three of them stand out in the middle of the gap with space on both
sides. Move the whole group RIGHT, so they are tucked hard against the cantina's side
wall — the right-hand wall of the slot. Count the space:

- The figure nearest the cantina stands within a hand's breadth of that wall. Her
  shoulder and her raised arm are almost touching it.
- Behind the group, between their backs and the neighbouring building on the left,
  there is a clear band of empty shadow — the widest open space in the slot is
  BEHIND them, not in front of them.
- All three are deeper into the slot than they are now, further from the street, so
  more of each figure sits in shadow and less of them catches the warm doorway light.

They keep their same poses, their same faces, their same costumes, their same
relationship to one another and the same sizes — the woman with the ruby goggles and
cyber arm still turned toward the others and pointing toward the cantina, the tall
man in the wine-aubergine cape in the middle, the man in the white shirt with the red
cross patch at the left. Move the group; do not re-pose it and do not resize it.

Their boots stay in contact with the paving with a small soft shadow under each.

LIGHTING. They are now deeper in shadow than before, so they read DARKER, not
lighter. Only a thin warm rim from the cantina doorway catches their nearest edges.
Do not brighten them. The warm pool across the steps stays exactly as bright as it
is, the alley stays dark, and the cool blue dome light above is unchanged.

Everything else is unchanged: the sign with its lettering and robot emblem, the
canopy with its two matching stepped ends, the staircase with its two chamfered
piers and both handrails running the full length on three posts each, the swept
paving with no rocks or rubble, the street, the dome, the distant figures and the
lamps.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
