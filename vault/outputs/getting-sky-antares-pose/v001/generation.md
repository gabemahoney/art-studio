# getting-sky-antares-pose v001

User request verbatim: yes (plan: paint the Antares alone at the canyon's angle, paste into the gorge, blend pass)
Mode: Layer 2 step 1: Antares alone on grey, nose to lower right toward viewer. Roll 1 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a1087f-20bc-7c20-a166-fe77a99e61e8/exec-8fb17300-a23a-4dbd-abf8-5b1606ca6e49.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/ships/the_antares/reference.png; frozen assets/ships/the_antares/candidates/v033/image.png
Date: 2026-10-04
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.63 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
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
LOWER RIGHT of the picture and toward the viewer, her tail toward the UPPER LEFT. We see
her from in front and slightly below, looking at her nose, windscreen and her port
side with the cargo door. Banked a little.
- Exactly TWO engine pods, one on each side at her REAR, their fan intakes facing
  forward, short orange exhaust flames trailing from their backs toward the upper left.
- Her design exactly as image 2: proportions, colours, cockpit, spine, cargo door.
- She fills about the middle half of the picture, with plain grey all around.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
