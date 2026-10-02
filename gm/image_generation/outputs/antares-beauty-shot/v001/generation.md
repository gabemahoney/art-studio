# Antares beauty shot v001

## User request (verbatim)

give me a beauty shot of the Antares at at 2160 × 1440 px (3:2 landscape). it prints full column width at 184mm, so it needs that resolution to hit ~300
  dpi.

## Generation

- Mode: fresh scene, illustration-story
- Tool: built-in image_gen (image_gen.imagegen); model managed by tool
- Style: v2
- Cast: Antares description v12, immutable description at assets/ships/the_antares/description_versions/description-v12.md
- Requested output: 2160 × 1440 PNG, 3:2 landscape; effective resolution at 184 mm width: 298.17 dpi
- Image 1 — STYLE: ref_images/style_references/canonical_style_reference.png (style v2; immutable snapshot style_versions/canonical_style_reference-v2.png)
- Image 2 — IDENTITY: assets/ships/the_antares/reference.png (= the_antares/candidates/v004/image.png); candidate generation record assets/ships/the_antares/candidates/v004/generation.md
- Reference validation: sidecar names candidates/v004/; candidate image and record exist; reference and candidate MD5 both 19b2d8940703a1031339de0473275f4f
- No edit target. Current design text v12 used with approved v004 reference; unapproved subsequent candidates were not attached.
- Status: generated and inspected; not promoted
- Generated source: /Users/gmahoney/.codex/generated_images/01a0e10a-e606-7a60-ac77-8792df2504bc/exec-adc78ec1-a562-43d3-9038-c5ebf994a145.png (1536 × 1024)
- Delivery: image.png, Lanczos upscaled to 2160 × 1440; density metadata 298.1739130435 pixels/inch for 184 mm print width. This is an upscaled delivery, not native 2160 × 1440 generation.
- Visual check: single full ship, two pods, ivory/orange livery, dark cockpit, raised spine and recessed deck, closed side cargo door, matte painted treatment. Cargo door retains some reinforcement divisions from the approved v004 identity sheet; it is not an exact reproduction of the later v12 uninterrupted-face specification.

## Print export replay

```sh
magick /Users/gmahoney/.codex/generated_images/01a0e10a-e606-7a60-ac77-8792df2504bc/exec-adc78ec1-a562-43d3-9038-c5ebf994a145.png -filter Lanczos -resize 2160x1440 -units PixelsPerInch -density 298.1739130435 outputs/antares-beauty-shot/v001/image.png
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

Image 1 is STYLE: canonical_style_reference.png. Match this image's rendering technique only. Ignore its people, clothing, equipment, and setting.
Image 2 is IDENTITY: the approved Antares reference sheet. Copy this spacecraft's silhouette, proportions, hull design, cockpit, engine pods, and color placement. Ignore its rendering and sheet layout. Show only ONE ship, no extra views or insets.

Antares identity (description v12): A broad, low utilitarian spacecraft with a blunt wedge-shaped cockpit nose, dark angular windscreen, raised central spine, recessed deck, compact near-upright hull shoulders, and two widely separated cylindrical side engine pods on outboard mounting bridges; ivory/light-gray hull with orange-red upper cockpit panels around a circular roof hatch and orange-red rear engine housings, ivory bands, dark intakes. Preserve the distinctive shallow cockpit shoulders, mild lateral cargo-door housing protrusion and shallow aft hull flare with a square return beside the engine mounts; keep both engine intake rims clear of the body, with the visible near pod slightly forward and outboard of the adjacent hull protrusion. One closed broad rectangular cargo door occupies the port lateral midship opening, below a continuous fixed ivory upper hull band, with a dark seam and two simple recessed grips; no additional personnel hatch, no broad wings, no extra engines.

Use case: illustration-story
Asset type: full-column print illustration, spacecraft beauty shot.
Primary request: a single stunning Antares beauty shot at exactly 2160 × 1440 pixels, 3:2 landscape, intended to print 184 mm wide at approximately 298 dpi.
Scene: the Antares alone coasting through deep space. A restrained dark slate-blue and charcoal painted field with a handful of tiny quiet ivory star marks. No planets, other ships, people, lettering, captions, borders or watermark.
Composition: large front-port three-quarter hero view, slightly above the ship, nose pointing toward the lower left and the engine pods toward the upper right. Show the entire vessel with generous clean breathing room around all extremities, occupying about 80 percent of the canvas width. Both engine pods must be visibly distinct; the near circular intake is fully exposed. Make the cockpit, orange roof panel and hatch, recessed deck, central spine and closed lateral cargo door readily readable. A single coherent perspective, substantial workhorse proportions, no lens distortion. This is one complete scene, never a reference sheet.
Lighting: warm ivory directional light over the upper hull and muted slate-blue shadow underneath, expressed as broad flat paint planes with hard angular edges. Rich value separation against the darker backdrop, quiet painterly texture, no glow, no neon, no lens flare. Emphasize the iconic silhouette and livery instead of dense surface detail. Maintain the anchor's large brush scale even at the requested print resolution.
Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.
