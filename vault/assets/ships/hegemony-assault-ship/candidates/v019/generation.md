# hegemony-assault-ship v019

User request verbatim: Unfornutately they look cartoonish.
Mode: Edit off approved v014: a few whole plates worn blood-red, no outlines. Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a109c5-69ec-7e11-bf71-736c8357f905/exec-f0b9521f-eda8-4d67-9d98-60f1f8ef2e29.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: assets/ships/hegemony-assault-ship/reference.png; frozen assets/ships/hegemony-assault-ship/candidates/v014/image.png
Date: 2026-10-04
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.88 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Worn red plates, no outlines. Superseded: user switched the scene concept before choosing; v014 stays the reference.

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

TASK: Repaint the livery on this ship reference sheet.

Reproduce image 2, the reference sheet, exactly — every view, the ship's shape,
proportions and layout unchanged. Change only the paint, in all four views, to add
more red in a gritty, military way:
- A few whole armour plates are painted dark blood-red: the two big plates either side
  of the cockpit on the nose, and the large plate behind the star on the top deck.
  The rest of the hull stays matte black.
- The red paint is old and worn: chipped along the plate edges, scuffed and
  sand-blasted, with black showing through, streaked with grime — the same weathering
  as the rest of the hull.
- No outlines, no pinstripes, no trim along the edges.
- The thruster bands and the star stay red.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
