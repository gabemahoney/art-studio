# Antares v031

User feedback verbatim: No the thrusers are still not aligned and are too long now
Mode: edit from original detailed v022 baseline, with dimensioned compact-cylinder guide v2. Rejected v030 not attached.
Tool: built-in image_gen.imagegen; model not exposed
Style: v2
Design: description v19 = description_versions/description-v19.md
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png (style v2; frozen style_versions/canonical_style_reference-v2.png)
- Image 2 EDIT TARGET: assets/ships/the_antares/candidates/v022/image.png
- Image 3 IDENTITY (construction only): assets/ships/the_antares/sources/engine-axis-construction-v2.png; original support vector source sources/engine-axis-construction-v2.svg. Guide uses same canvas coordinates as edit target. Approximate axis -21 degrees; projected near diameter 144 and axial length 124; far diameter 104 and axial length 90; projected circular cross-section ratio 0.70. All three guide axes parallel by construction. Guide is not a calibrated 3D ship model.
Guide rasterization: magick -background '#526b7d' assets/ships/the_antares/sources/engine-axis-construction-v2.svg assets/ships/the_antares/sources/engine-axis-construction-v2.png
Status: failed assistant review; not promoted. Generated pods are smaller, hull and other views drifted, and the alignment guide was not followed reliably. Do not use as baseline. Manual geometry/compositing method requested from user; no such edit performed yet.
Output: image.png, 1536 × 1024, copied from /Users/gmahoney/.codex/generated_images/01a0e10a-e606-7a60-ac77-8792df2504bc/exec-044cc74b-4fd9-4331-8370-3026941a1a6d.png

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

Image 1 is STYLE: match rendering only, ignore its people and scene.
Image 2 is EDIT TARGET: original detailed Antares sheet v022. Preserve its detailed hero hull.
Image 3 is IDENTITY: exact compact engine construction guide, in the SAME 1536x1024 canvas coordinates as image 2. Copy the two compact cylinder shapes, their locations, lengths, diameters and directions from image 3 onto image 2's HERO engines. The plain central beam in image 3 is only an alignment guide; never copy it over the detailed hull. Image 3 is geometry only, not a rendering reference.

Use case: precise-object-edit
Design:
# Antares

**Description version: v19** (2026-09-26)


## Exterior

Broad, low utilitarian spacecraft with a wedge-shaped cockpit nose, raised central spine, recessed deck and paired cylindrical side engine pods. Ivory/light-gray hull, orange-red cockpit upper panels and rear engine housings, dark windows and engine openings. The orange marking behind the cockpit forms a deliberate roof panel around a circular hatch and clean side bands separated by ivory. Preserve the reference silhouette, proportions and color placement.

The hull shoulders are compact and the lateral walls stand nearly upright, with a modest angular chamfer rather than a broad outward flare. Front, rear, and top orthographic projections agree with the hero three-quarter view: the body sits inward of the unchanged engine-pod centers, the side walls do not spread into wide wing-like cheeks, and the top outline has restrained shoulders. Cockpit width, body length, central spine, and engine diameter and spacing remain consistent across views.

A single broad rectangular cargo-door panel occupies the lateral midship port-side opening, behind the cockpit and ahead of the port engine pod. Its top hinge is on the side wall, well below the upper deck and raised central spine. A continuous clean band of fixed ivory hull separates the hinge from the upper deck. The closed panel extends downward from this hinge to the opening's lower sill and occupies the side opening only; no part of it lies on the roof, upper deck, or central spine. The door has one uninterrupted rectangular face, a dark perimeter seam, and two simple recessed opening grips. There are no stacked doors, separate upper flaps, or adjacent second hatches. The open panel is the identical rectangle rotated upward about the same side-wall top hinge; panel width, height, opening, and hinge position agree in every view. A short loading ramp and two to three generic adult crew provide believable scale in the open-bay detail. The cargo door is lateral, never front-facing. No personnel hatch appears on the cockpit-side hull.

The rear orthographic view shows the same widely separated engine axes as the front and top views. Engine-center separation is approximately four turbine diameters, with mounting structures bridging the gap to the narrower aft hull. The rear drawing uses a consistent local scale for the hull and turbines while fitting its allocated sheet area. In the open cargo-bay detail, the fixed upper hull, recessed deck, and raised central spine remain visibly present behind and above the lifted door. The door is on the lower lateral side wall of a substantial ship; the surrounding upper structure occludes the sheet background where the view looks into the ship. The raised panel remains a separate foreground rectangle at its original low hinge; the structure behind it is fixed hull, not a second door.

Both cargo-door detail panels use the same viewing angle and magnification and show the surrounding ship structure continuously. Their framing includes the full fixed upper side-wall band, the recessed deck receding inward, and the raised central spine above and behind the hinge. Fixed hull fills the upper crop edge of both details; there is no slate-blue exterior background wedge directly above the door. The inset framing leaves enough room above the raised door to make the upper ship mass legible. Opening the single panel changes only its rotation and reveals the bay; the surrounding hull and deck geometry are identical in both states. All hull edges follow one coherent perspective.

In plan view, the hull has a broad tapered outline with articulated, shallow changes of direction. The blunt cockpit nose, sloping windscreen shoulders, wider cabin roof, and slight neck behind the cockpit preserve the same contours visible in the three-quarter hero. The cargo-door housing makes a mild local outward bulge. Farther aft, the side body flares outward slightly and then turns through a clear 90-degree return at the turbine mounting area. These shallow bulges and square returns belong to the structural hull; they are compact rather than broad wing-like lobes. The outline is not a single uninterrupted straight triangle. The central spine, recessed deck, and cockpit retain their established proportions.

The paired engine pods sit on outboard mounts with their intake faces clear of the adjacent aft body shoulders. Their fore-aft placement and mounting bridges are consistent in the three-quarter, top, side, and head-on projections. In the hero view the visible near turbine sits sufficiently forward and outboard of the adjacent body protrusion to expose its complete intake rim; it does not look buried behind that protrusion. The head-on view retains two unobstructed turbine faces at the established lateral spacing.

The detailed three-quarter view defines the aft structure. The upper hull has articulated ivory shoulders, stepped mounting blocks, a raised central spine and recessed panelled deck surfaces. The top-down projection depicts these same structural masses and deck panels at the corresponding positions: ivory raised sections, shallow gray panelled recesses, transverse braces and aft mounting steps. The recessed deck is not a pair of large empty dark channels. All projections describe the same detailed solid ship.

Both engine pods are rigid round cylinders, with their longitudinal axes parallel to the central spine and straight fore-aft deck edges. Their front hubs, housing centers and aft nozzle centers lie on those axes. Intake rims, fans, ivory bands and rear caps share one coherent cylindrical projection with circular physical cross-sections and unchanged diameter and length. The near and far pods use mirrored mounting geometry, without outward yaw or independent pitch.

The engine pods are compact, squat drums. In side elevation, the complete pod including its short aft nozzle is approximately 1.4 times its diameter in length. Their barrels retain the original compact proportions in every projection; they are not long nacelles. Axis alignment is achieved by orienting each entire pod, without increasing barrel length or shifting its attachment point.

## Interior

A working ship, worn and patchworked rather than sleek. Scuffed painted metal, mismatched replacement panels, visible fasteners, repaired upholstery, accessible cable runs and practical maintenance patches. Controls are analog: physical toggle switches, rotary knobs, mechanical levers, round needle gauges and small recessed CRT-style instrumentation displays. No floating holograms or glossy touchscreen walls.

Cockpit has two forward-facing seats, pilot control yoke shaped like an aircraft steering wheel, instrument consoles in front of and beside both seats, and an aft access doorway. Instruments and controls have coherent practical mounting and remain reachable from the seats.

PRIORITY: the hero pods must be COMPACT and PARALLEL TO THE SPINE, exactly as constructed in image 3. Trace that construction rather than inventing new engine silhouettes. Keep the front centers exactly at their guide positions. The near engine front-to-rear center vector is (116,-44); the far engine vector is (84,-32). Both are parallel to the spine. The guide's near pod diameter is 144 pixels and axial center-to-center length is 124 pixels. Far diameter is 104 and axial length is 90. These compact dimensions are intentional. Do not elongate either engine, bring it forward, yaw it outward, shrink its diameter or squash the face. Transfer the guide's entire coherent round-cylinder geometry, then paint the existing red/ivory bands, dark fan with three chunky spokes, circular lip and short rear nozzle in the original gouache finish. The existing hull conceals appropriate portions of the far mount, without changing the pod itself.

Preserve every part of the detailed three-quarter HULL in image 2, including its cockpit, spine, blocky stepped shoulders, cargo door and panelled deck.
Also update the TOP-DOWN view to depict that detailed hero structure: shallow gray panelled deck, raised ivory blocks and transverse sections in matching positions, not broad empty dark troughs. Keep its engine pods at the original short lengths shown in image 2.
Preserve the other views, cargo insets, layout and background. No guide beam, guide text, arrows, lines or diagrams in the final image.
Output one complete 1536x1024 reference sheet.
Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.
