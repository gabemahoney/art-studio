# Antares v012
User feedback: "It looks like it might be too flared on the sides if I extrapolate what it should look like from the 3/4 view."
User authorization: "yes", accepting the proposal to preserve hero geometry and engine spacing and bring the orthographic hull sides inward and more upright.
Mode: edit of user-designated candidates/v010/image.png
Style: v2
Tool: built-in image_gen (model not exposed)
Output: image.png, copied from /Users/gmahoney/.codex/generated_images/01a0df6c-410c-7971-bfd1-ebf9b1f5f347/exec-a85844ad-6708-4e93-86f5-f573b62e4d64.png
Visual check: reduced orthographic flare, but preservation still failed: hero shoulder paint/geometry changed and front-view engine centers moved inward. Candidate not promoted. v011 retains engine spacing better; neither meets all preservation constraints. A deterministic composite of v011's revised orthographic body regions into v010 would preserve the hero and insets exactly, but requires explicit user instruction to use editing outside image_gen.
Reason for retry: v011 also changed the hero shoulders. This attempt reuses v010 and adds strict spatial preservation instructions.
Inputs:
- Image 1 STYLE: gm/image_generation/ref_images/style_references/canonical_style_reference.png (style v2; frozen counterpart style_versions/canonical_style_reference-v2.png)
- DESIGN: description.md (v8 = description_versions/description-v8.md)
- Image 2 EDIT TARGET: gm/image_generation/assets/ships/the_antares/candidates/v010/image.png

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

Image 1 is STYLE: canonical_style_reference.png. Match rendering technique only. Ignore its people, clothing, equipment, and setting.
Image 2 is EDIT TARGET: Antares candidates/v010/image.png. The user has accepted a targeted adjustment to this sheet: reconcile its too-flared orthographic hull sides with its preserved upper-left hero 3/4 view. That hero retains the user's v005 geometry authority and the accepted cargo-door correction.

Use case: precise-object-edit
Asset type: spacecraft exterior reference sheet.

Design:
# Antares

**Description version: v8** (2026-09-26)


## Exterior

Broad, low utilitarian spacecraft with a wedge-shaped cockpit nose, raised central spine, recessed deck and paired cylindrical side engine pods. Ivory/light-gray hull, orange-red cockpit upper panels and rear engine housings, dark windows and engine openings. The orange marking behind the cockpit forms a deliberate roof panel around a circular hatch and clean side bands separated by ivory. Preserve the reference silhouette, proportions and color placement.

The hull shoulders are compact and the lateral walls stand nearly upright, with a modest angular chamfer rather than a broad outward flare. Front, rear, and top orthographic projections agree with the hero three-quarter view: the body sits inward of the unchanged engine-pod centers, the side walls do not spread into wide wing-like cheeks, and the top outline has restrained shoulders. Cockpit width, body length, central spine, and engine diameter and spacing remain consistent across views.

A single broad rectangular cargo-door panel occupies the lateral midship port-side opening, behind the cockpit and ahead of the port engine pod. Its top hinge is on the side wall, well below the upper deck and raised central spine. A continuous clean band of fixed ivory hull separates the hinge from the upper deck. The closed panel extends downward from this hinge to the opening's lower sill and occupies the side opening only; no part of it lies on the roof, upper deck, or central spine. The door has one uninterrupted rectangular face, a dark perimeter seam, and two simple recessed opening grips. There are no stacked doors, separate upper flaps, or adjacent second hatches. The open panel is the identical rectangle rotated upward about the same side-wall top hinge; panel width, height, opening, and hinge position agree in every view. A short loading ramp and two to three generic adult crew provide believable scale in the open-bay detail. The cargo door is lateral, never front-facing. No personnel hatch appears on the cockpit-side hull.

## Interior

A working ship, worn and patchworked rather than sleek. Scuffed painted metal, mismatched replacement panels, visible fasteners, repaired upholstery, accessible cable runs and practical maintenance patches. Controls are analog: physical toggle switches, rotary knobs, mechanical levers, round needle gauges and small recessed CRT-style instrumentation displays. No floating holograms or glossy touchscreen walls.

Cockpit has two forward-facing seats, pilot control yoke shaped like an aircraft steering wheel, instrument consoles in front of and beside both seats, and an aft access doorway. Instruments and controls have coherent practical mounting and remain reachable from the seats.


LOCAL RETOUCH WITH STRICT SPATIAL LIMITS. Image 2 is a 1536 x 1024 sheet. Treat ALL pixels in the rectangle x=0..1120, y=0..540 as locked and untouchable: this is the hero view. DO NOT repaint, straighten, narrow, reinterpret, simplify, or modify ANY part of that hero. Its side shoulders, nose, side-wall slopes, hull perimeter, color planes, edges, panel seams, engine pods and cargo door must retain their exact original positions and appearance. Also lock ALL pixels at x=925..1535, y=715..1023 (both inset details). The only authorized paint areas are the outer cream hull shoulders of the smaller TOP view (x=1150..1485, y=190..445), FRONT view (x=135..535, y=565..715), and REAR view (x=140..300, y=790..945). Keep every other region as the original. Do not redraw the full sheet. Within those three local paint areas only, revise the hull shoulder shapes as follows. EDIT ONLY THE ORTHOGRAPHIC HULL SHOULDERS. Preserve the entire upper-left hero 3/4 view exactly, preserve the two lower-right cargo-door insets exactly, and preserve the sheet's arrangement, background, palette, brushwork, and view scales. The hero ship is the geometry authority. Make the front-on view at middle left, the top view at upper right, and the rear view at bottom left agree with the compact side-wall geometry seen in that hero. The current front view splays the outer hull cheeks too far outward. Pull those outer hull shoulders inward toward the cockpit and make the outside walls more upright: a restrained, clearly visible correction, about 15 percent inward movement of each shoulder relative to its current distance from the centerline. Keep the center cockpit completely unchanged in width and height. Keep both engine pods completely unchanged in diameter and center position; let their short mounting bridges span the revised gap naturally. Do not shrink the whole ship or move the engines inward. Preserve hull depth/height and the belly. The body should read as a compact utilitarian box with angled chamfers, not wide flared wings.

Apply the corresponding reduced shoulder width to the TOP orthographic outline: gently pull the widest lateral hull cheeks inward and straighten their outer run, with restrained taper into the nose. Preserve the center spine, nose, engines, and length. In the REAR orthographic view, keep the same compact nearly upright body sides. Keep the side profiles unchanged unless a tiny consistency adjustment to the shoulder edge is necessary; no shortening or height change. All projections represent the same ship.

CRITICAL PRESERVATION: keep the corrected single lateral rectangular cargo panel exactly as in the hero: low side-wall top hinge, uninterrupted fixed ivory hull band above it, closed rectangle extending downward only. Do not alter the closed door, its dimensions, hinge, or clean hull band. Keep both cargo insets and the three generic adult crew and short ramp exactly as shown. No upper flap, second door, cockpit-side personnel hatch, front-facing cargo opening, or roof hatch expansion. Keep the hero silhouette intact. No new views, labels, arrows, text, or scenery.

Keep everything else identical to the edit target, and keep all repainted areas in the STYLE image's rendering.
Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.
