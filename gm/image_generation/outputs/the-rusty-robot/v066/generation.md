# the-rusty-robot v066

User request verbatim: Lets try to make the entrance to the cantina a bit more symmertrical. the left side is thinner than the right side. the left side also has a dark rectangle the right side is missing. I think the dark rectangle is a good way to break up the space of the wall so we shuld include that on the right side. Maybe these are darkened windows. Also, the rightside of the staircase ends on the last STAIR instead of the ground. It should end on the GROUND, like the left side does.
Mode: Edit off v065: narrow the right wall strip so both flank the door equally; add a mirrored unlit window on the right; extend the staircase's right side wall down to the pavement.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0fd8b-9bc0-7d13-b99d-fb27ef0298d5/exec-6bf5818f-4904-460b-85f6-266d746b3ea4.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v065/image.png
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

Reproduce image 2 and change THREE things. Everything else stays exactly as it is.

FIRST: BALANCE THE TWO WALLS BESIDE THE DOOR.

The arched door sits in a flat wall. The strip of wall between the door and the
building's left corner is about half the width of the strip between the door and the
building's right corner, so the entrance looks lopsided.

Make the two strips read as the same width in the picture. Do it by bringing the
right-hand corner of the building IN toward the door, so the right strip narrows to
match the left. Do NOT move the door, do not resize the door, and do NOT move the
building's LEFT corner — that corner and everything left of it must stay exactly
where it is.

A small difference is acceptable and correct: the camera stands left of the doorway,
so the two walls are seen at slightly different angles. Aim for them to look like
equal walls seen from slightly off-centre, not for identical shapes.

SECOND: PUT A DARKENED WINDOW ON THE RIGHT TO MATCH THE ONE ON THE LEFT.

On the wall to the LEFT of the door there is a tall dark recessed panel — an unlit
window, about three times as tall as it is wide, set flush into the wall, its top
level with the point where the door's arch begins to curve. It breaks up the flat
wall nicely. KEEP IT EXACTLY AS IT IS.

Add ONE matching unlit window to the wall on the RIGHT of the door. Count it: ONE
window, the same proportions as the left one, the same height above the steps, the
same depth of recess, mirrored about the centre of the door. Same dark flat interior,
same plain surround, no glazing bars, no sill ornament, no light inside.

After this there is exactly one dark window on each side of the door and no others on
this wall.

THIRD: CARRY THE RIGHT SIDE OF THE STAIRCASE DOWN TO THE GROUND.

The staircase has a solid side wall on each side. On the LEFT the wall runs all the
way down and finishes on the pavement, so the staircase sits on the ground. On the
RIGHT the wall stops short, ending in mid-air at the level of the bottom step.

Extend the right-hand side wall downward so it finishes on the pavement, exactly as
the left one does. Its bottom edge meets the paving in a single straight line, at the
same height on the page as the left wall's bottom edge. The staircase then reads as
one solid block resting on the ground on both sides, with nothing floating.

FREEZE EVERYTHING ELSE. These are correct now and must not move:

- The canopy above the door: its top edge is ONE unbroken straight line, and each end
  is ONE plain undivided block with a flat end face and a downlight beneath. Both
  ends stay exactly as they are.
- Where the alley wall meets the front of the cantina on the LEFT of the steps there
  is ONE vertical corner line, the near wall is one unbroken slab meeting the
  pavement, and one plain buttress block sits on the pavement. Keep all of it, and do
  not move that corner.
- The wall between the door and the right-hand window carries NO rod, bracket, sconce
  or fitting of any kind. It stays plain apart from the new window.
- All four crew members at the left, their poses, faces, clothing and the robot arm.
- The door itself, its arch and its ironwork; the steps and their treads; the sign
  board, its lettering and its robot emblem; every downlight; the louvre vents on the
  canopy; the domed city beyond; the paving and its reflections.
- There are NO handrails anywhere on the steps and none may be added.

LIGHTING IS UNCHANGED. The crew stand in deep shadow and the steps are lit: the
crew's region measures 0.298 times the brightness of the lit steps, and it must still
measure 0.298 after this edit. Do not brighten the crew to make them legible.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
