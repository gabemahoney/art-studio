# rusty-robot-street v013

User request verbatim: you decide. you are learning, and wil update the skills if you learn something useful
Mode: Edit off v010 (Codex, free): regular dome lattice. Only the sky, inside a mask following the rooftops and skyline, will be kept.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a103ff-52b4-7113-88be-e7c031015ffd/exec-b1c4a6cf-2e71-4800-9567-9db36ade31c0.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: assets/locations/rusty-robot-street/candidates/v010/image.png
Date: 2026-10-03
Status: approved and promoted to reference.png on 2026-10-03. User approval: "actually 13 looks better. Ther eis an artifact above one of the buildings in 14."
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.07 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Codex edit off v010: regular lattice. Whole frame repainted; only the sky inside a mask following the rooftops and skyline is used, in v014.

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

Image 1 is STYLE: Match its hand-painted matte rendering only. Ignore its subjects.
Image 2 is EDIT TARGET: The street view being revised. Preserve everything the spec does not change.

TASK: Revise the dome lattice in this street illustration.

Reproduce image 2 and change ONE thing: the city dome's structural ribs in the sky.
Keep everything else exactly as it is — every building, the Rusty Robot, the street,
the distant domed towers, the painting style and the night palette.

The dome is one huge regular lattice seen from below, close overhead:
- MERIDIAN ribs: thick dark bands that all converge toward a single point high above
  the top of the picture, fanning out evenly as they come down — like the spokes of an
  umbrella seen from beneath.
- RING ribs: thick dark bands crossing the meridians as smooth concentric arcs, evenly
  spaced, each curving the same way.
- Every rib is the same thickness and meets its neighbours at a clean crossing. No rib
  runs at an odd angle, stops short, or comes down into the city.
Deep night blue between the ribs.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
