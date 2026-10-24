# getting-sky v001

User request verbatim: Now we need an image for Scene 6. I think its The Antares, flyig through the storm, maybe inside a ravine, with two assault ships chasing it. Its still in the kalagra planet atmosphere.
Mode: Fresh scene: hero crops of the approved Antares and assault ship, storm from the-ride-out. Roll 1 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a104d8-8472-7922-82ad-75e94fe6c411/exec-d728ece8-10ed-4a62-93da-1b998b93c415.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/ships/the_antares/sources/hero-crop-from-reference.png
- Image 3 IDENTITY: assets/ships/hegemony-assault-ship/sources/hero-crop-from-reference.png
- Image 4 IDENTITY: outputs/getting-sky/kalagra-storm-from-the-ride-out.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.75 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: REJECTED by user: 'no thats garbage'.

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
Image 2 is IDENTITY: The Antares. Copy its design exactly.
Image 3 is IDENTITY: The Hegemony assault ship. Copy its design exactly.
Image 4 is IDENTITY: Kalagra's storm. Copy its sky, lightning and palette only.

TASK: A single scene illustration: the Antares chased through a storm canyon by two Hegemony assault ships.

ONE single continuous scene illustration, a 3:2 horizontal rectangle. Not a reference
sheet: no panels, borders, captions or text.

Night, inside the planet-wide storm on Kalagra. The Antares (image 2) races through a
deep, narrow canyon cut into a crater wall, banking hard, its engines blazing. Two
Hegemony assault ships (image 3) chase her down the canyon behind, firing red laser
bolts that streak past her.

- The Antares is in the foreground, three-quarter view, sharp and clear.
- The two assault ships are behind her, smaller with distance, one higher than the
  other.
- Sheer rock canyon walls on both sides, lit by lightning; sand and wind whip through
  the canyon; the storm sky churns overhead, as in image 4.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
