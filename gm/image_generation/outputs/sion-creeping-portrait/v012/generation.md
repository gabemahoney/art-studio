# Sion creeping portrait — v012

## User request
You did not fix the goggle angle.

## Run
- Mode: local goggle rotation correction against approved v010 baseline; v009 user-designated angle reference.
- Style version: v2.
- Tool: built-in image_gen; model not exposed.
- Character: Sion description v1.
- Image 1 STYLE: gm/image_generation/ref_images/style_references/canonical_style_reference.png (style v2; frozen at gm/image_generation/style_versions/canonical_style_reference-v2.png).
- Image 2 EDIT TARGET: gm/image_generation/outputs/sion-creeping-portrait/v010/image.png.
- Image 3 GOGGLE ANGLE: gm/image_generation/outputs/sion-creeping-portrait/v009/image.png.
- Output generated 1122 × 1402; trimmed one pixel per edge with sips to exact 1120 × 1400 (4:5).
- Visual check: top rim now visibly descends toward viewer-right.

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

Image 1 is STYLE: match only its matte gouache painting technique. Image 2 is EDIT TARGET: approved v010 hair, face and composition. Image 3 is GOGGLE ANGLE reference v009, user explicitly requests this angle.
Correct the goggles' ROTATION, not just the bottom contour. In image 2 their top edge is almost horizontal. That is WRONG. Rotate the ENTIRE goggle assembly CLOCKWISE as viewed on the page, around its center, so the long TOP FRAME EDGE visibly slopes DOWN toward the RIGHT side of the image, matching image 3. The viewer-right temple attachment and right end of the top rim must move DOWN; the viewer-left end moves slightly UP. Target roughly 8 degrees clockwise relative to the current horizontal top rim: across the goggles' width the right end should be about 30 pixels lower than the left at this image scale. Apply this same tilt to the top rim, lens plane, lower rim and side attachments together, preserving their shape. Do not merely deepen the right lens or redraw the nose notch. The correction must visibly change the top frame angle. Keep goggles seated naturally on the fixed face with the bridge over the nose.
Keep the exact compact goggle design and fully opaque ruby lenses from image 2, with one pale diagonal painted reflection, no eyes visible. Preserve image 2 hair and head orientation EXACTLY. Do not rotate the whole head or image. Preserve all other artwork: face, pose, hands, clothes, cyber arm, ledge, moons, moving ship, painted stars, tight composition. Repaint ONLY goggles and tiny adjacent face/temple areas needed for the rotation. Output 4:5 portrait. No text or borders.
Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.
