# Antares beauty shot v003

## User request (verbatim)

Ok now I need that beauty shop

Retained format request: 2160 × 1440 px, 3:2 landscape; print width 184 mm, approximately 298 dpi.

## Generation

- Mode: fresh beauty shot from newly approved v033 reference; no previous beauty-shot baseline
- Tool: built-in image_gen.imagegen; underlying model not exposed
- Style: v2
- Design context: Antares description v19 = assets/ships/the_antares/description_versions/description-v19.md; approved v033 resolves visual geometry and detail
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png (style v2; frozen style_versions/canonical_style_reference-v2.png)
- Image 2 IDENTITY: assets/ships/the_antares/reference.png (= assets/ships/the_antares/candidates/v033/image.png)
- Reference validation: sidecar points to v033, candidate image and generation record exist, reference/candidate MD5 match: de99be9a47f6fbc992171f10d492c456
- No old model, old reference or rejected beauty shot attached
- Status: generated and visually reviewed; not promoted
- Generated source: /Users/gmahoney/.codex/generated_images/01a0e10a-e606-7a60-ac77-8792df2504bc/exec-ba10e3e6-b1dc-41ea-80fe-b8af73080502.png, native 1536 × 1024
- Delivery: image.png, Lanczos upscaled to 2160 × 1440 with 298.173913 dpi density metadata for 184 mm print width. Not native 2160 × 1440 generation.
- Visual review: one complete ship, retaining the approved stepped hull, raised spine, recessed panels, transverse structures, cockpit facets, closed cargo door and two cone-intake pods. Engine direction and camera angle visually consistent with approved v033. Matte paint and quiet dark star field. Full silhouette fits, with narrower side margins than the requested 82–86 percent width target. No approved asset overwritten.

## Print export replay

```sh
magick /Users/gmahoney/.codex/generated_images/01a0e10a-e606-7a60-ac77-8792df2504bc/exec-ba10e3e6-b1dc-41ea-80fe-b8af73080502.png -filter Lanczos -resize 2160x1440 -units PixelsPerInch -density 298.1739130435 outputs/antares-beauty-shot/v003/image.png
```

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

Image 1 is STYLE: canonical_style_reference.png. Match this image's rendering technique only. Ignore its people, clothing, equipment and setting.
Image 2 is IDENTITY: the APPROVED Antares reference sheet v033. The large UPPER-LEFT THREE-QUARTER ship is the exact approved design, perspective and engine alignment. Use this view as the geometric basis for the beauty shot; do not copy the other views, sheet layout or cargo insets.

Antares identity: broad low ivory/light-gray utilitarian ship with faceted wedge cockpit, dark windows, brick-orange cockpit roof surrounding a circular hatch, layered lower hull, detailed stepped shoulders, raised central spine, transverse bridges, notches and recessed panelled deck. One broad rectangular closed cargo door sits low on the visible side with a top hinge and two recessed grips. Two substantial orange/ivory cylindrical engine pods with dark intake cones and short dark rear nozzles preserve the exact size, placement, barrel direction and coherent fore-aft alignment of the approved upper-left view.

Use case: illustration-story
Asset type: full-column print spacecraft beauty shot.
Primary request: one polished, single-view Antares beauty shot at exactly 2160 × 1440 pixels, 3:2 landscape, printing at 184 mm width (approximately 298 dpi).

GEOMETRY AND DETAIL LOCK: Take the approved upper-left view from image 2 and present that same detailed ship larger in a finished composition. Preserve its existing camera angle and internal perspective. The hull and engine arrangement have been carefully approved: neither rotate nor lengthen either engine, neither turn an intake towards the viewer nor squash a rim, and do not change the camera to invent a new projection. Keep the protruding intake cones aligned with the barrels and hull exactly as in the approved drawing. Retain the layered ivory structural blocks, stepped rear shoulders, recessed panelled deck, bridges, raised spine, vent blocks, cargo-door details and cockpit facets. Structural complexity should stay at the reference level even though the paint remains broad and matte. Do not substitute a simple smooth roof slab or long empty deck channels.

Composition: entire ship in front-port three-quarter view, nose toward the lower left and engines toward the upper right, centered in the 3:2 frame. Scale and reposition the WHOLE ship uniformly to fill about 82–86 percent of the width while keeping generous breathing room around nose, both engines and every extremity. One ship only.
Setting: quiet deep space, dark slate-blue and charcoal painted background, a sparse handful of tiny ivory stars. No nebula, planets, ground, ground shadow, other craft or people.
Lighting: warm ivory light across upper surfaces and restrained cool slate shadows underneath; broad flat opaque paint planes and coarse brush texture, no new glossy highlights, lens flare, bloom or rim lighting. Keep the silhouette distinct from the dark backdrop.
No text, labels, watermark, borders, insets or multiple views.
Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.
