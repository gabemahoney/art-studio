# the-rusty-robot v034

User request verbatim: The side of the alley still blends with the stair case. Thats impossible geometry
Mode: Path 3: v033 baseline. Give the staircase a visible side face so it reads as a solid block in front of the alley wall. Counted as three vertical planes by value, darkest-to-lightest, with one crisp vertical corner edge.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f5fa-849e-7f13-be97-7381c6c893da/exec-7887ee70-46fb-4c14-91df-d12fa519f6d3.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v033/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.95 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
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

Reproduce image 2 exactly and change ONE area: the left-hand side of the staircase,
where it meets the alley. Everything else in the picture stays as it is.

THE FAULT. In image 2 the staircase has no thickness on that side. Its diagonal
parapet runs down to the left and simply stops in mid-air, and the whole pale surface
underneath it continues unbroken into the wall of the alley, so one flat plane is
doing duty as both the side of the staircase and the wall of a building. There is no
corner anywhere. It is impossible geometry.

THE FIX. The staircase is a solid block of masonry sitting on the street IN FRONT OF
the alley. Build it so its left side reads as solid. Count the vertical planes, and
paint each one a different value, going from left to right across that area:

1. THE ALLEY WALL, furthest back and DARKEST. A tall flat wall in deep cool
   blue-grey shadow, running back into the alley where the three figures stand. It
   is the darkest large surface in this part of the picture.
2. THE SIDE FACE OF THE STAIRCASE, in front of the wall and ONE CLEAR STEP LIGHTER
   than it. This is the new part: a tall vertical face of masonry, turned away from
   the doorway lamps and therefore in shadow, but plainly lighter than the alley
   wall behind it. It is the side of a solid block, and it is what gives the
   staircase its thickness.
3. THE TOP OF THE PARAPET, LIGHTEST. The sloping band already in image 2, catching
   the warm light from the doorway.

Between plane 1 and plane 2 there must be ONE crisp, unmistakable VERTICAL EDGE
running from the ground up to where the parapet begins. That edge is the corner of
the staircase. The viewer must be able to tell exactly where the staircase stops and
the alley begins.

The diagonal parapet does NOT continue into the alley wall. It ends at the top of
the staircase's own side face, and below that line you see the side face, not more
parapet.

Where the staircase meets the street, it casts a soft shadow onto the paving to its
left, which also helps it read as standing clear of the wall.

Keep the pier with its chamfered cap exactly where it is at the foot of that side,
standing proud of the side face.

The alley stays as dark as it already is — do not light it up to show this. The
separation is made by the three values and the vertical edge, not by brightening
anything, and not by drawing an outline.

EVERYTHING ELSE IS UNCHANGED: both handrails running the full length of the stairs on
three posts each; both canopy ends as matching stepped blocks; both piers and their
chamfered caps; the steps; the sign, its lettering and its robot emblem; the three
crew at their exact positions, sizes, postures and depth of shadow; the building
faces and their colours; the street; the dome; the distant figures; the lamps; and
the warm pool of light across the steps at exactly its present brightness.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
