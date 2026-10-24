# the-job-the-pad v012

User request verbatim: The nose still points a bit to the camera.
Mode: Edit off v011 baseline, single facet correction: the nose's flat front face turned further away from the camera until it is foreshortened as hard as the near pod's intake face and the tail end — all three being parallel planes perpendicular to the hull axis, used as an in-picture reference. Front face reduced to a narrow sliver (<~1/5 of nose width), left flank made dominant, grille compressed but kept. Nose LENGTH held from v011; ship not rotated; angle, pods, plumes, buildings, lamps, figure, pad and sky all held.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0ef28-f11d-74c0-95f5-dfac8dd02a49/exec-38561612-2681-488c-83ee-7438899e1e86.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/ships/the_antares/sources/hero-3q-crop-from-v033.png
- Image 3 EDIT TARGET: outputs/the-job-the-pad/v011/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.06 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Front face de-canted. Measured on matched magnified crops, the nose's flat front facet went from roughly 115px wide in v011 to roughly 40px in v012 -- about a third of its former width, landing near the requested "no more than a fifth of the nose's apparent width". It now reads as a thin vertical edge at the very front rather than a panel presented to the viewer, and its foreshortening is consistent with the near pod's intake face and the tail end, which lie in the same family of planes perpendicular to the hull axis. Giving the model those two in-picture surfaces as the reference target, rather than describing the angle in words, is what finally moved it. The nose's left flank now dominates and runs cleanly away to the left, parallel to the hull behind it, with no kink at the cockpit join. Nose LENGTH held from v011 -- no drift back toward either the v007 snout or the v009 stub. The louvered intake grille survived the narrowing as a tight compressed slot, slats and ivory lip still legible, still the darkest shape on the nose. Everything else intact from v011: three-quarter viewing angle with upper deck on show, broad brick-red roof panel, circular hatch as a full circle, aft cockpit red block, raised spine, far pod above the roofline, near pod aft, ~5-pane windscreen, teal building patches with no red, inward-facing lamps, figure unmoved at lower left, pad, plus, and both plumes still straddling the plus on its left-right axis. No new discrepancies found. The above-eye-level top deck remains a deliberate perspective liberty accepted by the user; v008 is the geometrically strict alternative on record. Kia remains IMPROVISED -- no approved asset exists for her, so this image establishes nothing about her design. Belly landing thrusters remain absent from Antares description v20 and need a version bump if this candidate is promoted.

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
Image 2 is IDENTITY: A single three-quarter view of the freighter Antares, cropped from its approved reference sheet — the same viewing angle the scene uses. It is the authority on how narrow the nose's flat front face reads at this angle, and on the louvered intake grille set into it. Ignore its flat blue background.
Image 3 is EDIT TARGET: The scene baseline: the-job-the-pad v011, approved by the user except that the nose's flat front face is still angled toward the camera.

TASK: A single horizontal wide night illustration: the freighter Antares settling onto the centre of a derelict landing pad on Kalagra, flanked by large teal-marked service buildings, watched by one small distant operator.

THE SHIP — THE ANTARES (description v20, distilled for this scene). Image 2 is ONE single three-quarter view of this ship and is the authority on every shape below. It shows the whole ship at once; there are no other views to reconcile.

A broad, low, wedge-shaped utility freighter. Ivory / light-gray hull with brick-red accents; dark windows and openings.

HULL: one solid body, wider than it is tall and about twice as long as it is wide — a blunt wedge, not a long tube. The cockpit is at the very FRONT: a faceted glasshouse of dark angled windows in a sloping nose, with a brick-red roof panel around a circular hatch directly behind it. Behind the cockpit the body widens into a flat-shouldered midsection carrying a single raised central spine along the centerline and shallow recessed deck panels either side of it. A single broad rectangular cargo door sits low on the port side wall, behind the cockpit and ahead of the engines. The body ends in a squared-off tail.

ENGINE PODS — THE CRITICAL GEOMETRY: exactly TWO engine pods, and they are an IDENTICAL, MIRRORED PAIR. Both sit at the SAME position along the ship's length: aft of midships, flanking the rear third of the hull, level with each other. Neither pod is anywhere near the cockpit; no pod sits forward, beside, or ahead of the cabin. They are mounted outboard on short structural bridges, held clear of the hull sides, separated by roughly four pod diameters.

Each pod is a squat round drum — its total length including the short aft nozzle is only about 1.4 times its diameter. They are stubby barrels, NOT long nacelles. Both pod axes run straight fore-and-aft, exactly parallel to each other and to the ship's central spine: intake ring facing FORWARD, nozzle facing AFT. Neither pod is tilted, yawed, splayed, or rotated. Each pod is painted in banded blocks: dark gray intake rim, then brick-red, then an ivory band, then a dark aft cap.

Everything about the ship — proportions, the brick-red and ivory placement, the cockpit facets, the cargo door, the pod pair — is copied from image 2. Image 2 already shows the pods correctly placed; match that placement exactly.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame, horizontal. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO orthographic views, NO labels, NO text of any kind. There is exactly ONE spacecraft and exactly ONE human figure in this image and no other people anywhere. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors or composition. Image 2 contributes the SHIP'S DESIGN ONLY — do not copy its flat blue background. Image 3 is the SCENE BASELINE: reproduce it faithfully and change only the ONE thing specified below.

SCENE: "The Pad." Night on the barren planet Kalagra. A wide establishing shot of a lonely derelict landing pad on an open rock plain, with the freighter Antares coming down onto it and one small figure watching.

Image 3 is APPROVED and correct in every respect but one: the flat front face of the nose is still turned too far toward the camera. This is a final, narrow correction to that one facet. Reproduce image 3 exactly — same camera, same framing, same crop, same scale, same colours, same light, same paint handling, same ship, same nose LENGTH — and change only how far that front face is turned.

KEEP FROM IMAGE 3 — COMPLETELY UNCHANGED: the wide pulled-back camera and its framing and crop; the cracked circular ferrocrete pad, its concentric worn ivory ring markings and the large worn ivory PLUS at its centre; the two big ferrocrete service buildings flanking left and right, cut by the left and right frame edges, with their MUTED TEAL green-blue paint patches exactly as they are — no red anywhere on either building; the tilted weathered mast; the broken rock plain and its angular foreground shelves; the two dark near-side lamp posts seen from behind and the lit far-side lamps facing the viewer, every lamp pool falling inward on the slab; the small lone robed figure at lower left at exactly her current size and position, in her full-length slate blue-gray robe with ochre hem, dust mask, dark goggles and signal lamp, head tipped up watching; the pale flat moon at upper left; the flat deep slate blue-black sky and its sparse flat ivory stars; the distant cobalt storm wall with its lightning low on the right horizon; the warm ochre lamplight against deep slate blue-violet shadow. Do not re-frame, do not zoom, do not move or resize anything.

DO NOT ROTATE THE SHIP. The Antares keeps exactly the three-quarter viewing angle it has in image 3, with its upper deck on show. Do not turn the hull, do not flatten it into a side view, do not change the camera on it. It stays the same size, level, long axis horizontal and parallel to the pad, nose to the left, hull centred above the plus. Keep its broad brick-red roof panel and the circular roof hatch reading as a full circle within it, the red block on the cockpit's aft side wall, the raised central spine, the upper deck panels, the cargo door low on the side wall, the small square side windows, the ~5-pane windscreen with its thick ivory mullions, and its two brick-red banded engine pods with the near one aft on this side and the far one showing above the roofline — all exactly as image 3 has them. The NOSE KEEPS ITS CURRENT LENGTH: it was adjusted to the correct length already and must not get longer or shorter. Its two landing plumes stay exactly where they are and keep their present organic form and size: irregular billowing tongues of flame and blown dust with wobbling hand-painted contours, built from two or three FLAT OPAQUE shapes of solid colour — pale ochre outer mass, brighter ivory tongues inside — fully opaque, with no glow, bloom, halo, gradient, blur, feathered edge, transparency, light cone or volumetric beam. Their feet stay on the plus's left-to-right axis, straddling the plus. Exactly two plumes; no thrust from the engine pods.

THE ONE CHANGE — TURN THE NOSE'S FRONT FACE FURTHER AWAY FROM THE CAMERA. In image 3 the blunt flat face at the front of the nose — the facet carrying the louvered grille — still reads as angled toward the viewer, as though the very tip of the ship were swivelled to show us its front. It must sit much closer to edge-on.

USE THE SHIP'S OWN GEOMETRY AS THE REFERENCE. The nose's flat front face is PERPENDICULAR to the ship's long axis. So is the round intake face at the front of the near engine pod, and so is the flat squared-off end of the tail. All three lie in PARALLEL planes. At this camera angle the pod's intake face is compressed into a narrow oblique ellipse, and the tail end is compressed into a narrow sliver. THE NOSE'S FRONT FACE MUST BE COMPRESSED EXACTLY AS HARD. If the nose's front face looks broader or more face-on than the pod's intake face does, it is wrong — narrow it until they match.

Concretely, after the change:
- The front face is a NARROW SLIVER at the very front of the ship, taking up no more than about a fifth of the nose's apparent width. It is a thin edge, not a panel.
- The nose's LEFT FLANK dominates completely — it is by far the largest surface we see of the nose, running away cleanly toward the left of the frame, exactly parallel to the hull's flank behind it and to the line running back through the cargo door to the engine pods.
- The nose's upper deck likewise runs away to the left, parallel to the rest of the ship's upper deck. No facet of the nose fans outward toward the viewer.
- There is no kink, step or change of direction where the nose meets the cockpit: one unbroken line along the ship's left side from tip to tail.

THE LOUVERED GRILLE STAYS. It is set into the lower part of that front face and keeps its horizontal slats, recessed frame and raised ivory lip. As the face narrows the grille narrows with it — it becomes a tight, steeply compressed slot seen almost edge-on. Keep it legible and keep it the darkest shape on the nose, but do not widen it, do not turn it toward the camera, and do not remove it.

The nose stays blunt-ended and keeps its full width and heft right up to that narrow front edge; its sides converge only gently. It is not a spike and not a stump.

Keep the hull centred above the plus and keep both plume feet exactly where they are on the plus's axis — the plumes do not move.

PAINT IT LIKE THE REST OF THE PICTURE: image 2 is a flat sheet drawing on a plain background and is a guide to SHAPE ONLY. The repainted nose belongs in this night scene — lit from below by the warm ochre lamp pools, edged along its upper surfaces by the cold pale moon and sky, with its underside and far flank in one deep slate blue-violet shadow plane, built from flat opaque colour planes with hard angular edges exactly like every other form in image 3.

LIGHT: night scene, unchanged from image 3. No neon, no rim lighting, no bloom, no light rays.

Change nothing else about image 3.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
