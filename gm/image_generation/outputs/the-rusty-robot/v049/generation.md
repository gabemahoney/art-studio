# the-rusty-robot v049

User request verbatim: The handrails are still assymettrical in v48. And the leftside handrail seems to be in the MIDDLE of the stairs case instead of the side.
Mode: Left handrail relocated onto the top of the left parapet to mirror the right, posts on the parapet not the treads, lowest post on the left pier. Diagnosed as a placement fault, not a length fault.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f8b7-474e-7461-83d4-3affeb6e60fd/exec-67557766-febd-4680-802d-76131ac02976.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v048/image.png
Date: 2026-10-01
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.00 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
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

Reproduce image 2 and move ONE thing: the left-hand handrail. Everything else in the
picture stays exactly as it is — the sign, the canopy, the steps, the two piers, the
three crew in the alley, the street, the dome and the city beyond.

THE FAULT. The two handrails are not built the same way.

The RIGHT handrail is correct: it runs directly along the TOP OF THE RIGHT PARAPET —
the sloping side wall of the staircase — with its posts standing on that parapet, and
its lowest post landing on the right pier at the foot of the flight.

The LEFT handrail is wrong. It stands out over the STEPS, set well in from the left
side of the staircase, and its posts come down onto the step treads themselves. It
reads as a rail stranded in the middle of the flight with open steps on both sides of
it.

THE FIX. Move the left handrail sideways, to the left, until it mirrors the right
one exactly:

- It runs directly along the TOP OF THE LEFT PARAPET, following the same slope as
  that parapet, hard against the left edge of the staircase.
- Its posts stand ON the parapet, not on the treads. NO post touches a step.
- Its lowest post lands on the LEFT PIER at the foot of the flight — the block with
  the chamfered cap — exactly as the right rail's lowest post lands on the right pier.
- It is carried by THREE posts, like the right rail, and the two rails start and
  finish at the same heights as each other.

When you are done, the steps are completely clear between the two rails: an unbroken
run of treads from the left parapet to the right parapet with nothing standing on
them. The two rails sit one on each outer edge of the staircase, mirroring each
other, and the staircase reads the same on both sides.

Because the camera stands to the left of the doorway, the left rail is nearer and
reads larger and at a different angle. That is correct perspective and must stay.

LIGHTING IS UNCHANGED: the warm pool across the steps at exactly its present
brightness, the alley at the left as dark as it is now, the three crew in shadow, the
cool blue dome light above. Do not brighten anything.

Everything else is unchanged: the sign with its lettering and robot emblem, the
canopy with its two matching stepped ends and its two downlights, both piers and
their chamfered caps, the number and shape of the steps, the swept paving with no
rocks or rubble, the crew at their exact positions, sizes, postures and depth of
shadow, the street, the dome, the distant figures and the lamps.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
