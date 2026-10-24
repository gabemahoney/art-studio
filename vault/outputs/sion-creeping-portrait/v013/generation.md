# Sion creeping portrait — v013

## User request
Now it looks like she has too much forehead. Can you just got back to v008 and make her hair look like it does in the reference picture?

## Run
- Mode: hair-only edit directly against user-selected v008; no later revisions used.
- Style version: v2.
- Tool: built-in image_gen; model not exposed.
- Character: Sion description v1.
- Image 1 STYLE: gm/image_generation/ref_images/style_references/canonical_style_reference.png (style v2; frozen at gm/image_generation/style_versions/canonical_style_reference-v2.png).
- Image 2 EDIT TARGET: gm/image_generation/outputs/sion-creeping-portrait/v008/image.png.
- Image 3 IDENTITY (hair only): gm/image_generation/assets/characters/sion/reference.png (= sion/candidates/v001/image.png), previously validated sidecar and matching bytes.
- Output generated 1122 × 1402; trimmed one pixel per edge using sips to exact 1120 × 1400 (4:5).

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

Image 1 is STYLE: match its matte gouache painting technique only. Image 2 is EDIT TARGET: v008, explicitly selected by the user as the baseline to return to. Image 3 is IDENTITY: Sion's approved reference sheet; use ONLY its hair design, particularly the bottom-row busts.
Return to image 2 EXACTLY, and change ONLY THE HAIR. Replace its oversized windblown mane with the compact tousled shoulder-length dark hairstyle in image 3: modest crown, asymmetric side-swept fringe, short chunky jagged ends around jaw and neck, restrained width. Match the reference's hair silhouette and hair-to-head proportions. Retain the fringe's low coverage across the upper forehead; do not pull hair back or expose more forehead. Keep image 2's existing hairline boundary against the forehead and temples fixed; reduce excess outer hair volume instead. Preserve the original forehead size, the exact face and skull dimensions, and all visible skin from image 2. Paint the hair as a few broad dark angular masses, no fine strands.
CRITICAL: do not edit the goggles at all. Preserve image 2's exact goggles, their angle, position, frame, lenses, reflection, and fit to the face. Do not import the reference sheet's goggles or any later version's face, hairline or goggle changes. No changes to expression, head angle, face, clothing, pose, body scale, hands, cyber arm, scarf, backpack, ledge, stars, moons, or moving ship. Fill only the small spaces exposed by reducing the OUTER hair silhouette with matching background or clothing. Keep the tight 4:5 composition of image 2, 1120 by 1400 pixels. This is a hair-only edit of v008, not a new portrait. All repainted marks match the STYLE image. No text or borders.
Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.
