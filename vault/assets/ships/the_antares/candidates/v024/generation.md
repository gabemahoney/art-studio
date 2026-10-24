# Antares v024

User request (verbatim): are the angles of the thrusers on the 3/4 in the upper left correct? They look a little askew. Perhaos facing a little much towards camera? Hard for me to be sure. Can you check and if so, adjust?

Mode: retry from the same v022 baseline; not chained from v023.
Style: v2
Tool: built-in image_gen.imagegen; underlying model not exposed
Design: description v13 = description_versions/description-v13.md
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png (style v2; frozen style_versions/canonical_style_reference-v2.png)
- Image 2 EDIT TARGET: assets/ships/the_antares/candidates/v022/image.png
Reason for retry: v023 moved the near pod inward and changed unrelated orthographic engine details. Add fixed-center constraints and explicit ellipse orientation.
Status: REJECTED by user: "looks way worse". Do not use as a baseline. Prior positive visual assessment below is superseded by this feedback. v014 description restores v012 design wording (removes the added v013 perspective prescription). Candidate image retained for history; reference.png unchanged.
Output: image.png, 1536 × 1024; copied from /Users/gmahoney/.codex/generated_images/01a0e10a-e606-7a60-ac77-8792df2504bc/exec-7f61f6c4-edf1-4469-b7f6-8255895b3228.png
Visual check: both hero intake faces narrower; cylindrical housings read more consistently with the hull fore-aft direction. Near intake remains clear of the hull. Overall sheet layout, hull design, door details and orthographic views retained, with minor generative repaint differences; not pixel-identical outside the pods. Perspective judged visually; not verified against a 3D model. v024 preserves mounting placement better than rejected v023.

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

Image 1 is STYLE: canonical_style_reference.png. Match this image's rendering technique only. Ignore its people, clothing, equipment, and setting.
Image 2 is EDIT TARGET: Antares reference-sheet candidate v022, the latest sheet whose upper-left three-quarter thrusters the user asks to correct. Preserve this sheet and correct only the projection of the TWO cylindrical thruster pods in its UPPER-LEFT HERO VIEW.

Use case: precise-object-edit
Asset type: spacecraft reference sheet.
Design:
# Antares

**Description version: v13** (2026-09-26)


## Exterior

Broad, low utilitarian spacecraft with a wedge-shaped cockpit nose, raised central spine, recessed deck and paired cylindrical side engine pods. Ivory/light-gray hull, orange-red cockpit upper panels and rear engine housings, dark windows and engine openings. The orange marking behind the cockpit forms a deliberate roof panel around a circular hatch and clean side bands separated by ivory. Preserve the reference silhouette, proportions and color placement.

The hull shoulders are compact and the lateral walls stand nearly upright, with a modest angular chamfer rather than a broad outward flare. Front, rear, and top orthographic projections agree with the hero three-quarter view: the body sits inward of the unchanged engine-pod centers, the side walls do not spread into wide wing-like cheeks, and the top outline has restrained shoulders. Cockpit width, body length, central spine, and engine diameter and spacing remain consistent across views.

A single broad rectangular cargo-door panel occupies the lateral midship port-side opening, behind the cockpit and ahead of the port engine pod. Its top hinge is on the side wall, well below the upper deck and raised central spine. A continuous clean band of fixed ivory hull separates the hinge from the upper deck. The closed panel extends downward from this hinge to the opening's lower sill and occupies the side opening only; no part of it lies on the roof, upper deck, or central spine. The door has one uninterrupted rectangular face, a dark perimeter seam, and two simple recessed opening grips. There are no stacked doors, separate upper flaps, or adjacent second hatches. The open panel is the identical rectangle rotated upward about the same side-wall top hinge; panel width, height, opening, and hinge position agree in every view. A short loading ramp and two to three generic adult crew provide believable scale in the open-bay detail. The cargo door is lateral, never front-facing. No personnel hatch appears on the cockpit-side hull.

The rear orthographic view shows the same widely separated engine axes as the front and top views. Engine-center separation is approximately four turbine diameters, with mounting structures bridging the gap to the narrower aft hull. The rear drawing uses a consistent local scale for the hull and turbines while fitting its allocated sheet area. In the open cargo-bay detail, the fixed upper hull, recessed deck, and raised central spine remain visibly present behind and above the lifted door. The door is on the lower lateral side wall of a substantial ship; the surrounding upper structure occludes the sheet background where the view looks into the ship. The raised panel remains a separate foreground rectangle at its original low hinge; the structure behind it is fixed hull, not a second door.

Both cargo-door detail panels use the same viewing angle and magnification and show the surrounding ship structure continuously. Their framing includes the full fixed upper side-wall band, the recessed deck receding inward, and the raised central spine above and behind the hinge. Fixed hull fills the upper crop edge of both details; there is no slate-blue exterior background wedge directly above the door. The inset framing leaves enough room above the raised door to make the upper ship mass legible. Opening the single panel changes only its rotation and reveals the bay; the surrounding hull and deck geometry are identical in both states. All hull edges follow one coherent perspective.

In plan view, the hull has a broad tapered outline with articulated, shallow changes of direction. The blunt cockpit nose, sloping windscreen shoulders, wider cabin roof, and slight neck behind the cockpit preserve the same contours visible in the three-quarter hero. The cargo-door housing makes a mild local outward bulge. Farther aft, the side body flares outward slightly and then turns through a clear 90-degree return at the turbine mounting area. These shallow bulges and square returns belong to the structural hull; they are compact rather than broad wing-like lobes. The outline is not a single uninterrupted straight triangle. The central spine, recessed deck, and cockpit retain their established proportions.

The paired engine pods sit on outboard mounts with their intake faces clear of the adjacent aft body shoulders. Their fore-aft placement and mounting bridges are consistent in the three-quarter, top, side, and head-on projections. In the hero view the visible near turbine sits sufficiently forward and outboard of the adjacent body protrusion to expose its complete intake rim; it does not look buried behind that protrusion. The head-on view retains two unobstructed turbine faces at the established lateral spacing.

Both cylindrical engine pods have longitudinal axes parallel to the ship's fore-aft centerline, with no toe-in, toe-out, or independent pitch. Intake rims, ivory bands, and rear nozzle cross-sections are perpendicular to their respective pod axes. In three-quarter projection, the intake ellipses and the visible barrel lengths share the hull's perspective; neither intake is independently turned toward the viewer. Both pods use the same mirrored physical geometry and coherent foreshortening, retaining their existing mounting positions and clear near-side intake.

## Interior

A working ship, worn and patchworked rather than sleek. Scuffed painted metal, mismatched replacement panels, visible fasteners, repaired upholstery, accessible cable runs and practical maintenance patches. Controls are analog: physical toggle switches, rotary knobs, mechanical levers, round needle gauges and small recessed CRT-style instrumentation displays. No floating holograms or glossy touchscreen walls.

Cockpit has two forward-facing seats, pilot control yoke shaped like an aircraft steering wheel, instrument consoles in front of and beside both seats, and an aft access doorway. Instruments and controls have coherent practical mounting and remain reachable from the seats.


Requested local perspective correction:
Apply an extremely localized redraw only inside the TWO HERO ENGINE POD regions. The rest of this image is locked. In the attached 1536x1024 sheet, the NEAR HERO intake center must stay at approximately (925,272), and the FAR HERO intake center at approximately (380,124). Do not move either intake center or change either pod's physical length, diameter or mounting bridge. Retain the same rear tip positions, around (1080,218) for the near pod and (523,73) for the far pod.

Correct the FRONT RIM ellipse orientation and the connected barrel construction so both cylinders point forward along the ship's longitudinal axis toward lower-left. The hull's projected fore-aft direction runs approximately 25 degrees upward to the right (rearward) or 25 degrees downward to the left (forward). Both pods share that direction, with the usual small perspective convergence. The current intake circles are too face-on and too upright. Their corrected elliptical major axes should lean about 25 degrees to the RIGHT from vertical; their minor axes should follow the projected pod axes. Use a projected minor-to-major diameter ratio about 0.58–0.65, a moderately narrower face. KEEP the long diameter and centers unchanged. The front aperture, red rim, inner throat, three fan struts and central cone must all share that ONE ellipse projection. The circular cross-sections at the red/ivory band and rear cap must be parallel to it in 3D. Give the cone a short forward projection along the same longitudinal direction. Preserve the chunky paintwork, muted palette, heavy pod design and mounting clearances. Do not add rings or hardware. Correct both pods symmetrically in physical space.

LOCK every hull mark, the entire top orthographic drawing including its engines and intake cones, both side elevations, front and rear elevations, both cargo inset drawings and crew, and the background. Leave every region outside the hero's two engine pods untouched. No whole-sheet repaint. No moving the near engine leftward onto the body. No smaller engines. No changed fan designs in other views. No text or guides. Repaint only these local engine regions in the STYLE rendering.
Output one complete 1536 × 1024 reference sheet with the same framing as image 2. Keep everything else identical to image 2.
Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.
