# the-rusty-robot v068

User request verbatim: The stair on the right sticks out in front of the right concrete wall, on the left it does not. It should be the same on each.
Mode: Edit off v067: trim the lower treads back so no tread projects past the right side wall, matching the left.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0fd9a-fc53-71b0-b3fc-eca2551cfbd0/exec-d52d8068-9ff1-4c6e-9b1e-a21b8de4a4e1.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v067/image.png
Date: 2026-10-02
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
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

Image 1 is STYLE: Match its hand-painted matte rendering only. Ignore its subjects.
Image 2 is EDIT TARGET: Reproduce this picture and change only what the spec names.

TASK: A single scene illustration: the exterior of the Rusty Robot cantina at night in the domed city of Kannan.

Reproduce image 2 and change ONE thing. Everything else stays exactly as it is.

THE STEPS MUST NOT STICK OUT PAST THE SIDE WALL ON THE RIGHT.

The staircase has a solid side wall on each side, and the two sides are built
differently:

- On the LEFT, the side wall stands in front of the steps. Every tread stops at the
  inner face of that wall. No tread pokes out past it. This is correct.
- On the RIGHT, the lower treads run out BEYOND the face of the side wall and
  continue into the pavement, so the bottom of the staircase spills sideways past its
  own wall.

Make the right side behave exactly like the left. Count it: every tread, from the top
step to the bottom step, ends at the inner face of the right-hand side wall and goes
no further. ZERO treads project past that wall. The side wall is the outer edge of
the staircase on both sides.

The right-hand side wall keeps its present outline — it still runs down and finishes
on the pavement, as it does now. Do not shorten it, do not move it sideways, and do
not change its slope. Only the treads change: the ones that currently overshoot are
trimmed back to meet it.

Where a trimmed tread end used to be, paint the pavement that lies behind it, matching
the paving and the warm reflected light already there, so no stub, ledge or leftover
shadow remains.

Seen from the front the staircase then reads as one block of steps held between two
side walls, the same on the left and the right.

FREEZE EVERYTHING ELSE. These are correct now and must not move:

- The number of steps, their heights, their treads and the lit edge along each tread.
- Both side walls' outlines, including where each meets the pavement.
- The two dark unlit windows, one on each side of the door, and the balance of wall
  either side of the door.
- The canopy above the door: its single straight top edge, and each end a plain
  undivided block with a flat end face and a downlight beneath.
- The alley corner on the LEFT of the steps: ONE vertical corner line, the near wall
  one unbroken slab meeting the pavement, one plain buttress block on the pavement.
- All four crew members at the left, their poses, faces, clothing and the robot arm.
- The door, its arch and ironwork; the sign board, its lettering and robot emblem;
  every downlight; the louvre vents; the domed city beyond; the paving and its
  reflections everywhere except the small area being repaired.
- There are NO handrails anywhere on the steps and none may be added.

LIGHTING IS UNCHANGED. The crew stand in deep shadow and the steps are lit: the
crew's region measures 0.297 times the brightness of the lit steps, and it must still
measure 0.297 after this edit. Do not brighten the crew to make them legible.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
