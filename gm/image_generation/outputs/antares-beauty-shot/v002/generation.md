# Antares beauty shot v002

## User request (verbatim)

[Image #1] I dont know if this will help? I did a 3d render. You can ignore the fine grained details, but can you use this 3d alignment as a basis for a new render? Maybe having this correctly aligned model can help you get the perspective correct.

## Generation

- Mode: style-transfer repaint of user-designated 3D render; new beauty-shot version
- Tool: built-in image_gen.imagegen; underlying model not exposed
- Style: v2
- Design context: Antares description v19 = assets/ships/the_antares/description_versions/description-v19.md. For this render, the user's newly supplied 3D image explicitly overrides prior inferred camera/engine proportions. This is not a canonical-reference promotion or a redesign of the global description.
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png (style v2; immutable snapshot style_versions/canonical_style_reference-v2.png)
- Image 2 EDIT TARGET: assets/ships/the_antares/sources/user-3d-alignment-2026-09-27.png, untouched copy of /Users/gmahoney/Screenshots/Screenshot 2026-09-27 at 15.40.07.png, user-provided geometric authority
- No old sheet or rejected generation attached; the new user model supplies the required geometry directly.
- Requested delivery: 2160 × 1440 pixels, 3:2; 298.173913 dpi at 184 mm width
- Status: generated and visually reviewed; not promoted
- User source MD5: d80e55e3b1afcd3f842a3c19ad9d7d8b
- Generated source: /Users/gmahoney/.codex/generated_images/01a0e10a-e606-7a60-ac77-8792df2504bc/exec-101acba6-a78f-4803-80a0-9d812f66a6d8.png (1536 × 1024)
- Delivery: image.png, Lanczos upscaled to 2160 × 1440; density 298.173913 pixels/inch for 184 mm width. Not native 2160 × 1440 generation.
- Visual check: source three-quarter camera, hull profile, roof masses, outboard mounts and complete engine orientations carried into the painted result. Glossy 3D lighting replaced with matte broken paint planes; studio ground removed for space backdrop. Surface grilles and fittings remain somewhat more literal than the simplified prompt. Geometry correspondence judged visually, not pixel-exact.

## Print export replay

```sh
magick /Users/gmahoney/.codex/generated_images/01a0e10a-e606-7a60-ac77-8792df2504bc/exec-101acba6-a78f-4803-80a0-9d812f66a6d8.png -filter Lanczos -resize 2160x1440 -units PixelsPerInch -density 298.1739130435 outputs/antares-beauty-shot/v002/image.png
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

Image 1 is STYLE: canonical_style_reference.png. Match its hand-painted rendering technique only. Ignore its people, clothing and setting.
Image 2 is EDIT TARGET: the USER'S CORRECTLY ALIGNED 3D MODEL of the Antares. This is the authority for the entire ship's perspective and geometry. Repaint this view into image 1's matte gouache medium, preserving the model's camera angle, silhouette, hull proportions and both complete engine pods.

Antares identity: a broad low ivory utilitarian spacecraft, faceted wedge cockpit, dark angular windows, red-orange cockpit roof surrounding a circular hatch, raised ivory central spine and a broad closed top-hinged cargo door on the visible lateral side. Two red-orange cylindrical engines with ivory bands, dark front openings and short dark aft nozzles sit on outboard mounts.

PRIMARY TASK: create a new single-image painted spacecraft beauty shot using the supplied 3D render as a geometric underdrawing. Preserve the model's actual outlines, front and rear engine center positions, complete barrel lengths and diameters, mounting locations, intake-plane orientations and the perspective shared with the hull. Follow the pixels of image 2 for these relationships. Do not solve the engine angles again from text. Do not turn either intake towards the camera. Do not squeeze either opening, lengthen a barrel, move a pod or adjust the camera. Both engines must remain the same correctly aligned solids shown by the user.

Change the MEDIUM, not the geometry: replace smooth specular highlights, gradients, shiny cylinders and 3D surface finish with a few opaque flat gouache planes and coarse broken brush edges at image 1's brush scale. The user allows minor surface details to be simplified: vents become dark painted blocks, hinges and fittings become a few broad marks. Retain the roof masses, layered hull shoulders, central spine, cargo door, cockpit and livery of the model. No additional structures, raised-block redesigns, new wings or extra engines. Do not copy the model's glossy lighting.

Scene: a clean beauty shot of this single ship coasting in deep space, with a restrained dark slate-blue painted background and just a few small quiet ivory stars. Remove the studio floor and ground shadow. Warm ivory upper hull, cool dark underside in broad flat values. No glow, rim light, lens flare, planets, other ships, people, labels, captions or watermark.
Composition: same front-port three-quarter angle as image 2, entire ship visible, nose lower left and engines upper right. Center the ship within a 3:2 landscape canvas with breathing room at all extremities; uniform repositioning/scaling of the whole ship is fine, but all internal perspective and proportions remain locked to image 2.
Deliver at exactly 2160 × 1440 pixels for printing at 184 mm wide, approximately 298 dpi.
Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.
