# the-job-the-pad v003

User request verbatim: Yes the plumes need to come from places on the ship that look like they are symmetrical. maybe one under the nose and one under the back? Also, the Antares should be coming down at a more parallel angle. Its a little 3/4. / the light also need to face INTO the circle / and make the marking in the middle of the landing pade be a + / Also, the buildings along the side need to be a little bigger.
Mode: Edit off v002 baseline with hero 3/4 crop retained as IDENTITY: ship rotated toward near-profile and leveled; engine-pod exhaust replaced by two symmetrical belly landing thrusters (nose and tail) painted as flat opaque quads; stanchion lamps turned inward; pad center marking changed to a plus; service huts enlarged; sky and moon flattened
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0ee60-54d0-7070-ab64-5d697c93e609/exec-bd0b7e9e-8f2c-4f61-8463-9bab9563945c.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/ships/the_antares/sources/hero-3q-crop-from-v033.png
- Image 3 EDIT TARGET: outputs/the-job-the-pad/v002/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.27 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Five of six requested changes landed. Ship is near-profile and level, parallel to the pad. Pad centre marking is a plainly readable worn plus. Every stanchion lamp now faces inward with its pool falling toward the centre. Service huts are substantially larger and read as buildings. Sky and moon are much flatter, striping and gradient cratering largely gone. Thrust now comes from two belly positions rather than the pods. Failures: (1) the plumes are STILL painted as soft glowing gradient cones with feathered edges and light spill — third consecutive failure of the flat-opaque-quadrilateral instruction; the model appears to hold a strong 'downward thruster = spotlight cone' prior that prompt wording has not moved; (2) the forward plume sits under the mid-forward hull rather than under the nose, and the two columns are tall enough that the ship reads as standing on stilts; (3) at near-profile the far engine pod appears forward of and above the near pod, reading as a dorsal mount rather than the matched aft pair; (4) hull proportions have drifted longer and flatter than the chunky broad wedge in the identity crop; (5) the dust skirts at the plume bases read as rubble piles rather than flat angular dust sheets. Kia remains IMPROVISED — no approved asset exists for her. Belly landing thrusters are NOT in description v20; if kept, the Antares design needs a version bump.

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
Image 3 is EDIT TARGET: The scene baseline: the-job-the-pad v002. Its setting, framing, composition and lighting are what 'unchanged' refers to below.

TASK: A single horizontal wide night illustration: the freighter Antares descending level onto a derelict landing pad on Kalagra, watched by one small distant operator.

THE SHIP — THE ANTARES (description v20, distilled for this scene). Image 2 is ONE single three-quarter view of this ship and is the authority on every shape below. It shows the whole ship at once; there are no other views to reconcile.

A broad, low, wedge-shaped utility freighter. Ivory / light-gray hull with brick-red accents; dark windows and openings.

HULL: one solid body, wider than it is tall and about twice as long as it is wide — a blunt wedge, not a long tube. The cockpit is at the very FRONT: a faceted glasshouse of dark angled windows in a sloping nose, with a brick-red roof panel around a circular hatch directly behind it. Behind the cockpit the body widens into a flat-shouldered midsection carrying a single raised central spine along the centerline and shallow recessed deck panels either side of it. A single broad rectangular cargo door sits low on the port side wall, behind the cockpit and ahead of the engines. The body ends in a squared-off tail.

ENGINE PODS — THE CRITICAL GEOMETRY: exactly TWO engine pods, and they are an IDENTICAL, MIRRORED PAIR. Both sit at the SAME position along the ship's length: aft of midships, flanking the rear third of the hull, level with each other. Neither pod is anywhere near the cockpit; no pod sits forward, beside, or ahead of the cabin. They are mounted outboard on short structural bridges, held clear of the hull sides, separated by roughly four pod diameters.

Each pod is a squat round drum — its total length including the short aft nozzle is only about 1.4 times its diameter. They are stubby barrels, NOT long nacelles. Both pod axes run straight fore-and-aft, exactly parallel to each other and to the ship's central spine: intake ring facing FORWARD, nozzle facing AFT. Neither pod is tilted, yawed, splayed, or rotated. Each pod is painted in banded blocks: dark gray intake rim, then brick-red, then an ivory band, then a dark aft cap.

Everything about the ship — proportions, the brick-red and ivory placement, the cockpit facets, the cargo door, the pod pair — is copied from image 2. Image 2 already shows the pods correctly placed; match that placement exactly.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame, horizontal. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO orthographic views, NO labels, NO text of any kind. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors or composition. Image 2 contributes the SHIP'S DESIGN ONLY — one three-quarter view of the whole ship; do not copy its flat blue background or its camera angle. Image 3 is the SCENE BASELINE: reproduce its setting, framing and composition, and change only what is specified below.

SCENE: "The Pad." Night on the barren planet Kalagra. A wide establishing shot of a lonely derelict landing pad on an open rock plain, with the freighter Antares coming down onto it and one small figure watching.

KEEP FROM IMAGE 3 — UNCHANGED: the wide pulled-back camera and its slightly elevated viewpoint; the cracked circular ferrocrete pad and its concentric worn ivory ring markings; the ring of squat stanchion lamps in their current positions; the tilted weathered mast at left; the broken rock plain and its angular foreground shelves; the small lone robed figure at lower left at exactly her current size and position; the pale moon at upper left; the distant cobalt storm wall with its lightning low on the right horizon; the night palette of deep slate blue-violet shadow against warm ochre lamplight; the overall dark, quiet, spacious composition. Do not re-frame. Do not zoom in. Do not enlarge the figure.

CHANGE ONE — THE SHIP'S ATTITUDE AND ANGLE: in image 3 the Antares is turned too far into three-quarter. Rotate it toward a near-PROFILE view. Its long axis now runs almost PARALLEL to the picture plane — a broadside side-on view of the ship with only a slight three-quarter turn remaining, just enough to show a sliver of the near flank and keep the form solid. The nose still points left.

The ship is also LEVEL. Its long axis is horizontal and parallel to the pad below it — no nose-up tilt, no nose-down tilt, no bank or roll. It is settling straight down onto the pad on a flat, even descent, hovering a few ship-lengths above the slab. Keep its size in frame as it is in image 3 — about one third of the frame's width, in the upper middle, with open sky around it.

From this near-profile angle the far engine pod is mostly hidden behind the hull; only the near pod on this side is fully visible, with a small part of the far pod showing above or beyond the hull line. Both pods stay exactly where image 2 puts them — an identical matched pair, aft of midships, flanking the rear of the hull, level with each other, their axes horizontal and running fore-and-aft. The ship's design is otherwise unchanged from image 2: ivory and light-gray hull, brick-red cockpit roof panel with its circular hatch, faceted dark cockpit windows in the sloping nose, raised central spine, the broad rectangular cargo door low on the side wall, and the banded dark-gray, brick-red, ivory, dark-cap engine pods.

CHANGE TWO — THE LANDING THRUST: delete the exhaust plumes in image 3 entirely. They come from the wrong places and are painted as glowing light. Replace them with TWO landing-thruster plumes, and only two, in these positions:

- Plume A fires straight down from a flat thruster block on the BELLY UNDER THE NOSE, below and just behind the cockpit.
- Plume B fires straight down from an identical flat thruster block on the BELLY UNDER THE TAIL, below the rear of the hull.

Both thruster blocks sit on the ship's underside centerline, are the same size and shape as each other, and are simple flat dark rectangular housings. Because the ship is level, Plume A and Plume B are the same length and hang the same distance below the hull, so the pair reads as deliberately symmetrical — one forward, one aft, balanced. NO thrust of any kind comes from the engine pods, from the aft nozzles, from the hull sides, or from anywhere else. Exactly two plumes in the whole image.

HOW TO PAINT EACH PLUME — THIS IS NOT LIGHT, IT IS PAINT: each plume is ONE flat opaque quadrilateral of solid pale ochre, wider at the bottom than at the top, with completely straight hard edges on all four sides, as if cut from a sheet of colored paper and laid on the picture. Inside it, at most one narrower solid ivory shape, also with straight hard edges. Two flat colors total per plume, maximum. The plume is fully opaque: the rock and pad behind it are completely hidden, not showing through. FORBIDDEN in the plumes: any glow, bloom, halo, corona, aura or light spill; any gradient, fade, blur, feathering or soft edge; any transparency; any light cone, light shaft or volumetric beam; any particles, sparks or speckles; any lightening of the air around them. A plume must look like a painted flat shape, not like a lamp shining through dust. Where each plume meets the slab it throws a low flat skirt of ochre dust to either side, painted as two or three flat angular sheets with hard edges.

CHANGE THREE — FLATTEN THE SKY AND MOON: repaint the sky as large quiet FLAT areas of deep slate blue-black. Remove all diagonal striping, streaking, rain texture and granular noise from it. Stars are a sparse scatter of small flat ivory dots. Repaint the moon as a plain flat pale disc with two or three simple darker flat patches for craters — no gradient, no shading, no fine cratering.

CHANGE FOUR — TURN THE STANCHION LAMPS INWARD: every stanchion lamp around the pad rim must FACE INTO THE CIRCLE. Each lamp head is angled inward toward the pad's center, so its bright lit face and its hard flat pool of warm ochre both fall INWARD onto the slab, toward the middle of the pad. No lamp points outward at the rock plain, sideways along the rim, or out of the frame; no lamp pool spills outward off the pad. Lamps on the far side of the circle face back toward the viewer, and lamps on the near side face away from the viewer — they all point at the same center. Each lamp's housing is a simple flat dark block; only the inward-facing lens is bright.

CHANGE FIVE — A CROSS AT THE CENTER: the marking painted at the middle of the landing pad is a large, plainly readable PLUS SIGN — one broad horizontal bar crossing one broad vertical bar of equal length, meeting at the pad's exact center, painted in worn, chipped ivory with hard straight edges and drawn in the pad's perspective so it lies flat on the slab. It is big enough to read instantly from this distance. It replaces any other central marking: no circle, no ring, no letter, no numeral, no chevron and no text at the pad's center. The concentric ring markings further out toward the rim stay as they are.

CHANGE SIX — ENLARGE THE SERVICE HUTS: the blocky ferrocrete service buildings along the side of the pad are currently too small to read. Make them noticeably LARGER — roughly half again to twice their size in image 3 — so they have real presence as buildings rather than reading as crates. Each is a simple low angular ferrocrete block with a flat or shallow-sloped roof, a dark recessed doorway, one or two small dark windows, and a warm ochre lamp pool at its base. Keep them in their current positions along the pad's edge, keep them plain and under-detailed, and keep them clearly smaller than the ship. The robed figure stays her current size; only the buildings grow.

LIGHT: night scene, unchanged from image 3. Two light sources only — the warm ochre stanchion lamps on the pad below, which rake the underside of the ship, and the cold pale moon and sky, which edge the ship's upper hull with one flat lighter plane. Everything else falls into a single deep slate blue-violet shadow plane. No neon, no rim lighting, no bloom, no light rays.

Change nothing else about image 3.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
