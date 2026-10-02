# the-rusty-robot v064

User request verbatim: Left arrow: The overhang is a 3d volume but the left side of it melds with the face of the building. Right arrow: The overhang still is not symmetrical in its design. The right side, for example, has a horizontal divide that does not exist on the left side. Also, some candle stick looking things appeared to the right of the door that needs to be removed.
Mode: Edit off v063: add a flat end face closing the canopy's LEFT end; delete the horizontal division from the RIGHT end so both ends are one undivided block; delete the rod and looped bracket on the wall right of the door.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0fd80-42fc-7f40-801c-ba45e86b7522/exec-1623a14d-e589-4c14-9be1-59169489d13c.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v063/image.png
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

The canopy is the deep slab above the door and below the sign. It is a solid
rectangular volume, like a shoebox pushed into the wall, seen from slightly left of
centre. Its two ends must be built the same way as each other.

FIRST: GIVE THE CANOPY A LEFT END.

Right now the canopy's left end has no end at all: its underside and its top surface
run leftward and simply dissolve into the flat face of the building, so the slab
reads as a smear rather than as a box.

Close it. The left end gets ONE flat vertical end face — a plain four-sided panel,
standing upright, facing left and slightly toward the camera, exactly like the panel
that closes the right end. Its top edge meets the canopy's top surface, its bottom
edge meets the canopy's underside, and its outer edge stands clear of the building
wall so you can see that the slab is a separate solid object sitting in front of the
wall. There must be a visible line where that end face meets the building, not a
fade.

SECOND: MAKE THE TWO ENDS MATCH.

The right end is currently cut across by a horizontal ledge that divides it into an
upper part and a lower part. The left end has no such division.

Delete that horizontal division from the right end. Each end is then ONE plain
undivided block: one top surface, one end face, one underside, and nothing crossing
them. Count the horizontal lines on each end face: ZERO. The two ends become mirror
images of one another about the centre of the door, allowing for the fact that the
left end is nearer the camera and so reads slightly larger. That difference in size
is correct perspective and must stay.

THIRD: CLEAR THE WALL TO THE RIGHT OF THE DOOR.

On the lit wall between the door and the window, two slender dark objects are
mounted: a thin upright rod running from the canopy down toward the steps, and below
it an elongated looped bracket. Together they read as a candlestick stuck to the
wall.

Delete both. Paint plain lit wall where they were — the same flat wall surface that
surrounds them, carrying the same soft pool of light that falls from the downlight
above. Leave no bracket, no socket, no fixing plate, no stub and no leftover shadow.
The wall between the door and the window is then completely plain.

FREEZE EVERYTHING ELSE. These are correct now and must not move:

- The top edge of the canopy is ONE unbroken straight line from the building to the
  sign board. Keep it exactly as it is. Do not add steps, shoulders or tabs to it.
- Where the alley wall meets the front of the cantina on the left of the steps there
  is ONE vertical corner line, the near wall is one unbroken slab meeting the
  pavement, and one plain buttress block sits on the pavement. Keep all of it.
- All four crew members at the left, their poses, faces, clothing and the robot arm.
- The sign board, its lettering and its robot emblem.
- The door, its ironwork, the steps, every downlight, the louvre vents on the canopy
  fascia, the window to the right, the domed city beyond, the paving and its
  reflections.
- There are NO handrails anywhere on the steps and none may be added.

LIGHTING IS UNCHANGED. The crew stand in deep shadow and the steps are lit: the
crew's region measures 0.298 times the brightness of the lit steps, and it must still
measure 0.298 after this edit. Do not brighten the crew to make them legible.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
