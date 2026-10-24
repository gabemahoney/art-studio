# antares-ringed-planet-beauty v005

User request verbatim: the jet from the rightmost engine is not cleatly coming out of it. It almost looks like its coming out of the center.
Mode: Retry of failed v004 (which copied the anchor's figures and split into two comic panels). Same trail re-rooting edit of v003, with the single-image guard, no-people guard and the ship design text restored.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0ebbc-a50e-7a93-a2ad-9f90dd31c8fa/exec-fab8eeee-75e8-4b98-b5c6-ad6de931a931.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/antares-ringed-planet-beauty/v003/image.png
Date: 2026-09-28
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.19 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: TODO — fill in

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
Image 2 is EDIT TARGET: the Antares beauty shot v003 — the image being modified. Preserve everything the prompt does not explicitly change.

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

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration of ONE spacecraft in space, filling the whole frame. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO orthographic views, NO labels. There are NO people, NO figures, NO faces, NO interiors, NO cockpit interiors anywhere in this image. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, its clothing, its interior, its panel layout or its composition.

TASK: This is a targeted edit of image 2. Image 2 is already correct in almost every respect. Reproduce image 2 — its hull and all its structural panel detail, its cockpit, its cargo door, its camera angle, its composition and crop, its barren planet below, its stars, its dark background, its colors and its lighting — and change ONE thing: where the engine trails attach.

THE PROBLEM in image 2: the trail behind the near (right-hand, lower) engine pod does not clearly emerge from that pod's nozzle. It appears to start above and inboard of the pod, so it reads as exhaust venting from the middle of the hull rather than from the engine.

THE FIX: each trail must begin AT the dark circular nozzle opening in the aft end of its own engine pod, and nowhere else.
- The root of each trail is the same width as that pod's nozzle opening and sits centered on it, physically touching it, no gap and no offset. The nozzle stays visible as the dark circular aft face of the pod; the trail starts at its rim.
- Each trail runs straight back along its own pod's cylindrical axis, parallel to the ship's fore-aft line. It does not angle inward toward the hull centerline, does not cross the hull, and does not start anywhere on the hull.
- The near pod sits lower and further right, so its trail sits lower and further right than the far pod's. The two trails stay clearly separate along their whole length.
- No exhaust, plume, streak or haze emerges from the hull, the roof, the raised spine, the cargo door, or the gap between the pods.

TRAIL RENDERING: two or three flat opaque tapering shapes with hard straight edges — a brighter ivory-ochre core shape and one muted slate outer shape — narrowing as they recede. Painted shapes, not light: no glow, no bloom, no halo, no soft or feathered edges, no transparency gradient, no particles.

SETTING (as in image 2, unchanged): a barren airless planet below, built from a few large flat planes of dead gray-ochre rock with at most two or three simple crater shapes and large empty under-detailed areas. No planetary rings of any kind. Deep near-black space above with a handful of flat dot stars. One directional light from the upper right.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
