# the-job-the-pad v014

User request verbatim: Now the nose is facing the camera to much.
Mode: BRANCH off v010, abandoning the v011-v013 line which oscillated between slab and face-on. Diagnosis: trimming nose LENGTH while leaving the tip's cross-section unchanged makes the front face proportionally larger, which reads as the nose swinging toward the camera — so each length fix reintroduced the angle fault. Fix: from v010 (user: nose angle and shape perfect, only too long), scale the ENTIRE nose down uniformly to ~5/6 in every dimension at once — length and front-face width and height together, all facet angles identical, nothing re-aimed. Also restates the moon as cool gray-ivory to undo v013's warm drift.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f03f-2dd6-7130-a5e8-2394f5f16590/exec-85fe517d-0e43-4e33-8a2f-c95836b697c0.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/ships/the_antares/sources/hero-3q-crop-from-v033.png
- Image 3 EDIT TARGET: outputs/the-job-the-pad/v010/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.13 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Branch off v010 rather than a fourth correction on the v011-v013 line, which had begun oscillating: narrowing the front facet produced a vertical slab (v012), widening it by proportion produced a face-on nose (v013). Root cause identified: every pass trimmed nose LENGTH while leaving the blunt tip's cross-section unchanged, which makes the front face proportionally larger and reads as the nose swinging toward the camera -- so each length fix silently reintroduced the angle fault. Fix applied here: from v010, whose nose angle and shape the user called perfect, scale the ENTIRE nose down uniformly to ~5/6 in every dimension at once, all facet angles identical. Side-by-side crops of v010 and v014 confirm it worked: the nose is visibly shorter with the windscreen closer to the tip, while the front face keeps v010's aspect -- low, wide, turned away -- and the left flank still dominates, running unbroken to the left with no kink at the cockpit join. The louvered grille scaled down with the tip and remains a horizontal slot with side-to-side slats, legible and still the darkest shape on the nose. v013's warm moon drift is undone: the moon is back to a cool pale gray-ivory disc. Everything else intact: three-quarter viewing angle with upper deck on show, broad brick-red roof panel, circular hatch as a full circle, aft cockpit red block, raised spine, far pod above the roofline, near pod aft, ~5-pane windscreen, teal building patches with no red, inward-facing lamps, figure unmoved at lower left, pad, plus, and both plumes still straddling the plus on its left-right axis. No new discrepancies found. The above-eye-level top deck remains a deliberate perspective liberty accepted by the user; v008 is the geometrically strict alternative on record. The belly landing thrusters are a DELIBERATE scene-local invention: the user has decided they will NOT be added to Antares description.md, since this is the only landing shot of the ship. Do not "fix" that gap in a later session. Kia remains IMPROVISED -- no approved asset exists for her, so this image establishes nothing about her design.

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
Image 2 is IDENTITY: A single three-quarter view of the freighter Antares, cropped from its approved reference sheet — the same viewing angle the scene uses. It is the authority on the nose's proportions: a flattened wedge, broad in plan and shallow in height, ending in a low horizontal chisel edge with a wide louvered intake slot. Ignore its flat blue background.
Image 3 is EDIT TARGET: The scene baseline: the-job-the-pad v010, which the user approved in every respect except that the nose is slightly too long. Its nose ANGLE and SHAPE are correct and must be preserved.

TASK: A single horizontal wide night illustration: the freighter Antares settling onto the centre of a derelict landing pad on Kalagra, flanked by large teal-marked service buildings, watched by one small distant operator.

THE SHIP — THE ANTARES (description v20, distilled for this scene). Image 2 is ONE single three-quarter view of this ship and is the authority on every shape below. It shows the whole ship at once; there are no other views to reconcile.

A broad, low, wedge-shaped utility freighter. Ivory / light-gray hull with brick-red accents; dark windows and openings.

HULL: one solid body, wider than it is tall and about twice as long as it is wide — a blunt wedge, not a long tube. The cockpit is at the very FRONT: a faceted glasshouse of dark angled windows in a sloping nose, with a brick-red roof panel around a circular hatch directly behind it. Behind the cockpit the body widens into a flat-shouldered midsection carrying a single raised central spine along the centerline and shallow recessed deck panels either side of it. A single broad rectangular cargo door sits low on the port side wall, behind the cockpit and ahead of the engines. The body ends in a squared-off tail.

ENGINE PODS — THE CRITICAL GEOMETRY: exactly TWO engine pods, and they are an IDENTICAL, MIRRORED PAIR. Both sit at the SAME position along the ship's length: aft of midships, flanking the rear third of the hull, level with each other. Neither pod is anywhere near the cockpit; no pod sits forward, beside, or ahead of the cabin. They are mounted outboard on short structural bridges, held clear of the hull sides, separated by roughly four pod diameters.

Each pod is a squat round drum — its total length including the short aft nozzle is only about 1.4 times its diameter. They are stubby barrels, NOT long nacelles. Both pod axes run straight fore-and-aft, exactly parallel to each other and to the ship's central spine: intake ring facing FORWARD, nozzle facing AFT. Neither pod is tilted, yawed, splayed, or rotated. Each pod is painted in banded blocks: dark gray intake rim, then brick-red, then an ivory band, then a dark aft cap.

Everything about the ship — proportions, the brick-red and ivory placement, the cockpit facets, the cargo door, the pod pair — is copied from image 2. Image 2 already shows the pods correctly placed; match that placement exactly.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame, horizontal. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO orthographic views, NO labels, NO text of any kind. There is exactly ONE spacecraft and exactly ONE human figure in this image and no other people anywhere. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors or composition. Image 2 contributes the SHIP'S DESIGN ONLY — do not copy its flat blue background. Image 3 is the SCENE BASELINE: reproduce it faithfully and change only the ONE thing specified below.

SCENE: "The Pad." Night on the barren planet Kalagra. A wide establishing shot of a lonely derelict landing pad on an open rock plain, with the freighter Antares coming down onto it and one small figure watching.

Image 3 is APPROVED. Its composition, its ship, its lighting and — importantly — the ANGLE AND SHAPE of its nose are all correct. The single fault is that the nose is slightly too LONG. Reproduce image 3 exactly and make the nose a little smaller.

KEEP FROM IMAGE 3 — COMPLETELY UNCHANGED: the wide pulled-back camera and its framing and crop; the cracked circular ferrocrete pad, its concentric worn ivory ring markings and the large worn ivory PLUS at its centre; the two big ferrocrete service buildings flanking left and right, cut by the left and right frame edges, with their MUTED TEAL green-blue paint patches exactly as they are — no red anywhere on either building; the tilted weathered mast; the broken rock plain and its angular foreground shelves; the two dark near-side lamp posts seen from behind and the lit far-side lamps facing the viewer, every lamp pool falling inward on the slab; the small lone robed figure at lower left at exactly her current size and position, in her full-length slate blue-gray robe with ochre hem, dust mask, dark goggles and signal lamp, head tipped up watching; the pale GRAY-IVORY moon at upper left — a cool pale disc, not warm or ochre; the flat deep slate blue-black sky and its sparse flat ivory stars; the distant cobalt storm wall with its lightning low on the right horizon; the warm ochre lamplight against deep slate blue-violet shadow. Do not re-frame, do not zoom, do not move or resize anything.

DO NOT ROTATE THE SHIP. The Antares keeps exactly the three-quarter viewing angle it has in image 3, with its upper deck on show. It stays the same size, level, long axis horizontal and parallel to the pad, nose to the left, hull centred above the plus. Keep its broad brick-red roof panel and the circular roof hatch reading as a full circle within it, the red block on the cockpit's aft side wall, the raised central spine, the upper deck panels, the cargo door low on the side wall, the small square side windows, the ~5-pane windscreen with its thick ivory mullions, and its two brick-red banded engine pods with the near one aft on this side and the far one showing above the roofline — all exactly as image 3 has them. Its two landing plumes stay exactly where they are and keep their present organic form and size: irregular billowing tongues of flame and blown dust with wobbling hand-painted contours, built from two or three FLAT OPAQUE shapes of solid colour — pale ochre outer mass, brighter ivory tongues inside — fully opaque, with no glow, bloom, halo, gradient, blur, feathered edge, transparency, light cone or volumetric beam. Their feet stay on the plus's left-to-right axis, straddling the plus. Exactly two plumes; no thrust from the engine pods.

THE ONE CHANGE — SHRINK THE WHOLE NOSE UNIFORMLY BY ABOUT ONE SIXTH. Treat the nose — everything forward of the windscreen — as a single solid object and SCALE IT DOWN as a whole, to roughly five sixths of its current size, about it staying attached to the cockpit. This is a uniform reduction, not a trim.

THIS IS THE CRITICAL PART: shrink it in EVERY dimension AT ONCE, by the SAME fraction.
- Its LENGTH reduces by about one sixth.
- Its blunt front end reduces by the SAME one sixth — the front face becomes correspondingly SMALLER in both its width across the ship and its height.
- Every facet angle stays IDENTICAL. Nothing rotates. Nothing is re-aimed.

DO NOT simply pull the tip backwards while leaving the front end the size it is. That is the mistake to avoid: if the nose gets shorter but its blunt end stays as big as before, the front face ends up proportionally larger, and the nose starts to look as though it has swung round to face the camera. It must not. The whole nose gets smaller together, so that its proportions and its apparent aspect are exactly what they are in image 3 — just scaled down.

Everything about the nose's SHAPE AND AIM in image 3 is correct and must be preserved exactly, only smaller:
- It points along the hull's long axis, to the left and slightly away from the viewer. Its blunt front face stays turned away to the same degree, no more face-on than it is now.
- Its LEFT FLANK remains the dominant surface we see, running away cleanly toward the left of the frame, flush and unbroken with the cockpit and hull behind it — one continuous line from tip to tail, no kink at the join.
- The front end stays a LOW, WIDE horizontal chisel — wider across the ship than it is tall — never an upright slab, never a vertical rectangle, never a square.
- The nose stays blunt and keeps its heft: its sides converge only gently, it is not a spike and not a stump.
- The DARK LOUVERED GRILLE stays in the lower part of that front face, scaled down with it, still a horizontal slot wider than it is tall with side-to-side slats, a recessed frame and a raised ivory lip. It remains legible and remains the darkest shape on the nose.

Shrinking the nose shortens the ship slightly overall. Keep the hull centred above the plus and keep both plume feet exactly where they are on the plus's axis — the plumes do not move.

PAINT IT LIKE THE REST OF THE PICTURE: image 2 is a flat sheet drawing on a plain background and is a guide to SHAPE ONLY. The repainted nose belongs in this night scene — lit from below by the warm ochre lamp pools, edged along its upper surfaces by the cold pale moon and sky, with its underside and far flank in one deep slate blue-violet shadow plane, built from flat opaque colour planes with hard angular edges exactly like every other form in image 3.

LIGHT: night scene, unchanged from image 3. No neon, no rim lighting, no bloom, no light rays.

Change nothing else about image 3.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
