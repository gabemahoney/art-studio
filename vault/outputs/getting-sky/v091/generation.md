# getting-sky v091

User request verbatim: There is sort of a halo around the right side of the ship now, on the rocks. Can we get it to look just like 85 did there?
Mode: Edit off v090: repaint the halo band around the Antares; only that band will be kept. Roll 1 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10cc5-6995-77f2-b568-9377c8ce3f36/exec-b303e2b7-c2a9-4e23-a8ec-1f9b0fb9d88b.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/getting-sky/v090/image.png
Date: 2026-10-05
Status: approved and promoted to final.png on 2026-10-05. User approval: "Lets do 91. Promote it and add it to the PDF"
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.26 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Edit off v090: halo gone — rock and blowing sand around the Antares's nose now continuous, like v085. Rest held (whole-frame diff 2.5/255; ships, trails, lasers checked). Taken whole.

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

TASK: Remove a halo from this scene.

Reproduce image 2 exactly. Change only the rock and blowing sand immediately around
the cream-and-orange ship on the right, especially above and to the right of its nose:
there is a faint outline/halo there, the ghost of an earlier position of the ship.
Repaint that area as continuous canyon rock and blowing sand, matching the rock
around it, with no outline, no halo and no glow around the ship. Do not change the
ship itself, its trails, the red lasers, the other ships or anything else.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
