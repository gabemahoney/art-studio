# hegemony-assault-ship v002

User request verbatim: Now we need an image for Scene 6. I think its The Antares, flyig through the storm, maybe inside a ravine, with two assault ships chasing it.
Mode: New asset, sheet v1 (design proposed by Claude; no Hegemony ship design existed). Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10433-9d54-7de1-98db-c38d8836c5f7/exec-2a52abd9-e389-4e81-912e-dbaa60427182.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.69 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: REJECTED by user: 'Looks too much like a jet.'

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

TASK: A reference sheet of the Hegemony assault ship.

SUBJECT DESIGN (description v1, restated so nothing is invented):
The Hegemony's storm-patrol gunship: a two-seat atmospheric interceptor built to hunt
unauthorized flights through Kalagra's planet-wide storm. Two of them chase the
Antares as she climbs out. *(Whole design provisional — first pass.)*

## Exterior

- Small and predatory beside the Antares — about half her length.
- A long, narrow arrowhead hull: a sharp pointed nose, a slim fuselage, and two
  short downswept wings set far back, angular and blade-like.
- A single narrow canopy of dark tinted glass set low on the nose, two seats in
  tandem.
- Two twin-barrel laser cannons slung under the nose, pointing forward.
- One large round engine in the tail, glowing hard white-blue when firing; two small
  vertical tail fins, splayed outward.
- Hard, flat, armoured panels with straight seams; no curves except the engine.

## Colour

- Dark gunmetal grey hull, matte, weathered by sandstorms.
- One thin blood-red stripe along each flank from nose to tail, and a red band
  around the engine housing — the Hegemony's marking.
- No lettering, numbers or insignia text.

A single reference sheet on a plain flat mid-grey background, a 3:2 horizontal
rectangle. No text, labels, arrows or frames.

The same ship in four views at one consistent scale, separated by empty grey:
- LEFT HALF, largest: a three-quarter view from in front, above and to the left, in
  flight, its engine glowing.
- Upper right: a side elevation, nose to the left.
- Middle right: a top-down plan view, nose to the left.
- Lower right: a head-on front view.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
