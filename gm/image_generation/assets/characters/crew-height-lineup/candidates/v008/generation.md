# Crew height lineup v008
User request: The latest crew lineup looks good — just fix Graxo's face to match his reference. explain your steps
Mode: local edit of user-designated candidates/v007/image.png
Style: v2
Tool: built-in image_gen (model not exposed)
Inputs (ordered):
- STYLE: gm/image_generation/ref_images/style_references/canonical_style_reference.png (style v2)
- EDIT TARGET: gm/image_generation/assets/characters/crew-height-lineup/candidates/v007/image.png
- IDENTITY: graxo/reference.png (= graxo/candidates/v024/image.png)
- IDENTITY: daxus/reference.png (= daxus/candidates/v001/image.png)
- IDENTITY: sion/reference.png (= sion/candidates/v001/image.png)
Descriptions: crew-height-lineup v2; Graxo v10; Daxus v1; Sion v1. No design change; correcting local likeness to an existing approved design.

## Skill route
create_asset multi-character revision + illustrate local scene fix. User-liked latest lineup v007 is baseline. All three references validated: sidecars, real candidate images and receipts, byte-identical reference images. Full Style Block first, style anchor first, numbered image roles, rules.md closing line last. Face-only repaint; Daxus/Sion inputs satisfy multi-character identity requirement without requesting any changes to them. Save next candidate and review; no promotion.

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

Image 1 is STYLE: match rendering technique only; ignore its people, clothing, equipment and setting.
Image 2 is EDIT TARGET: the user-liked crew lineup v007. Preserve this composition.
Image 3 is IDENTITY: Graxo's approved reference, promoted from v024. Use his facial anatomy and hairline to correct ONLY the center man's face in image 2. Ignore this reference's rendering, layout and body poses.
Image 4 is IDENTITY: Daxus's approved reference. The left man in image 2 is Daxus; preserve his existing appearance in the lineup without repainting him.
Image 5 is IDENTITY: Sion's approved reference. The right woman in image 2 is Sion; preserve her existing appearance in the lineup without repainting her.

Use case: identity-preserve. Local face correction to an existing crew height lineup.
Graxo, center: elongated angular adult face, long projecting nose with a broad softly rounded bulbous tip and full nostril wings, tall exposed forehead, deep-set appraising eyes, strong jaw and rounded chin, regular neatly trimmed dark mustache, swept dark hair with loose forelock and silver temples. Copy the specific proportions and likeness of image 3, especially its three-quarter portraits, adapting them to the existing head angle in image 2. His approved nose tip is visibly fuller and rounder than the current lineup's narrow pointed nose. Match the reference forehead height, eye shape and spacing, chin contour and mustache. Preserve the existing head position, gaze direction and overall head scale.
Daxus, left: glasses, swept dark hair, off-white medical jacket, orange shirt, brown trousers and medical harness. Keep his face, body, clothing and equipment exactly as they are in image 2.
Sion, right: red opaque goggles, dark swept hair, ochre jacket, teal scarf, exposed anatomical left cyber arm. Keep her face, body, clothing and equipment exactly as they are in image 2.

Repaint ONLY Graxo's face and the immediately adjoining forehead/hairline required to match image 3. All repainted marks must match the STYLE image's matte angular gouache rendering: a few broad flat shapes, restrained detail and coarse painted edges, no smooth nose modeling or glossy highlights. Keep everything else identical to the edit target. Preserve Graxo's clothing, cape, collar, pins, ascot, hands, equipment and body, all other characters, all chart lines and labels, background, spacing, canvas size and full-body composition. Preserve the established 6 feet 2 inches Graxo, 6 feet Daxus and 5 feet 9 inches Sion comparison. No added portraits or reference-sheet panels. Do not restyle or regenerate the whole lineup.

Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.

## Self-check
Graxo nose tip is visibly fuller and rounder, forehead/hairline and face closer to approved v024. Existing pose, head angle, mustache and silver temples retained. Chart, layout and other characters visually close to v007; minor paint-mark changes outside the face mean this is not a pixel-identical local composite. Matte angular rendering retained, with some inherited facial detail and small nose highlights. Saved as candidate, not promoted.
