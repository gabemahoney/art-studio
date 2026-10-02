# the-job-the-pad v004

User request verbatim: Make the ship landing more in the center of the pad. Make the building even bigger. They extend beyond the frame of the image. Make the plumes a little more organic, less geometric.
Mode: Edit off v003 baseline (user-designated): ship re-centred over the pad's plus with both plumes landing symmetrically about it; service buildings enlarged until cropped by the left and right frame edges; plume contours changed from straight-sided cones to irregular organic flame tongues while keeping flat opaque paint and the no-glow ban; dust skirts restated as torn sheets not rubble
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0ee74-bbc3-7981-af25-9550d7e92dd6/exec-073dc3e8-001d-45c5-b378-3e7934390298.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/ships/the_antares/sources/hero-3q-crop-from-v033.png
- Image 3 EDIT TARGET: outputs/the-job-the-pad/v003/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.34 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: All three requests landed. The service buildings are now large flanking masses cut by the left and right frame edges, rooflines well above the horizon, pad still unobstructed between them. The ship sits centred over the pad with both plumes coming down symmetrically either side of the painted plus. The plumes are markedly more organic — irregular billowing flame-and-dust tongues with wobbling hand-painted contours, no straight-sided cones — and much flatter and more opaque than v003's spotlights, though a little soft glow remains at their bases. Lamps still face inward; plus, moon, sky and figure carried over unchanged. Remaining discrepancies: (1) the far engine pod still reads as a brick-red drum mounted ON TOP of the hull, forward of the near pod, rather than the far half of a matched aft pair — persists from v003; (2) hull proportions remain longer and flatter than the broad chunky wedge in the identity crop, with the cockpit undersized; (3) the distant storm has shrunk and is now half-occluded by the right-hand building, weakening the 'weather not yet arrived' beat; (4) foreground rock is densely faceted, against the Style Block's instruction that large areas stay quiet. Kia remains IMPROVISED — no approved asset. Belly landing thrusters are still not in description v20; the Antares design needs a bump if they are kept. NOTE: a first attempt at this prompt generated and billed an image but crashed in bin/gen.py before allocating v004 (target_dir signature mismatch — bin/ changed under the run); that output is orphaned at ~/.codex/generated_images/01a0ee72-90c0-7e12-b8d6-d8225d7d1259 and was never part of this scene's history.

CORRECTION (2026-09-29): this receipt's Review claims the far engine pod reads as a brick-red drum mounted on top of the hull. That finding was WRONG and is withdrawn. Magnified measurement against the identity crop shows the far pod correctly behind the hull, peeking above the roofline, with its forward offset explained by perspective foreshortening (~49% of hull length in the crop's strong three-quarter, ~23% here). See outputs/the-job-the-pad/v005/generation.md.

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
Image 3 is EDIT TARGET: The scene baseline: the-job-the-pad v003, designated by the user. Its setting, framing, composition and lighting are what 'unchanged' refers to below.

TASK: A single horizontal wide night illustration: the freighter Antares descending level onto the centre of a derelict landing pad on Kalagra, flanked by large service buildings, watched by one small distant operator.

THE SHIP — THE ANTARES (description v20, distilled for this scene). Image 2 is ONE single three-quarter view of this ship and is the authority on every shape below. It shows the whole ship at once; there are no other views to reconcile.

A broad, low, wedge-shaped utility freighter. Ivory / light-gray hull with brick-red accents; dark windows and openings.

HULL: one solid body, wider than it is tall and about twice as long as it is wide — a blunt wedge, not a long tube. The cockpit is at the very FRONT: a faceted glasshouse of dark angled windows in a sloping nose, with a brick-red roof panel around a circular hatch directly behind it. Behind the cockpit the body widens into a flat-shouldered midsection carrying a single raised central spine along the centerline and shallow recessed deck panels either side of it. A single broad rectangular cargo door sits low on the port side wall, behind the cockpit and ahead of the engines. The body ends in a squared-off tail.

ENGINE PODS — THE CRITICAL GEOMETRY: exactly TWO engine pods, and they are an IDENTICAL, MIRRORED PAIR. Both sit at the SAME position along the ship's length: aft of midships, flanking the rear third of the hull, level with each other. Neither pod is anywhere near the cockpit; no pod sits forward, beside, or ahead of the cabin. They are mounted outboard on short structural bridges, held clear of the hull sides, separated by roughly four pod diameters.

Each pod is a squat round drum — its total length including the short aft nozzle is only about 1.4 times its diameter. They are stubby barrels, NOT long nacelles. Both pod axes run straight fore-and-aft, exactly parallel to each other and to the ship's central spine: intake ring facing FORWARD, nozzle facing AFT. Neither pod is tilted, yawed, splayed, or rotated. Each pod is painted in banded blocks: dark gray intake rim, then brick-red, then an ivory band, then a dark aft cap.

Everything about the ship — proportions, the brick-red and ivory placement, the cockpit facets, the cargo door, the pod pair — is copied from image 2. Image 2 already shows the pods correctly placed; match that placement exactly.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame, horizontal. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO orthographic views, NO labels, NO text of any kind. There is exactly ONE spacecraft and exactly ONE human figure in this image and no other people anywhere. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors or composition. Image 2 contributes the SHIP'S DESIGN ONLY; do not copy its flat blue background or its camera angle. Image 3 is the SCENE BASELINE: reproduce its setting, framing and composition, and change only what is specified below.

SCENE: "The Pad." Night on the barren planet Kalagra. A wide establishing shot of a lonely derelict landing pad on an open rock plain, with the freighter Antares coming down onto it and one small figure watching.

KEEP FROM IMAGE 3 — UNCHANGED: the wide pulled-back camera and its slightly elevated viewpoint; the cracked circular ferrocrete pad, its concentric worn ivory ring markings and the large worn ivory PLUS painted at its exact centre; the ring of squat stanchion lamps, every one of them still angled INWARD so its lit face and its hard flat pool of warm ochre fall toward the pad's centre; the tilted weathered mast at left; the broken rock plain and its angular foreground shelves; the small lone robed figure at lower left at exactly her current size and position, in her full-length slate blue-gray robe with the ochre hem, dust mask and dark goggles, signal lamp in hand, head tipped up watching; the pale flat moon at upper left; the flat deep slate blue-black sky and its sparse flat ivory stars; the distant cobalt storm wall with its lightning low on the right horizon; the night palette of deep slate blue-violet shadow against warm ochre lamplight. Do not re-frame. Do not zoom. Do not enlarge or move the figure. The ship keeps its near-profile, level attitude — long axis horizontal and parallel to the pad, nose left, no tilt, no bank.

CHANGE ONE — CENTRE THE SHIP OVER THE PAD: in image 3 the ship is set back and its thrust comes down off-centre, short of the pad's middle. Move the Antares so it is squarely CENTRED above the landing pad: the midpoint of its hull sits directly over the painted PLUS at the pad's exact centre, and both of its landing plumes come straight down onto the slab close on either side of that plus, symmetrically placed about it. The ship reads as lined up on its mark and settling onto it. Keep the ship at the same size in frame and hovering a few ship-lengths above the slab, with open sky above it.

CHANGE TWO — MUCH LARGER SERVICE BUILDINGS THAT BREAK THE FRAME: the ferrocrete service buildings flanking the pad are still too small. Make them MUCH larger — substantial structures that dominate the left and right thirds of the middle ground. They are now big enough that they RUN OFF THE EDGES OF THE PICTURE: the building on the left is cut by the left frame edge and the building on the right is cut by the right frame edge, each continuing beyond the crop so only part of it is visible. Their rooflines rise well above the horizon line. Keep them plain, blocky and under-detailed — low angular ferrocrete masses with flat or shallow-sloped roofs, a dark recessed doorway, a few small dark windows, one or two simple vents or buttresses, and a warm ochre lamp pool at the base. They stay clearly lower than the hovering ship and they must not crowd the pad itself: the circular slab, its plus and its inward-facing lamps stay fully visible and unobstructed between them. The robed figure stays exactly her current size — only the buildings grow.

CHANGE THREE — MAKE THE PLUMES ORGANIC, NOT GEOMETRIC: the two landing plumes stay exactly where they are — one from a flat dark thruster block on the belly under the forward hull, one from an identical block on the belly under the tail, both on the ship's underside centreline, matched in size so the pair reads as deliberately symmetrical. No thrust comes from the engine pods, the aft nozzles, or anywhere else; there are exactly two plumes in the image.

Repaint their SHAPE. They are currently stiff, straight-sided geometric cones. Instead paint each plume as a loose, irregular, living tongue of fire and blown dust: uneven hand-painted contours that wobble and kink, a bulge here and a pinch there, a soft ragged flare where it spreads at the bottom, a few torn wisps and licks breaking off the sides. No ruler-straight edges, no symmetry between the left and right outline of a single plume, no clean triangle or trapezoid. Let each plume lean and curl slightly, as a flame does.

But keep the PAINT flat: each plume is still built from two or three FLAT OPAQUE shapes of solid colour with hard painted edges — an outer pale ochre mass and one or two brighter ivory tongues inside it — just with irregular, organic outlines instead of straight ones. The contour is loose; the colour inside each shape is dead flat. The plumes are completely opaque: the slab behind them does not show through. Still FORBIDDEN: any glow, bloom, halo, corona or light spill; any gradient, fade, blur or feathered edge; any transparency; any light cone, shaft or volumetric beam; any sparks or speckles; any brightening of the air around them. A plume is a painted flame-shape, not a lamp shining through dust.

Where each plume strikes the slab it throws blown dust outward — a few flat, irregular, wind-torn sheets of pale ochre with ragged hand-painted edges, lying low and spreading sideways across the pad. These are drifting dust, NOT heaps of rubble, boulders or debris piles.

LIGHT: night scene, unchanged from image 3. Two light sources only — the warm ochre stanchion lamps on the pad, which rake the underside of the ship and the front of the buildings, and the cold pale moon and sky, which edge the ship's upper hull and the building rooflines with one flat lighter plane. Everything else falls into a single deep slate blue-violet shadow plane. No neon, no rim lighting, no bloom, no light rays.

THE SHIP'S DESIGN IS UNCHANGED: ivory and light-gray hull, brick-red cockpit roof panel with its circular hatch, faceted dark cockpit windows in the sloping nose, raised central spine, the broad rectangular cargo door low on the side wall, and the two banded engine pods as a matched pair aft of midships, level with each other, axes horizontal and fore-and-aft. Keep the hull the broad, chunky, blunt wedge that image 2 shows — do not stretch it long and flat.

Change nothing else about image 3.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
