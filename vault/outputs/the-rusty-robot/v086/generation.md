# the-rusty-robot v086

User request verbatim: Not quite. They should be more bunched together in the lefthand side of the frame. See v5 for exact propoertions. It looks like they are in the leftmost 15% or so?  more darkly light, as well. And Sion should be looking at Graxo and Daxus.
Mode: Edit off v085: crew huddled within the leftmost quarter (4-25% of width, measured on old v005), Graxo ~half frame height, deep shadow with warm edge light only, Sion facing the men.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a1040d-24bb-71c3-ac14-b5be3e1fe459/exec-36052534-d54c-4543-80a4-5951b6efa0e3.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v085/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
- Image 4 IDENTITY: outputs/the-rusty-robot/crew-pose-from-v005.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.05 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Sion now faces Daxus and Graxo; crew slightly darker. MISSES: group still spans to ~35% of width and grew again; the cantina's steps are compressed short — third chained edit (v083->v085->v086) has drifted the building away from its reference.

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
Image 2 is EDIT TARGET: The scene being revised. Preserve everything the spec does not change.
Image 3 is IDENTITY: The approved crew lineup. Keep the crew's likenesses and clothing matching it.
Image 4 is IDENTITY: A crop of an earlier painting of this scene. Copy only the crew's grouping, size, poses and lighting.

TASK: Revise this scene: the crew conferring in the dark alley beside the Rusty Robot cantina.

Reproduce image 2 and change only the three crew. Keep the alley, the Rusty Robot,
the street, the dome and the framing exactly as they are. Their likenesses and
clothing stay as in image 3.

Image 4 is the target for the crew: copy its grouping, size, poses and lighting
closely.

PLACEMENT AND SIZE, measured on image 4:
- All three stand inside the LEFTMOST QUARTER of the picture: the group spans from
  about 4% to 25% of the picture's width. In image 2 they spread to 35%; pull them
  left and close together.
- They stand shoulder to shoulder, overlapping one another — a tight huddle, not a
  row.
- Graxo, the tallest, is about half the picture's height, his head in the upper
  middle of the frame and his feet near the bottom.

POSES:
- Daxus at the left and Graxo at the back lean in toward the middle of the group.
- SION, at the front right of the group, is turned to her left, facing Daxus and
  Graxo, looking at them — her goggled face in profile toward them, not toward the
  door. She gestures with her natural right hand.

LIGHTING — DARK:
- The crew are in deep shadow inside the alley. Their bodies are dark, dim masses:
  colours muted almost to the shadow tone of the alley wall behind them.
- Only a thin edge of warm light from the cantina entrance catches the sides turned
  toward it: the right edge of Sion's jacket and her steel arm, a cheekbone, the gold
  pins at Graxo's collar.
- They are far darker than the lit cantina entrance, which remains the brightest
  thing in the picture.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
