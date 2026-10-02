# Graxo v022
User request: v20 graxo is close. we just need to make his nose a little more bulbous and his forehead a little taller. Explain how you walk through the skill so I can debug.
Mode: edit of user-designated candidates/v020/image.png
Style: v2
Tool: built-in image_gen (model not exposed)
Inputs (ordered):
- STYLE: gm/image_generation/ref_images/style_references/canonical_style_reference.png (style v2)
- EDIT TARGET: gm/image_generation/assets/characters/graxo/candidates/v020/image.png
- DESIGN: description.md (v9 = description_versions/description-v9.md); face constraints incorporated into edit prompt, remaining design preserved from designated baseline.

## Skill route
create_asset → rules.md + style.md → close-feedback designated-baseline branch → description v9 snapshot → built-in imagegen edit → self-check. v020 takes precedence over reference.png and v021. Only the two requested changes apply. Closing line follows rules.md, whose wording differs slightly from style.md.

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

Image 1 is STYLE: match its rendering technique only. Ignore its people, clothing, equipment, and setting.
Image 2 is EDIT TARGET: Graxo candidates/v020/image.png, expressly designated by the user as close. Preserve this sheet.

Use case: identity-preserve.
Make only two subtle anatomical adjustments to image 2: make Graxo's nose a little more bulbous, giving the tip a modestly fuller rounded silhouette while preserving its length and bridge; make his forehead a little taller by modestly increasing the exposed brow-to-hairline distance, preserving the loose forelock and swept hairstyle. Keep these changes small and natural, never a spherical caricature nose or exaggerated forehead. Apply consistently to all visible faces, including full-body views and expression portraits.
Absolute face design for this revision: elongated angular adult face, long projecting nose with a broad softly rounded bulbous tip and full nostril wings, tall forehead with a generous exposed brow-to-hairline plane, heavy brow, legible deep-set eyes, angular cheekbones, strong jaw and rounded chin; dark trimmed mustache, swept dark hair with loose forelock and silver temples.

Keep everything else identical to the edit target, and keep all repainted areas in the STYLE image's rendering. Preserve eye shapes and spacing, expressions, face length, mustache, silver temples, body proportions, clothing, equipment, colors, poses, four full-body views above four portraits, gray background, and composition. Preserve the existing visible broad matte painted brushwork; paint adjusted anatomy with broad flat angular planes. No additional redesign, text, or layout changes.

Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.

## Self-check
Nose tips appear modestly fuller and rounder, and exposed forehead planes taller, most legibly in the large portraits. Layout, poses, costume and equipment remain visually close to v020. Broad matte angular paint handling retained; inherited small face facets and dense background strokes remain relative to the stricter anchor limits. No obvious new glossy rendering drift. Candidate saved, not promoted.
