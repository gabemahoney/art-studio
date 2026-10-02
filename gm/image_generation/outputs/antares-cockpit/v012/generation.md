# Antares cockpit v012
User request: nope. Graxo is looking straigt forward in that image. He should be looking in the same direction at the same point as sIOn.
Mode: retry from v010 baseline, not failed v011
Style: v2
Tool: built-in image_gen (model not exposed)
Inputs (ordered):
- STYLE: ref_images/style_references/canonical_style_reference.png (style v2)
- EDIT TARGET: outputs/antares-cockpit/v010/image.png
Descriptions: Graxo v10, Daxus v1, Sion v1 unchanged.
Diagnosis: previous prompt specified a frontal face and point just beyond camera, incorrectly producing direct eye contact. This attempt specifies viewer-right three-quarter head yaw matching Sion, with shared distant target.

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

Image 1 is STYLE: rendering technique only, not character design or gaze.
Image 2 is EDIT TARGET: cockpit v010, baseline before failed gaze edit v011.

Use case: identity-preserve. Correct Graxo's gaze to match Sion's EXISTING gaze in image 2. Sion is the pilot at viewer right; keep her head orientation unchanged. She faces slightly toward VIEWER RIGHT, looking at an off-screen point beyond the camera's right side. Graxo, the man standing in the central doorway, must turn his HEAD AND EYES in that SAME viewer-right direction toward that SAME distant point. His face must be visibly THREE-QUARTER, not frontal: nose pointing somewhat toward the right edge, far cheek foreshortened, pupils shifted toward viewer right. Approximate a 20–25 degree turn to viewer right and a level gaze, matching Sion's head yaw. Both are looking through the unseen forward window beyond the camera to its RIGHT. Do NOT make Graxo stare straight into the camera. Do NOT turn him toward Sion herself: their sightlines continue approximately parallel past the camera's right side toward a distant object. The previous attempt failed by making his face symmetrical and frontal.

Keep his expression serious, mouth closed, with his same mustache, full rounded nose, tall forehead, silver temples and face proportions. Preserve his standing body, hand on doorway, dark walnut-brown vest, cape and all equipment. Keep Sion, Daxus, hands, yoke, instruments and architecture unchanged. No visible window or external object. Change only Graxo's head orientation and eye direction; all repainted areas match the matte gouache STYLE.

Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.

## Self-check — retry
Graxo turned too far right compared with Sion; reduce head yaw from same baseline.
