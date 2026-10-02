# Antares v014
User request: It looks good. One small note we should fix. In the cargo door break out, it shows blue background just above the door. But if you were to view the ship from that angle, you would actually see the top part of the ship above the cargo door, not blue background. It makes it look like the ship is flatter than it truly is.

Also, The front view has the engine turbines very wide apart while the back view has them very close. The back view is wrong. Looking at the 2/3 and top views it does seem like the turbines should be more far apart. Modify the back view.
Mode: edit of user-designated candidates/v013/image.png
Style: v2
Tool: built-in image_gen (model not exposed)
Output: image.png, copied from /Users/gmahoney/.codex/generated_images/01a0df6c-410c-7971-bfd1-ebf9b1f5f347/exec-6c4a278e-1dd6-414d-b391-3ffdec1514ef.png
Visual check: upper structure added behind open hatch. Rear turbines farther apart, but still too large relative to separation, and rear view encroaches on adjacent profile. Use as a local donor for the authorized composite; do not promote this full-sheet output.
Design: description.md (v9 = description_versions/description-v9.md)
Inputs:
- Image 1 STYLE: gm/image_generation/ref_images/style_references/canonical_style_reference.png (style v2)
- Image 2 EDIT TARGET: gm/image_generation/assets/ships/the_antares/candidates/v013/image.png
Planned isolation: if the generator changes unrelated regions, use the already-authorized direct compositing workflow to retain only the rear view and open inset corrections on v013.

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

Image 1 is STYLE: canonical_style_reference.png. Match rendering technique only; ignore subjects and setting.
Image 2 is EDIT TARGET: Antares candidates/v013/image.png, designated by the user's approving feedback. Preserve this sheet except for TWO LOCAL CORRECTIONS: lower-right open cargo-door inset and lower-left rear orthographic view.

Design specification:
# Antares

**Description version: v9** (2026-09-26)


## Exterior

Broad, low utilitarian spacecraft with a wedge-shaped cockpit nose, raised central spine, recessed deck and paired cylindrical side engine pods. Ivory/light-gray hull, orange-red cockpit upper panels and rear engine housings, dark windows and engine openings. The orange marking behind the cockpit forms a deliberate roof panel around a circular hatch and clean side bands separated by ivory. Preserve the reference silhouette, proportions and color placement.

The hull shoulders are compact and the lateral walls stand nearly upright, with a modest angular chamfer rather than a broad outward flare. Front, rear, and top orthographic projections agree with the hero three-quarter view: the body sits inward of the unchanged engine-pod centers, the side walls do not spread into wide wing-like cheeks, and the top outline has restrained shoulders. Cockpit width, body length, central spine, and engine diameter and spacing remain consistent across views.

A single broad rectangular cargo-door panel occupies the lateral midship port-side opening, behind the cockpit and ahead of the port engine pod. Its top hinge is on the side wall, well below the upper deck and raised central spine. A continuous clean band of fixed ivory hull separates the hinge from the upper deck. The closed panel extends downward from this hinge to the opening's lower sill and occupies the side opening only; no part of it lies on the roof, upper deck, or central spine. The door has one uninterrupted rectangular face, a dark perimeter seam, and two simple recessed opening grips. There are no stacked doors, separate upper flaps, or adjacent second hatches. The open panel is the identical rectangle rotated upward about the same side-wall top hinge; panel width, height, opening, and hinge position agree in every view. A short loading ramp and two to three generic adult crew provide believable scale in the open-bay detail. The cargo door is lateral, never front-facing. No personnel hatch appears on the cockpit-side hull.

The rear orthographic view shows the same widely separated engine axes as the front and top views. Engine-center separation is approximately four turbine diameters, with mounting structures bridging the gap to the narrower aft hull. The rear drawing uses a consistent local scale for the hull and turbines while fitting its allocated sheet area. In the open cargo-bay detail, the fixed upper hull, recessed deck, and raised central spine remain visibly present behind and above the lifted door. The door is on the lower lateral side wall of a substantial ship; the surrounding upper structure occludes the sheet background where the view looks into the ship. The raised panel remains a separate foreground rectangle at its original low hinge; the structure behind it is fixed hull, not a second door.

## Interior

A working ship, worn and patchworked rather than sleek. Scuffed painted metal, mismatched replacement panels, visible fasteners, repaired upholstery, accessible cable runs and practical maintenance patches. Controls are analog: physical toggle switches, rotary knobs, mechanical levers, round needle gauges and small recessed CRT-style instrumentation displays. No floating holograms or glossy touchscreen walls.

Cockpit has two forward-facing seats, pilot control yoke shaped like an aircraft steering wheel, instrument consoles in front of and beside both seats, and an aft access doorway. Instruments and controls have coherent practical mounting and remain reachable from the seats.


Use case: precise-object-edit
Asset type: spacecraft reference sheet.
User request:
It looks good. One small note we should fix. In the cargo door break out, it shows blue background just above the door. But if you were to view the ship from that angle, you would actually see the top part of the ship above the cargo door, not blue background. It makes it look like the ship is flatter than it truly is.

Also, The front view has the engine turbines very wide apart while the back view has them very close. The back view is wrong. Looking at the 2/3 and top views it does seem like the turbines should be more far apart. Modify the back view.

CORRECTION 1 — LOWER-RIGHT OPEN CARGO-DOOR INSET:
In the open inset at approximately x1213..1501, y730..975 on the 1536x1024 sheet, the slate-blue area immediately above and behind the raised door falsely implies there is no ship above the hatch. Replace that blue void WITH THE EXISTING SHIP'S UPPER HULL, RECESSED DECK, AND CENTRAL SPINE, seen at the appropriate matching angle. Use the upper-left hero as the geometry guide: its low door hinge sits beneath a substantial ivory hull band, deck and raised spine. Show that same fixed upper architecture extending upward/backward behind the raised rectangular door. The structure should continue into the TOP CROP EDGE of this tight inset, making its bulk clear. This is a close crop of a thick ship, not a flat wall floating in blue. Preserve the existing raised panel's exact outline, height, width, low hinge, and angle. The new hull is BEHIND the door, not above the door as a second hinged panel. No second flap, hatch, or roof door. Keep the dark opening, three adult crew, ramp, left/right jambs, and inset border unchanged. Keep all new hull within the existing inset neighborhood, without overlapping the side profile above. The current door slightly projects above its frame; leave that foreground silhouette alone. Add fixed hull behind it inside the frame and around its sides, so blue background no longer substitutes for structure. Use broad quiet cream/ivory top planes and slate shadow side planes, consistent with the hero.

CORRECTION 2 — LOWER-LEFT REAR ORTHOGRAPHIC:
Only the rear view at x25..405, y770..952 is wrong. Reconstruct this one small rear projection with its two turbines clearly widely spaced, consistent with the front view and top view. Preserve the front, top, side, and hero views exactly. The front view's engine center separation is about FOUR turbine diameters; use the SAME physical ratio in the rear view. In the rear view currently the separation is only about TWO diameters: correct that. Keep the rear image within its existing roughly 380-pixel-wide allocation by rendering this single projection at a smaller consistent local scale. Aim for turbine diameters about 72 pixels and centers around x70 and x363 at y865: far apart, connected by visible ivory mounting arms to the compact central aft hull around x216. Scale the aft hull consistently with those turbines; never merely widen or stretch its body. Keep the raised central spine, dark rectangular aft center recess, flat angular cream hull and brick-red circular turbine bands. No duplicate engines. Do not move or resize any other sheet view and do not overlap the adjacent starboard profile at x420.

All other views, original hero geometry, corrected orthographic shoulders, low lateral cargo hinge, clean fixed hull band above the closed door, layout, palette, slate background, and flat gouache brushwork are LOCKED. No text, labels, arrows, scenery, extra views, or new inset borders.

Keep everything else identical to the edit target, and keep all repainted areas in the STYLE image's rendering.
Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.
