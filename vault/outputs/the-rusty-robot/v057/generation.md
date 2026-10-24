# the-rusty-robot v057

User request verbatim: and can you now make the top corners of the overhang (above the door, below the sign) symmetrical?
Mode: Canopy TOP corners: left steps down in two square tiers cutting a notch, right is a plain blunt corner. Right rebuilt to match — exactly two square tiers at each end, same depth and height, no diagonals or chamfers. Canopy's ends, depth, vents and lights frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f8ce-e9c8-7e71-bcb6-b8f984056ba1/exec-032dbc0a-345d-4b8f-aaa6-308a105c5e4f.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v056/image.png
Date: 2026-10-01
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.98 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
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

Reproduce image 2 and change ONE thing: the TOP corners of the canopy over the door —
the deep horizontal slab that sits above the doorway and below the sign. Everything
else in the picture stays exactly as it is.

THE FAULT. The canopy's top edge is finished differently at its two ends, where it
meets the building's wall.

At the LEFT end, the top of the canopy STEPS DOWN toward the wall in square tiers,
cutting a notch into its top corner, so the silhouette there is a little staircase of
square shoulders.

At the RIGHT end there is no such notch. The top simply runs out to a plain blunt
corner with a block sitting against the wall, and the stepped shoulders are missing
altogether.

THE FIX. Give the canopy TWO MATCHING TOP CORNERS, both built the way the left one is
now. Count the steps:

- EACH top corner steps down toward the wall in exactly TWO square tiers, the same
  two tiers at each end, before the canopy meets the wall.
- The two tiers are the same depth and the same height as each other at both ends,
  so the notch cut into the right top corner is the same shape as the notch at the
  left.
- Each corner's steps are square: horizontal tops and vertical faces, no diagonals,
  no chamfers and no curves anywhere in them.
- At both ends the canopy's top edge arrives at the wall at the same height above
  the doorway.

When you are done, the canopy's silhouette is a mirror of itself about the centre of
the door: two matching stepped shoulders at the top, and the two matching stepped
ends underneath that it already has.

Because the camera stands to the left of the doorway, the left corner is nearer and
reads larger, and the two are seen at different angles. That is correct perspective
and must stay — they are the same form seen from different distances, not two shapes
drawn at the same size.

CHANGE NOTHING ELSE ABOUT THE CANOPY: its depth, how far it projects from the wall,
the louvred vents along its face, its bolt heads, the orange trim line, its two
downlights underneath, and the two stepped ends at its left and right extremities all
stay exactly as they are.

LIGHTING IS UNCHANGED: the warm pool of light across the steps at exactly its present
brightness, the alley at the left as dark as it is now, the three crew in shadow, the
cool blue dome light above. Do not brighten anything.

Everything else is unchanged: the sign with its lettering and robot emblem, the
taller round-arched door, the shallow grimy steps, both parapets and piers, no
handrails anywhere, the three crew at their exact positions, sizes, postures and
depth of shadow, the swept paving, the street, the dome, the distant figures and the
lamps.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
