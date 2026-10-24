# Antares v025

User feedback verbatim:
> looks way worse
> Not only that, they are MORE facing towards the camera when they should have been made LESS

Mode: edit of pre-correction v022 baseline; neither rejected v023 nor v024 attached.
Tool: built-in image_gen.imagegen; model not exposed
Style: v2
Design: description v15 = description_versions/description-v15.md
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png (style v2; frozen style_versions/canonical_style_reference-v2.png)
- Image 2 EDIT TARGET: assets/ships/the_antares/candidates/v022/image.png
Requested correction: less visible frontal fan face, more visible cylinder side; pods point toward nose along hull.
Status: rejected by user: "They became squashed. Ovals instead of circles." Do not use as edit baseline. Direction changed but whole-cylinder geometry was not preserved.
Output: image.png, 1536 × 1024. Source: /Users/gmahoney/.codex/generated_images/01a0e10a-e606-7a60-ac77-8792df2504bc/exec-cc2b80b2-62d1-4914-b2c9-61a23d3c611f.png
Visual assessment: both hero intake faces are substantially narrower and the colored barrel sides are more visible than in v022, correcting the requested direction. The change is pronounced; exact 3D alignment is not validated. Minor generative changes remain elsewhere in the sheet. Neither reference.png nor the standalone beauty shot was replaced.

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

Image 1 is STYLE: canonical_style_reference.png. Match its rendering only; ignore its subjects and setting.
Image 2 is EDIT TARGET: Antares sheet v022, BEFORE the rejected engine-angle edits. Preserve this image's layout and design.

Use case: precise-object-edit
Design:
# Antares

**Description version: v15** (2026-09-26)


## Exterior

Broad, low utilitarian spacecraft with a wedge-shaped cockpit nose, raised central spine, recessed deck and paired cylindrical side engine pods. Ivory/light-gray hull, orange-red cockpit upper panels and rear engine housings, dark windows and engine openings. The orange marking behind the cockpit forms a deliberate roof panel around a circular hatch and clean side bands separated by ivory. Preserve the reference silhouette, proportions and color placement.

The hull shoulders are compact and the lateral walls stand nearly upright, with a modest angular chamfer rather than a broad outward flare. Front, rear, and top orthographic projections agree with the hero three-quarter view: the body sits inward of the unchanged engine-pod centers, the side walls do not spread into wide wing-like cheeks, and the top outline has restrained shoulders. Cockpit width, body length, central spine, and engine diameter and spacing remain consistent across views.

A single broad rectangular cargo-door panel occupies the lateral midship port-side opening, behind the cockpit and ahead of the port engine pod. Its top hinge is on the side wall, well below the upper deck and raised central spine. A continuous clean band of fixed ivory hull separates the hinge from the upper deck. The closed panel extends downward from this hinge to the opening's lower sill and occupies the side opening only; no part of it lies on the roof, upper deck, or central spine. The door has one uninterrupted rectangular face, a dark perimeter seam, and two simple recessed opening grips. There are no stacked doors, separate upper flaps, or adjacent second hatches. The open panel is the identical rectangle rotated upward about the same side-wall top hinge; panel width, height, opening, and hinge position agree in every view. A short loading ramp and two to three generic adult crew provide believable scale in the open-bay detail. The cargo door is lateral, never front-facing. No personnel hatch appears on the cockpit-side hull.

The rear orthographic view shows the same widely separated engine axes as the front and top views. Engine-center separation is approximately four turbine diameters, with mounting structures bridging the gap to the narrower aft hull. The rear drawing uses a consistent local scale for the hull and turbines while fitting its allocated sheet area. In the open cargo-bay detail, the fixed upper hull, recessed deck, and raised central spine remain visibly present behind and above the lifted door. The door is on the lower lateral side wall of a substantial ship; the surrounding upper structure occludes the sheet background where the view looks into the ship. The raised panel remains a separate foreground rectangle at its original low hinge; the structure behind it is fixed hull, not a second door.

Both cargo-door detail panels use the same viewing angle and magnification and show the surrounding ship structure continuously. Their framing includes the full fixed upper side-wall band, the recessed deck receding inward, and the raised central spine above and behind the hinge. Fixed hull fills the upper crop edge of both details; there is no slate-blue exterior background wedge directly above the door. The inset framing leaves enough room above the raised door to make the upper ship mass legible. Opening the single panel changes only its rotation and reveals the bay; the surrounding hull and deck geometry are identical in both states. All hull edges follow one coherent perspective.

In plan view, the hull has a broad tapered outline with articulated, shallow changes of direction. The blunt cockpit nose, sloping windscreen shoulders, wider cabin roof, and slight neck behind the cockpit preserve the same contours visible in the three-quarter hero. The cargo-door housing makes a mild local outward bulge. Farther aft, the side body flares outward slightly and then turns through a clear 90-degree return at the turbine mounting area. These shallow bulges and square returns belong to the structural hull; they are compact rather than broad wing-like lobes. The outline is not a single uninterrupted straight triangle. The central spine, recessed deck, and cockpit retain their established proportions.

The paired engine pods sit on outboard mounts with their intake faces clear of the adjacent aft body shoulders. Their fore-aft placement and mounting bridges are consistent in the three-quarter, top, side, and head-on projections. In the hero view the visible near turbine sits sufficiently forward and outboard of the adjacent body protrusion to expose its complete intake rim; it does not look buried behind that protrusion. The head-on view retains two unobstructed turbine faces at the established lateral spacing.

The engine pods are fixed parallel to the ship's fore-aft axis. In the front three-quarter hero view, their cylindrical sides dominate over their intake faces: the intake openings are seen obliquely as narrow ellipses and point along the hull toward the cockpit nose. Neither pod turns outward to face the viewer. The mounts, physical dimensions and outboard clearance remain consistent with the orthographic views.

## Interior

A working ship, worn and patchworked rather than sleek. Scuffed painted metal, mismatched replacement panels, visible fasteners, repaired upholstery, accessible cable runs and practical maintenance patches. Controls are analog: physical toggle switches, rotary knobs, mechanical levers, round needle gauges and small recessed CRT-style instrumentation displays. No floating holograms or glossy touchscreen walls.

Cockpit has two forward-facing seats, pilot control yoke shaped like an aircraft steering wheel, instrument consoles in front of and beside both seats, and an aft access doorway. Instruments and controls have coherent practical mounting and remain reachable from the seats.

LOCAL EDIT: In the UPPER-LEFT THREE-QUARTER view only, turn BOTH thruster intakes AWAY FROM THE VIEWER and TOWARD THE SHIP'S NOSE at the lower left. The user is explicit: the intakes must face LESS toward the camera, not more. We must see LESS of the dark circular fan faces and MORE of the long orange/ivory cylindrical SIDE surfaces. The near pod's intake currently reads almost like a round disc presented to the viewer. Make it a visibly NARROWER, obliquely viewed opening. Reduce the apparent face width substantially (about one third narrower than this input), maintaining its diameter in the long direction. The near barrel should read as a side-on cylinder running parallel to the ship's long central spine. Apply the same physical direction to the far pod. Do not move the camera or turn the hull.

Keep the existing engine mounts, spacing, physical scale and overall positions. Redraw the intake lip, interior fan, white band and orange barrel together so the surface and the face agree. The face must not be a round frontal circle pasted on a side-on cylinder. Keep the current near intake clear of the body, but do not use a camera-facing rotation to achieve clearance. Only modify these two engines within the hero view. Preserve every hull detail and every other view on the sheet, including all other engines in the orthographic projections. No labels or guide lines.

The critical acceptance check: compared with image 2, substantially LESS fan face is visible, and MORE orange barrel side is visible. If the fans look more circular or more presented to the viewer, that is the opposite of the requested change.
Keep all repainted marks in image 1's rendering. Output the same 1536x1024 sheet.
Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.
