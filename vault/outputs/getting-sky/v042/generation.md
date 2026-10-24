# getting-sky v042

User request verbatim: Naw...too monotone and yellow. The storm also became yellow. That's definitely wrong. How about some dark blues and purples?
Mode: Recolour off v038: dark blues and purples, lighter haze behind the gunship; gunship star red. Roll 1 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a1093d-2c24-74f1-a2ad-94922f8b75b1/exec-9c3c4dff-ac7f-4e0a-bbeb-76c29971c198.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/getting-sky/v038/image.png
Date: 2026-10-04
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.42 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: REJECTED by user ('No. Not good.'); back to the v038/v039 slate palette.

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

TASK: Recolour this storm scene.

Reproduce image 2 exactly — the same gorge shapes, the same two ships in the same
places, sizes and angles, the same exhaust trails. Change only two things.

1. Recolour the canyon and storm in DARK BLUES AND PURPLES, with variety: deep indigo
   and blue-black rock in shadow; cliff faces catching the lightning in cool violet and
   steel blue; the storm sky a churning mix of dark purple and navy cloud, lit by pale
   violet-white lightning; blowing sand a dusky lavender-grey haze, lighter in the air
   between the ships than on the rock, so the black assault ship stands out as a dark
   shape against it. The ivory-and-orange Antares and her orange flames glow warm
   against the cool palette. Cold violet light rims the black ship's edges.
2. The star on the top of the black assault ship is bright red.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
