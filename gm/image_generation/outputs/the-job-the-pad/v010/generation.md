# the-job-the-pad v010

User request verbatim: The nose is too stubby and angled toward the camera.
Mode: Edit off v009 baseline, single change to the nose only: lengthened by about half again (v009 overshot the shortening from v007), and de-yawed so it follows the hull's long axis instead of swinging its blunt front face flat toward the camera — front face now edge-on and foreshortened, left flank continuous with the cockpit and hull, louvered grille kept but compressed to a narrow slot. Viewing angle, red roof panel, circular hatch, spine, pods, plumes, buildings, lamps, figure, pad and sky all held.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0ef21-db6b-7e83-bdd1-c3e89ad6c83a/exec-317292f3-47de-4033-8b4d-497211a85850.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/ships/the_antares/sources/hero-3q-crop-from-v033.png
- Image 3 EDIT TARGET: outputs/the-job-the-pad/v009/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.99 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Both nose faults fixed. Length: the stump is gone -- the nose now reads as a substantial forward-reaching wedge with real hull ahead of the windscreen, sitting between v007's over-long snout and v009's over-cut stub. Orientation: the blunt front face is no longer swung flat toward the camera. It is now steeply foreshortened to a narrow facet at the far left, with the nose's left flank and sloping upper deck running away to the left, flush and continuous with the cockpit and hull behind them -- one unbroken line from tip to tail, no kink at the cockpit join. The louvered intake grille survived the de-yaw: still the darkest shape on the nose, still legible with horizontal slats and a raised ivory lip, correctly compressed into a narrow slot seen at a steep angle. Windscreen holds at ~5 broad trapezoidal panes with thick mullions. Everything else carried over from v009 intact: three-quarter viewing angle, broad brick-red roof panel, circular hatch as a full circle, aft cockpit red block, raised spine, upper deck panels, far pod above the roofline, near pod aft, teal building patches with no red, inward-facing lamps, figure, pad, plus, and both plumes unmoved on the plus's left-right axis. Residual: the nose may sit a touch longer than the hero crop's and its underside plane reads slightly thin -- both minor at full size. The above-eye-level top deck remains a deliberate perspective liberty accepted by the user; v008 is the geometrically strict alternative on record. Kia remains IMPROVISED -- no approved asset. Belly landing thrusters remain absent from Antares description v20 and need a bump if this is promoted.

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
Image 2 is IDENTITY: A single three-quarter view of the freighter Antares, cropped from its approved reference sheet — the same viewing angle the scene uses. It is the authority on the nose: its length ahead of the windscreen, its blunt end, how its front face sits nearly edge-on with the hull's axis, and the windscreen's pane count. Ignore its flat blue background.
Image 3 is EDIT TARGET: The scene baseline: the-job-the-pad v009. Everything in it is correct except that the nose is too short and is yawed toward the camera.

TASK: A single horizontal wide night illustration: the freighter Antares settling onto the centre of a derelict landing pad on Kalagra, flanked by large teal-marked service buildings, watched by one small distant operator.

THE SHIP — THE ANTARES (description v20, distilled for this scene). Image 2 is ONE single three-quarter view of this ship and is the authority on every shape below. It shows the whole ship at once; there are no other views to reconcile.

A broad, low, wedge-shaped utility freighter. Ivory / light-gray hull with brick-red accents; dark windows and openings.

HULL: one solid body, wider than it is tall and about twice as long as it is wide — a blunt wedge, not a long tube. The cockpit is at the very FRONT: a faceted glasshouse of dark angled windows in a sloping nose, with a brick-red roof panel around a circular hatch directly behind it. Behind the cockpit the body widens into a flat-shouldered midsection carrying a single raised central spine along the centerline and shallow recessed deck panels either side of it. A single broad rectangular cargo door sits low on the port side wall, behind the cockpit and ahead of the engines. The body ends in a squared-off tail.

ENGINE PODS — THE CRITICAL GEOMETRY: exactly TWO engine pods, and they are an IDENTICAL, MIRRORED PAIR. Both sit at the SAME position along the ship's length: aft of midships, flanking the rear third of the hull, level with each other. Neither pod is anywhere near the cockpit; no pod sits forward, beside, or ahead of the cabin. They are mounted outboard on short structural bridges, held clear of the hull sides, separated by roughly four pod diameters.

Each pod is a squat round drum — its total length including the short aft nozzle is only about 1.4 times its diameter. They are stubby barrels, NOT long nacelles. Both pod axes run straight fore-and-aft, exactly parallel to each other and to the ship's central spine: intake ring facing FORWARD, nozzle facing AFT. Neither pod is tilted, yawed, splayed, or rotated. Each pod is painted in banded blocks: dark gray intake rim, then brick-red, then an ivory band, then a dark aft cap.

Everything about the ship — proportions, the brick-red and ivory placement, the cockpit facets, the cargo door, the pod pair — is copied from image 2. Image 2 already shows the pods correctly placed; match that placement exactly.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame, horizontal. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO orthographic views, NO labels, NO text of any kind. There is exactly ONE spacecraft and exactly ONE human figure in this image and no other people anywhere. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors or composition. Image 2 contributes the SHIP'S DESIGN ONLY — do not copy its flat blue background. Image 3 is the SCENE BASELINE: reproduce it faithfully and change only the ONE thing specified below.

SCENE: "The Pad." Night on the barren planet Kalagra. A wide establishing shot of a lonely derelict landing pad on an open rock plain, with the freighter Antares coming down onto it and one small figure watching.

Image 3 is correct in every respect except the length and the orientation of the ship's nose. Reproduce it exactly — same camera, same framing, same crop, same scale, same colours, same light, same paint handling — and repaint only the nose.

KEEP FROM IMAGE 3 — COMPLETELY UNCHANGED: the wide pulled-back camera and its framing and crop; the cracked circular ferrocrete pad, its concentric worn ivory ring markings and the large worn ivory PLUS at its centre; the two big ferrocrete service buildings flanking left and right, cut by the left and right frame edges, with their MUTED TEAL green-blue paint patches exactly as they are — no red anywhere on either building; the tilted weathered mast; the broken rock plain and its angular foreground shelves; the two dark near-side lamp posts seen from behind and the lit far-side lamps facing the viewer, every lamp pool falling inward on the slab; the small lone robed figure at lower left at exactly her current size and position, in her full-length slate blue-gray robe with ochre hem, dust mask, dark goggles and signal lamp, head tipped up watching; the pale flat moon at upper left; the flat deep slate blue-black sky and its sparse flat ivory stars; the distant cobalt storm wall with its lightning low on the right horizon; the warm ochre lamplight against deep slate blue-violet shadow. Do not re-frame, do not zoom, do not move or resize anything.

KEEP THE SHIP'S VIEWING ANGLE, POSITION, SIZE AND EVERY OTHER PART OF IT: the Antares keeps exactly the three-quarter viewing angle it has in image 3, with its upper deck on show. Do NOT rotate the ship, do NOT flatten it into a side view, do NOT change the camera on it. It stays the same size, level, long axis horizontal and parallel to the pad, nose to the left, hull centred above the plus. Keep its broad brick-red roof panel and the circular roof hatch reading as a full circle within it, the red block on the cockpit's aft side wall, the raised central spine, the upper deck panels, the cargo door low on the side wall, the small square side windows, and its two brick-red banded engine pods with the near one aft on this side and the far one showing above the roofline — all exactly as image 3 has them. Its two landing plumes stay exactly where they are and keep their present organic form and size: irregular billowing tongues of flame and blown dust with wobbling hand-painted contours, built from two or three FLAT OPAQUE shapes of solid colour — pale ochre outer mass, brighter ivory tongues inside — fully opaque, with no glow, bloom, halo, gradient, blur, feathered edge, transparency, light cone or volumetric beam. Their feet stay on the plus's left-to-right axis, straddling the plus. Exactly two plumes; no thrust from the engine pods.

THE ONE CHANGE — LENGTHEN THE NOSE AND TURN ITS FACE AWAY FROM THE CAMERA. Two faults, both in the nose alone:

FAULT ONE — IT IS TOO STUBBY. In image 3 the nose was cut back too far and now reads as a squat stump. LENGTHEN it: extend the nose forward, away from the windscreen, by about half again its current length. It should read as a purposeful forward-reaching wedge — a nose with real length ahead of the cockpit — while still being blunt-ended and chunky rather than a slim tapering snout. It is neither a stump nor a spike: a substantial wedge with a blunt end.

FAULT TWO — IT IS YAWED TOWARD THE VIEWER. In image 3 the blunt front face of the nose, with its louvered grille, is swung around to face the camera almost flat-on, as though the nose were rotated independently of the rest of the ship. That is wrong. The ship is ONE rigid body on ONE axis: the nose points where the hull points.

Turn the nose so it follows the hull's own long axis — pointing LEFT and slightly AWAY from the viewer, exactly parallel to the line running back through the cargo door to the engine pods. The consequences, all of which must be visible:
- The nose's blunt FRONT FACE is nearly edge-on to us. It is strongly foreshortened — a NARROW sliver of surface at the very front, not a broad flat panel presented to the camera.
- What we mainly see of the nose is its LEFT FLANK and the sloping top of its upper deck, both running away from us toward the left of the frame.
- The nose's left flank lies flush and continuous with the cockpit's left flank and the hull's left side behind it: one unbroken line from the nose tip back along the ship. There is no kink, step or change of direction where the nose meets the cockpit.
- The DARK LOUVERED GRILLE stays — it is set into the lower part of that blunt front face and keeps its horizontal slats, recessed frame and raised ivory lip — but because the face is now edge-on, the grille is correspondingly narrow and foreshortened. Keep it legible and keep it the darkest shape on the nose, but it is a compressed slot seen at a steep angle, not a rectangle facing us.

Keep the WINDSCREEN as image 2 draws it: a wrapping band of dark angled panes separated by THICK ivory mullions, about FIVE panes across, the panes broad and trapezoidal rather than many narrow slivers. It sits high and forward, and with the longer nose it now has proper hull ahead of it.

Lengthening the nose lengthens the ship slightly overall. Keep the hull centred above the plus and keep both plume feet exactly where they are on the plus's axis — the plumes do not move.

PAINT IT LIKE THE REST OF THE PICTURE: image 2 is a flat sheet drawing on a plain background and is a guide to SHAPE ONLY. The repainted nose belongs in this night scene — lit from below by the warm ochre lamp pools, edged along its upper surfaces by the cold pale moon and sky, with its underside and far flank in one deep slate blue-violet shadow plane, built from flat opaque colour planes with hard angular edges exactly like every other form in image 3.

LIGHT: night scene, unchanged from image 3. No neon, no rim lighting, no bloom, no light rays.

Change nothing else about image 3.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
