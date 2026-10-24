# antares-ringed-planet-beauty v004

User request verbatim: the jet from the rightmost engine is not cleatly coming out of it. It almost looks like its coming out of the center.
Mode: Targeted edit of v003 (user-designated baseline): re-root both exhaust trails at their own pods' nozzle openings, on the pod axes. Everything else preserved.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0ebbb-0f9a-7f31-bb86-38a240e05571/exec-509e5636-bd7c-4bbd-a6f4-4acd6b3344bd.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/antares-ringed-planet-beauty/v003/image.png
Date: 2026-09-28
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.76 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: TODO — fill in

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

Image 1 is STYLE: Match its hand-painted matte rendering technique only. Ignore its subjects.
Image 2 is EDIT TARGET: the Antares beauty shot v003. This is the image being modified; preserve everything the prompt does not explicitly change.

TASK: This is a targeted edit of image 2. Change ONE thing: where the engine trails attach. Everything else in image 2 must be preserved exactly — the hull, its structure and panel detail, the cockpit, the cargo door, the planet, the stars, the background, the camera angle, the composition, the colors and the lighting are all already correct and must not be redrawn or shifted.

THE PROBLEM: the trail behind the near (right-hand, lower) engine pod does not clearly emerge from that pod's nozzle. It currently appears to start above and inboard of the pod, so it reads as exhaust venting from the middle of the hull rather than from the engine.

THE FIX: each trail must begin AT the dark circular nozzle opening in the aft end of its own engine pod, and nowhere else.
- The root of each trail is the same width as that pod's nozzle opening and sits centered on it, physically touching it, with no gap and no offset. The nozzle opening remains visible as the dark circular aft face of the pod; the trail starts at its rim.
- Each trail runs straight back along that pod's own cylindrical axis, parallel to the ship's fore-aft line — the same axis the pod is drawn on. It does not angle inward toward the hull centerline, does not cross the hull, and does not start anywhere on the hull.
- The near pod's trail belongs to the near pod and the far pod's trail belongs to the far pod. Because the near pod sits lower and further right, its trail sits lower and further right than the far pod's, and the two trails stay clearly separate along their whole length.
- No exhaust, plume, streak or haze emerges from any part of the hull, the roof, the spine, the cargo door, or the gap between the pods.

TRAIL RENDERING (unchanged from image 2): two or three flat opaque tapering shapes with hard straight edges — a brighter ivory-ochre core shape and one muted slate outer shape — narrowing as they recede. Painted shapes, not light: no glow, no bloom, no halo, no soft or feathered edges, no transparency gradient, no particles.

Do not add rings, do not add detail to the planet, do not change the crop.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
