# the-rusty-robot v044

User request verbatim: I feel like we are not capturing the way the crew was tucked into the alley well in these later images. Not as well as v5.
Mode: Diagnosed the v005 tuck as three things none of which had been specified: foreground masonry OVERLAPPING the nearest figure, a featureless near-black void behind the group, and rim-only lighting. v005 attached for concealment only.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f60e-9e38-75a0-8b0b-3322c5125ba0/exec-7b7a5207-b4d4-4958-a399-505500236169.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v043/image.png
- Image 3 IDENTITY: outputs/the-rusty-robot/v005/image.png
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
Image 2 is EDIT TARGET: Reproduce this picture and change only what the spec names.
Image 3 is IDENTITY: An earlier version of this scene. Use it ONLY for how the crew are concealed in the alley — the overlap, the void behind them, the rim lighting. Ignore everything else in it.

TASK: A single scene illustration: the exterior of the Rusty Robot cantina at night in the domed city of Kannan.

Reproduce image 2 and change only the alley at the left, so the crew read as hidden
in a dark pocket rather than standing beside a lit building. The cantina's front, its
sign, canopy, staircase, the street and the city beyond stay exactly as they are.

WHAT IS WRONG. In image 2 all three figures stand fully visible in a corner, with a
lit wall behind them showing its masonry, and a lamp burning above them. Nothing
overlaps them and nothing hides them. They look like people standing next to a
building, not people tucked into an alley.

THREE CHANGES, ALL ABOUT CONCEALMENT.

ONE — SOMETHING OVERLAPS THE NEAREST FIGURE. The cantina's masonry comes FORWARD of
the group on the right: a vertical corner of wall, nearer to the camera than they
are, crosses IN FRONT of the woman with the ruby goggles and the cyber arm. It hides
her outer shoulder and part of her outer arm, so she is partly behind it and the
viewer sees her through the gap. She is not standing clear of it — she is behind it.
This single overlap is what makes the group read as tucked in, and image 2 has none.

TWO — BEHIND THEM IS A VOID. The surface behind the group is FLAT, NEAR-BLACK and
EMPTY. Paint no masonry, no courses, no panels, no pipes, no vents, no texture and
no highlights on it — it carries no detail of any kind. It is the darkest area in the
whole picture, a hole in the wall of light, and the figures are silhouetted against
it. Remove any lamp, window or lit surface above or behind them: there is no light
source inside the alley at all.

THREE — THEY ARE LIT ONLY BY A RIM. The sole light reaching them is the warm spill
from the cantina doorway, striking them from the right and catching only the edges
nearest it: a thin warm line down one side of each face, one shoulder, one arm, the
top of a boot. Everything else about them falls into shadow and merges with the dark
behind them. Their clothing colours are still readable but heavily darkened — this
is a group seen in near-darkness, not a group standing in shade.

Keep their poses, faces, costumes, sizes and their arrangement relative to one
another exactly as image 2 has them, and keep their boots in contact with the paving
with a small soft shadow under each. Do not re-pose them, do not resize them, and do
not move them deeper or further out — only the overlap, the void behind them and the
light on them change.

The alley stays the narrow slot it is in image 2, about one eighth of the frame's
width, with the cantina's side wall running back and to the left from its front
corner, and nothing visible beyond the group.

Everything else is unchanged: the sign with its lettering and robot emblem, the
canopy with its two matching stepped ends, the staircase with its two chamfered
piers and both handrails running the full length on three posts each, the warm pool
of light across the steps at exactly its present brightness, the swept paving with
no rocks or rubble, the street, the dome, the distant figures and the street lamps
outside the alley.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
