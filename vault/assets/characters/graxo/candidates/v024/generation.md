# Graxo v024
User request: v22 facial features look correct. But re-stylize because it became too smooth and detailed. Tell me how you navigate the skills to do so.
Mode: style-transfer repaint of user-designated candidates/v022/image.png
Style: v2
Tool: built-in image_gen (model not exposed)
Inputs (ordered):
- STYLE: gm/image_generation/ref_images/style_references/canonical_style_reference.png (style v2; frozen as style_versions/canonical_style_reference-v2.png)
- EDIT TARGET: gm/image_generation/assets/characters/graxo/candidates/v022/image.png (identical preserved copy: sources/design-from-candidate-v022.png)
- DESIGN: description.md (v10 = description_versions/description-v10.md); design contours supplied by v022, no anatomical change requested.

## Skill route and diagnosis
Read v022 receipt: identity-preserve edit of v020, with explicit preservation of brushwork. Prior self-check accepted excessive detail. User now designates v022 facial geometry as correct and rejects rendering. create_asset re-style branch → preserve source copy → sync description and snapshot v10 (correct per-region plane wording to whole-face limit) → escalation step 1, total style-transfer repaint → imagegen built-in edit. Full sheet is EDIT TARGET, not IDENTITY in a fresh generation. Any retry uses v022 again. Reference validation is inapplicable because no reference.png is attached. Style block first, numbered roles, rules.md closing line last.

Retry: v023 failed to repaint sufficiently; same v022 baseline, stronger flattening instruction.

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

Image 1 is STYLE: match this image's rendering technique only. Ignore its people, clothing, equipment, and setting.
Image 2 is EDIT TARGET: Graxo v022, whose facial features the user explicitly says are correct. This image is the drawing authority only; its smooth detailed paint handling is rejected.

Use case: style-transfer. TOTAL STYLE-TRANSFER REPAINT, preserving the underlying drawing exactly.
Repaint this entire image in the STYLE image's rendering technique — flatten all shading into broad opaque angular planes, coarse dry-brush, limited values. Change NOTHING else: preserve layout, poses, facial geometry, hair shapes, and all clothing/equipment design exactly.

Lock the precise v022 nose silhouette, bulbous tip width and projection, forehead height, hairline and loose forelock, face length, chin contour, eyes and spacing, mustache, silver temples, and every expression. Do not enlarge or shorten the nose, lower the forehead, or redesign the face. Retain all four body views and four expression portraits at their existing positions and scales, all costume/equipment silhouettes and placement, colors and gray background. No text.

Replace the interior rendering across the ENTIRE sheet. Trace the approved contours, then repaint them with a broad worn flat brush. Each face must be just five to eight large connected skin-color planes TOTAL, with small simple marks only for the existing eyes and mustache. Merge all the tiny cheek, forehead and nose facets into large quiet opaque strokes. The forehead is one light plane and one shadow plane; each cheek a single broad stroke. Preserve the rounded anatomical nose contour but paint its interior with a simple flat light and shadow; eliminate the tiny shiny highlights and smoothly modeled nose surface. Hair becomes two dark masses and broad silver temple marks within the same outer silhouette.

Make actual broad paint strokes visible on faces, shirt and cape: loaded opaque paint, blunt squared stroke ends, irregular bristle-drag edges and occasional broken coverage in individual large marks. Portrait strokes about a nose-width; cape strokes about a forearm-width. No tiny polygon mosaics, small overlapping tonal facets, polished shading, or fine scratch texture. Keep large quiet unbroken areas between strokes. Simplify the equipment to flat recognizable blocks without specular shine, preserving its design. Replace the all-over diagonal background scratches with a quiet flat gray field and a handful of broad sparse brush marks.

This is a substantial change of PAINT HANDLING with zero change of facial anatomy. Preserve design contours, NOT existing interior shading marks. Keep all repainted areas in the STYLE image's rendering. The result must read as broad handmade matte gouache at ordinary viewing size, with the economy and brush scale of image 1.

MANDATORY REPAINT OVERRIDE: the prior attempt failed by copying image 2 almost unchanged. This time discard ALL of image 2's interior paint marks. Keep only its contour drawing and feature positions, as if traced in pencil onto fresh gray illustration board. Paint that drawing anew entirely with image 1's coarse opaque flat-brush technique. A nearly identical output is a failure. Make the change in brushwork unmistakable across the entire image.

Eliminate at least three quarters of the small color patches. On each portrait use ONE large uninterrupted ochre forehead stroke, ONE light cheek stroke and ONE connected umber shadow spanning the opposite cheek and jaw. Use only two flat tones on the nose, with NO highlight dots. Preserve the same bulbous outer nose contour and high hairline. Lay these forms in thick blunt overlapping gouache brushstrokes with visible broken bristle edges, with no blended transitions. The face must look hand-painted with a brush too large to draw small facets. Hair must be broad dark brush masses, no individually segmented locks. Cape must be four or five long broad opaque strokes per view, no nested patches. Reduce vest and trousers to two broad values, and equipment to flat silhouettes plus one light plane. Keep the existing costume outlines and equipment locations. COMPLETELY REMOVE the repeating scratched background and paint one flat gray ground with only a few wide quiet strokes.

The drawing is preserved, but every interior paint mark is replaced. Treat this as a bold handmade gouache study from the supplied drawing, visibly rough and spare, with the stylistic economy of image 1.

Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.

## Self-check — failed
Still near-identical to v022, insufficient flattening. Full-sheet edit target dominates. Move to fresh generation with tight face crop for likeness per escalation step 3; step 2 text-only would abandon the facial reference the user explicitly values.
