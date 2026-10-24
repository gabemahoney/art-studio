# the-rusty-robot v093

User request verbatim: v91 is it. Can we add some passersby on the street so it does not look so empty? They should be non-descript.
Mode: Edit off v091 (user-approved base): five or six nondescript pedestrians along the street to the right. Roll 1 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a1041e-b654-7dd0-b189-8d8dd93f072c/exec-87967f65-349d-4e03-be03-9126a3c55bc1.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v091/image.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.01 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Six nondescript coated pedestrians down the street to the right, nearest beside the cantina's right steps wall; crew, cantina and framing held. The crew read slightly brighter than v091.

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

TASK: Add passersby to this street scene.

Reproduce image 2 exactly and add a few passersby on the street.
- Five or six ordinary pedestrians, nondescript: plain dark coats and clothes in muted
  colours, no distinctive features, faces mostly in shadow or turned away.
- Spread along the street to the right of the cantina, walking, at varying distances
  down the receding street — the nearest no closer than the cantina's steps, most of
  them further away and smaller. To scale with the buildings.
- Nobody on the cantina's steps, and nobody in the alley or near the three crew.
- Dimly lit like the rest of the street; the crew and the cantina entrance stay as
  they are.
Everything else stays exactly as it is.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
