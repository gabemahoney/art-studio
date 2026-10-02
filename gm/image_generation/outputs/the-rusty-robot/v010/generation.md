# the-rusty-robot v010

User request verbatim: make the left ear (foreground) of the robot not shadowed. it looks 3d whereas the rest of the image looks 2d.
Mode: Edit off v009. Single detail change: the near ear of the sign's painted robot emblem — the robot's own left, appearing on the viewer's right — carried a curved interior shadow that modelled it as a rounded three-dimensional form while every other part of the emblem was a flat stencil, so it read as 3D against a 2D image and broke the painted-sign illusion. That ear is flattened to one solid shape of the same chipped ivory with no interior shadow, gradient, crescent or highlight, described by outline alone, and the flat-stencil rule is restated across the whole emblem with chipping to bare rust as the only permitted variation. The hooded lamp's wash across the board is explicitly distinguished from shading inside the emblem's shapes so it is not removed as well.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f4b0-5395-7291-bd4d-dd8306e15c00/exec-afb29cc9-c8a6-4496-b2de-9c044c5385f3.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v009/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.06 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Emblem flattened; verified on a side-by-side magnified comparison against v009. The near ear — the robot's own left, on the viewer's right — is now a single solid shape of the same chipped ivory with no interior shadow, no curved crescent along its inner edge, no gradient and no highlight, described by outline alone. The flat-stencil rule also took across the rest of the emblem: the dome head, face plate, eyes, neck, shoulders, bow tie and body all read as uniform flat shapes separated only by the dark board showing through, with the previous soft modelling on the head and shoulders gone. The only variation remaining inside the ivory is flat hard-edged chipping to bare rust, which is wear rather than shading. The emblem now reads as a sign painter's silhouette rather than a rendered object, and no longer pops as a 3D element against an otherwise flat image. The hooded lamp's warm wash still falls across the upper part of the whole board, correctly preserved as lighting on the board rather than shading inside the emblem's shapes. Nothing else changed: the sign stays flat on the wall with its edges parallel to the wall's horizontal lines and grey wall all around it, the lettering still reads exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals, and the armoured brow, arched ribbed door, steps, handrail, angular machined lamps, grey ferrocrete with its muted teal bands and no red or orange, domed tower, dome underside, two distant silhouettes, pitch-black alley, clean dry dusty paving with no rocks, Sion's folded arms and squared alert stance, Graxo's wine-aubergine cape with both gold pins, and Daxus's likeness are all intact. File is 2.06 MB, comfortably inside the 2.5 MB book-float budget, at 1536x1024 exact 3:2 matching the other scene images in the book. ONE ITEM REMAINS OUTSTANDING from earlier in the scene, never addressed: the crew are lit at close to full value rather than as the dark masses with a thin cool rim that the user's original "conferring more in the shadows" request implied. The user has not raised it again and may be content; it is recorded here rather than assumed resolved.

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

## Note on the Forbidden list

Every item in the Style Block's "Forbidden" line names a **rendering tell**, not a
subject: smooth gradients, airbrush, photographic detail, fine linework,
micro-detail, more than three values, granular noise, polygon mosaics, the polished
modern AI look — and, in that same company, **"neon or rim lighting."**

So "neon" there forbids the *look*: saturated glow, bloom, halo, soft falloff, the
lit-from-within sheen of modern digital art. It does **not** forbid lit signage,
lamps, glowing instruments or electric light as subject matter. The world can have
neon in it; the painting must not be rendered like neon.

A lit sign is therefore fine when it is painted the way this style paints
everything else: flat opaque shapes with hard edges, a bright core and at most one
darker band of the same hue, no glow, no gradient, no rays. Recorded 2026-09-30
after the electric sign in `outputs/the-rusty-robot/`, where reading the ban as a
subject prohibition would have blocked a legitimate art direction.

This note sits outside the Style Block and changes none of its text, so it does not
require a style version bump.

Image 1 is STYLE: Match this image's hand-painted matte rendering technique ONLY. Ignore and do not reproduce its people, clothing, equipment, interior, setting or composition.
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v009, approved by the user. Correct except that the near ear of the sign's painted robot emblem is shaded into a 3D form.

TASK: A single 3:2 horizontal evening street scene: a domed-city cantina whose wall sign carries flat stencilled lettering reading THE RUSTY ROBOT and a flat painted robot emblem, with three travellers conferring in a dark alley opposite.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the ONE small thing below.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers confer in the shadow of a narrow left-hand alley, across from the lit door of a cantina called The Rusty Robot.

IMAGE 2 IS APPROVED AND CORRECT IN EVERY RESPECT BUT ONE TINY DETAIL. Keep absolutely everything else exactly as it is: the whole street, its perspective and framing; the sign board flat on the wall above the armoured brow with grey wall all around it and its edges parallel to the wall's horizontal lines; its chipped ivory lettering reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals; its rusted dark metal board and the hooded lamp above it; the armoured brow, the round-arched ribbed door, the steps and pipe handrail; the two angular machined lamps and their warm pools; the grey ferrocrete buildings with their muted teal painted bands and no red, rust or orange; the domed tower and stepped rooflines; the dome's ribbed underside overhead; the two distant silhouettes; the pitch-black alley behind the crew with no lights in it; the clean dry dusty paving with no rocks or rubble; all three crew at their current sizes, positions and poses, including Sion's folded arms and squared, alert stance; Graxo's wine-aubergine cape and gold collar pins; Daxus's likeness and cross patches; and every part of the lighting. Do not re-frame, do not zoom, do not move anyone, do not alter the lettering.

THE ONE CHANGE — FLATTEN THE ROBOT EMBLEM ON THE SIGN. The painted butler-robot beside the lettering is almost entirely a flat stencil, but ONE element is wrong: its NEAR EAR — the ear on the viewer's RIGHT side of its head, the one that reads as closest to us — is painted with a curved shadow inside it that rounds it into a three-dimensional form. Because everything else in the emblem is flat, that single shaded piece pops out as 3D and breaks the illusion that this is paint on a metal board.

Repaint that ear FLAT. It becomes one single solid shape of the SAME chipped ivory as the rest of the emblem, edge to edge, with NO interior shadow, NO curved shading, NO gradient, NO darker crescent along its inner edge and NO highlight. Its form is described by its OUTLINE alone.

Apply the same rule across the WHOLE emblem while you are there: the robot is a FLAT STENCIL. Its dome head, its face plate, its two round eyes, its neck, its shoulders, its bow tie and its body are all flat shapes in one uniform pale ivory, separated only by the dark board showing through between them. Nowhere in the emblem is there any modelling, rounding, shading, gradient, highlight or sense of volume. It is a sign painter's silhouette, not a rendered object.

The ONLY variation allowed within the ivory is WEAR: flat, hard-edged flecks and patches where the paint has chipped away to show the rusted metal beneath, exactly as elsewhere on the sign. Wear is not shading.

Keep the emblem at its current size and position beside the lettering, and keep the warm wash from the hooded lamp falling across the upper part of the whole board as it already does — that lamplight lies across board and emblem alike and is not the same thing as shading inside the emblem's shapes.

LIGHT AND COLOUR: unchanged from image 2 in every respect. No neon, no bloom, no halos, no lens flare, no light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
