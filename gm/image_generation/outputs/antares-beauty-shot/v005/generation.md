# Antares beauty shot v005

## User request (verbatim)

Make the planet more arid and less in view. Just in the lower right corner.

## Generation

- Mode: background edit from the same fixed v003 ship baseline, restating accumulated planet changes; not chained from v004
- Tool: built-in image_gen.imagegen; model not exposed
- Style: v2
- Antares design: description v19 = assets/ships/the_antares/description_versions/description-v19.md; scene baseline derived from approved reference v033
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png (style v2; frozen style_versions/canonical_style_reference-v2.png)
- Image 2 EDIT TARGET: outputs/antares-beauty-shot/v003/image.png
- Planet: unnamed arid background world, ochre/tan/terracotta; cropped curved limb restricted to lower-right corner, ~5–10% of frame
- Requested delivery: 2160 × 1440, 3:2; print width 184 mm (~298 dpi)
- Status: generated and visually reviewed; not promoted
- Generated source: /Users/gmahoney/.codex/generated_images/01a0e10a-e606-7a60-ac77-8792df2504bc/exec-1a23860a-749c-45e4-a6ce-c2301bb991c6.png, native 1536 × 1024
- Delivery: image.png, Lanczos upscaled to 2160 × 1440; density 298.173913 pixels/inch for 184 mm width. Not native 2160 × 1440 generation.
- Visual review: arid ochre/terracotta planet limited to lower-right corner, no oceans or clouds. Planet enters bottom around 63% width and right around 65% height, leaving dark space between it and the ship. Ship silhouette, detailed structure, alignment and framing visually retained. Prior outputs and reference remain unchanged.

## Print export replay

```sh
magick /Users/gmahoney/.codex/generated_images/01a0e10a-e606-7a60-ac77-8792df2504bc/exec-1a23860a-749c-45e4-a6ce-c2301bb991c6.png -filter Lanczos -resize 2160x1440 -units PixelsPerInch -density 298.1739130435 outputs/antares-beauty-shot/v005/image.png
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

Image 1 is STYLE: canonical_style_reference.png. Match its rendering only; ignore its people and setting.
Image 2 is EDIT TARGET: Antares beauty-shot v003, the fixed ship baseline. Preserve the entire ship and existing composition.

Antares identity: broad faceted ivory workhorse spacecraft with brick-red cockpit roof and cylindrical outboard engine housings, dark windows and intake cones, raised stepped spine, recessed panelled deck, layered shoulders and a closed lateral cargo door. All details, engine alignment, proportions, camera angle, position, scale and lighting remain exactly as in image 2.

Use case: precise-object-edit.
User request: "Make the planet more arid and less in view. Just in the lower right corner."

BACKGROUND-ONLY EDIT: Add only a small visible section of an enormous ARID DESERT PLANET in the LOWER-RIGHT CORNER. Its center and most of its surface lie outside the frame below and to the right. A curved planetary limb enters the BOTTOM edge at about 65 percent of the image width and exits the RIGHT edge at about 70 percent of the image height. The planet occupies only the corner wedge beyond that arc—roughly 5–10 percent of the total canvas. It must not stretch across the full bottom, reach the left side, run behind the cockpit, or fill the center. This is a cropped curved limb, not a small complete globe floating in space. Leave dark star-filled space around the whole Antares and across nearly all of the image.

Planet surface: dry muted warm ochre, sand, dusty terracotta and restrained brown rock shapes, painted as a few broad broken flat planes with simplified desert basins and ridges. No oceans, blue water, green vegetation, white cloud banks or ice caps. A very thin pale dusty-ivory painted edge may suggest atmosphere, without glow or gradients. The small planet area has quiet broad texture, no photographic terrain or micro-detail. It lies far below and behind the ship and covers none of it. Remove stars only from the small area occupied by the planet.

Keep the Antares unchanged, particularly the approved engine geometry. Do not move or resize the ship to make room. Preserve its existing background everywhere except the lower-right planet wedge. No other craft, moons, stations, text or borders.
Output 2160 × 1440 pixels, 3:2 landscape.
Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.
