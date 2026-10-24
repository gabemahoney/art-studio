# getting-sky v009

User request verbatim: Thats getting there. The composition needs to be more dynamic though. The ships flying at dramatic angles like in the first few. Also, make sure the projectiles are shooting in a straight line from the barell of the gun through the tip.
Mode: Fresh: diagonal diving chase toward camera, steep banks; bolts along each barrel's axis. Roll 1 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a104e8-dd52-7fa1-bc8b-1e7b1091f703/exec-f8d3a6f2-298a-437b-baac-2efbc8d3440a.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/ships/the_antares/sources/hero-crop-from-reference.png
- Image 3 IDENTITY: assets/ships/hegemony-assault-ship/sources/hero-crop-from-reference.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.69 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: Diving diagonal chase, steep banks. Antares spot-checked at 140%: cockpit nose leads, side cargo door, both pods at the rear with fan faces aft, matches reference. Near gunship 4 pods; FAR gunship shows only 3 pods (4th missing). Bolts leave the near gunship along its barrels, but the bolts streaking past the Antares don't line up with any gun.

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
Image 2 is IDENTITY: The Antares. Copy its design exactly; engines at the rear.
Image 3 is IDENTITY: The Hegemony assault ship. Copy its design exactly.

TASK: A single scene illustration: the Antares fleeing two Hegemony assault ships through a storm gorge at night.

ONE single continuous scene illustration, a 3:2 horizontal rectangle. No panels,
borders or text.

Night, in the heart of a planet-wide storm. A narrow, twisting gorge between towering
black cliffs; wind-driven sand in grey curtains; lightning in the strip of sky throws
cold blue-white light on the cliff faces. Dark slate, storm blue and black, with warm
light only from engines and gunfire.

A dramatic, diagonal chase. The camera is low in the gorge, looking up the line of the
chase as it dives and banks toward us from upper left to lower right:
- The Antares (image 2) nearest the camera, lower right, banked steeply about 30
  degrees, diving out of a turn, seen in strong three-quarter perspective — cockpit
  nose leading toward lower right, engine pods at her rear, exhausts flaring behind.
- Two Hegemony assault ships (image 3) behind her at upper left, each banked and tilted
  at a different steep angle as they swing round the bend, noses pointed at her.
- GUNFIRE: each gunship fires its two chin guns. Every projectile is a small glowing
  red bolt with a thin straight trail, travelling along the exact line of the barrel
  it came from — the line through the barrel's base and its muzzle tip, extended
  straight out. Each pair of trails runs parallel, continuing its barrels' axis, and
  heads toward the Antares; some bolts flash just past her.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
