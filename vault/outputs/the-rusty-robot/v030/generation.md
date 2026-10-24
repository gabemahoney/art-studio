# the-rusty-robot v030

User request verbatim: Stairs are still not symmetrical. Nor is the overhang below the sign.
Mode: Path 3 again: v029 baseline. Enumerates the three stair-flank differences (pier caps, the extra right-hand block, bottom-step projection) and the two canopy-end differences (chamfer, bracket) individually rather than asking for symmetry in general.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f5ef-6dc9-7e13-9b6a-b6a692a000cb/exec-4cde82ae-44af-44eb-96a2-21136365c2fd.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v029/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.99 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
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

Reproduce image 2 exactly and change only the two pieces of architecture listed
below. Both are cases where the left and right of the same structure were built
differently; each must become one structure with two matching ends.

CHANGE ONE — THE TWO ENDS OF THE CANOPY OVER THE DOOR.

In image 2 the canopy's two ends are different shapes. Its LEFT end is sculpted: the
outer corner is cut back on a diagonal chamfer, and one stepped bracket sits
underneath it against the wall. Its RIGHT end is a plain blunt slab, cut straight
off, with no chamfer and no bracket.

Give the canopy TWO MATCHING ENDS, both built like its left end is now:
- The outer corner of EACH end is cut back on the same diagonal chamfer, at the same
  angle and the same depth as the other.
- EXACTLY ONE stepped bracket sits beneath EACH end, left and right, and the two
  brackets are the same size and the same shape.
- The canopy projects the same distance from the wall at both ends, and its front
  edge is one straight line from end to end.

CHANGE TWO — THE TWO FLANKS OF THE STAIRCASE.

Each flank already has one pier at the foot and one diagonal parapet above it. Keep
that. Three things differ between them and all three must match:

- CAPS. The RIGHT pier has a chamfered cap: a thin angled lip running round its top.
  The LEFT pier has a plain flat top with no lip. Give BOTH piers the same chamfered
  cap, the same thickness and the same angle.
- THE EXTRA BLOCK. Beyond the RIGHT pier, further from the steps and lower, there is
  an additional block stepping down toward the street. Nothing like it stands beyond
  the left pier. REMOVE IT. When you are done there is EXACTLY ONE pier on each side
  of the steps and NOTHING beyond either pier — no second block, no lower block, no
  stepped tier, no wedge.
- THE BOTTOM STEP. The lowest step projects further sideways past the right pier
  than it does past the left. Make it project the SAME distance past each pier, so
  the foot of the staircase is the same width on both sides.

Both flanks are then the same structure: one pier with a chamfered cap, one unbroken
diagonal parapet above it, and nothing else.

Because the camera stands to the left of the doorway, the left flank is nearer and
therefore larger in frame, and the two are seen at different angles. That is correct
perspective and must stay. They are the same structure seen from different
distances, not two shapes drawn at the same size.

LIGHTING IS UNCHANGED. Keep the warm pool of light from the doorway and its lamps
falling across the steps exactly as it is, the same brightness and the same falloff,
and keep the deep cool shadow in the alley at the left exactly as dark as it already
is. Do not brighten anything.

Everything else is unchanged: the sign, its lettering and its robot emblem, the
building faces and their colours, the three crew in the alley at their exact
positions, sizes, postures and depth of shadow, the street, the dome, the distant
figures and the lamps.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
