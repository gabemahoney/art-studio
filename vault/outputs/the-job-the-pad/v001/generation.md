# the-job-the-pad v001

User request verbatim: I need an image for Scene 3 the Pad. I want it to be the Antares landing on Kalagra. On the desolate landing pad. Have the operator, Kia, watching. The operator, Kia, is a woman in a full length robe and dust mask. Its night time. The storm has not yet arrived.
Mode: Fresh scene, first pass: night landing on derelict pad, Kia improvised (no approved asset)
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0ee0f-26ad-78c3-830a-5d662b32d41a/exec-3b5b75a3-490a-4392-a16d-a512029fb1cc.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/ships/the_antares/reference.png; frozen assets/ships/the_antares/candidates/v033/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.47 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Ship matches description v20 — silhouette, ivory/brick-red placement, cockpit, lateral cargo door, squat engine pods all correct; painted once in the scene, no sheet layout leaked through. Night, derelict pad, stanchion lamps, distant unarrived storm and lone masked operator all present. Discrepancies: (1) exhaust plumes render as soft glowing gradient cones rather than the specified flat opaque wedges — the clearest Style Block violation; (2) plumes issue from beneath the pods rather than from the aft nozzles, and the pods' thrust axes read horizontal; (3) ship is seen front-three-quarter with nose left, not the rear-three-quarter specified; (4) moon and sky carry gradient/striated texture beyond the anchor's flatness. Kia is IMPROVISED — no approved asset for her exists; this figure is off-canon and establishes nothing.

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
Image 2 is IDENTITY: Copy this ship's design exactly — hull silhouette, proportions, ivory and brick-red color placement, cockpit, cargo door and engine pods. Ignore this image's sheet layout, multiple views, inset panels, blue background and rendering.

TASK: A single horizontal night illustration: the freighter Antares descending onto a derelict landing pad on Kalagra, watched by a lone masked operator.

SUBJECT DESIGN (description v20, restated so nothing is invented):
Broad, low utilitarian spacecraft with a wedge-shaped cockpit nose, raised central spine, recessed deck and paired cylindrical side engine pods. Ivory/light-gray hull, orange-red cockpit upper panels and rear engine housings, dark windows and engine openings. The orange marking behind the cockpit forms a deliberate roof panel around a circular hatch and clean side bands separated by ivory. Preserve the reference silhouette, proportions and color placement.

The hull shoulders are compact and the lateral walls stand nearly upright, with a modest angular chamfer rather than a broad outward flare. Front, rear, and top orthographic projections agree with the hero three-quarter view: the body sits inward of the unchanged engine-pod centers, the side walls do not spread into wide wing-like cheeks, and the top outline has restrained shoulders. Cockpit width, body length, central spine, and engine diameter and spacing remain consistent across views.

A single broad rectangular cargo-door panel occupies the lateral midship port-side opening, behind the cockpit and ahead of the port engine pod. Its top hinge is on the side wall, well below the upper deck and raised central spine. A continuous clean band of fixed ivory hull separates the hinge from the upper deck. The closed panel extends downward from this hinge to the opening's lower sill and occupies the side opening only; no part of it lies on the roof, upper deck, or central spine. The door has one uninterrupted rectangular face, a dark perimeter seam, and two simple recessed opening grips. There are no stacked doors, separate upper flaps, or adjacent second hatches. The open panel is the identical rectangle rotated upward about the same side-wall top hinge; panel width, height, opening, and hinge position agree in every view. A short loading ramp and two to three generic adult crew provide believable scale in the open-bay detail. The cargo door is lateral, never front-facing. No personnel hatch appears on the cockpit-side hull.

The rear orthographic view shows the same widely separated engine axes as the front and top views. Engine-center separation is approximately four turbine diameters, with mounting structures bridging the gap to the narrower aft hull. The rear drawing uses a consistent local scale for the hull and turbines while fitting its allocated sheet area. In the open cargo-bay detail, the fixed upper hull, recessed deck, and raised central spine remain visibly present behind and above the lifted door. The door is on the lower lateral side wall of a substantial ship; the surrounding upper structure occludes the sheet background where the view looks into the ship. The raised panel remains a separate foreground rectangle at its original low hinge; the structure behind it is fixed hull, not a second door.

Both cargo-door detail panels use the same viewing angle and magnification and show the surrounding ship structure continuously. Their framing includes the full fixed upper side-wall band, the recessed deck receding inward, and the raised central spine above and behind the hinge. Fixed hull fills the upper crop edge of both details; there is no slate-blue exterior background wedge directly above the door. The inset framing leaves enough room above the raised door to make the upper ship mass legible. Opening the single panel changes only its rotation and reveals the bay; the surrounding hull and deck geometry are identical in both states. All hull edges follow one coherent perspective.

In plan view, the hull has a broad tapered outline with articulated, shallow changes of direction. The blunt cockpit nose, sloping windscreen shoulders, wider cabin roof, and slight neck behind the cockpit preserve the same contours visible in the three-quarter hero. The cargo-door housing makes a mild local outward bulge. Farther aft, the side body flares outward slightly and then turns through a clear 90-degree return at the turbine mounting area. These shallow bulges and square returns belong to the structural hull; they are compact rather than broad wing-like lobes. The outline is not a single uninterrupted straight triangle. The central spine, recessed deck, and cockpit retain their established proportions.

The paired engine pods sit on outboard mounts with their intake faces clear of the adjacent aft body shoulders. Their fore-aft placement and mounting bridges are consistent in the three-quarter, top, side, and head-on projections. In the hero view the visible near turbine sits sufficiently forward and outboard of the adjacent body protrusion to expose its complete intake rim; it does not look buried behind that protrusion. The head-on view retains two unobstructed turbine faces at the established lateral spacing.

The detailed three-quarter view defines the aft structure. The upper hull has articulated ivory shoulders, stepped mounting blocks, a raised central spine and recessed panelled deck surfaces. The top-down projection depicts these same structural masses and deck panels at the corresponding positions: ivory raised sections, shallow gray panelled recesses, transverse braces and aft mounting steps. The recessed deck is not a pair of large empty dark channels. All projections describe the same detailed solid ship.

The topside is bilaterally symmetrical about the longitudinal centerline through the cockpit roof hatch and the midpoint between the engine mounts. A single raised central spine and its aft vent sit on this axis. Port and starboard deck recesses, shoulder steps, raised blocks, rails, transverse bridges and openings mirror one another in physical dimensions and fore-aft position. Perspective naturally foreshortens and occludes far-side features; symmetry does not mean equal screen-space shapes. The detailed stepped upper structure remains substantial, rather than becoming a plain slab. This topside symmetry does not duplicate the port-side cargo door.

Both engine pods are rigid round cylinders, with their longitudinal axes parallel to the central spine and straight fore-aft deck edges. Their front hubs, housing centers and aft nozzle centers lie on those axes. Intake rims, fans, ivory bands and rear caps share one coherent cylindrical projection with circular physical cross-sections and unchanged diameter and length. The near and far pods use mirrored mounting geometry, without outward yaw or independent pitch.

The engine pods are compact, squat drums. In side elevation, the complete pod including its short aft nozzle is approximately 1.4 times its diameter in length. Their barrels retain the original compact proportions in every projection; they are not long nacelles. Axis alignment is achieved by orienting each entire pod, without increasing barrel length or shifting its attachment point.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame, horizontal. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO orthographic views, NO labels, NO text of any kind. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, interior, colors, panel layout or composition. Image 2 contributes the SHIP'S DESIGN ONLY — do not copy its blue background, its sheet layout, its multiple views or its inset panels; paint the ship ONCE, in the new setting described below.

SCENE: "The Pad." Night on the barren planet Kalagra. The freighter Antares is coming down onto a lonely, derelict landing pad out on the open rock plain, watched by a single operator. The storm is still far away; it has not arrived.

THE SHIP: the Antares, seen from a low three-quarter rear view, still a few ship-lengths above the pad on final descent, nose angled slightly away from the viewer and tilted a few degrees nose-up. It occupies roughly the upper-middle third of the frame and is the focal silhouette. Its ivory hull and brick-red cockpit and engine-housing bands read clearly against the night sky. Both squat engine pods fire downward-angled thrust: short, flat, opaque tapering wedges of pale ochre and ivory beneath each nozzle — painted shapes, not light, with no glow, bloom, halo or feathering. That thrust blows a low flat skirt of ochre dust outward across the pad in angular sheets. A few small hard points of ivory and red navigation light sit on the hull as flat dots; they do not glow.

THE PAD: a wide circular ferrocrete landing pad, cracked and dust-drifted, its painted guide markings worn to faded ivory fragments. It fills the lower half of the frame in steep perspective. Around its rim stand a handful of squat, battered stanchion lamps on angular posts, throwing hard flat pools of warm ochre light onto the slab; between them the pad falls into deep slate blue-violet shadow. At the pad's edge sit one or two low, blocky ferrocrete service huts with dark doorways, and a single tilted, weathered mast. Nothing else: no crowd, no vehicles, no cargo stacks, no other ships. The place is plainly abandoned to one caretaker.

THE OPERATOR — KIA: a woman standing alone in the lower-left foreground, on the pad, in the nearest plane of the picture, seen from behind and slightly to her side in three-quarter view, a dark silhouetted mass against the lit slab. She is roughly one quarter the height of the frame. She wears a full-length robe that reaches her boots — heavy slate blue-gray cloth with a warm ochre banded hem and a deep hood pushed back off her head — and a compact ferrous dust mask covering her nose, mouth and jaw, with flat dark goggle lenses above it; only a narrow band of skin shows at her temple. The robe is built from a few large flat planes with a few straight angular fold strokes; its hem and skirt pull sideways in stiff angular sheets where the ship's downwash hits her. One hand holds a stubby handheld signal lamp at her side, its lens a flat pale ochre shape. Her head is tipped up, watching the ship come down. She is still, calm and unhurried — the only living figure in the image.

THE NIGHT AND THE DISTANT STORM: deep slate blue-black sky with a scatter of flat ivory stars and one pale cratered moon low in the upper left. Along the far horizon at the right, a distant cobalt and blue-violet storm wall stands as a single quiet mass with a hard angular top edge and two or three thin branching bolts of pale yellow lightning inside it. It is far away and low on the horizon, small in the frame — approaching weather, not weather that has arrived. The air over the pad is clear; no haze, no rain, no wind-driven murk across the ship or the figure. Beyond the pad, flat ochre-gray rock plain and a few angular rock shelves recede to that horizon.

LIGHT: night scene. Two light sources only — the warm ochre stanchion lamps on the pad below, which rake the underside of the ship and the front of Kia's robe, and the cold pale blue moon and sky, which edge the ship's upper hull with one flat lighter plane. Everything else falls into a single deep slate blue-violet shadow plane. Keep the overall image dark and quiet with a small number of bright shapes; no neon, no rim lighting, no bloom, no light rays.

COMPOSITION: strong diagonal from Kia in the lower left, across the lit pad, up to the descending ship at upper right. Large quiet dark areas in the sky and in the unlit pad; detail concentrated on the ship, the lamp pools and the figure. Clear foreground (Kia), middle distance (pad and huts), background (plain, storm, sky).

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
