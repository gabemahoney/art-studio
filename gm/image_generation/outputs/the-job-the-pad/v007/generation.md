# the-job-the-pad v007

User request verbatim: No. The plumes should be on the middle axis of the + / Also, lets give the buildings another color scheme. Maybe a matching green-ish blue for the pain splots
Mode: Edit off v006 baseline (user-designated), two changes: (1) ship moved so the plus's left-to-right axis passes through the centre of both plume feet, feet symmetric about the plus and the plus left unobscured; (2) the brick-red paint patches on both service buildings recoloured to a matching muted green-blue teal, positions and shapes held, ship's red accents untouched
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0ef01-1793-72a3-8d19-08a4fe50b648/exec-a778da30-b990-4db0-99e0-5c68d46c0c7e.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/ships/the_antares/sources/hero-3q-crop-from-v033.png
- Image 3 EDIT TARGET: outputs/the-job-the-pad/v006/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.07 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Both changes landed. Measured on a magnified crop: the plus's left-to-right arm centres on y~674 and both plume feet bottom out at y~688 — within ~14px, reading as on the axis; plume midpoint x~775 against plus centre x~762, so the pair straddles the plus near-symmetrically (left foot 178px from centre, right 204px — a ~7% asymmetry, the only residual). The plus stays fully visible between the plumes and the hull centre remains above it. Building paint patches are now a matching muted teal on both structures with no red remaining on either, so they no longer echo the Antares; ferrocrete stays pale gray-ivory and the ship's brick-red cockpit panel and pod bands are untouched. Ship size, level near-profile attitude, lamps, figure, moon, sky and storm carried over unchanged. Note: the stanchion lamp posts still carry brick-red bands, which continue to echo the ship's palette — out of scope here, which named only the buildings. Kia remains IMPROVISED: no approved asset exists for her. The belly landing thrusters are still absent from Antares description v20 and need a version bump if this scene is promoted.

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
Image 3 is EDIT TARGET: The scene baseline: the-job-the-pad v006, approved by the user except for the plumes' placement relative to the plus. Everything in it is correct unless a change below says otherwise.

TASK: A single horizontal wide night illustration: the freighter Antares settling onto the exact centre of a derelict landing pad on Kalagra, flanked by large teal-marked service buildings, watched by one small distant operator.

THE SHIP — THE ANTARES (description v20, distilled for this scene). Image 2 is ONE single three-quarter view of this ship and is the authority on every shape below. It shows the whole ship at once; there are no other views to reconcile.

A broad, low, wedge-shaped utility freighter. Ivory / light-gray hull with brick-red accents; dark windows and openings.

HULL: one solid body, wider than it is tall and about twice as long as it is wide — a blunt wedge, not a long tube. The cockpit is at the very FRONT: a faceted glasshouse of dark angled windows in a sloping nose, with a brick-red roof panel around a circular hatch directly behind it. Behind the cockpit the body widens into a flat-shouldered midsection carrying a single raised central spine along the centerline and shallow recessed deck panels either side of it. A single broad rectangular cargo door sits low on the port side wall, behind the cockpit and ahead of the engines. The body ends in a squared-off tail.

ENGINE PODS — THE CRITICAL GEOMETRY: exactly TWO engine pods, and they are an IDENTICAL, MIRRORED PAIR. Both sit at the SAME position along the ship's length: aft of midships, flanking the rear third of the hull, level with each other. Neither pod is anywhere near the cockpit; no pod sits forward, beside, or ahead of the cabin. They are mounted outboard on short structural bridges, held clear of the hull sides, separated by roughly four pod diameters.

Each pod is a squat round drum — its total length including the short aft nozzle is only about 1.4 times its diameter. They are stubby barrels, NOT long nacelles. Both pod axes run straight fore-and-aft, exactly parallel to each other and to the ship's central spine: intake ring facing FORWARD, nozzle facing AFT. Neither pod is tilted, yawed, splayed, or rotated. Each pod is painted in banded blocks: dark gray intake rim, then brick-red, then an ivory band, then a dark aft cap.

Everything about the ship — proportions, the brick-red and ivory placement, the cockpit facets, the cargo door, the pod pair — is copied from image 2. Image 2 already shows the pods correctly placed; match that placement exactly.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame, horizontal. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO orthographic views, NO labels, NO text of any kind. There is exactly ONE spacecraft and exactly ONE human figure in this image and no other people anywhere. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors or composition. Image 2 contributes the SHIP'S DESIGN ONLY; do not copy its flat blue background or its camera angle. Image 3 is the SCENE BASELINE: reproduce it faithfully and change only the TWO things specified below.

SCENE: "The Pad." Night on the barren planet Kalagra. A wide establishing shot of a lonely derelict landing pad on an open rock plain, with the freighter Antares coming down onto it and one small figure watching.

Image 3 is correct in every other respect and the user has approved it as it stands. Reproduce it exactly — same camera, same framing, same crop, same scale, same light, same paint handling — and change only the ship's position on the pad and the colour of the paint patches on the two buildings.

KEEP FROM IMAGE 3 — UNCHANGED: the wide pulled-back camera and its slightly elevated viewpoint; the cracked circular ferrocrete pad and its concentric worn ivory ring markings; the large worn ivory PLUS at the pad's exact centre, at its current size and position; the SHAPES and SIZES of the two big ferrocrete service buildings flanking left and right, cut by the left and right frame edges; the tilted weathered mast; the broken rock plain and its angular foreground shelves; the two dark near-side lamp posts seen from behind and the lit far-side lamps facing the viewer, every lamp pool falling inward on the slab; the small lone robed figure at lower left at exactly her current size and position, in her full-length slate blue-gray robe with ochre hem, dust mask, dark goggles and signal lamp, head tipped up watching; the pale flat moon at upper left; the flat deep slate blue-black sky and its sparse flat ivory stars; the distant cobalt storm wall with its lightning low on the right horizon; the warm ochre lamplight against deep slate blue-violet shadow. Do not re-frame, do not zoom, do not resize anything, do not move the figure, the buildings, the lamps or the plus.

THE SHIP IS UNCHANGED EXCEPT FOR ITS POSITION: same size in frame, same near-profile level attitude with its long axis horizontal and parallel to the pad and its nose to the left, no tilt or bank; same ivory and light-gray hull, same BRICK-RED cockpit roof panel with circular hatch, faceted dark cockpit windows, raised central spine, broad rectangular cargo door low on the side wall, and the same two BRICK-RED banded engine pods — the near one aft on this side, the far one showing above the roofline behind the hull exactly as in image 3. The ship keeps its red accents; the colour change below applies ONLY to the buildings. Do not redraw or reproportion the ship. Its two landing plumes keep their present organic form and size: irregular billowing tongues of flame and blown dust with wobbling hand-painted contours, built from two or three FLAT OPAQUE shapes of solid colour — pale ochre outer mass, brighter ivory tongues inside — fully opaque, with no glow, bloom, halo, gradient, blur, feathered edge, transparency, light cone or volumetric beam. One plume from the belly block under the forward hull, one from the belly block under the tail. Exactly two plumes; no thrust from the engine pods.

CHANGE ONE — PUT THE PLUMES ON THE PLUS'S LEFT–RIGHT AXIS: the painted plus at the pad's centre has two arms. One arm runs LEFT-TO-RIGHT across the picture; the other runs away from the viewer into depth. The left-to-right arm is the AXIS that matters here.

In image 3 the two plumes land near that axis but not on it: their feet sit slightly in FRONT of it, toward the viewer, and both stop short of the plus's arms so the axis does not pass through them.

Move the whole ship — hull and both plumes together — so that the plus's LEFT-TO-RIGHT AXIS RUNS STRAIGHT THROUGH THE CENTRE OF BOTH PLUME FEET. If that arm of the plus were extended outward in both directions across the slab, the extended line would pass exactly through the middle of the left plume's base and exactly through the middle of the right plume's base. Both feet sit centred on that one line, at the same depth as the plus itself — not in front of it, not behind it.

The two plumes also stay symmetric about the plus: the left plume's foot and the right plume's foot are the same distance from the centre of the plus, one to its left and one to its right, and the plus itself stays fully visible and unobscured between them. The ship's hull centre stays directly above the plus's centre, exactly as it already is in image 3 — the horizontal placement is already correct and must not change.

Adjust the ship's height only as much as this requires. It stays level, keeps its size, remains clearly airborne with open sky above it and its hull clear of the buildings' rooflines.

CHANGE TWO — RECOLOUR THE BUILDINGS' PAINT PATCHES: the two ferrocrete service buildings currently carry brick-red painted patches, bands and blocks on their walls. Repaint every one of those patches a muted GREEN-BLUE — a desaturated teal, like weathered blue-green industrial paint, darker and cooler than the ochre lamplight and clearly distinct from the slate blue-violet shadows. Use the SAME green-blue on both buildings so the pair reads as one matching colour scheme, and keep the patches in their current positions, shapes and sizes — this is a colour swap, not a redesign.

Paint them the way every other surface here is painted: flat opaque blocks of colour with hard edges, at most three value steps, no gradients. Where a patch falls under a lamp pool it takes one lighter flat step of the same green-blue; where it falls in shadow, one darker flat step. Weathered and chipped at the edges, as they already are.

The ferrocrete itself stays pale gray-ivory. No red remains anywhere on either building. The ship's brick-red markings, the stanchion lamps' red bands, and every other colour in the picture are unchanged.

LIGHT: night scene, unchanged from image 3. The warm ochre lamp pools on the slab and the cold pale moon edging the ship's upper hull and the building rooflines; everything else in one deep slate blue-violet shadow plane. No neon, no rim lighting, no bloom, no light rays.

Change nothing else about image 3.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
