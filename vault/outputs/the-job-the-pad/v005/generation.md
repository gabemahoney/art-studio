# the-job-the-pad v005

User request verbatim: Look good but the lights in the foreground still are not facing INTO the landing pad. Also, the Antares could be still more cental on the landing pad.
Mode: Edit off v004 baseline (user-designated), two changes only: ship moved down and forward in depth so both plumes terminate at the painted plus in the middle of the circle instead of on the far rim; near-side stanchion lamps repainted as dark backs-to-viewer silhouettes throwing their pools inward, away from the camera
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0ee97-62de-77a3-a719-fdba9bcceeef/exec-559ae69c-5c62-414f-8b75-4ddcf2b1f419.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/ships/the_antares/sources/hero-3q-crop-from-v033.png
- Image 3 EDIT TARGET: outputs/the-job-the-pad/v004/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.11 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Both requests landed. The two near-side stanchion lamps are now dark backs-to-viewer silhouettes with no lit face toward the camera, throwing their ochre pools inward across the slab; the mid/far lamps correctly still show their lit lenses, since facing the centre from the far side means facing the viewer. Every pool now lies inside the circle. The ship has come down and forward in depth: both plumes now strike inside the inner ring, straddling the painted plus, with open lit slab visible beyond them instead of touching down on the far rim. Ship size, level near-profile attitude, buildings, figure, moon, sky and storm all carried over unchanged. Remaining discrepancies, all inherited and none newly introduced: (1) the plume feet still sit a little deeper than the plus itself rather than level with it; (2) CORRECTED 2026-09-29 after user challenge and measurement: the earlier claim in the v003/v004 receipts that the far engine pod reads as a dorsal drum mounted on top of the hull was WRONG. Magnified inspection shows it sitting behind the hull and peeking above the roofline, which is correct for a far-side pod. Its apparent forward offset is perspective foreshortening, not a misplaced mount: in the identity crop the far pod is offset ~49% of hull length toward the nose, in v005 only ~23% — exactly the reduction a rotation from strong three-quarter toward near-profile should produce. No pod defect. (3) hull proportions stay longer and flatter than the broad chunky wedge in the identity crop; (4) the distant storm remains small and half-occluded by the right-hand building; (5) foreground rock is densely faceted against the Style Block's 'large areas stay quiet'. Kia remains IMPROVISED — no approved asset exists for her. Belly landing thrusters are still absent from description v20.

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
Image 3 is EDIT TARGET: The scene baseline: the-job-the-pad v004, designated by the user. Its setting, framing, composition and lighting are what 'unchanged' refers to below.

TASK: A single horizontal wide night illustration: the freighter Antares settling onto the middle of a derelict landing pad on Kalagra, flanked by large service buildings, watched by one small distant operator.

THE SHIP — THE ANTARES (description v20, distilled for this scene). Image 2 is ONE single three-quarter view of this ship and is the authority on every shape below. It shows the whole ship at once; there are no other views to reconcile.

A broad, low, wedge-shaped utility freighter. Ivory / light-gray hull with brick-red accents; dark windows and openings.

HULL: one solid body, wider than it is tall and about twice as long as it is wide — a blunt wedge, not a long tube. The cockpit is at the very FRONT: a faceted glasshouse of dark angled windows in a sloping nose, with a brick-red roof panel around a circular hatch directly behind it. Behind the cockpit the body widens into a flat-shouldered midsection carrying a single raised central spine along the centerline and shallow recessed deck panels either side of it. A single broad rectangular cargo door sits low on the port side wall, behind the cockpit and ahead of the engines. The body ends in a squared-off tail.

ENGINE PODS — THE CRITICAL GEOMETRY: exactly TWO engine pods, and they are an IDENTICAL, MIRRORED PAIR. Both sit at the SAME position along the ship's length: aft of midships, flanking the rear third of the hull, level with each other. Neither pod is anywhere near the cockpit; no pod sits forward, beside, or ahead of the cabin. They are mounted outboard on short structural bridges, held clear of the hull sides, separated by roughly four pod diameters.

Each pod is a squat round drum — its total length including the short aft nozzle is only about 1.4 times its diameter. They are stubby barrels, NOT long nacelles. Both pod axes run straight fore-and-aft, exactly parallel to each other and to the ship's central spine: intake ring facing FORWARD, nozzle facing AFT. Neither pod is tilted, yawed, splayed, or rotated. Each pod is painted in banded blocks: dark gray intake rim, then brick-red, then an ivory band, then a dark aft cap.

Everything about the ship — proportions, the brick-red and ivory placement, the cockpit facets, the cargo door, the pod pair — is copied from image 2. Image 2 already shows the pods correctly placed; match that placement exactly.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame, horizontal. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO orthographic views, NO labels, NO text of any kind. There is exactly ONE spacecraft and exactly ONE human figure in this image and no other people anywhere. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors or composition. Image 2 contributes the SHIP'S DESIGN ONLY; do not copy its flat blue background or its camera angle. Image 3 is the SCENE BASELINE: reproduce its setting, framing and composition, and change only the two things specified below.

SCENE: "The Pad." Night on the barren planet Kalagra. A wide establishing shot of a lonely derelict landing pad on an open rock plain, with the freighter Antares coming down onto it and one small figure watching.

KEEP FROM IMAGE 3 — UNCHANGED: the wide pulled-back camera and its slightly elevated viewpoint; the cracked circular ferrocrete pad, its concentric worn ivory ring markings and the large worn ivory PLUS painted at its exact centre; the big ferrocrete service buildings flanking left and right, cut by the left and right frame edges, rooflines above the horizon; the tilted weathered mast; the broken rock plain and its angular foreground shelves; the small lone robed figure at lower left at exactly her current size and position, in her full-length slate blue-gray robe with the ochre hem, dust mask and dark goggles, signal lamp in hand, head tipped up watching; the pale flat moon at upper left; the flat deep slate blue-black sky and its sparse flat ivory stars; the distant cobalt storm wall with its lightning low on the right horizon; the night palette of deep slate blue-violet shadow against warm ochre lamplight. Do not re-frame. Do not zoom. Do not enlarge or move the figure. Do not resize the buildings.

THE SHIP'S DESIGN AND ATTITUDE ARE UNCHANGED: near-profile, level, long axis horizontal and parallel to the pad, nose left, no tilt or bank; ivory and light-gray hull, brick-red cockpit roof panel with its circular hatch, faceted dark cockpit windows in the sloping nose, raised central spine, broad rectangular cargo door low on the side wall, two banded engine pods as a matched pair aft of midships. Keep it the same size in frame. The two landing plumes keep their present organic form: irregular billowing tongues of flame and blown dust with wobbling hand-painted contours, built from two or three FLAT OPAQUE shapes of solid colour — pale ochre outer mass, brighter ivory tongues inside — fully opaque, with no glow, bloom, halo, gradient, blur, feathered edge, transparency, light cone or volumetric beam. One plume from a flat dark thruster block on the belly under the forward hull, one from an identical block under the tail, both on the underside centreline, matched in size. Exactly two plumes; no thrust from the engine pods or anywhere else.

CHANGE ONE — BRING THE SHIP DOWN ONTO THE MIDDLE OF THE PAD, NOT ITS FAR RIM: in image 3 the ship is centred left-to-right but sits too far BACK in depth — its two plumes strike the slab up at the pad's FAR edge, well beyond the painted plus, so it reads as landing on the back rim rather than on its mark.

Move the Antares DOWN in the frame and FORWARD in depth, toward the viewer, so that:
- both plumes come down onto the MIDDLE of the circle and terminate right at the painted PLUS, one just left of it and one just right of it, straddling it symmetrically;
- the feet of the plumes sit at the plus's own depth in the picture — level with it, not above it;
- a clear, generous band of empty lit slab remains visible BEYOND the plumes, between them and the pad's far rim, so the ship plainly sits inside the circle rather than at its back edge;
- the near half of the pad, between the plus and the viewer, stays open and readable.

The ship is lower in the frame as a result, hovering closer above the slab, but still clearly airborne with open sky above it and its hull well clear of the buildings' rooflines. Keep it level and keep its size unchanged.

CHANGE TWO — THE NEAR STANCHION LAMPS MUST FACE AWAY FROM THE VIEWER, INTO THE CIRCLE: every stanchion lamp around the rim points at the pad's centre. For the lamps on the FAR side of the pad that means their lit lenses face toward the viewer. But for the lamps on the NEAR side — the ones in the foreground, closest to the bottom of the picture, on the viewer's side of the circle — facing the centre means facing AWAY from the viewer. Those near lamps are therefore seen FROM BEHIND.

Paint each near lamp as a plain dark unlit silhouette: we see the BACK of its housing, a flat dark angular block with no bright lens, no glowing face, no lit panel turned toward the camera. Its light is thrown forward AWAY from us, landing as a hard flat pool of warm ochre on the slab BEYOND the lamp, between it and the plus — deeper into the picture, never in front of the lamp toward the viewer, never spilling down or outward onto the foreground rock. The rock in front of and below the near lamps stays in deep slate blue-violet shadow.

No lamp anywhere points outward at the rock plain, sideways along the rim, down at its own base, or out of the frame. Every single lamp pool lies INSIDE the circle. If a lamp's bright face is visible, it is a far-side lamp and the pad's centre is between it and the viewer.

LIGHT: night scene, unchanged from image 3. Two light sources only — the warm ochre stanchion lamps, whose pools all fall inward on the slab, and the cold pale moon and sky, which edge the ship's upper hull and the building rooflines with one flat lighter plane. Everything else falls into a single deep slate blue-violet shadow plane. No neon, no rim lighting, no bloom, no light rays.

Change nothing else about image 3.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
