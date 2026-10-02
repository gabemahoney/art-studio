# the-rusty-robot v040

User request verbatim: Again I think the way v5 drew the alley was great. It angles off the side of the Rusty Robot correctly, they are tucked into it, and it does not take up a lot of the scene. You get a sense of there being an alley without showing anything else beyond it.
Mode: Back to v037's framing; alley respecified as v005's narrow dark slot. v005 attached as IDENTITY for alley shape only. Key constraint: nothing visible beyond the crew — depth implied by the angled side wall, not shown.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f607-b482-7992-ba16-06b28d0fa20a/exec-bf29168b-5669-4a78-93ad-eae60a4289ec.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v037/image.png
- Image 3 IDENTITY: outputs/the-rusty-robot/v005/image.png
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
Image 2 is EDIT TARGET: Reproduce this picture and change only the alley, as the spec says.
Image 3 is IDENTITY: An earlier version of this same scene. Use it ONLY for the alley's shape and depth. Ignore everything else in it.

TASK: A single scene illustration: the exterior of the Rusty Robot cantina at night in the domed city of Kannan.

Reproduce image 2 and rebuild ONLY the alley at the left, following image 3's
treatment of it. The cantina's front, its sign, canopy, staircase, and the street and
city beyond stay exactly as image 2 has them.

WHAT IS WRONG IN IMAGE 2. The alley is too open and takes too much of the picture. It
is painted as a corridor you can see down, with its own floor and walls competing
with the cantina for attention.

WHAT IMAGE 3 DOES RIGHT, AND WHAT TO COPY. In image 3 the alley is a NARROW DARK
SLOT. You are given the idea of an alley without being shown one. Copy exactly that:

- **It is narrow.** The gap takes up only a small part of the frame's width — about
  one fifth — and the cantina keeps the rest. It is a slot between two buildings,
  not a street.
- **The cantina's side wall angles back into it.** From the crisp vertical corner
  where the cantina's front facade ends, its side wall turns and runs BACK AND TO
  THE LEFT, away from the camera. It is a receding plane: a tall narrow trapezoid,
  tallest at the near corner and shrinking as it goes back, its top edge sloping
  down to the left and its base sloping up to the left. This angled wall is what
  tells the viewer the alley has depth.
- **Nothing is visible beyond the crew.** A short way past them the alley falls to
  flat darkness and stops. Paint NO far wall, NO back door, NO receding floor
  running into the distance, NO lit surfaces deeper in, NO second buildings, NO sky
  and NO light at the far end. The depth is implied by the angled wall and by the
  figures standing in shadow — not by showing what is back there.
- **The crew are tucked into the slot**, standing in its mouth in shadow, their
  backs to the darkness, lit only by the warm spill from the cantina doorway. Keep
  their exact positions, sizes, poses, faces and costumes from image 2, with their
  boots on the paving and a small soft shadow under each.
- **At the far left edge of the frame**, the neighbouring building presents a simple
  upright corner, catching a little light on its street-facing side. It frames the
  shot and closes the composition on that side.

IGNORE EVERYTHING ELSE ABOUT IMAGE 3: its sign, its building colours, its canopy, its
staircase, the loose rock and rubble on its ground, and its overall lighting. It is
here for the shape and depth of the alley alone.

The ground stays as image 2 has it — swept paving, no rocks, no rubble, no gravel.

LIGHTING IS UNCHANGED: the warm pool across the steps at its present brightness, the
crew as dark as they are now, the cool blue dome light above. Do not brighten
anything.

Everything else is unchanged: the sign with its lettering and robot emblem, the
canopy with its two matching stepped ends, the staircase with its two chamfered
piers and both handrails running the full length on three posts each, the street, the
dome, the distant figures and the lamps.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
