# the-rusty-robot v087

User request verbatim: Also we sort of lost the design of the Rusty Robot. The staircase got somehow smooshed very short. / They should be more bunched together in the lefthand side of the frame... more darkly lit... Sion should be looking at Graxo and Daxus.
Mode: FRESH from the approved street (no earlier candidate attached): crew in leftmost quarter, Graxo ~1.5x door height, dark, Sion facing the men; camera and cantina held. Roll 1 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a1040e-9926-7920-b38a-27a75b709c1b/exec-ac8b8c0c-8389-4c85-b532-33a209b93f55.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: assets/locations/rusty-robot-street/reference.png; frozen assets/locations/rusty-robot-street/candidates/v013/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
- Image 4 IDENTITY: outputs/the-rusty-robot/crew-pose-from-v005.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.08 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: FRESH from approved street: framing and cantina held, full stair intact. Crew huddled in leftmost ~28%, Sion facing the men, darker. Graxo ~60% of frame height (~2.5x door).

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
Image 2 is EDIT TARGET: The approved street. Reproduce it exactly and add only the crew.
Image 3 is IDENTITY: The approved crew lineup. Copy their likenesses and clothing only.
Image 4 is IDENTITY: A crop of an earlier painting of this scene. Copy only the crew's grouping, poses and lighting.

TASK: A single scene illustration: the crew conferring in the dark alley beside the Rusty Robot cantina, at night inside the domed city of Kannan.

ONE single continuous scene illustration, a 3:2 horizontal rectangle. Not a reference
sheet: no panels, borders, captions, names or numbers.

Image 2 is the approved street. Reproduce it EXACTLY: the same camera, the same
framing, the Rusty Robot at the same size and position, its full flight of steps with
matching side walls and handrails, its sign and canopy, the alley at the left, the
street and buildings to the right, the dome. Do not move the camera, zoom, or resize
the cantina. Only add the crew.

Image 3 is the approved crew lineup — copy their likenesses and clothing only.

Image 4 is a crop of an earlier painting: copy how the crew are grouped, posed and
lit there.

THE CREW, in the alley at the left edge of the picture:
- All three stand inside the LEFTMOST QUARTER of the picture — from about 3% to 25%
  of its width — shoulder to shoulder, overlapping, a tight huddle.
- Their size is set by the cantina: Graxo, the tallest, is about one and a half times
  the height of the cantina's arched door. Daxus and Sion are in proportion.
- Feet on the alley paving near the bottom of the picture.
- Daxus at the left and Graxo at the back lean in toward the middle. SION, at the
  front right of the group, is turned to her left facing Daxus and Graxo, her goggled
  face in profile toward them, gesturing with her natural right hand.
- DARK: they stand in deep shadow inside the alley — dim, muted masses nearly the
  tone of the alley wall. Only a thin warm edge of light from the cantina entrance
  catches the sides turned toward it: the right edge of Sion's jacket and steel arm, a
  cheekbone, the gold pins at Graxo's collar.

DAXUS: broad young man, thin glasses, dark swept-back hair; off-white medical jacket
with red-cross sleeve patches over a burnt-orange shirt, brown cargo trousers, boots.
GRAXO: tallest; long weathered face, mustache, silver temples; long aubergine cape
with two gold pins, walnut vest, plum ascot, charcoal trousers. Only Graxo wears a
cape. SION: slighter young woman, dark hair swept to one side, ruby-red goggles; ochre
jacket, LEFT sleeve absent and a steel cyber arm, slim teal scarf, charcoal trousers.

The lit cantina entrance stays the brightest, warmest thing in the picture.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
