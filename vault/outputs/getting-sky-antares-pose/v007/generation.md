# getting-sky-antares-pose v007

User request verbatim: v2 (upper atmosphere approved; next: the Antares climbing out)
Mode: Pose: climbing to upper right; fan intakes forward, rear caps toward viewer. Roll 1 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a109cf-44c3-7031-b284-b77f261a7080/exec-3ebdf0bc-3cd1-43ce-b7f3-639a4e876d90.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/ships/the_antares/reference.png; frozen assets/ships/the_antares/candidates/v033/image.png
Date: 2026-10-04
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.96 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: pending — record with bin/review.py once you have seen it

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

Image 1 is STYLE: Match this image's rendering technique only. Ignore its people, clothing, equipment, and setting.
Image 2 is IDENTITY: The Antares reference sheet. Copy its design exactly; ignore the sheet layout.

TASK: A single flight view of the Antares on plain grey.

ONE single view of the Antares (image 2) on a plain flat mid-grey background, a 3:2
horizontal rectangle. No other objects, no text.

She is climbing steeply toward the UPPER RIGHT of the picture: cockpit nose to the
upper right, tail to the lower left. Seen from her left side and slightly below.

ENGINES, exactly as image 2's front view shows: each pod's round FAN INTAKE is at its
FRONT, facing the same way as her nose — toward the upper right. From this angle the
fans face away from us and are hidden or seen only edge-on; what we see at the lower
left is the BACK of each pod: a plain closed rear cap with a dark exhaust nozzle. The
two pods are a matched pair at the very rear of the hull. No exhaust flames.

Her design exactly as image 2. She fills about the middle half of the picture.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
