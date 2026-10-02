# the-rusty-robot v036

User request verbatim: The geometry is still bizarre. Sion is standing in front of a shadow that somehow becomes a wall at her feet. The whole alley needs a redo.
Mode: Full alley rebuild, not a patch. Accumulated compositing left the crew (v005), their surroundings (v027 lineage) and the adjacent architecture (v034) describing different spaces. Alley respecified as floor + two walls + depth, every dark area a surface with an orientation, crew repainted so their ground contact is coherent.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f5ff-afa9-7e90-a636-5d681e3457bd/exec-c681108a-5851-48b7-81cd-f99c86ec304c.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v035/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.11 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
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
Image 2 is EDIT TARGET: Reproduce this picture and rebuild only the area the spec names.

TASK: A single scene illustration: the exterior of the Rusty Robot cantina at night in the domed city of Kannan.

Reproduce image 2 and REBUILD THE ALLEY on the left-hand third of the picture. The
right two thirds — the cantina front, its sign, its canopy, its staircase and the
street and city beyond — stay exactly as they are.

THE FAULT. The alley is not currently a place. It is a flat dark shape with people
standing against it. The dark area behind the three crew has no floor, no walls you
can orient, and no depth; at the woman's boots it simply stops at a hard vertical
line and the lit street begins, so the darkness reads as a wall rising out of the
ground in front of her rather than as space she is standing in.

REBUILD IT AS A REAL SPACE. The alley is a narrow gap between two buildings, running
straight back from the street, away from the viewer. Build it from these surfaces,
and give EVERY ONE of them a clear orientation. There are no flat dark shapes in this
picture: every dark area is a surface turned away from the light.

1. THE FLOOR. The same paving as the street continues without a break into the
   alley and runs back into it. You can see the ground the whole way: it is brightest
   where it meets the lit street, and falls off gradually into shadow deeper in. The
   paving lines run back toward the vanishing point, which is what makes the alley
   read as deep. There is NO hard vertical line where the alley floor meets the
   street — the two are one continuous surface, and the light simply fades across it.
2. THE LEFT WALL — the neighbouring building. A tall flat face running back in
   perspective, its top and bottom edges converging toward the vanishing point. In
   cool blue-grey shadow, but still a lit surface, not a void: you can read its
   masonry and a faint vertical seam or two.
3. THE RIGHT WALL — the cantina's own side wall, meeting its front face at a crisp
   vertical corner, running back parallel to the left wall.
4. THE BACK. Deeper in, the alley fades into the darkest part of the picture.

THE THREE CREW STAND ON THE FLOOR, a little way inside the alley mouth. Each one's
boots make contact with the paving, and each casts a small soft shadow on the
ground at their feet. They are standing in a space with room behind them, not
pressed flat against a backdrop. Keep their exact positions, their sizes, their
poses, their faces and their costumes as they are in image 2 — the man in the white
shirt with the red cross patch at the left, the tall man in the wine-aubergine cape
in the middle, the woman with the ruby goggles, teal scarf, ochre vest and steel
cyber arm at the right, pointing toward the cantina.

THE CREW STAY IN SHADOW. They are lit only by the spill of warm light reaching into
the alley mouth from the cantina doorway, so they read as dark figures with warm
edges, clearly darker than the lit steps and paving outside. Do not brighten them to
show them off — their being in shadow is the point of the shot.

RENDERING. Paint them with the same crisp flat angular facets as the rest of the
picture: decisive opaque shapes with clean edges, not soft blended shading. Faces,
jackets and boots are each built from a few flat planes.

Everything else is unchanged: the sign and its lettering and robot emblem, the
canopy with its two matching stepped ends, the staircase with its two chamfered
piers and the handrails running the full length on three posts each, the warm pool
of light across the steps at exactly its present brightness, the street, the dome,
the distant figures and the lamps.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
