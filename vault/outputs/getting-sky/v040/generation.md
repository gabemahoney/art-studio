# getting-sky v040

User request verbatim: Can we try another pass on the canyon that has a color that will make both the Antares and the Hegemony ship pop? / the Hegemony symbol on the top of the Hegemony ship is grey. It should be red.
Mode: Recolour off v038: palette a (ochre sandstorm); gunship star red.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a1093a-34ee-74b0-9671-c3b755a97ab1/exec-050f1f64-9698-405b-981a-d814d41c68aa.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/getting-sky/v038/image.png
Date: 2026-10-04
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.61 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: REJECTED by user: too monotone (and v040 yellow — storm turned yellow, wrong). Gunship star fix praised.

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

1. Recolour the canyon and sky so both ships stand out: the storm becomes a dusty
   OCHRE sandstorm — the air and the lit cliff faces pale warm ochre and sand, the
   shadowed rock a deep warm umber-brown, the sky between the cliffs a churning
   amber-grey with pale lightning. The black assault ship now reads as a dark shape
   against the pale haze; the ivory Antares reads against the deeper rock below her.
2. The star on the top of the black assault ship is bright red.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
