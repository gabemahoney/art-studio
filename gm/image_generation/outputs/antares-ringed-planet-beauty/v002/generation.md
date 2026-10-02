# antares-ringed-planet-beauty v002

User request verbatim: by the the image needs to be landscape... [reverses the earlier 4:5 portrait spec]
Mode: Landscape rebuild of v001. New camera (hull horizontal across a wide frame), not a crop. Ring occlusion behind the planet limb made explicit after v001 painted bands across the rock.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 2160x1440, actual 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0eba2-ca8f-7d70-961a-f101e473ab39/exec-257bf59b-2c82-428c-b3d2-7f90716a5038.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/ships/the_antares/reference.png; frozen assets/ships/the_antares/candidates/v033/image.png
Date: 2026-09-28
Delivered: delivered-1536x1024.png, 1536x1024, sRGB 8-bit PNG-24 no alpha, flattened onto #1b1e26, 2.20 MB; scaled to fit from raw 1536x1024
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered (superseded): delivered-1200x800.png, 1200x800, sRGB 8-bit PNG-24 no alpha, flattened onto #1b1e26, 1.37 MB; scaled to fit from raw 1536x1024
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

Image 1 is STYLE: canonical_style_reference.png. Match its hand-painted matte rendering technique only. Ignore its people, clothing, equipment and setting entirely.
Image 2 is IDENTITY: the approved Antares reference sheet. Copy this ship's design exactly — silhouette, proportions, hull structure, color placement, engine geometry. Ignore its sheet layout, its blue backing panel, and its multiple orthographic views; you are painting ONE view of this ship, not a sheet.

TASK: A single horizontal beauty shot. The Antares in flight above a barren ringed planet.

SHIP DESIGN (from image 2, restated so nothing is invented):
A broad, low utilitarian workhorse with a wedge-shaped cockpit nose, a raised central spine along the roof, recessed panelled deck surfaces either side of that spine, and articulated ivory shoulders. Hull is ivory and light gray. Cockpit upper panels and the rear engine housings are orange-red. Windows and engine openings are dark. A circular hatch sits on the cockpit roof inside its orange roof panel. One broad rectangular cargo door on the lower port side wall, closed, with its dark perimeter seam and two recessed grips.
Two outboard engine pods: compact squat round drums, roughly 1.4 diameters long including the short aft nozzle — never long nacelles. Both pod axes run parallel to the central spine and to the straight fore-aft deck edges. Intake rims, hub, ivory bands and aft nozzle share one coherent cylindrical projection with circular cross-sections. Mounting bridges span outward from the narrower aft hull. No outward yaw, no independent pitch.

FRAMING (this is a 3:2 WIDE LANDSCAPE frame, wider than it is tall):
Three-quarter view from slightly below and ahead, the ship travelling to the left across the frame. The long axis of the hull runs broadly horizontal, using the full width of the wide frame — this is a landscape-proportioned ship in a landscape-proportioned frame, so let it stretch across. The ship occupies the upper two thirds. Keep the entire hull and all readable structural detail well inside the frame — nothing important near any edge, nothing cropped.

SETTING:
Below and behind, a barren airless planet — dead gray-ochre rock, flat cratered plains, no water, no vegetation, no city lights. Its planetary ring system crosses the lower frame as a few flat hard-edged bands of muted ochre and slate, thin and taut, seen at a shallow angle. The bands pass BEHIND the planet's body: where a band meets the planet it is cleanly interrupted and hidden, never painted across the rock. The planet's limb is a clean angular arc. Deep near-black space above, dark enough to sit comfortably against a very dark page. A handful of stars at most, painted as single flat dots — not a dense starfield. One directional light source from the upper right: lit planes ivory, shadowed planes one flat darker slate step. No engine glow bloom, no lens flare, no atmospheric haze, no nebula.

Not a reference sheet. No orthographic views, no insets, no labels, no borders, no signature.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
