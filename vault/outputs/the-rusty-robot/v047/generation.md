# the-rusty-robot v047

User request verbatim: 1. The handrails are not symmetrical. Both should go down to the last step. 3. Th overhang under the sign also has a ghost section and is not semmetrical
Mode: Left handrail extended to the bottom step (3 posts each, both ending at the same step); right canopy end rebuilt as a mirror of the left's blocky stepped form instead of a long diagonal taper.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f88a-aa73-76a1-85f6-c84c6255fd49/exec-819f7097-86db-44ee-a912-7d5147bc65c3.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v046/image.png
Date: 2026-10-01
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

Reproduce image 2 and correct TWO pieces of architecture. Everything else — the
sign, the three crew in the alley at the left, the alley itself, the street, the
dome and the city beyond — stays exactly as it is.

CHANGE ONE — BOTH HANDRAILS MUST REACH THE BOTTOM STEP.

In image 2 the two handrails are different lengths. The RIGHT rail descends the full
flight and ends in a post standing on the lowest step. The LEFT rail stops about
three steps short of the bottom: it ends in mid-air above a post that lands partway
up the staircase, leaving the lowest steps with no rail beside them.

Extend the LEFT rail down so that both rails are the same. Each rail runs in ONE
unbroken straight line, parallel to the slope of the steps, from the landing at the
doorway all the way down to the LOWEST step, where it ends in a short vertical post
standing on that bottom step. Each rail is carried by THREE vertical posts — one
near the top, one at the middle, one at the bottom end. Both rails end at the same
step and project the same distance beyond the lowest tread. Neither rail stops early
and neither ends in mid-air.

CHANGE TWO — THE TWO ENDS OF THE CANOPY MUST MATCH.

The canopy over the door ends differently on each side. Its LEFT end is a blocky
stepped form: the profile steps outward and downward in short square tiers and
stops, with the downlight set beneath it in a square recess. Its RIGHT end instead
runs out along a LONG DIAGONAL underside that tapers away and reaches further from
the doorway than the left end does.

Rebuild the RIGHT end as a mirror of the LEFT end: the same blocky stepped profile,
stepping outward and downward in short square tiers and stopping, with its downlight
set beneath it in the same square recess. The right end must NOT taper along a long
diagonal and must NOT reach further from the centre of the door than the left end
does. Measure them against the doorway: both ends stop the same distance out, so the
canopy is the same length on each side, and its front edge is one straight line from
end to end.

Because the camera stands to the left of the doorway, the left end is nearer and
reads larger. That is correct perspective and must stay — the two ends are the same
form seen from different distances, not two shapes drawn at the same size.

LIGHTING IS UNCHANGED: the warm pool across the steps at exactly its present
brightness, the alley at the left as dark as it is now, the crew in shadow, the cool
blue dome light above. Do not brighten anything.

Everything else is unchanged: the sign with its lettering and robot emblem, the two
wall downlights, the staircase's two piers with their chamfered caps, the steps, the
swept paving with no rocks or rubble, the three crew at their exact positions, sizes,
postures and depth of shadow, the street, the dome, the distant figures and the lamps.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
