# the-job-the-pad v008

User request verbatim: Is the nose correct? It seems a little different than in the reference / Try that out. Whichever you think is best.
Mode: Edit off v007 baseline. IDENTITY switched from the hero 3/4 crop to a true SIDE ELEVATION crop of reference.png (= the_antares/candidates/v033), saved as sources/side-elevation-crop-from-v033.png. Single change: the ship repainted in true profile at eye level to fix a camera inconsistency — v007 showed the full top deck, a broad red roof panel, the circular hatch head-on and the far pod above the roofline, while the ship floats above the horizon. Now: no top deck, no circular hatch, red reduced to a thin swept roofline stripe, low sharp compact nose wedge, 3-4 pane windscreen, far pod occluded, shallow underside band visible. Ship position, size, attitude, plumes, buildings, teal patches, lamps, figure, pad and sky all held.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0ef08-e71c-7b41-b654-4aa2162b1b7d/exec-e4a6b2d3-8f05-43e6-ba14-879b2d5d071c.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/ships/the_antares/sources/side-elevation-crop-from-v033.png
- Image 3 EDIT TARGET: outputs/the-job-the-pad/v007/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.03 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Camera inconsistency fixed. Compared crop-to-crop against the side elevation: the top deck is gone, the circular roof hatch is gone, and the red now reads as canon does in profile — a swept stripe tapering forward along the cockpit roofline PLUS the solid red block on the cockpit's aft side wall. Windscreen is a low 3-4 pane band with thick ivory mullions, the two small square side windows sit correctly below it, the far pod is properly occluded and the near pod sits aft as a banded drum. Residual nose delta: v008 runs the nose out to a longer, sharper point than the reference's blunter vertical chisel tip, and the small dark intake grille set into the nose tip is missing entirely. Also unmet: the shallow underside band requested for an above-eye-level subject did not appear — the belly reads as a flat bottom line and the two thruster blocks are not legible as housings. Consequence of the correction worth confirming with the user: with the far pod occluded, only one engine pod is visible, so this image no longer shows the Antares as a twin-pod ship. That is correct for a true side view and matches the side elevation, but it changes a silhouette the user had previously approved. Scene held throughout: teal building patches with no red, inward-facing lamps, figure, pad, plus, and both plumes still on the plus's left-right axis. Kia remains IMPROVISED. Belly landing thrusters remain absent from Antares description v20.

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
Image 2 is IDENTITY: The TRUE SIDE ELEVATION of the freighter Antares, cropped from its approved reference sheet. It is the authority on the ship's profile: outline, proportions, nose wedge, cockpit band, and where every red marking sits when the ship is seen from the side. Ignore its flat blue background; it is a guide to shape, not to lighting.
Image 3 is EDIT TARGET: The scene baseline: the-job-the-pad v007, approved by the user. Its setting, framing, composition, colours and lighting are all correct; only the ship is repainted.

TASK: A single horizontal wide night illustration: the freighter Antares, seen in true side profile at eye level, settling onto the centre of a derelict landing pad on Kalagra, flanked by large teal-marked service buildings, watched by one small distant operator.

THE SHIP — THE ANTARES (description v20, distilled for this scene). Image 2 is the ship's TRUE SIDE ELEVATION, cropped from its approved reference sheet. It is the authority on the ship's profile: outline, proportions, nose shape, cockpit, and where the colour sits when the ship is seen from the side. Match it.

A broad, low, wedge-shaped utility freighter. Ivory / light-gray hull with brick-red accents; dark windows and openings.

IN PROFILE, as image 2 shows it:

NOSE AND COCKPIT — the part that must match image 2 most closely. The nose is a LOW, SHARP WEDGE. Its underside sweeps up toward the front and its upper deck slopes down, and the two meet in a narrow, almost pointed tip low on the ship's centreline. The nose is compact — short from windscreen to tip — not a long tapering snout.

The windscreen is a SHALLOW, LOW BAND of dark angled panes set well forward and close to the tip, divided by thick ivory mullions into only THREE OR FOUR panes across in this view. It is a low slot, not a tall many-paned glasshouse.

The brick-red on the cockpit is a THIN SWEPT STRIPE running along the top of the cockpit roofline, tapering forward to a point above the windscreen. In profile it is a narrow racing stripe following the roof edge. It is NOT a broad red roof panel and NOT a large red field.

There is NO circular hatch visible in profile. The circular roof hatch sits flat on the top deck; from the side it is edge-on and simply is not seen. Do not draw a circle, ring, disc or bullseye anywhere on the cockpit.

Two small square dark windows sit low on the cockpit's side wall, below and behind the windscreen.

BODY: behind the cockpit the roofline steps UP to the taller midbody. A single broad rectangular cargo door with a dark perimeter seam and a hinge bar along its top sits low on the side wall, behind the cockpit and ahead of the engines. Small square dark windows and vents are scattered sparsely along the flank. The body ends in a squared-off tail.

ENGINE PODS: exactly TWO, an identical mirrored pair at the SAME station along the ship's length — aft of midships, flanking the rear third of the hull, level with each other, mounted outboard on short structural bridges and separated by roughly four pod diameters. Each is a squat round drum whose total length including its short aft nozzle is about 1.4 times its diameter — a stubby barrel, never a long nacelle. Both axes run straight fore-and-aft, parallel to each other and to the hull: intake ring forward, nozzle aft. Each pod is banded: dark gray intake rim, then brick-red, then an ivory band, then a dark aft cap. In a side view the NEAR pod is fully visible against the flank; the FAR pod is almost entirely hidden behind the hull.

Everything — proportions, outline, the placement of every red marking, the nose wedge, the cockpit band — is copied from image 2's profile.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame, horizontal. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO orthographic views, NO labels, NO text of any kind. There is exactly ONE spacecraft and exactly ONE human figure in this image and no other people anywhere. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors or composition. Image 2 is the ship's TRUE SIDE ELEVATION and contributes the SHIP'S PROFILE AND DESIGN ONLY — do not copy its flat blue background, and do not reproduce it as a flat diagram. Image 3 is the SCENE BASELINE: reproduce its setting, framing and composition exactly, and repaint only the ship.

SCENE: "The Pad." Night on the barren planet Kalagra. A wide establishing shot of a lonely derelict landing pad on an open rock plain, with the freighter Antares coming down onto it and one small figure watching.

KEEP FROM IMAGE 3 — COMPLETELY UNCHANGED: the wide pulled-back camera and its framing and crop; the cracked circular ferrocrete pad, its concentric worn ivory ring markings and the large worn ivory PLUS at its exact centre; the two big ferrocrete service buildings flanking left and right, cut by the left and right frame edges, with their MUTED TEAL green-blue paint patches exactly as they are — no red anywhere on either building; the tilted weathered mast; the broken rock plain and its angular foreground shelves; the two dark near-side lamp posts seen from behind and the lit far-side lamps facing the viewer, every lamp pool falling inward on the slab; the small lone robed figure at lower left at exactly her current size and position, in her full-length slate blue-gray robe with ochre hem, dust mask, dark goggles and signal lamp, head tipped up watching; the pale flat moon at upper left; the flat deep slate blue-black sky and its sparse flat ivory stars; the distant cobalt storm wall with its lightning low on the right horizon; the warm ochre lamplight against deep slate blue-violet shadow. Do not re-frame, do not zoom, do not move or resize the buildings, lamps, figure, pad or plus.

KEEP THE SHIP'S POSITION AND SIZE EXACTLY: the ship stays where image 3 puts it — same size in frame, hull centred directly above the plus, level, long axis horizontal and parallel to the pad, nose to the left, no tilt or bank. Its two landing plumes stay exactly where they are and keep their present organic form and size: irregular billowing tongues of flame and blown dust with wobbling hand-painted contours, built from two or three FLAT OPAQUE shapes of solid colour — pale ochre outer mass, brighter ivory tongues inside — fully opaque, with no glow, bloom, halo, gradient, blur, feathered edge, transparency, light cone or volumetric beam. One plume from the belly block under the forward hull, one from the belly block under the tail, their feet on the plus's left-to-right axis, straddling the plus. Exactly two plumes; no thrust from the engine pods.

THE ONE CHANGE — REPAINT THE SHIP IN TRUE PROFILE, AT EYE LEVEL: image 3 draws the Antares as if seen from ABOVE — its whole top deck is on show, with a broad red roof panel, a circular roof hatch facing the viewer as a full circle, the raised spine along the top, and the far engine pod riding up over the roofline. That viewpoint is wrong for this shot. The ship floats at and slightly ABOVE the horizon line — above the viewer's eye level — so we cannot be looking down onto its roof.

Repaint the ship as image 2's SIDE ELEVATION: seen from the SIDE, at eye level, with only the faintest hint of a three-quarter turn. Specifically:

- NO TOP DECK ON SHOW. The upper surfaces are seen edge-on and almost disappear. Only a very shallow sliver of roof is visible at most, foreshortened to a thin band.
- NO CIRCULAR HATCH. The circular roof hatch is edge-on and not visible. Do not paint a circle, ring, disc or bullseye anywhere on the ship.
- THE RED ON THE COCKPIT IS A THIN SWEPT STRIPE along the top of the cockpit roofline, tapering forward to a point above the windscreen — a narrow racing stripe following the roof edge, NOT a broad red panel or field.
- THE NOSE IS A LOW, SHARP, COMPACT WEDGE, exactly as image 2 draws it: the underside sweeps up toward the front, the upper deck slopes down, and they meet in a narrow tip low on the centreline. Short from windscreen to tip. Not a long tapering snout.
- THE WINDSCREEN IS A SHALLOW LOW BAND of dark angled panes set well forward, divided by thick ivory mullions into only THREE OR FOUR panes across — a low slot, not a tall many-paned glasshouse.
- THE RAISED CENTRAL SPINE is seen edge-on: at most a low bump breaking the roofline in silhouette, not a broad deck feature laid out for the viewer.
- THE FAR ENGINE POD IS HIDDEN. Behind the hull and below the roofline, it is almost entirely occluded. It must NOT appear as a drum sitting above the roofline. At most a small sliver of it shows past the hull's LOWER edge, at the same fore-and-aft station as the near pod — never above the ship.
- BECAUSE WE LOOK SLIGHTLY UP AT IT, a shallow band of the ship's UNDERSIDE is visible along its bottom: a flat darker plane in shadow, with the two belly thruster blocks reading clearly as flat dark rectangular housings on the centreline.

Everything else about the ship's design is unchanged and comes from image 2: ivory and light-gray hull; the roofline stepping up behind the cockpit to the taller midbody; two small square dark windows low on the cockpit's side wall; the broad rectangular cargo door with its dark perimeter seam and top hinge bar, low on the side wall behind the cockpit and ahead of the engines; sparse small dark windows and vents along the flank; a squared-off tail; and the near engine pod fully visible aft on this side as a squat banded drum — dark gray intake rim, brick-red, ivory band, dark aft cap — its axis horizontal and fore-and-aft.

Keep the ship's brick-red markings brick-red. The teal is for the buildings only and must not appear on the ship.

PAINT IT LIKE THE REST OF THE PICTURE, NOT LIKE A DIAGRAM: image 2 is a flat sheet drawing on a plain background and is a guide to SHAPE ONLY. The repainted ship belongs in this night scene — lit from below by the warm ochre lamp pools on the pad, edged along its upper hull by the cold pale moon and sky, with its underside and far flank in one deep slate blue-violet shadow plane, built from flat opaque colour planes with hard angular edges exactly like every other form in image 3.

LIGHT: night scene, unchanged from image 3. The warm ochre lamp pools on the slab and the cold pale moon edging the ship's upper hull and the building rooflines; everything else in one deep slate blue-violet shadow plane. No neon, no rim lighting, no bloom, no light rays.

Change nothing else about image 3.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
