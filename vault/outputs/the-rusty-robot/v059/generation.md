# the-rusty-robot v059

User request verbatim: There is still assymetry and cruft around the overhang that sits above the steps and below the sign.
Mode: Mirrored the two canopy ends to compare: left is TWO large square tiers, right is four-plus small tiers with extra nibs and ledges. Left frozen as the referent; right rebuilt to exactly two tiers with all small fragments deleted and the surface behind them repainted.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f8f5-6248-7ce1-9ce8-e48b1cf4504a/exec-aa83e98a-4e87-4d76-b80b-be7b0768f117.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v058/image.png
Date: 2026-10-01
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
Image 2 is EDIT TARGET: Reproduce this picture and change only what the spec names.

TASK: A single scene illustration: the exterior of the Rusty Robot cantina at night in the domed city of Kannan.

Reproduce image 2 and rebuild ONE thing: the RIGHT-HAND END of the canopy — the deep
slab above the door and below the sign. Everything else stays exactly as it is.

THE LEFT END IS CORRECT. DO NOT CHANGE IT. Look at how it is built, because the right
end must be made to match it. The left end is simple and bold: the slab finishes in
exactly TWO large square tiers, one stepping back and down from the other, and then
it stops against the wall. Two steps, both big, both plain. Beneath that corner sits
one downlight in a plain square recess. Nothing else projects from it.

THE RIGHT END IS CLUTTERED AND MUST BE SIMPLIFIED. In image 2 its profile is broken
into FOUR OR MORE small tiers instead of two large ones, and several extra pieces
stick out of it: small blocks, short nibs and narrow ledges projecting from the
corner and from the wall beside it. The silhouette there is a jagged little
staircase of odd fragments.

REBUILD THE RIGHT END AS A MIRROR OF THE LEFT. Count it:

- EXACTLY TWO tiers, not three, not four, not five. Both large, the same size as the
  left end's two tiers, one stepping back and down from the other, then stopping
  against the wall.
- Each tier is plainly square: a horizontal top and a vertical face. No diagonals,
  no chamfers, no curves.
- DELETE every extra piece: no small blocks, no nibs, no narrow ledges, no stubs, no
  fragments projecting from the corner or from the wall beside it. If a shape is
  smaller than one of the two tiers, it should not be there.
- Beneath the corner, ONE downlight in a plain square recess, the same as the left.
- The right end stops the same distance from the centre of the door as the left end
  does, so the canopy is the same length on both sides.

Where a deleted piece used to be, paint the surface that sits behind it — the plain
wall face, or the plain side of the canopy — so no stub, socket, patch or leftover
shadow remains.

When you are done, the canopy's silhouette reads as one simple slab with two large
square tiers at each end, mirrored about the centre of the door, and nothing else
protruding anywhere along it.

Because the camera stands to the left of the doorway, the left end is nearer and
reads larger, and the two ends are seen at different angles. That is correct
perspective and must stay.

LIGHTING IS UNCHANGED: the warm pool across the steps at exactly its present
brightness, the alley at the left as dark as it is now, the three crew in shadow, the
cool blue dome light above. Do not brighten anything.

Everything else is unchanged: the sign with its lettering and robot emblem, the
louvred vents along the canopy's face and its orange trim line, the taller
round-arched door, the shallow grimy steps, both parapets and piers, no handrails
anywhere, the three crew at their exact positions, sizes, postures and depth of
shadow, the swept paving, the street, the dome, the distant figures and the lamps.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
