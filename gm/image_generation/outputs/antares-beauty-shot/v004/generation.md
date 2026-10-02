# Antares beauty shot v004

## User request (verbatim)

Can you make it so its above a planet?

## Generation

- Mode: background edit of user-designated beauty-shot v003 baseline; all ship details and alignment retained
- Tool: built-in image_gen.imagegen; underlying model not exposed
- Style: v2
- Antares design: description v19 = assets/ships/the_antares/description_versions/description-v19.md; scene baseline derived from approved reference v033
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png (style v2; frozen style_versions/canonical_style_reference-v2.png)
- Image 2 EDIT TARGET: outputs/antares-beauty-shot/v003/image.png
- Planet: unnamed generic background element, provisional blue-gray terrestrial surface with ivory clouds and ochre land; no named campaign location implied
- Requested delivery: 2160 × 1440, 3:2, 184 mm print width (~298 dpi)
- Status: generated and visually reviewed; not promoted
- Generated source: /Users/gmahoney/.codex/generated_images/01a0e10a-e606-7a60-ac77-8792df2504bc/exec-c25fc031-b223-41a5-a0ff-f58186d578d4.png, native 1536 × 1024
- Delivery: image.png, Lanczos upscaled to 2160 × 1440, density 298.173913 pixels/inch for 184 mm width; not native 2160 × 1440 generation
- Visual review: curved planetary limb and blue/ochre surface with ivory clouds behind ship; star field above. Ship geometry, detailed stepped hull, engine alignment, camera angle and framing visually retained. Planet fills more of the background than requested, with limb in upper third. No canonical reference or prior output replaced.

## Print export replay

```sh
magick /Users/gmahoney/.codex/generated_images/01a0e10a-e606-7a60-ac77-8792df2504bc/exec-c25fc031-b223-41a5-a0ff-f58186d578d4.png -filter Lanczos -resize 2160x1440 -units PixelsPerInch -density 298.1739130435 outputs/antares-beauty-shot/v004/image.png
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
Image 2 is EDIT TARGET: Antares beauty shot v003. Preserve the whole ship exactly as shown: detailed stepped hull, recessed deck, raised spine, ivory/brick-red colors, cockpit, cargo door, every engine's dimensions and alignment, perspective, camera angle, lighting, position and scale.

Antares identity: broad low faceted ivory workhorse spacecraft, brick-red roof and cylindrical outboard engine housings, dark windows and intake cones. Its raised stepped central spine, recessed panelled deck, layered shoulders and low closed lateral cargo door retain the design in image 2.

Use case: precise-object-edit
Primary request: make the ship fly above a planet. Change the BACKGROUND ONLY.

Replace the lower background with the vast curved limb of an unnamed blue-gray terrestrial planet far beneath the ship. The planet should be large enough to extend off the left, right and bottom frame edges, with a clearly visible curved horizon sweeping behind the ship across the lower half of the composition. Show slate-blue oceans, a few broad muted ochre land shapes, and chunky ivory cloud banks painted as sparse opaque broken shapes. A narrow pale blue painted band at the limb can suggest atmosphere, with a crisp edge and no glow or gradient. Keep dark star-speckled space above the curved horizon, establishing the Antares high in orbit. The planet is distant and entirely BEHIND the ship; no part covers or touches the foreground vessel. Remove any old stars where the planet now blocks the sky.

Render the planet in the same broad matte gouache as the ship and style anchor, with a maximum of three value steps, quiet large shapes and coarse brush edges. No satellite-photo texture, swirling micro-clouds, city lights, photographic Earth, lens flare or glowing atmosphere. The ship remains the main focal point and its silhouette stays clearly readable against both space and the planet.

Keep the Antares pixels and composition as unchanged as the edit allows. Do not redesign, rerotate, lengthen, shrink or repaint the ship. No other ships, moons, stations, people, text, labels or borders.
Output 2160 × 1440 pixels, 3:2 landscape, maintaining the current framing.
Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.
