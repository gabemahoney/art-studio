# the-rusty-robot v095

User request verbatim: can u make them look a little more sci fi? The silhoueetes? Their clothes look a little mundane.
Mode: Edit off v094: passersby given sci-fi silhouettes (collars, hoods, wraps, mask, helmet, backpack unit). Roll 1 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10425-0b67-7651-8482-6b8433b4dfce/exec-45482403-c264-4d1f-ae78-092ab86b0ff9.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v094/image.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.94 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Passersby given sci-fi silhouettes: high collars, wraps, a round helmet, a backpack unit with antenna; rest held.

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
Image 2 is EDIT TARGET: This is the image being modified. Preserve everything the prompt does not change.

TASK: Revise the passersby in this street scene.

Reproduce image 2 exactly and change only the passersby walking down the street.
Keep their number, positions, sizes and dim lighting; they stay anonymous, faces in
shadow or turned away. Give them science-fiction silhouettes instead of ordinary
coats:
- high stiff collars and hoods, long asymmetric wraps and tabards, angular shoulder
  plates;
- one with a breathing mask, one with a small round helmet, one with a backpack
  unit with a short antenna;
- muted colours, simple shapes — readable as people of a future city at a glance.
The three crew in the alley, the cantina and everything else stay exactly as they
are.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
