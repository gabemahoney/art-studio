# the-job-the-pad v002

User request verbatim: It got the ship geometry totally wrong. Have it more zoomed out, too. Kia should be smaller in the scene. / I think it probably just needs the 3/4 view.
Mode: Fresh pass, not an edit of v001: IDENTITY narrowed to a hero 3/4 crop of reference.png (= the_antares/candidates/v033) instead of the full multi-view sheet; design text distilled to scene-relevant geometry with explicit matched-pair pod placement; camera pulled well back; Kia reduced to ~1/10 frame height; plumes restated as flat opaque wedges and sky as flat masses
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0ee5a-8d1d-7ca3-bbd8-c9b60e7e3d5e/exec-18d039c5-4c8d-43b1-a554-8d245594b908.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/ships/the_antares/sources/hero-3q-crop-from-v033.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.41 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Ship geometry corrected — the two engine pods now read as the matched aft pair in the same relative arrangement as the hero crop, with the cockpit, brick-red roof panel and circular hatch, lateral cargo door and pod banding all matching. Narrowing IDENTITY from the six-view sheet to a single three-quarter crop is what fixed it. Camera is pulled well back and Kia is now a small distant silhouette, as requested. Remaining discrepancies: (1) thrust still renders as soft glowing gradient cones issuing from BENEATH the pods rather than flat opaque wedges from the aft nozzles — same Style Block violation as v001, unmoved by stronger wording; (2) sky carries diagonal striation and the moon gradient cratering, against the flat-mass instruction; (3) overall surface is granular/dithered beyond the anchor's flatness. Kia remains IMPROVISED — no approved asset exists for her; this figure is off-canon.

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

Image 1 is STYLE: Match this image's hand-painted matte rendering technique ONLY. Ignore and do not reproduce its people, clothing, equipment, interior or setting.
Image 2 is IDENTITY: A single three-quarter view of the freighter Antares, cropped from its approved reference sheet. Copy this ship's design exactly — hull proportions, cockpit, cargo door, and above all the position and matched pairing of its two engine pods. Ignore its flat blue background.

TASK: A single horizontal wide night illustration: the freighter Antares descending onto a derelict landing pad on Kalagra, watched by one small distant operator.

THE SHIP — THE ANTARES (description v20, distilled for this scene). Image 2 is ONE single three-quarter view of this ship and is the authority on every shape below. It shows the whole ship at once; there are no other views to reconcile.

A broad, low, wedge-shaped utility freighter. Ivory / light-gray hull with brick-red accents; dark windows and openings.

HULL: one solid body, wider than it is tall and about twice as long as it is wide — a blunt wedge, not a long tube. The cockpit is at the very FRONT: a faceted glasshouse of dark angled windows in a sloping nose, with a brick-red roof panel around a circular hatch directly behind it. Behind the cockpit the body widens into a flat-shouldered midsection carrying a single raised central spine along the centerline and shallow recessed deck panels either side of it. A single broad rectangular cargo door sits low on the port side wall, behind the cockpit and ahead of the engines. The body ends in a squared-off tail.

ENGINE PODS — THE CRITICAL GEOMETRY: exactly TWO engine pods, and they are an IDENTICAL, MIRRORED PAIR. Both sit at the SAME position along the ship's length: aft of midships, flanking the rear third of the hull, level with each other. Neither pod is anywhere near the cockpit; no pod sits forward, beside, or ahead of the cabin. They are mounted outboard on short structural bridges, held clear of the hull sides, separated by roughly four pod diameters.

Each pod is a squat round drum — its total length including the short aft nozzle is only about 1.4 times its diameter. They are stubby barrels, NOT long nacelles. Both pod axes run straight fore-and-aft, exactly parallel to each other and to the ship's central spine: intake ring facing FORWARD, nozzle facing AFT. Neither pod is tilted, yawed, splayed, or rotated. Each pod is painted in banded blocks: dark gray intake rim, then brick-red, then an ivory band, then a dark aft cap.

Everything about the ship — proportions, the brick-red and ivory placement, the cockpit facets, the cargo door, the pod pair — is copied from image 2. Image 2 already shows the pods correctly placed; match that placement exactly.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame, horizontal. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO orthographic views, NO labels, NO text of any kind. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors or composition. Image 2 contributes the SHIP'S DESIGN ONLY — one three-quarter view of the whole ship. Do not copy its flat blue background. Paint this exact ship ONCE, in the new setting described below.

SCENE: "The Pad." Night on the barren planet Kalagra. A WIDE ESTABLISHING SHOT of a lonely derelict landing pad on an open rock plain, with the freighter Antares coming down onto it and a single small figure watching. This is a landscape first and a ship shot second: the emptiness of the place is the subject.

SCALE AND FRAMING — PULL WAY BACK: the camera is far away and slightly elevated, taking in the whole pad, the plain around it and a broad sweep of sky. The Antares is a MID-DISTANCE object, not a hero close-up: it spans only about one third of the frame's width and sits in the upper middle of the picture with clear open sky above and around it. The watching figure is SMALL — a distant silhouette about one tenth of the frame's height. Both ship and figure sit inside a much larger empty landscape. Do not crop in. Do not fill the frame with hull.

THE SHIP IN THE SCENE: the Antares hangs a few ship-lengths above the pad on final descent, seen from a low three-quarter angle with its nose angled away from the viewer and the hull tilted a few degrees nose-up. Because both engine pods are a level, matched pair at the same station near the tail, they read as two matching drums flanking the rear of the ship, one nearer and one farther in perspective — never one forward and one aft. Both pods are clearly behind the cabin. Thrust issues from the AFT NOZZLE of each pod, angled down toward the pad: two short, flat, opaque tapering wedges of pale ochre and ivory with hard straight edges. These are painted shapes, not light — no glow, no bloom, no halo, no soft or feathered edges, no transparency gradient, no light cone, no volumetric rays. Where the thrust meets the slab it throws a low flat skirt of ochre dust outward in a few angular sheets. A few small hard dots of ivory and red navigation light sit flat on the hull; they do not glow.

THE PAD: a wide circular ferrocrete landing pad, cracked and dust-drifted, its painted guide markings worn to faded ivory fragments. Seen from this distance it reads as a pale disc set into the dark plain, occupying the lower middle of the frame with plain visible all around it. Around its rim stand a handful of squat battered stanchion lamps on angular posts, casting small hard flat pools of warm ochre onto the slab; between the pools the pad falls into deep slate blue-violet shadow. At the pad's edge sit two low blocky ferrocrete service huts with dark doorways and a single tilted weathered mast. Nothing else: no crowd, no vehicles, no cargo stacks, no other ships. The place is plainly abandoned to one caretaker.

THE OPERATOR — KIA: one small lone figure standing on the near edge of the pad, low and left of center, seen from behind in three-quarter view as a dark shape against a lamp pool. She is about one tenth of the frame's height — small enough that she reads as a silhouette with a few flat planes, not a portrait. She wears a full-length robe falling to her boots, heavy slate blue-gray with a warm ochre band at the hem, and a dust mask over the lower half of her face with flat dark goggle lenses above it; from this distance the mask and goggles read as two simple dark blocks. Her hood is down and her hair is one chunky dark painted mass. One hand holds a stubby signal lamp at her side. Her head is tipped up, watching the ship come down. She is still and unhurried — the only living figure in the image. Do not enlarge her, do not move her into the foreground, and do not render her face in detail.

THE NIGHT AND THE DISTANT STORM: a deep slate blue-black sky painted as large quiet FLAT areas — no striping, no diagonal streaking, no rain texture, no granular noise. A sparse scatter of flat ivory star dots. One pale moon low in the upper left, rendered as a plain flat disc with two or three simple darker flat patches for craters — no gradient, no fine cratering. Along the far horizon at the right, a distant cobalt and blue-violet storm wall stands as a single quiet mass with a hard angular top edge and two or three thin branching bolts of pale yellow lightning inside it. It is far off and low on the horizon, small in the frame — approaching weather, not weather that has arrived. The air over the pad is clear: no haze, no rain, no wind-driven murk. Beyond the pad, a flat ochre-gray rock plain and a few angular rock shelves recede to that horizon.

LIGHT: night scene. Two light sources only — the warm ochre stanchion lamps on the pad below, which rake the underside of the ship, and the cold pale blue moon and sky, which edge the ship's upper hull with one flat lighter plane. Everything else falls into a single deep slate blue-violet shadow plane. Keep the image dark and quiet with only a few bright shapes; no neon, no rim lighting, no bloom, no light rays.

COMPOSITION: a wide, spacious, mostly empty picture. Large quiet dark masses of sky and plain; detail concentrated in the small bright island of the lit pad, the ship above it and the distant storm. Clear foreground (near rock and pad edge), middle distance (pad, huts, tiny figure), background (plain, storm, sky).

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
