# Antares v010
User request: Use v005 as the geometry authority. Correct the Antares reference sheet without changing its overall silhouette or layout.

Critical cargo-door correction: In the upper-left hero 3/4 view, the cargo bay door must be a single lateral rectangular panel on the port side. Its top hinge line is well below the upper deck/central spine, at the side-wall pivot where v005’s raised door meets the opening. When closed, the panel extends downward from that hinge into the side opening only. Leave a continuous clean band of hull above it—do not let the closed hatch climb onto the roof, upper deck, or central spine.

Do not create two stacked doors, a separate upper flap, or any adjacent second hatch. The closed hatch is one uninterrupted rectangle.

The lower-right open-bay inset must show the exact same rectangular panel, opening, hinge position, width, and height as the hero view. Rotate that same panel upward from its top hinge; show a short ramp and 2–3 generic adult crew at believable scale. The cargo door is lateral, never front-facing. Remove any cockpit-side personnel hatch.

Keep the existing cream/ivory hull, brick-red engine bands, slate-blue shadow treatment, and late-1970s flat angular gouache reference-sheet style.
Mode: edit of user-designated candidates/v005/image.png
Style: v2
Tool: built-in image_gen (model not exposed)
Output: image.png (1536 x 1024), copied from /Users/gmahoney/.codex/generated_images/01a0df6c-410c-7971-bfd1-ebf9b1f5f347/exec-8fc54457-95a8-4420-a631-d628b8f2be50.png
Visual check: single closed lateral panel below fixed hull band; no stacked flap; matching open-bay concept with short ramp and three adult crew; v005 view arrangement, silhouette, and palette retained. Panel correspondence assessed visually, not by a mechanical model. Saved as candidate; no promotion performed.
Inputs:
- Image 1 STYLE: gm/image_generation/ref_images/style_references/canonical_style_reference.png (style v2; frozen counterpart style_versions/canonical_style_reference-v2.png)
- DESIGN: description.md (v7 = description_versions/description-v7.md)
- Image 2 EDIT TARGET: gm/image_generation/assets/ships/the_antares/candidates/v005/image.png

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

Image 1 is STYLE: canonical_style_reference.png. Match its rendering technique only; ignore its people, clothing, equipment, and setting.
Image 2 is EDIT TARGET: Antares candidates/v005/image.png, explicitly designated by the user as geometry authority. Preserve this sheet's layout, ship silhouette, proportions, camera angles, background, and palette.

Use case: precise-object-edit
Asset type: spacecraft exterior reference sheet.
Design specification:
# Antares

**Description version: v7** (2026-09-26)


## Exterior

Broad, low utilitarian spacecraft with a wedge-shaped cockpit nose, raised central spine, recessed deck and paired cylindrical side engine pods. Ivory/light-gray hull, orange-red cockpit upper panels and rear engine housings, dark windows and engine openings. The orange marking behind the cockpit forms a deliberate roof panel around a circular hatch and clean side bands separated by ivory. Preserve the reference silhouette, proportions and color placement.

A single broad rectangular cargo-door panel occupies the lateral midship port-side opening, behind the cockpit and ahead of the port engine pod. Its top hinge is on the side wall, well below the upper deck and raised central spine. A continuous clean band of fixed ivory hull separates the hinge from the upper deck. The closed panel extends downward from this hinge to the opening's lower sill and occupies the side opening only; no part of it lies on the roof, upper deck, or central spine. The door has one uninterrupted rectangular face, a dark perimeter seam, and two simple recessed opening grips. There are no stacked doors, separate upper flaps, or adjacent second hatches. The open panel is the identical rectangle rotated upward about the same side-wall top hinge; panel width, height, opening, and hinge position agree in every view. A short loading ramp and two to three generic adult crew provide believable scale in the open-bay detail. The cargo door is lateral, never front-facing. No personnel hatch appears on the cockpit-side hull.

## Interior

A working ship, worn and patchworked rather than sleek. Scuffed painted metal, mismatched replacement panels, visible fasteners, repaired upholstery, accessible cable runs and practical maintenance patches. Controls are analog: physical toggle switches, rotary knobs, mechanical levers, round needle gauges and small recessed CRT-style instrumentation displays. No floating holograms or glossy touchscreen walls.

Cockpit has two forward-facing seats, pilot control yoke shaped like an aircraft steering wheel, instrument consoles in front of and beside both seats, and an aft access doorway. Instruments and controls have coherent practical mounting and remain reachable from the seats.


Requested edit:
Use v005 as the geometry authority. Correct the Antares reference sheet without changing its overall silhouette or layout.

Critical cargo-door correction: In the upper-left hero 3/4 view, the cargo bay door must be a single lateral rectangular panel on the port side. Its top hinge line is well below the upper deck/central spine, at the side-wall pivot where v005’s raised door meets the opening. When closed, the panel extends downward from that hinge into the side opening only. Leave a continuous clean band of hull above it—do not let the closed hatch climb onto the roof, upper deck, or central spine.

Do not create two stacked doors, a separate upper flap, or any adjacent second hatch. The closed hatch is one uninterrupted rectangle.

The lower-right open-bay inset must show the exact same rectangular panel, opening, hinge position, width, and height as the hero view. Rotate that same panel upward from its top hinge; show a short ramp and 2–3 generic adult crew at believable scale. The cargo door is lateral, never front-facing. Remove any cockpit-side personnel hatch.

Keep the existing cream/ivory hull, brick-red engine bands, slate-blue shadow treatment, and late-1970s flat angular gouache reference-sheet style.

Precise geometric instruction for image 2: In its upper-left hero view, the REAL hinge is the LOWER dark hinge bar immediately above the dark cargo opening, approximately from (596,248) to (753,216) on the 1536-by-1024 reference. The upper edge of the currently raised panel at approximately (631,154) to (771,118) is its FREE EDGE, NOT its pivot. Close that raised panel by rotating it DOWN about the LOWER hinge bar until it fills the existing dark opening beneath, approximately down to the sill from (617,375) to (770,348). Preserve the actual side-wall pivot. Restore quiet fixed ivory hull behind the formerly raised panel. Absolutely do not trace the raised panel's upper free edge as a new closed-door top edge. Do not extend a tall closed slab from the central spine down to the cargo floor. One simple rectangular face, without a horizontal subdivision. The panel is rectangular in physical geometry and appropriately foreshortened in this 3/4 projection.

In the lower-right open inset, preserve this same low side-wall hinge and the same panel dimensions and opening dimensions. Raise the single panel from its top hinge and show two or three simple generic adult figures beside/on a short ramp. Adult height approximately 65–75 percent of the opening height; the opening must read as useful cargo access. Keep the existing inset position and frame. Preserve the neighboring closed-door inset, making its hinge and panel match. Remove any small personnel-door outline on the cockpit side and fill with continuous hull paint. Preserve all other orthographic views and their arrangement, correcting only matching port-door geometry if necessary. No additional views, labels, arrows, explanatory text, or diagram marks. This is an exterior sheet; do not add cockpit interior views.

Keep everything else identical to the edit target, and keep all repainted areas in the STYLE image's rendering.
Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.
