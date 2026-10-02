# the-rusty-robot v055

User request verbatim: Can you make the steps less tall and the door to the cantina a little taller? Also, make the steps look a little grimier.
Mode: Risers to ~2/3 height keeping the same step count; door grown ~1/5 taller upward only; step grime as 3-4 flat tones (corner bands, end wedges, worn patches, pale nosings) with speckle/grain/dots explicitly banned.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f8c5-7058-7162-bca8-913035d6679f/exec-d8bdefc2-6181-4471-a0cc-933c1c292b25.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v054/image.png
Date: 2026-10-01
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
Image 2 is EDIT TARGET: Reproduce this picture and change only what the spec names.

TASK: A single scene illustration: the exterior of the Rusty Robot cantina at night in the domed city of Kannan.

Reproduce image 2 and change THREE things about the cantina's entrance. Everything
else stays exactly as it is.

CHANGE ONE — THE STEPS ARE SHALLOWER.

In image 2 each step is tall, so the flight climbs steeply and the landing sits high.
Keep the SAME NUMBER of steps, in the same place in the frame and the same width, but
make each riser SHALLOWER — roughly two thirds of its present height — so the whole
flight rises about two thirds as high as it does now. The treads stay the same depth,
so the staircase reads as an easy, low flight rather than a steep climb.

The two parapets follow the new, gentler slope down to the two piers, and the piers
stand at the foot as before with their chamfered caps.

CHANGE TWO — THE DOOR IS TALLER.

The round-arched door is too squat. Make it about one fifth TALLER, growing UPWARD:
the crown of its arch rises closer to the underside of the canopy above, while the
bottom of the door stays on the landing where it is. Its width does not change, and
its round arch keeps the same shape — the same semicircular head, the same recessed
surround, the same spoked wheel pattern on the leaves. It is the same door, taller.

Together these two changes open up the front of the building: a lower flight of steps
leading to a taller doorway.

CHANGE THREE — THE STEPS ARE GRIMY.

The stone of the steps is clean in image 2. Make it worn and dirty, in flat painted
shapes:

- A darker band of grime gathers in the inside corner of every step, where the tread
  meets the riser behind it, and runs the full width of the flight.
- A darker wedge of dirt collects at each end of every tread, where the steps meet
  the parapets on the left and on the right.
- Across the middle of the flight, where feet have worn a path, two or three broad
  dull patches sit on the treads — slightly darker and greyer than the clean stone.
- The front edge of each step is RUBBED PALER than the rest of the tread, a thin
  light line along every nosing where boots have polished the stone smooth.

Paint all of it as a handful of flat tonal shapes, the way the rest of the picture is
painted. Use only three or four tones of the step stone in total — clean, dulled,
and dark in the corners. NO speckle, NO scattered dots, NO grain, NO noise, NO
hatching and NO individual specks of dirt anywhere.

The grime is on the STEPS only. The parapets, the piers, the paving of the street and
the building faces stay as clean as they are now.

LIGHTING IS UNCHANGED: the warm pool of light falls across the steps exactly as
brightly as it does now and reaches just as far; the alley at the left stays as dark
as it is; the three crew stay in shadow; the cool blue dome light above is unchanged.
Do not brighten anything.

Everything else is unchanged: no handrails anywhere on the staircase, the sign with
its lettering and robot emblem, the canopy with its two stepped ends and its two
downlights, the three crew at their exact positions, sizes, postures and depth of
shadow, the swept paving with no rocks or rubble, the street, the dome, the distant
figures and the lamps.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
