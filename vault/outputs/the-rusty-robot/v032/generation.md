# the-rusty-robot v032

User request verbatim: The hand rails should go all the way down the stairs. The overhang is still assymetrical. Also, the edge of the alleyway has now merged with the side of the staircase.
Mode: Path 3: v031 baseline. Handrails full length with 3 posts each; right canopy end rebuilt as a copy of the left's stepped block; restore the tonal separation between the left pier and the alley wall that v030 merged.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f5f5-9bcc-72b0-927f-ae039cc15a4e/exec-34e95fd9-5ad4-4a3e-b914-c0a3335ae4ed.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v031/image.png
Date: 2026-09-30
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
Image 2 is EDIT TARGET: Reproduce this picture and change only what the spec lists.

TASK: A single scene illustration: the exterior of the Rusty Robot cantina at night in the domed city of Kannan.

Reproduce image 2 exactly and change only the three things listed below.

CHANGE ONE — THE HANDRAILS MUST REACH THE BOTTOM STEP.

In image 2 each handrail stops partway down the staircase: it descends from the
doorway, ends at a short post that lands on top of the pier, and the lowest steps
have no rail beside them at all.

Extend BOTH handrails so each one runs the WHOLE length of the stairs. Each rail
starts at the landing by the door and descends in ONE unbroken straight line,
parallel to the slope of the steps, all the way to the LOWEST step, where it ends in
a short vertical post standing on that bottom step. Count the posts: each rail is
carried by THREE evenly spaced vertical posts — one near the top, one at the middle,
one at the bottom end. The two rails are the same length as each other and end at the
same step. No rail stops early, and no rail ends in mid-air.

CHANGE TWO — THE TWO ENDS OF THE CANOPY STILL DO NOT MATCH.

The canopy over the door ends differently at each side. Its LEFT end is a blunt
stepped block: the profile steps back twice in short square tiers and stops. Its
RIGHT end instead tapers away in one long thin diagonal wedge that reaches much
further out and comes to a narrow point.

Rebuild the RIGHT end as a copy of the LEFT end: a blunt stepped block whose profile
steps back twice in short square tiers and then stops. The right end must NOT taper,
must NOT come to a point, and must NOT reach further from the doorway than the left
end does. Measure them against the doorway: each end stops the same distance out from
the centre of the door, so the canopy is the same length on both sides.

CHANGE THREE — SEPARATE THE STAIRCASE FROM THE ALLEY WALL.

In image 2 the staircase's left pier and the wall of the alley behind it have merged
into one continuous pale grey mass with no boundary between them; they read as a
single slab.

Put the edge back. The pier is a separate block standing clear IN FRONT of the alley
wall, and there is ONE crisp vertical edge where the pier's side ends and the wall
behind begins. Mark that edge by value, not by outline: the alley wall behind stays
in deep cool shadow, clearly darker than the lit face of the pier, so the two planes
read as separate objects at different depths. A narrow band of shadow falls on the
wall immediately behind the pier. Do not draw a line — let the change in tone do it.

LIGHTING IS OTHERWISE UNCHANGED. Keep the warm pool of light from the doorway and
its lamps across the steps exactly as it is, the same brightness and the same
falloff, and keep the alley at the left as dark as it already is. Do not brighten
anything.

Everything else is unchanged: the sign, its lettering and its robot emblem, the
building faces and their colours, the three crew in the alley at their exact
positions, sizes, postures and depth of shadow, the piers and their chamfered caps,
the diagonal parapets, the street, the dome, the distant figures and the lamps.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
