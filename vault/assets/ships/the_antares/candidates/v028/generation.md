# Antares v028

User request verbatim: Perhaps you can reconfigure the backend of the ship to make the re-alignment more easy. I noticed that the 3/4 view in the upper left does not quite match the top down view anyways. The top down view has a clean dark grey recessed area that does not exist in the 3/4 view. Perhaps try to make the 3/4 less convulated to match the top down view.
Mode: aft-hull simplification from original v022; its top-down view is the user's design authority. Rejected thruster edits are not attached.
Style: v2
Design: description v17 = description_versions/description-v17.md
Tool: built-in image_gen.imagegen; underlying model not exposed
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png (style v2; immutable style_versions/canonical_style_reference-v2.png)
- Image 2 EDIT TARGET: assets/ships/the_antares/candidates/v022/image.png
Status: rejected by user. Revert simplified structure; detailed v022 hero is the authority and top-down view must match it. Not promoted; retained for history.
Output: image.png, 1536 × 1024; copied from /Users/gmahoney/.codex/generated_images/01a0e10a-e606-7a60-ac77-8792df2504bc/exec-6c3350b3-d732-444d-b57e-b99e4aa09e0c.png
Visual check: clean broad dark recessed deck areas now appear on both sides of the hero central spine; perimeter rails and aft shoulders are simplified. Cockpit, livery and lateral cargo door remain recognizable. The tool also propagated simplification into the top projection, side drawings and cargo insets despite the prompt's preservation request. Hero engine faces retain the original substantial circular-cylinder appearance. This pass improves rear-hull legibility; exact engine-axis correctness is not established by a calibrated 3D model.

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

Image 1 is STYLE: canonical_style_reference.png. Match rendering technique only. Ignore its people, clothing and setting.
Image 2 is EDIT TARGET: Antares sheet candidates/v022/image.png. Its TOP-DOWN VIEW at upper right is the design authority for the rear hull and engine layout. Edit the upper-left THREE-QUARTER view to depict that simpler structure faithfully.

Use case: precise-object-edit.
Asset type: spacecraft reference sheet.
Design:
# Antares

**Description version: v17** (2026-09-26)


## Exterior

Broad, low utilitarian spacecraft with a wedge-shaped cockpit nose, raised central spine, recessed deck and paired cylindrical side engine pods. Ivory/light-gray hull, orange-red cockpit upper panels and rear engine housings, dark windows and engine openings. The orange marking behind the cockpit forms a deliberate roof panel around a circular hatch and clean side bands separated by ivory. Preserve the reference silhouette, proportions and color placement.

The hull shoulders are compact and the lateral walls stand nearly upright, with a modest angular chamfer rather than a broad outward flare. Front, rear, and top orthographic projections agree with the hero three-quarter view: the body sits inward of the unchanged engine-pod centers, the side walls do not spread into wide wing-like cheeks, and the top outline has restrained shoulders. Cockpit width, body length, central spine, and engine diameter and spacing remain consistent across views.

A single broad rectangular cargo-door panel occupies the lateral midship port-side opening, behind the cockpit and ahead of the port engine pod. Its top hinge is on the side wall, well below the upper deck and raised central spine. A continuous clean band of fixed ivory hull separates the hinge from the upper deck. The closed panel extends downward from this hinge to the opening's lower sill and occupies the side opening only; no part of it lies on the roof, upper deck, or central spine. The door has one uninterrupted rectangular face, a dark perimeter seam, and two simple recessed opening grips. There are no stacked doors, separate upper flaps, or adjacent second hatches. The open panel is the identical rectangle rotated upward about the same side-wall top hinge; panel width, height, opening, and hinge position agree in every view. A short loading ramp and two to three generic adult crew provide believable scale in the open-bay detail. The cargo door is lateral, never front-facing. No personnel hatch appears on the cockpit-side hull.

The rear orthographic view shows the same widely separated engine axes as the front and top views. Engine-center separation is approximately four turbine diameters, with mounting structures bridging the gap to the narrower aft hull. The rear drawing uses a consistent local scale for the hull and turbines while fitting its allocated sheet area. In the open cargo-bay detail, the fixed upper hull, recessed deck, and raised central spine remain visibly present behind and above the lifted door. The door is on the lower lateral side wall of a substantial ship; the surrounding upper structure occludes the sheet background where the view looks into the ship. The raised panel remains a separate foreground rectangle at its original low hinge; the structure behind it is fixed hull, not a second door.

Both cargo-door detail panels use the same viewing angle and magnification and show the surrounding ship structure continuously. Their framing includes the full fixed upper side-wall band, the recessed deck receding inward, and the raised central spine above and behind the hinge. Fixed hull fills the upper crop edge of both details; there is no slate-blue exterior background wedge directly above the door. The inset framing leaves enough room above the raised door to make the upper ship mass legible. Opening the single panel changes only its rotation and reveals the bay; the surrounding hull and deck geometry are identical in both states. All hull edges follow one coherent perspective.

In plan view, the hull has a broad tapered outline with articulated, shallow changes of direction. The blunt cockpit nose, sloping windscreen shoulders, wider cabin roof, and slight neck behind the cockpit preserve the same contours visible in the three-quarter hero. The cargo-door housing makes a mild local outward bulge. Farther aft, the side body flares outward slightly and then turns through a clear 90-degree return at the turbine mounting area. These shallow bulges and square returns belong to the structural hull; they are compact rather than broad wing-like lobes. The outline is not a single uninterrupted straight triangle. The central spine, recessed deck, and cockpit retain their established proportions.

The aft upper hull follows the plan view's simple organization: a narrow raised ivory central spine, clean dark slate-gray recessed deck areas alongside it, and low continuous ivory perimeter rails. These recesses are broad, quiet and visibly below the rails, with minimal panel divisions and no crowded tiers of raised blocks. The three-quarter view shows the same open recessed areas and the same boundaries as the top view. At the aft ends of the side rails, simple short mounting bridges connect the two outboard engine pods symmetrically to the hull. The bridges and low shoulders form a legible structural connection without bulky stacks or protrusions crowding the intake faces. The rear body is compact and orderly, with shallow structural steps rather than multiple interlocking raised masses.

The paired engine pods sit on simple outboard mounting bridges with their intake faces clear of the low aft hull shoulders. Their fore-aft placement, lateral spacing and mounting relationships follow the top-down view and agree across the three-quarter, side and head-on projections. Their complete cylindrical forms run parallel to the central spine; clearance comes from the simple hull and mount geometry. The head-on view retains two unobstructed turbine faces at the established lateral spacing.

The two engine pods are rigid round cylinders with circular, constant-diameter cross-sections and matching circular intake rims. The intake lip, fan, hub, orange housing, ivory band and aft nozzle belong to one coherent solid. Both pod axes run parallel to the ship's fore-aft centerline. Their three-quarter appearance is the projection of this complete cylindrical geometry; the opening is never independently compressed, stretched, flattened or rotated relative to its barrel. Physical diameter, barrel length and mounting clearance agree across views.

## Interior

A working ship, worn and patchworked rather than sleek. Scuffed painted metal, mismatched replacement panels, visible fasteners, repaired upholstery, accessible cable runs and practical maintenance patches. Controls are analog: physical toggle switches, rotary knobs, mechanical levers, round needle gauges and small recessed CRT-style instrumentation displays. No floating holograms or glossy touchscreen walls.

Cockpit has two forward-facing seats, pilot control yoke shaped like an aircraft steering wheel, instrument consoles in front of and beside both seats, and an aft access doorway. Instruments and controls have coherent practical mounting and remain reachable from the seats.

USER DIRECTION:
"Perhaps you can reconfigure the backend of the ship to make the re-alignment more easy. I noticed that the 3/4 view in the upper left does not quite match the top down view anyways. The top down view has a clean dark grey recessed area that does not exist in the 3/4 view. Perhaps try to make the 3/4 less convulated to match the top down view."

This is a rear-hull simplification and projection-consistency pass. Use the EXISTING TOP VIEW as the blueprint. Change the aft portion of the upper-left three-quarter HERO from just behind the cargo door/cabin to the engines:
- Make the broad DARK GRAY RECESSED DECK of the top view clearly exist in the hero. It is a real horizontal recessed area below the surrounding ivory hull, not a dark sidewall or shadow painted on top of raised blocks. Show its broad clean slate-gray floor receding aft in perspective beside the narrow central ivory spine. Mirror the top view's boundaries, rails and aft termination. Simplify it to a few quiet dark planes; remove the current carpet of raised cream tiles.
- Simplify the complex aft ivory shoulders and interlocking blocks. Replace their multiple projections and stacked steps with the clean low continuous perimeter structure seen from above. Keep the central spine, recess and perimeter hull visually separate and easily readable. The upper hull is open and recessed, not filled by a solid slab.
- Fit the two existing ROUND engine pods on short, simple, symmetrical mounting bridges, with unobstructed intakes. Use the top-down layout to set their longitudinal alignment: both axes parallel to the central spine. Construct each COMPLETE cylinder with consistent front ring, circular physical cross-section, housing, ivory band and aft cap. Keep the original chunky diameter and length. Do not squash the fronts into narrow vertical ovals, do not swivel the intakes independently toward the viewer. Let the simplified hull make the correct mounting and alignment easy to see.

Scope: the HERO's rear deck, surrounding aft structure, engine mounts and the engine orientations may change. Preserve the HERO cockpit/nose and its circular hatch, cabin windows, orange/ivory livery, cargo-door panel and hinge, and the main forward proportions. Keep the TOP-DOWN projection exactly as supplied because it is the authority being matched. Keep the other orthographic drawings and cargo insets as supplied. No new wings, fins, extra engines, tall rear walls, labels, arrows, or extra views. Preserve sheet framing and slate background.
This should read as the same ship with a much simpler, cleaner rear deck that now agrees between top and three-quarter views.
Output one complete 1536 × 1024 reference sheet. All repainted areas match image 1's coarse flat matte paint.
Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.
