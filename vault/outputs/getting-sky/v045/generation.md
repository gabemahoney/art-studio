# getting-sky v045

User request verbatim: Maybe we could go back to the original v39 color scheme, I did like it. Could we add a red trim around the Hegeomny ship to make it stand out. Like maybe some kind of rad force field.
Mode: Edit off v038 (original slate palette): red force-field outline around the gunship, red star. Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10940-bfd8-7900-8d89-f583ed721297/exec-7aca804c-d892-434c-b84e-5368d34e9efc.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/getting-sky/v038/image.png
Date: 2026-10-04
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.27 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: User: 'it does not look good.' Shield halo rejected; adding more red to the ship's livery instead.

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

TASK: Add a red energy shield to the assault ship in this scene.

Reproduce image 2 exactly — the same gorge, colours, storm, the same two ships in the
same places, sizes and angles, the same exhaust trails. Change only the black assault
ship (upper left):
- Wrap it in a red energy shield: a thin shell of red light a short distance out from
  its hull, following its whole outline — around the hull and all four thruster pods.
  Painted flat: a bright red edge with one darker red band inside it, broken here and
  there by blowing sand. It makes the ship stand out from the dark rock behind it.
- The star on the top of its hull is bright red.
Nothing else changes.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
