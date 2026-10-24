# the-rusty-robot v084

User request verbatim: Lets give it a try. Use v5 as the reference for the crews composition, posture and lighting (from the old passes).
Mode: Crew into the approved street (rusty-robot-street v013); old v005 crew crop for placement, pose and lighting; lineup for likeness. Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10404-d5a5-7723-a76c-c11967cc8ae0/exec-c087b58f-98b5-4888-9cbe-ad354e4a8b81.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: assets/locations/rusty-robot-street/reference.png; frozen assets/locations/rusty-robot-street/candidates/v013/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
- Image 4 IDENTITY: outputs/the-rusty-robot/crew-pose-from-v005.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.26 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Same crew placement and likenesses as v083, slightly larger; street reframed similarly, cantina pushed right; a thick dark pier splits the crew from the cantina. Crew lit fairly brightly.

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
Image 2 is EDIT TARGET: The approved street. Reproduce it and change only what the spec names.
Image 3 is IDENTITY: The approved crew lineup. Copy their likenesses and clothing only.
Image 4 is IDENTITY: A crop of an earlier painting of this scene. Copy only the crew's placement, poses and lighting.

TASK: A single scene illustration: the crew conferring in the dark alley beside the Rusty Robot cantina, at night inside the domed city of Kannan.

ONE single continuous scene illustration, a 3:2 horizontal rectangle, one and a half
times as wide as it is tall. Not a reference sheet: no panels, borders, insets,
captions, names or numbers.

Image 2 is the approved street: reproduce it exactly — the Rusty Robot, its sign and
entrance, the dark alley at the left, the street and buildings to the right, the dome
overhead, the paving, the light. Change only one thing: put the crew in the alley.

Image 3 is the approved crew lineup — Daxus left, Graxo centre, Sion right. Copy their
faces, builds, hair, clothing and equipment. Ignore its plain background, its standing
poses, its side-by-side layout and its height chart; reproduce none of its numbers.

Image 4 is a crop of an earlier painting of this scene. Copy ONLY how the three crew
are placed, posed and lit there: a tight cluster at the alley mouth in the left part
of the picture, large in the frame — about half the picture's height — leaning in
close, heads angled toward one another, conspiratorial, mid-conversation; Sion at the
front right of the group glancing out toward the lit doorway. Copy its lighting on
them: mostly in shadow, lit from the right by warm spill from the cantina entrance on
the faces and shoulders turned toward it, cool dark shadow on the sides turned away.
Ignore its buildings, colours, sign and ground.

THE CREW, in the alley at the left, standing on the paving at the alley's mouth, the
cantina's left side wall beside them:
- DAXUS: broad, sturdy young man, thin metal glasses, dark swept-back hair; short
  off-white medical jacket with orange-red sleeve patches with pale crosses over a
  burnt-orange shirt, off-white belt, dark brown cargo trousers, brown work boots.
- GRAXO: tallest; long weathered face, long nose with a rounded tip, neat dark
  mustache, dark hair with silver temples; long aubergine cape over both shoulders
  pinned by two square antique-gold pins, walnut-brown vest, ivory shirt, plum ascot,
  charcoal trousers and boots, blaster holstered at his right hip. ONLY Graxo wears a
  cape.
- SION: slighter young woman, dark shoulder-length hair swept to one side, large
  dark-framed goggles with opaque ruby-red lenses; worn ochre utility jacket over a
  black shirt, LEFT sleeve absent and a steel-grey cyber arm with brass fittings from
  shoulder to hand, slim teal scarf with short ends, charcoal cargo trousers, black
  boots.

The lit cantina entrance stays the brightest, warmest thing in the picture.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
