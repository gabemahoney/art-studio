# the-job-the-pad v006

User request verbatim: Thats supposed to look like that though. I think the image is loiking fine, we just need the Antares in the middle of the pad.
Mode: Edit off v005 baseline (user-approved except ship depth). Single change: ship and both plumes moved down and forward in depth so the plume feet land level with the painted plus and the two dark near-side lamp posts, instead of ~1/3 of the way back toward the far rim. Horizontal placement, ship size, attitude, design, plumes, buildings, lamps, figure and sky all held.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0eefe-6bd7-75a2-9767-ab4c71c6acff/exec-38dba105-db76-4da6-a883-4723e98e6724.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/ships/the_antares/sources/hero-3q-crop-from-v033.png
- Image 3 EDIT TARGET: outputs/the-job-the-pad/v005/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.07 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: pending — record with bin/review.py once you have seen it

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
Image 2 is IDENTITY: A single three-quarter view of the freighter Antares, cropped from its approved reference sheet. Copy this ship's design exactly — hull proportions, cockpit, cargo door, and the position and matched pairing of its two engine pods. Ignore its flat blue background and its camera angle.
Image 3 is EDIT TARGET: The scene baseline: the-job-the-pad v005, approved by the user in every respect except the ship's depth on the pad. Everything in it is correct unless the single change below says otherwise.

TASK: A single horizontal wide night illustration: the freighter Antares settling onto the exact middle of a derelict landing pad on Kalagra, flanked by large service buildings, watched by one small distant operator.

THE SHIP — THE ANTARES (description v20, distilled for this scene). Image 2 is ONE single three-quarter view of this ship and is the authority on every shape below. It shows the whole ship at once; there are no other views to reconcile.

A broad, low, wedge-shaped utility freighter. Ivory / light-gray hull with brick-red accents; dark windows and openings.

HULL: one solid body, wider than it is tall and about twice as long as it is wide — a blunt wedge, not a long tube. The cockpit is at the very FRONT: a faceted glasshouse of dark angled windows in a sloping nose, with a brick-red roof panel around a circular hatch directly behind it. Behind the cockpit the body widens into a flat-shouldered midsection carrying a single raised central spine along the centerline and shallow recessed deck panels either side of it. A single broad rectangular cargo door sits low on the port side wall, behind the cockpit and ahead of the engines. The body ends in a squared-off tail.

ENGINE PODS — THE CRITICAL GEOMETRY: exactly TWO engine pods, and they are an IDENTICAL, MIRRORED PAIR. Both sit at the SAME position along the ship's length: aft of midships, flanking the rear third of the hull, level with each other. Neither pod is anywhere near the cockpit; no pod sits forward, beside, or ahead of the cabin. They are mounted outboard on short structural bridges, held clear of the hull sides, separated by roughly four pod diameters.

Each pod is a squat round drum — its total length including the short aft nozzle is only about 1.4 times its diameter. They are stubby barrels, NOT long nacelles. Both pod axes run straight fore-and-aft, exactly parallel to each other and to the ship's central spine: intake ring facing FORWARD, nozzle facing AFT. Neither pod is tilted, yawed, splayed, or rotated. Each pod is painted in banded blocks: dark gray intake rim, then brick-red, then an ivory band, then a dark aft cap.

Everything about the ship — proportions, the brick-red and ivory placement, the cockpit facets, the cargo door, the pod pair — is copied from image 2. Image 2 already shows the pods correctly placed; match that placement exactly.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame, horizontal. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO orthographic views, NO labels, NO text of any kind. There is exactly ONE spacecraft and exactly ONE human figure in this image and no other people anywhere. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors or composition. Image 2 contributes the SHIP'S DESIGN ONLY; do not copy its flat blue background or its camera angle. Image 3 is the SCENE BASELINE: reproduce it faithfully and change only the ONE thing specified below.

SCENE: "The Pad." Night on the barren planet Kalagra. A wide establishing shot of a lonely derelict landing pad on an open rock plain, with the freighter Antares coming down onto it and one small figure watching.

THIS IS A SINGLE-CHANGE EDIT. Image 3 is correct in every other respect and the user has approved it as it stands. Reproduce it exactly — same camera, same framing, same crop, same scale, same colours, same light, same paint handling — and move ONE thing.

KEEP FROM IMAGE 3 — UNCHANGED: the wide pulled-back camera and its slightly elevated viewpoint; the cracked circular ferrocrete pad, its concentric worn ivory ring markings and the large worn ivory PLUS at its centre; the big ferrocrete service buildings flanking left and right, cut by the left and right frame edges; the tilted weathered mast; the broken rock plain and its angular foreground shelves; the two dark near-side lamp posts seen from behind, throwing their ochre pools inward, and the lit far-side lamps facing the viewer — every lamp pool inside the circle; the small lone robed figure at lower left at exactly her current size and position, in her full-length slate blue-gray robe with ochre hem, dust mask, dark goggles and signal lamp, head tipped up watching; the pale flat moon at upper left; the flat deep slate blue-black sky and its sparse flat ivory stars; the distant cobalt storm wall with its lightning low on the right horizon; the night palette of deep slate blue-violet shadow against warm ochre lamplight. Do not re-frame, do not zoom, do not resize anything, do not move the figure, the buildings or the lamps.

THE SHIP IS UNCHANGED IN EVERY RESPECT EXCEPT ITS POSITION: same size in frame, same near-profile level attitude with its long axis horizontal and parallel to the pad and its nose to the left, no tilt or bank; same ivory and light-gray hull, brick-red cockpit roof panel with circular hatch, faceted dark cockpit windows, raised central spine, broad rectangular cargo door low on the side wall, and the same two banded engine pods — the near one aft on this side, the far one showing above the roofline behind the hull exactly as it does in image 3. Do not redraw, reproportion or re-light the ship. Its two landing plumes keep their present organic form and size: irregular billowing tongues of flame and blown dust with wobbling hand-painted contours, built from two or three FLAT OPAQUE shapes of solid colour — pale ochre outer mass, brighter ivory tongues inside — fully opaque, with no glow, bloom, halo, gradient, blur, feathered edge, transparency, light cone or volumetric beam. One plume from the belly block under the forward hull, one from the belly block under the tail. Exactly two plumes; no thrust from the engine pods.

THE ONE CHANGE — SET THE SHIP DOWN ON THE MIDDLE OF THE PAD: in image 3 the ship's horizontal placement is already right — the centre of its hull is directly above the centre of the circle, and that stays. What is wrong is its DEPTH. Its two plumes touch down too far back: they strike the slab roughly a third of the way from the pad's centre toward its FAR rim, landing on the far arc of the inner ring instead of on the middle of the pad.

Move the whole ship — hull and both plumes together — DOWN in the frame and FORWARD in depth, toward the viewer, by that same amount, so that the plume feet come to rest on the MIDDLE of the circle. Use these three landmarks, which are all at the same depth in the picture and must not move:
- the painted PLUS at the pad's centre;
- the dark near-side lamp post at the LEFT of the circle, where the pad is at its widest;
- the dark near-side lamp post at the RIGHT of the circle, where the pad is at its widest.

When the move is correct, the bottoms of both plumes sit level with those three landmarks — on the same horizontal line across the picture as the plus and the two flanking lamp posts — with one plume just left of the plus and one just right of it, straddling it symmetrically. Neither plume foot is behind the plus or above that line.

The result: the ship plainly sits ON its mark in the middle of the circle, with a generous band of empty lit slab visible BEYOND the plumes between them and the far rim, and the near half of the pad still open and readable in front of them. The ship is correspondingly lower in the frame and hovering closer above the slab, but still clearly airborne with open sky above it and its hull clear of the buildings' rooflines. Do not change its size and do not tilt it.

LIGHT: night scene, unchanged from image 3. The warm ochre lamp pools on the slab and the cold pale moon edging the ship's upper hull and the building rooflines; everything else in one deep slate blue-violet shadow plane. No neon, no rim lighting, no bloom, no light rays.

Change nothing else about image 3.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
