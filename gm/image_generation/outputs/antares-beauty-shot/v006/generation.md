# Antares beauty shot v006

## User request (verbatim)

Good. Now make the topside of the ship symmetrical.

## Generation

- Mode: local edit of user-approved v005 baseline.
- Tool: built-in image_gen.imagegen; model not exposed.
- Style: v2.
- Antares design: description v20, frozen at assets/ships/the_antares/description_versions/description-v20.md.
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png (style v2; frozen style_versions/canonical_style_reference-v2.png).
- Image 2 EDIT TARGET: outputs/antares-beauty-shot/v005/image.png.
- Requested delivery: 2160 × 1440, 3:2; 184 mm print width.
- Design revision: bilateral physical topside symmetry. Approved reference v033 remains unchanged and needs a matching revision before it represents description v20 fully.
- Status: generated and visually reviewed; not promoted.
- Generated source: /Users/gmahoney/.codex/generated_images/01a0e10a-e606-7a60-ac77-8792df2504bc/exec-cb6561d7-a6b6-4420-92ea-387a683c69dd.png, native 1536 × 1024.
- Delivery: image.png, Lanczos upscaled to 2160 × 1440, density 298.173913 pixels/inch for 184 mm print width. Not native 2160 × 1440 generation.
- Visual review: paired longitudinal recessed deck panels and stepped structures now flank a continuous central spine. Far-side structure is partially occluded. Engine alignment, compact pods, cockpit, cargo door and small lower-right arid planet are visually retained. This is a visual symmetry correction, not a measured CAD projection.

## Print export replay

```sh
magick /Users/gmahoney/.codex/generated_images/01a0e10a-e606-7a60-ac77-8792df2504bc/exec-cb6561d7-a6b6-4420-92ea-387a683c69dd.png -filter Lanczos -resize 2160x1440 -units PixelsPerInch -density 298.1739130435 outputs/antares-beauty-shot/v006/image.png
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

Image 1 is STYLE: canonical_style_reference.png. Match its rendering technique only; ignore its people and setting.
Image 2 is EDIT TARGET: the user-approved Antares beauty shot v005. Edit this composition locally.

Antares identity: broad low ivory utilitarian spacecraft, faceted wedge cockpit with brick-red roof and centered circular hatch, stepped upper hull and raised fore-aft central spine, recessed gray panelled deck, articulated shoulders and closed port-side cargo door. Two compact cylindrical orange-red and ivory outboard engine pods, with dark intake cones and approved fore-aft alignment.

Use case: precise-object-edit.
User request: "Good. Now make the topside of the ship symmetrical."

Repaint ONLY the upper deck structures behind the cockpit to make the ship's topside physically BILATERALLY SYMMETRICAL across its longitudinal centerline. Establish the single central spine on the axis through the cockpit roof hatch and the midpoint between the engine mounts. Keep one raised central spine with its centered rear vent. On either side of it, mirror the same detailed sequence of ivory shoulder steps, raised blocks, recessed gray deck panels, outer rails, transverse bridges and rectangular openings. Corresponding port/starboard features must have equal physical widths, heights, lengths, and identical fore-aft positions. Make the two sides unmistakably the same structural design. Retain the existing detailed stepped industrial character.

This is symmetry of the THREE-DIMENSIONAL OBJECT, correctly projected in the existing three-quarter camera view. The far-side geometry is foreshortened and partly occluded naturally by the central spine. Do NOT mirror screen pixels, rotate the ship, change camera elevation, or make a top-down view. Keep all fore-aft edges coherent with the existing ship axis. Do not simplify the whole roof into a plain slab or add extra stacked levels.

Preserve the cockpit and hatch, hull silhouette, lower side walls and cargo door, both complete engine pods with their current diameter, compact length, exact orientation and mounting positions. Preserve ship scale and position in frame, lighting, palette and detailed painted treatment. Keep the starfield and the small dry ochre/terracotta planetary limb restricted to the LOWER-RIGHT CORNER exactly as in image 2; no water or clouds, no enlargement of the planet. No text, border or additional objects.
Output 2160 × 1440 pixels, 3:2 landscape.
Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.
