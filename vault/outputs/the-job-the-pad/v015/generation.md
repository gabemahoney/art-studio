# the-job-the-pad v015

User request verbatim: It still looks slightlt off. Could we angle the entire ship to align with the nose? Right now we are struggling because the ship is mostly a side view, then we are trying to make the nose show some of the width
Mode: Edit off v014. User's diagnosis, and it supersedes the whole v009-v014 nose line: a near-broadside hull cannot carry a nose that shows width, so every isolated nose fix traded one fault for another. Fix: rotate the ENTIRE ship ~30 degrees as one rigid body — nose toward viewer-left, tail receding right — into a true three-quarter matching the hero crop's own projection, so the identity reference and the painted view finally agree. Consequences specified: left flank foreshortened, hull reads broad not slab, BOTH pods visible as a matched pair with the far one displaced noseward by perspective, and the two plumes now separated in depth along the ship's axis with the plus midway between their feet. Ship stays level, same height, same size, hull centred over the plus; scene otherwise held.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f043-55be-75b2-9e71-3e322df325f8/exec-f01db73d-5f98-47c5-b3ae-7a26ca7f96ae.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/ships/the_antares/sources/hero-3q-crop-from-v033.png
- Image 3 EDIT TARGET: outputs/the-job-the-pad/v014/image.png
Date: 2026-09-29
Status: approved and promoted to final.png on 2026-09-29. User approval: "Yeah dude thats a keeper!"
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.13 MB — the raw output meets the book-float spec and is the placement file for that use. CHOSEN PRINT DELIVERABLE: delivered-2172x1448.png — sRGB 8-bit PNG-24, no alpha, 300 DPI (118.11 px/cm), 3.29 MB, sized for a 183.9 mm column (7.24 in x 300). Exactly 3:2 (aspect 1.5000), so it is a uniform upscale of image.png with identical scale factors on both axes (1.4140625) — full-bleed, no padding, no crop, no distortion. Over the 2.5 MB book-float budget, which does not apply to print use. NOTE: this is an UPSCALE of the approved 1536x1024 output, not a native-resolution render — the codex backend treats requested size as advisory, and regenerating would have produced a different picture rather than a larger copy of the approved one. Two earlier print derivations are SUPERSEDED and should not be used: delivered-2176x1440.png (1.5111:1, not 3:2 — required 8 px of #1b1e26 padding at left and right) and delivered-2160x1440.png (correct 3:2 but the wrong column width).
Review: The user's diagnosis was correct and this supersedes the entire v009-v014 nose line. Rotating the whole ship into a true three-quarter removed the conflict rather than managing it: a near-broadside hull cannot carry a nose that shows width, so every isolated nose adjustment traded one fault for another (too long, too stubby, yawed at camera, vertical slab, face-on). With the hull turned ~30 degrees the nose simply comes along with it, and its low wide chisel end and louvered grille now read naturally and honestly because nothing contradicts them. The hero crop's projection and the painted view finally agree, which is also why the identity reference is now doing useful work instead of being reinterpreted. Confirmed in the result: the hull reads broad and chunky rather than as a long slab; the left flank, cargo door and side windows are properly foreshortened; BOTH engine pods are visible as the matched pair they are, the far one displaced toward the nose by ordinary perspective exactly as the hero crop shows; upper deck, raised spine, brick-red roof panel and circular hatch read as a coherent top surface. Ship is level with no pitch or bank. The plumes correctly separated in depth along the ship's axis, the forward one nearer and lower, the aft one farther and higher. Two small residuals: the midpoint between the two plume feet sits roughly 27px right and 23px beyond the painted plus rather than exactly on it, so the ship is a touch back and right of dead centre on its mark; and the ship reads slightly larger in frame than v014 because the three-quarter pose exposes more of its top surface, which brings its tail a little closer to the right-hand building. Everything else held: teal building patches with no red, inward-facing lamps, figure unmoved at lower left, pad, plus, concentric rings, cool gray-ivory moon, flat sky, distant storm. The above-eye-level top deck remains a deliberate perspective liberty accepted by the user; v008 is the geometrically strict alternative on record. The belly landing thrusters are a DELIBERATE scene-local invention and will NOT be added to Antares description.md -- this is the only landing shot. Do not "fix" that gap in a later session. Kia remains IMPROVISED -- no approved asset exists for her.

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
Image 2 is IDENTITY: A three-quarter view of the freighter Antares, cropped from its approved reference sheet. This is BOTH the ship's design AND the viewing angle to produce: seen from in front and slightly to its left, broad and chunky, with both engine pods visible as a matched pair. Ignore its flat blue background.
Image 3 is EDIT TARGET: The scene baseline: the-job-the-pad v014. Its setting, framing, composition, colours and lighting are all correct; only the ship's pose changes.

TASK: A single horizontal wide night illustration: the freighter Antares, seen in three-quarter view, settling onto the centre of a derelict landing pad on Kalagra, flanked by large teal-marked service buildings, watched by one small distant operator.

THE SHIP — THE ANTARES (description v20, distilled for this scene). Image 2 is ONE single three-quarter view of this ship and is the authority on every shape below. It shows the whole ship at once; there are no other views to reconcile.

A broad, low, wedge-shaped utility freighter. Ivory / light-gray hull with brick-red accents; dark windows and openings.

HULL: one solid body, wider than it is tall and about twice as long as it is wide — a blunt wedge, not a long tube. The cockpit is at the very FRONT: a faceted glasshouse of dark angled windows in a sloping nose, with a brick-red roof panel around a circular hatch directly behind it. Behind the cockpit the body widens into a flat-shouldered midsection carrying a single raised central spine along the centerline and shallow recessed deck panels either side of it. A single broad rectangular cargo door sits low on the port side wall, behind the cockpit and ahead of the engines. The body ends in a squared-off tail.

ENGINE PODS — THE CRITICAL GEOMETRY: exactly TWO engine pods, and they are an IDENTICAL, MIRRORED PAIR. Both sit at the SAME position along the ship's length: aft of midships, flanking the rear third of the hull, level with each other. Neither pod is anywhere near the cockpit; no pod sits forward, beside, or ahead of the cabin. They are mounted outboard on short structural bridges, held clear of the hull sides, separated by roughly four pod diameters.

Each pod is a squat round drum — its total length including the short aft nozzle is only about 1.4 times its diameter. They are stubby barrels, NOT long nacelles. Both pod axes run straight fore-and-aft, exactly parallel to each other and to the ship's central spine: intake ring facing FORWARD, nozzle facing AFT. Neither pod is tilted, yawed, splayed, or rotated. Each pod is painted in banded blocks: dark gray intake rim, then brick-red, then an ivory band, then a dark aft cap.

Everything about the ship — proportions, the brick-red and ivory placement, the cockpit facets, the cargo door, the pod pair — is copied from image 2. Image 2 already shows the pods correctly placed; match that placement exactly.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame, horizontal. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO orthographic views, NO labels, NO text of any kind. There is exactly ONE spacecraft and exactly ONE human figure in this image and no other people anywhere. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors or composition. Image 2 contributes the SHIP'S DESIGN AND ITS VIEWING ANGLE — do not copy its flat blue background. Image 3 is the SCENE BASELINE: reproduce its setting, framing and composition exactly, and re-pose the ship.

SCENE: "The Pad." Night on the barren planet Kalagra. A wide establishing shot of a lonely derelict landing pad on an open rock plain, with the freighter Antares coming down onto it and one small figure watching.

KEEP FROM IMAGE 3 — COMPLETELY UNCHANGED: the wide pulled-back camera and its framing and crop; the cracked circular ferrocrete pad, its concentric worn ivory ring markings and the large worn ivory PLUS at its centre; the two big ferrocrete service buildings flanking left and right, cut by the left and right frame edges, with their MUTED TEAL green-blue paint patches exactly as they are — no red anywhere on either building; the tilted weathered mast; the broken rock plain and its angular foreground shelves; the two dark near-side lamp posts seen from behind and the lit far-side lamps facing the viewer, every lamp pool falling inward on the slab; the small lone robed figure at lower left at exactly her current size and position, in her full-length slate blue-gray robe with ochre hem, dust mask, dark goggles and signal lamp, head tipped up watching; the pale cool GRAY-IVORY moon at upper left; the flat deep slate blue-black sky and its sparse flat ivory stars; the distant cobalt storm wall with its lightning low on the right horizon; the warm ochre lamplight against deep slate blue-violet shadow. Do not re-frame, do not zoom, do not move or resize the buildings, lamps, figure, pad or plus.

THE ONE CHANGE — TURN THE WHOLE SHIP INTO A TRUE THREE-QUARTER VIEW. In image 3 the Antares is posed almost broadside, its long axis running flat across the picture, so its nose can only be seen edge-on. That is the problem: a side-on hull cannot carry a nose that shows any of its width, and the two have been fighting each other.

Rotate the ENTIRE SHIP — nose, cockpit, hull, cargo door, spine, upper deck, both engine pods, the belly thruster blocks, all of it — as ONE RIGID BODY, about its vertical centre, by roughly THIRTY DEGREES. The NOSE swings TOWARD the viewer and to the left; the TAIL swings AWAY from the viewer and to the right. The ship's long axis now runs diagonally INTO the picture instead of flat across it.

Match the viewing angle of image 2. Image 2 shows this exact ship from the front and slightly to its left — the pose you are producing. Use it.

WHAT THIS MUST MAKE TRUE, all of it consistent with one another:
- The nose's blunt front end now genuinely FACES partly toward us, at the same angle as the rest of the ship. Its low, wide horizontal chisel end and the dark louvered grille set into it read naturally and honestly, because the whole hull is turned the same way. The nose is not adjusted separately from the ship — it simply comes along with it.
- The LEFT FLANK of the hull is now FORESHORTENED, receding away to the right. The cargo door, the small square windows and the flank panels compress along with it. The flank is no longer the dominant broadside surface.
- The hull reads BROAD AND CHUNKY, as image 2 shows it — a blunt wedge seen from in front of its shoulder — rather than the long flat slab a broadside view produced.
- BOTH ENGINE PODS ARE VISIBLE, as the matched pair they are: same station aft of midships, level with each other, outboard on their mounts, axes running fore-and-aft. In this three-quarter view the FAR pod appears displaced toward the nose relative to the near pod — that is ordinary perspective foreshortening and is correct. Both are squat banded drums: dark gray intake rim, brick-red, ivory band, dark aft cap.
- The upper deck, raised central spine, broad brick-red roof panel and the circular roof hatch remain on show and read as a coherent top surface of a ship turned toward us.

THE SHIP DOES NOT OTHERWISE MOVE: it stays LEVEL — no pitch, no nose-up or nose-down tilt, no bank or roll. It stays at the same height above the slab, hovering a few ship-lengths up, clearly airborne with open sky above it and its hull clear of the buildings' rooflines. It stays about the same size in the frame, and the centre of its hull stays directly above the painted PLUS at the pad's centre.

THE PLUMES FOLLOW THE SHIP. The two belly thrusters stay where they belong on the ship — one on the underside centreline under the forward hull, one under the tail — so when the ship turns, they turn with it. Consequently the two plumes are now separated in DEPTH as well as across the picture: the forward plume comes down NEARER the viewer and lower in the frame, the aft plume comes down FARTHER away and higher in the frame. They land along the ship's own axis, running diagonally into the picture, with the painted PLUS midway between their two feet — one foot short of the plus toward the viewer, one foot beyond it. The ship still plainly sits centred on its mark.

Each plume keeps its present form: an irregular billowing tongue of flame and blown dust with wobbling hand-painted contours, built from two or three FLAT OPAQUE shapes of solid colour — pale ochre outer mass, brighter ivory tongues inside — fully opaque, with no glow, bloom, halo, gradient, blur, feathered edge, transparency, light cone or volumetric beam. Where each meets the slab it throws low flat irregular sheets of ochre dust with ragged edges. Exactly two plumes; no thrust from the engine pods.

THE SHIP'S DESIGN IS UNCHANGED, only its pose: ivory and light-gray hull; brick-red roof panel with its circular hatch; the red block on the cockpit's aft side wall; faceted dark cockpit windows in a ~5-pane windscreen with thick ivory mullions; raised central spine; broad rectangular cargo door low on the side wall; small square dark windows; squared-off tail; two brick-red banded engine pods. Keep the red brick-red — the teal belongs to the buildings only and must not appear on the ship.

PAINT IT LIKE THE REST OF THE PICTURE: image 2 is a flat sheet drawing on a plain background and is a guide to SHAPE AND POSE ONLY. The re-posed ship belongs in this night scene — lit from below by the warm ochre lamp pools, edged along its upper hull by the cold pale moon and sky, with its underside and far flank in one deep slate blue-violet shadow plane, built from flat opaque colour planes with hard angular edges exactly like every other form in image 3.

LIGHT: night scene, unchanged from image 3. No neon, no rim lighting, no bloom, no light rays.

Change nothing else about image 3.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
