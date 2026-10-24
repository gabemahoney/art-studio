# getting-sky-antares-pose v004

User request verbatim: The engines dont look entirely symmetrical. The right one is too far foward.
Mode: Pose again: pods as a matched pair at the rear, no flames (flames added later). Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10891-9610-7261-aa03-0a56018a249f/exec-52df121a-3bc2-42ec-9537-a8f8edddb8a3.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/ships/the_antares/reference.png; frozen assets/ships/the_antares/candidates/v033/image.png
Date: 2026-10-04
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.64 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
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

She is in flight, coming toward us on a diagonal: her cockpit nose points toward the
LOWER RIGHT of the picture and toward the viewer, her tail toward the UPPER LEFT. Seen
from in front and slightly above, looking at her nose, windscreen and port side with
the cargo door. Level, not banked.

ENGINES — the two pods are a matched pair, mounted opposite each other at the SAME
point along the hull, at the very REAR of the ship, behind the cargo door. A straight
line joining the centres of the two pods crosses the hull at right angles to its
length. In this view the far pod is therefore further up and to the LEFT than it
would be if it sat beside the cockpit: it sits behind the hull's rear shoulders, well
behind the cockpit and behind the cargo door. Both fan intakes face forward. No
exhaust flames at all.

Her design exactly as image 2. She fills about the middle half of the picture, plain
grey all around.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
