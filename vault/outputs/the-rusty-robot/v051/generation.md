# the-rusty-robot v051

User request verbatim: The rightside handrail is correct. It sits in the steps but directly on the side. The left hadnrail is wrong. It sits up high on the parapet where it could not be reached.
Mode: CORRECTING MY OWN EARLIER INSTRUCTION: v049 moved the left rail ONTO the parapet, which was backwards. The right rail stands on the treads at hand height; the left must come DOWN off the parapet crest onto the treads to match. Right rail explicitly frozen as the referent.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f8c0-148d-7322-aaca-653ca831bf33/exec-77e7aaab-c461-4ce8-9009-7c03624b2cdb.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v050/image.png
Date: 2026-10-01
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.96 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
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

Reproduce image 2 and move ONE thing: the LEFT handrail. Everything else in the
picture stays exactly as it is.

THE RIGHT HANDRAIL IS CORRECT. DO NOT CHANGE IT. Look at how it is built, because the
left one must match it: its posts stand ON THE STEP TREADS, close to the right edge
of the flight, and the rail itself runs at HAND HEIGHT above the steps — about the
height of a person's hip to waist, low enough that somebody climbing the stairs could
put a hand on it.

THE LEFT HANDRAIL IS WRONG. It has been mounted on TOP OF THE LEFT PARAPET — the
sloping side wall of the staircase. It runs along the crest of that wall, far above
the steps, well over head height for anyone on the flight. Nobody climbing the stairs
could reach it. It is a rail on a wall, not a rail on a staircase.

THE FIX. Take the left handrail DOWN off the parapet and stand it on the steps:

- Its posts come down onto the STEP TREADS, close to the LEFT EDGE of the flight,
  just inside the parapet — the mirror of where the right rail's posts stand.
- The rail runs at the SAME HEIGHT ABOVE THE TREADS as the right rail does. Compare
  them directly: if you sight along the steps, the two rails are at the same height
  above the stone, one at each side of the flight.
- THREE posts carry it, standing on the treads, descending with the steps.
- It is a hand's reach above the steps, not above the wall.

When you are done, both rails are at the same height above the same steps, one near
each edge of the flight, and a person standing on any step could reach either of
them. The left parapet still runs up the side of the staircase, but the rail no
longer sits on its crest — the parapet's top is bare stone.

Because the camera stands to the left of the doorway, the left rail is nearer and
reads larger. That is correct perspective and must stay.

LIGHTING IS UNCHANGED: the warm pool across the steps at exactly its present
brightness, the alley at the left as dark as it is now, the three crew in shadow, the
cool blue dome light above. Do not brighten anything.

Everything else is unchanged: the RIGHT handrail exactly as it is, the sign with its
lettering and robot emblem, the canopy with its two stepped ends and its two
downlights, both piers and their chamfered caps, the number and shape of the steps,
the swept paving with no rocks or rubble, the three crew at their exact positions,
sizes, postures and depth of shadow, the street, the dome, the distant figures and
the lamps.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
