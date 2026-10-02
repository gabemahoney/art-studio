# Antares v016
User request: "It looks [Image #1] , the area I circled in red still looks wrong."
Context: user circled both cargo-door inset upper regions, rejecting v015's incomplete/misaligned upper structure.
Mode: local edit of last accepted geometry baseline candidates/v013/image.png
Tool: built-in image_gen (model not exposed)
Output: image.png, copied from /Users/gmahoney/.codex/generated_images/01a0df6c-410c-7971-bfd1-ebf9b1f5f347/exec-a9086f6c-1864-4202-ab61-64cadbb973b0.png
Visual check: coherent wider-framed closed/open cargo insets, fixed upper hull clearly above the raised door. Use only these inset areas in final composite v017 to preserve the previous rear-engine correction.
Style: v2
Design: description.md (v10 = description_versions/description-v10.md)
Inputs:
- Image 1 STYLE: gm/image_generation/ref_images/style_references/canonical_style_reference.png (style v2)
- Image 2 EDIT TARGET: gm/image_generation/assets/ships/the_antares/candidates/v013/image.png
Preservation plan: composite only the corrected inset interiors onto sources/unmarked-v015-composite.png, retaining the widened rear view. The user's annotated candidates/v015/image.png is preserved untouched. The unmarked base was recovered from the previous turn's exact saved composite.

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

Image 1 is STYLE: canonical_style_reference.png. Match its painted rendering only; ignore its subjects.
Image 2 is EDIT TARGET AND GEOMETRY AUTHORITY: the last accepted Antares sheet, candidates/v013/image.png. Its large upper-left hero is authoritative for every deck, wall, hinge, and spine relationship.

Use case: precise-object-edit.
Design specification:
# Antares

**Description version: v10** (2026-09-26)


## Exterior

Broad, low utilitarian spacecraft with a wedge-shaped cockpit nose, raised central spine, recessed deck and paired cylindrical side engine pods. Ivory/light-gray hull, orange-red cockpit upper panels and rear engine housings, dark windows and engine openings. The orange marking behind the cockpit forms a deliberate roof panel around a circular hatch and clean side bands separated by ivory. Preserve the reference silhouette, proportions and color placement.

The hull shoulders are compact and the lateral walls stand nearly upright, with a modest angular chamfer rather than a broad outward flare. Front, rear, and top orthographic projections agree with the hero three-quarter view: the body sits inward of the unchanged engine-pod centers, the side walls do not spread into wide wing-like cheeks, and the top outline has restrained shoulders. Cockpit width, body length, central spine, and engine diameter and spacing remain consistent across views.

A single broad rectangular cargo-door panel occupies the lateral midship port-side opening, behind the cockpit and ahead of the port engine pod. Its top hinge is on the side wall, well below the upper deck and raised central spine. A continuous clean band of fixed ivory hull separates the hinge from the upper deck. The closed panel extends downward from this hinge to the opening's lower sill and occupies the side opening only; no part of it lies on the roof, upper deck, or central spine. The door has one uninterrupted rectangular face, a dark perimeter seam, and two simple recessed opening grips. There are no stacked doors, separate upper flaps, or adjacent second hatches. The open panel is the identical rectangle rotated upward about the same side-wall top hinge; panel width, height, opening, and hinge position agree in every view. A short loading ramp and two to three generic adult crew provide believable scale in the open-bay detail. The cargo door is lateral, never front-facing. No personnel hatch appears on the cockpit-side hull.

The rear orthographic view shows the same widely separated engine axes as the front and top views. Engine-center separation is approximately four turbine diameters, with mounting structures bridging the gap to the narrower aft hull. The rear drawing uses a consistent local scale for the hull and turbines while fitting its allocated sheet area. In the open cargo-bay detail, the fixed upper hull, recessed deck, and raised central spine remain visibly present behind and above the lifted door. The door is on the lower lateral side wall of a substantial ship; the surrounding upper structure occludes the sheet background where the view looks into the ship. The raised panel remains a separate foreground rectangle at its original low hinge; the structure behind it is fixed hull, not a second door.

Both cargo-door detail panels use the same viewing angle and magnification and show the surrounding ship structure continuously. Their framing includes the full fixed upper side-wall band, the recessed deck receding inward, and the raised central spine above and behind the hinge. Fixed hull fills the upper crop edge of both details; there is no slate-blue exterior background wedge directly above the door. The inset framing leaves enough room above the raised door to make the upper ship mass legible. Opening the single panel changes only its rotation and reveals the bay; the surrounding hull and deck geometry are identical in both states. All hull edges follow one coherent perspective.

## Interior

A working ship, worn and patchworked rather than sleek. Scuffed painted metal, mismatched replacement panels, visible fasteners, repaired upholstery, accessible cable runs and practical maintenance patches. Controls are analog: physical toggle switches, rotary knobs, mechanical levers, round needle gauges and small recessed CRT-style instrumentation displays. No floating holograms or glossy touchscreen walls.

Cockpit has two forward-facing seats, pilot control yoke shaped like an aircraft steering wheel, instrument consoles in front of and beside both seats, and an aft access doorway. Instruments and controls have coherent practical mounting and remain reachable from the seats.


PRIMARY TASK: Rebuild ONLY THE TWO CARGO-DOOR DETAIL INSETS at the lower right. Their current framing is geometrically wrong: they show an isolated low wall against blue background where the upper half of the ship should be. Both close-ups must clearly depict the full-depth surrounding upper ship structure seen in the HERO view. The user explicitly rejected the previous attempt's upper-deck geometry; resolve the perspective and solid geometry, not just the color.

Keep the sheet canvas, hero, all five orthographic views, background, and view placement exactly as image 2. Retain two separate rectangular detail frames at approximately x934..1187 and x1213..1501, y731..975 on the 1536x1024 sheet. Put ALL of each inset's artwork INSIDE its frame. No door panel poking out above the frame. Redraw both inset interiors coherently in one pass; do not collage a disconnected strip over them.

The two insets show exactly the same cargo bay, viewpoint, magnification, fixed hull and perspective. Left = door CLOSED. Right = that identical rectangular door OPEN, rotated upward about its same low lateral top hinge. The opening is in the port SIDE WALL, behind cockpit and forward of engine, as in the hero.

ZOOM OUT slightly within BOTH frames, and position the bay lower within them, so that the substantial UPPER SHIP is visible ABOVE the entire raised door. Reserve the upper approximately one third of each inset for FIXED IVORY HULL: the upper side-wall band flowing continuously back into the recessed horizontal deck, with the massive raised central spine farther inward. These are the exact structures above the hero's cargo door. They recede toward the SAME vanishing direction as the jambs and door, and physically connect to the side wall. Fixed ship structure fills each inset's complete TOP BORDER from left to right. There must be NO slate-blue sheet-background region inside either inset above the door. This is a tightly cropped view of a large solid spacecraft, not a freestanding façade. Do not invent a thin extra awning or a second door.

In the right inset, the raised panel must be visibly in FRONT OF and BELOW the continuous upper hull. Its entire top/free edge must have visible solid ship structure behind and above it. Leave meaningful visible height above the raised panel, roughly 40–60 pixels at the inset's native size, to show how much ship exists above the low hinge. The hinge remains on the low side wall and never migrates onto the roof. Repaint the full surrounding architecture to align it, with no seams from a pasted crop. Preserve the broad single rectangular panel aspect ratio, the same opening in both states, a short ramp, and three generic adult crew in the right inset. Figures may be modestly smaller to suit the slightly wider inset framing; maintain believable scale. In the left inset, show that same solid deck and spine background continuing above the closed rectangle. Make the fixed architecture obviously identical between both insets; only the door state and the right inset's ramp/crew differ.

No red circle, annotation, text, labels, arrows, extra hatch, split panel, stacked door, or layout changes. Cream/ivory hull, brick-red markings if visible, slate shadow planes, quiet broad flat gouache brushwork.
Keep everything else identical to image 2, and keep all repainted areas in image 1's rendering.
Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.
