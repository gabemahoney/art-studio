# antares-ringed-planet-beauty v001

User request verbatim: As the first test, I want a beauty shot of the Antares flying over a barren planet with planetry rings. [4:5 portrait, 1200x1500, sRGB no alpha, flatten onto #1b1e26, under 2.5MB, hull 30px off all edges]
Mode: First generation via bin/gen.py. Codex backend (API has no credits). Prompt relayed from disk into the image_gen tool argument so the Style Block is verbatim.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1920, actual 1122x1402 (built-in image_gen chose its own size; aspect 0.800 matched 4:5)
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0eb9c-c93b-75a3-8365-9723c602cb56/exec-01161f57-3a11-42ff-91d4-8ef0e40b493c.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/ships/the_antares/reference.png; frozen assets/ships/the_antares/candidates/v033/image.png
Date: 2026-09-28
Status: awaiting user evaluation
Output: image.png, 1122x1402 (raw model output, frozen)
Delivered: delivered-1200x1500.png, 1200x1500, sRGB 8-bit PNG-24 no alpha, flattened onto #1b1e26, 2.23 MB; scaled to fit from raw 1122x1402
Review: Spec met — 1200x1500, sRGB 8-bit, no alpha, 2.23 MB, corner reads srgb(30,35,47). Identity holds: ivory stepped hull, orange-red cockpit roof panel with circular hatch, dark windows, single lateral cargo door with top hinge and two grips, two compact outboard drums with axes parallel to the spine. Barren cratered planet and flat hard-edged ring bands both present, unlike the six landscape candidates in outputs/antares-beauty-shot/ whose receipts requested rings that never appeared. Departures from the brief: the nose reads level rather than high, and the ring bands cross the planet disc without clear occlusion. Raw output was 1122x1402, so the deliverable is a 1.07x upscale — request a larger raw next time. Hull clears all edges; nearest approach is the nose at roughly 45 px. Awaiting user evaluation.

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

Image 1 is STYLE: canonical_style_reference.png. Match its hand-painted matte rendering technique only. Ignore its people, clothing, equipment and setting entirely.
Image 2 is IDENTITY: the approved Antares reference sheet. Copy this ship's design exactly — silhouette, proportions, hull structure, color placement, engine geometry. Ignore its sheet layout, its blue backing panel, and its multiple orthographic views; you are painting ONE view of this ship, not a sheet.

TASK: A single vertical beauty shot. The Antares in flight above a barren ringed planet.

SHIP DESIGN (from image 2, restated so nothing is invented):
A broad, low utilitarian workhorse with a wedge-shaped cockpit nose, a raised central spine along the roof, recessed panelled deck surfaces either side of that spine, and articulated ivory shoulders. Hull is ivory and light gray. Cockpit upper panels and the rear engine housings are orange-red. Windows and engine openings are dark. A circular hatch sits on the cockpit roof inside its orange roof panel. One broad rectangular cargo door on the lower port side wall, closed, with its dark perimeter seam and two recessed grips.
Two outboard engine pods: compact squat round drums, roughly 1.4 diameters long including the short aft nozzle — never long nacelles. Both pod axes run parallel to the central spine and to the straight fore-aft deck edges. Intake rims, hub, ivory bands and aft nozzle share one coherent cylindrical projection with circular cross-sections. Mounting bridges span outward from the narrower aft hull. No outward yaw, no independent pitch.

FRAMING (this is a 4:5 tall portrait frame):
Three-quarter view from slightly below and ahead, nose high and to the upper left, hull climbing away from the viewer, so this landscape-proportioned ship fills a tall frame. The ship occupies the upper two thirds. Keep the entire hull and all readable structural detail well inside the frame — nothing important within a generous margin of any edge, nothing cropped.

SETTING:
Below and behind, a barren airless planet — dead gray-ochre rock, flat cratered plains, no water, no vegetation, no city lights. Its planetary ring system crosses the lower frame as a few flat hard-edged bands of muted ochre and slate, thin and taut, seen at a shallow angle. The planet's limb is a clean angular arc. Deep near-black space above, dark enough to sit comfortably against a very dark page. A handful of stars at most, painted as single flat dots — not a dense starfield. One directional light source from the upper right: lit planes ivory, shadowed planes one flat darker slate step. No engine glow bloom, no lens flare, no atmospheric haze, no nebula.

Not a reference sheet. No orthographic views, no insets, no labels, no borders, no signature.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
