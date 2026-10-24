# the-rusty-robot v038

User request verbatim: Perspective is wrong on the side of the Rusty Robot and the alley though. Shouldnnt it go at an angle like this?
Mode: Alley given its own vanishing point, low and to the left, opposite the street's. Both alley walls specified as trapezoids with converging top/bottom edges; floor joints fanning. Rule: nothing inside the alley is horizontal.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f603-9d6b-7720-ba84-81e21ad0622d/exec-c05624c8-3219-462c-9ca6-b9e027efcc30.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v037/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.05 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
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

Reproduce image 2 and fix ONE thing: the alley on the left has no perspective. The
right two thirds of the picture — the cantina's front, its sign, canopy, staircase,
and the street and city beyond — stay exactly as they are.

THE FAULT. The surfaces inside the alley are painted as flat upright bands parallel
to the picture plane. Their top and bottom edges run horizontally, so nothing
converges and the alley has no depth: it reads as a painted backdrop standing behind
the three crew rather than as a corridor going back into the block.

THE FIX — GIVE THE ALLEY ITS OWN VANISHING POINT. The street recedes to the RIGHT,
toward the distant archway. The alley is a corridor running the other way: it leads
back and to the LEFT, away from the camera, and every surface inside it converges
toward a second vanishing point deep inside it, low and to the left.

Build it from three receding planes, and let the convergence be clearly visible:

1. THE CANTINA'S SIDE WALL — the right-hand wall of the alley. The cantina's front
   facade turns a crisp vertical corner, and from that corner this wall runs BACK
   AND TO THE LEFT. It is a tall narrow TRAPEZOID, not a rectangle: it is TALLEST at
   the near corner, closest to the viewer, and it shrinks as it goes left and away.
   Its top edge slopes DOWNWARD to the left. Its bottom edge slopes UPWARD to the
   left. The two edges visibly tilt toward each other.
2. THE OPPOSITE WALL — the neighbouring building's flank, the left-hand wall of the
   alley, parallel to the first and converging to the same point. Its top edge also
   slopes down to the left and its bottom edge up to the left.
3. THE ALLEY FLOOR between them, continuous with the street paving. Its paving
   joints run back toward that same vanishing point, so they fan: the gap between
   them is widest at the front, near the viewer, and narrows going back. This is the
   clearest signal of depth in the shot and must read at a glance.

Every horizontal edge inside the alley — wall tops, wall bases, ledges, door heads,
pipe runs, paving joints — slopes. NOTHING inside the alley is horizontal. If an
edge in there runs flat across the picture, it is wrong.

The alley also narrows as it goes back, because its two walls converge.

THE CREW ARE UNCHANGED, and they stand on that floor near the alley mouth, close to
the viewer: same positions, same sizes, same poses, same faces, same costumes, boots
in contact with the paving, a small soft shadow under each. Keep them in shadow,
exactly as dark as they are now, lit only by the warm spill from the doorway. Do not
brighten them and do not move them.

LIGHTING IS UNCHANGED everywhere: the warm pool across the steps at its present
brightness, the alley dark and falling off toward its back, the cool blue dome light
above.

Everything else is unchanged: the sign with its lettering and robot emblem, the
canopy with its two matching stepped ends, the staircase with its two chamfered
piers and both handrails running the full length on three posts each, the street,
the dome, the distant figures and the lamps.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
