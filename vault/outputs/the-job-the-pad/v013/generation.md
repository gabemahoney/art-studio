# the-job-the-pad v013

User request verbatim: No, now the nose is a vertical rectangle.
Mode: Edit off v012 baseline, correcting my own over-correction: v012's front facet was specified by width alone and became a tall upright slab. Now specified by PROPORTION — the front face must be 2-3x wider than tall, a low horizontal letterbox, reached mainly by lowering the tip (underside up, upper deck down) rather than by swinging the face toward the camera; the louvered grille likewise respecified as a horizontal slot with side-to-side slats. Nose length and direction, ship rotation, angle, pods, plumes, buildings, lamps, figure, pad and sky all held.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0ef2b-e670-7843-bdbb-a15c673edfde/exec-b863b0b2-45a7-4b48-abb0-43850ad50ea8.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/ships/the_antares/sources/hero-3q-crop-from-v033.png
- Image 3 EDIT TARGET: outputs/the-job-the-pad/v012/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.09 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Proportion fixed. The upright slab is gone: the nose now ends in a low horizontal chisel, the front face clearly wider than it is tall, reached the intended way -- the underside sweeps up and the upper deck slopes down so the ship genuinely tapers to a shallow edge -- rather than by swinging the face back toward the camera. The louvered intake grille is correspondingly a wide horizontal slot with side-to-side slats, recessed frame and raised ivory lip, still the darkest shape on the nose. This corrects my own over-correction in v012, where I specified the facet by width alone and said nothing about its proportion; naming the target proportion (2-3x wider than tall) is what fixed it. Held from v012: nose length and direction, the de-yawed orientation with the left flank dominant and running unbroken to the left with no kink at the cockpit join, the three-quarter viewing angle with upper deck on show, broad brick-red roof panel, circular hatch as a full circle, aft cockpit red block, raised spine, far pod above the roofline, near pod aft, ~5-pane windscreen, teal building patches with no red, inward-facing lamps, figure unmoved at lower left, pad, plus, and both plumes still straddling the plus on its left-right axis. One minor drift to note: the moon has picked up a slightly warmer, more ochre cast than the pale gray-ivory disc in v012. Small, and only visible side by side. The above-eye-level top deck remains a deliberate perspective liberty accepted by the user; v008 is the geometrically strict alternative on record. Kia remains IMPROVISED -- no approved asset exists for her, so this image establishes nothing about her design. Belly landing thrusters remain absent from Antares description v20 and need a version bump if this candidate is promoted.

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
Image 3 is EDIT TARGET: The scene baseline: the-job-the-pad v012, approved by the user except that the nose's front end has become a tall upright vertical rectangle instead of a low wide chisel.

TASK: A single horizontal wide night illustration: the freighter Antares settling onto the centre of a derelict landing pad on Kalagra, flanked by large teal-marked service buildings, watched by one small distant operator.

THE SHIP — THE ANTARES (description v20, distilled for this scene). Image 2 is ONE single three-quarter view of this ship and is the authority on every shape below. It shows the whole ship at once; there are no other views to reconcile.

A broad, low, wedge-shaped utility freighter. Ivory / light-gray hull with brick-red accents; dark windows and openings.

HULL: one solid body, wider than it is tall and about twice as long as it is wide — a blunt wedge, not a long tube. The cockpit is at the very FRONT: a faceted glasshouse of dark angled windows in a sloping nose, with a brick-red roof panel around a circular hatch directly behind it. Behind the cockpit the body widens into a flat-shouldered midsection carrying a single raised central spine along the centerline and shallow recessed deck panels either side of it. A single broad rectangular cargo door sits low on the port side wall, behind the cockpit and ahead of the engines. The body ends in a squared-off tail.

ENGINE PODS — THE CRITICAL GEOMETRY: exactly TWO engine pods, and they are an IDENTICAL, MIRRORED PAIR. Both sit at the SAME position along the ship's length: aft of midships, flanking the rear third of the hull, level with each other. Neither pod is anywhere near the cockpit; no pod sits forward, beside, or ahead of the cabin. They are mounted outboard on short structural bridges, held clear of the hull sides, separated by roughly four pod diameters.

Each pod is a squat round drum — its total length including the short aft nozzle is only about 1.4 times its diameter. They are stubby barrels, NOT long nacelles. Both pod axes run straight fore-and-aft, exactly parallel to each other and to the ship's central spine: intake ring facing FORWARD, nozzle facing AFT. Neither pod is tilted, yawed, splayed, or rotated. Each pod is painted in banded blocks: dark gray intake rim, then brick-red, then an ivory band, then a dark aft cap.

Everything about the ship — proportions, the brick-red and ivory placement, the cockpit facets, the cargo door, the pod pair — is copied from image 2. Image 2 already shows the pods correctly placed; match that placement exactly.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame, horizontal. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO orthographic views, NO labels, NO text of any kind. There is exactly ONE spacecraft and exactly ONE human figure in this image and no other people anywhere. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors or composition. Image 2 contributes the SHIP'S DESIGN ONLY — do not copy its flat blue background. Image 3 is the SCENE BASELINE: reproduce it faithfully and change only the ONE thing specified below.

SCENE: "The Pad." Night on the barren planet Kalagra. A wide establishing shot of a lonely derelict landing pad on an open rock plain, with the freighter Antares coming down onto it and one small figure watching.

Image 3 is APPROVED and correct in every respect but one: the blunt front end of the nose has become a TALL UPRIGHT SLAB — a vertical rectangle standing on end at the front of the ship. That is the wrong proportion. Reproduce image 3 exactly — same camera, same framing, same crop, same scale, same colours, same light, same paint handling, same ship, same nose LENGTH, same orientation — and reshape only that front end.

KEEP FROM IMAGE 3 — COMPLETELY UNCHANGED: the wide pulled-back camera and its framing and crop; the cracked circular ferrocrete pad, its concentric worn ivory ring markings and the large worn ivory PLUS at its centre; the two big ferrocrete service buildings flanking left and right, cut by the left and right frame edges, with their MUTED TEAL green-blue paint patches exactly as they are — no red anywhere on either building; the tilted weathered mast; the broken rock plain and its angular foreground shelves; the two dark near-side lamp posts seen from behind and the lit far-side lamps facing the viewer, every lamp pool falling inward on the slab; the small lone robed figure at lower left at exactly her current size and position, in her full-length slate blue-gray robe with ochre hem, dust mask, dark goggles and signal lamp, head tipped up watching; the pale flat moon at upper left; the flat deep slate blue-black sky and its sparse flat ivory stars; the distant cobalt storm wall with its lightning low on the right horizon; the warm ochre lamplight against deep slate blue-violet shadow. Do not re-frame, do not zoom, do not move or resize anything.

DO NOT ROTATE THE SHIP AND DO NOT CHANGE THE NOSE'S LENGTH OR DIRECTION. The Antares keeps exactly the three-quarter viewing angle it has in image 3, with its upper deck on show. It stays the same size, level, long axis horizontal and parallel to the pad, nose to the left, hull centred above the plus. Keep its broad brick-red roof panel and the circular roof hatch reading as a full circle within it, the red block on the cockpit's aft side wall, the raised central spine, the upper deck panels, the cargo door low on the side wall, the small square side windows, the ~5-pane windscreen with its thick ivory mullions, and its two brick-red banded engine pods with the near one aft on this side and the far one showing above the roofline — all exactly as image 3 has them. The nose keeps its current LENGTH and keeps pointing where it points: along the hull's long axis, to the left and slightly away from the viewer, its left flank running away to the left, flush and unbroken with the cockpit and hull behind it. Its two landing plumes stay exactly where they are and keep their present organic form and size: irregular billowing tongues of flame and blown dust with wobbling hand-painted contours, built from two or three FLAT OPAQUE shapes of solid colour — pale ochre outer mass, brighter ivory tongues inside — fully opaque, with no glow, bloom, halo, gradient, blur, feathered edge, transparency, light cone or volumetric beam. Their feet stay on the plus's left-to-right axis, straddling the plus. Exactly two plumes; no thrust from the engine pods.

THE ONE CHANGE — MAKE THE NOSE'S FRONT END LOW AND WIDE INSTEAD OF TALL AND NARROW. Look at how image 2 ends the nose: the Antares is a FLATTENED wedge. In plan it is broad; in height it is shallow. Its underside sweeps UP toward the front and its upper deck slopes DOWN toward the front, and the two converge until they meet in a SHORT, LOW, HORIZONTAL CHISEL EDGE. The front end is a letterbox: a wide, shallow band lying on its side.

In image 3 that front end has instead become a tall upright rectangle — a narrow slab standing on end, taller than it is wide. Reshape it:

- The flat front face of the nose is WIDER ACROSS THE SHIP THAN IT IS TALL — roughly two to three times as wide as it is high. It is a low horizontal band. Seen at this three-quarter angle it appears as a slanted horizontal parallelogram, but it NEVER becomes taller than it is wide, and it is NEVER an upright rectangle, a vertical slab, or a square.
- Get there mainly by LOWERING THE TIP, not by swinging the face toward the camera. Bring the nose's underside further UP and its upper deck further DOWN as they approach the front, so the ship genuinely tapers to a shallow edge. The nose becomes a thin, flattened wedge at its end.
- The face may be a little wider than it is in image 3, but only a little. Do not fan it back around toward the viewer. Its orientation stays as in image 3 — perpendicular to the hull's long axis, parallel to the near pod's round intake face and to the flat end of the tail, and foreshortened accordingly.
- The nose keeps its full WIDTH and heft in plan right up to that low front edge; its sides converge only gently. It is blunt, not a spike, and not a stump.

THE LOUVERED GRILLE IS ALSO A HORIZONTAL SLOT, NOT AN UPRIGHT ONE. It sits in the lower part of that low front face and matches its proportion: clearly wider than it is tall, filled with a few HORIZONTAL slats running side to side, in a recessed frame with a raised ivory lip. Keep it legible and keep it the darkest shape on the nose. It must not be a tall narrow vertical slot.

Keep the hull centred above the plus and keep both plume feet exactly where they are on the plus's axis — the plumes do not move.

PAINT IT LIKE THE REST OF THE PICTURE: image 2 is a flat sheet drawing on a plain background and is a guide to SHAPE ONLY. The repainted nose belongs in this night scene — lit from below by the warm ochre lamp pools, edged along its upper surfaces by the cold pale moon and sky, with its underside and far flank in one deep slate blue-violet shadow plane, built from flat opaque colour planes with hard angular edges exactly like every other form in image 3.

LIGHT: night scene, unchanged from image 3. No neon, no rim lighting, no bloom, no light rays.

Change nothing else about image 3.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
