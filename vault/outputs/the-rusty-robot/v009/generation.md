# the-rusty-robot v009

User request verbatim: remove the lights in the alley, too. It looks like you can see building lights behind it. / Sion looks too casual now.
Mode: Edit off v008. Two changes: (1) ALLEY BLACKED OUT — the warm window lights glowing inside the slot behind the crew deleted, so nothing back there emits or reflects light and the alley reads as one large flat very dark shape with its far end featureless; the only light on the crew is now cool spill from the open lane. (2) SION RE-POSED — the earlier stance fix overshot from hunched into slouching, so she is now squared up and attentive: weight settled evenly on both feet rather than cocked onto one hip, shoulders level and squared toward the group, chin up, and her hand taken out of her pocket in favour of folded arms with the steel-grey cyber forearm resting on top. Folded arms also keep both hands closed and simple, which continues to avoid the malformed-finger problem that pointing caused. Her spine stays straight so the original hunch does not return, and her design is otherwise untouched.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f4ae-00e1-74f3-9fbf-a65911decb4b/exec-932ff642-4a21-4c01-b717-32acdd7031c4.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v008/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.12 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Both changes landed. ALLEY BLACKED OUT: the warm window lights that glowed inside the slot are gone. Behind and above the three figures the alley is now one large flat very dark mass with no windows, lit panels, lamps or glowing openings and no detail at its far end, so it reads as a dead-end slot rather than a gap with lit buildings standing in it. The only light on the crew is cool spill from the open lane. SION IS ALERT NOW: the previous correction had overshot from hunched into lounging, and she is repainted squared up and composed — weight settled evenly on both feet instead of cocked onto one hip, feet close together, shoulders level and squared toward the other two, chin up and head turned to listen with a trace of wariness. Her hand is out of her pocket and her arms are folded across her chest with the bare steel-grey cyber forearm resting on top, which reads guarded and attentive and also keeps both hands closed and simple, continuing to sidestep the malformed-finger problem that pointing caused earlier. Her spine stayed straight, so the original hunch did not return. Her design is untouched: ochre jacket with the left sleeve absent, black shirt, slim teal neck scarf, opaque ruby goggles, charcoal trousers, black boots. Everything else held: the wall-mounted sign with its edges parallel to the wall's horizontal lines, chipped ivory lettering and painted robot emblem on rusted metal, lit only by its hooded lamp, reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals; the armoured brow, arched ribbed door, steps and handrail; the angular machined lamps; the grey ferrocrete buildings with their muted teal painted bands and no red, rust or orange; the domed tower; the dome's ribbed underside; the two distant silhouettes; the clean dry dusty paving with no rocks or rubble; Graxo's wine-aubergine cape with both gold collar pins; Daxus's likeness and cross patches. File is 2.12 MB, inside the 2.5 MB book-float budget. DISCREPANCY raised by the user: on the sign's painted robot emblem, the near ear — the robot's own left, appearing on the viewer's right — carries a curved interior shadow that models it as a rounded three-dimensional form. Every other part of the emblem is a flat stencil, so that one shaded element reads as 3D against a 2D image and breaks the painted-sign illusion. Also still outstanding from earlier: the crew are lit at close to full value rather than as dark masses in the alley shadow.

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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v008, approved by the user. Correct except for the lit windows inside the alley and Sion's overly casual bearing.
Image 3 is IDENTITY: The approved CREW LINEUP — Daxus left, Graxo centre, Sion right. Copy their faces, builds, hair, clothing and equipment. Ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce NONE of its printed numbers or any other text.

TASK: A single 3:2 horizontal evening street scene: three travellers conferring against a pitch-black alley in a domed city, across from a cantina whose wall sign reads THE RUSTY ROBOT.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the two things below. Image 3 is the approved CREW LINEUP, for the characters' likenesses and clothing only; ignore its plain background, poses, layout and height chart, and reproduce none of its printed numbers.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers confer in the shadow of a narrow left-hand alley, across from the lit door of a cantina called The Rusty Robot.

KEEP FROM IMAGE 2 — UNCHANGED: the street, its perspective and framing; the SIGN exactly as it is, flat on the wall above the armoured brow with grey wall all around it, chipped ivory lettering and painted robot emblem on rusted metal, lit only by its hooded lamp, reading exactly "THE RUSTY ROBOT"; the armoured brow, the round-arched ribbed door, the steps and pipe handrail; the two angular machined lamps and their warm pools; the grey ferrocrete buildings; the muted teal-green painted bands and floor line, with no red, rust or orange on the architecture; the domed tower and stepped rooflines; the dome's ribbed underside overhead; the two distant silhouettes; the clean dry dusty paving with its drifted dust and few litter scraps and NO rocks, rubble or gravel; the alley at the left; the crew's size and positions; Graxo's face, pose and wine-aubergine cape with its two gold collar pins; Daxus's likeness, glasses, off-white jacket and cross patches; and the warm-amber-against-cool-grey light. Do not re-frame, do not zoom, do not touch the sign or the ground.

CHANGE ONE — PUT THE ALLEY INTO TOTAL DARKNESS. In image 2 small warm WINDOW LIGHTS glow inside the alley behind the crew, so the slot reads as having lit buildings standing in it. Delete every one of them.

Behind and above the three figures the alley goes SOLID BLACK. There are no windows, no lit panels, no lamps, no door lights, no glowing openings and no warm colour of any kind inside that slot — nothing back there emits or reflects light. Its side walls fall away into an unbroken dark mass, and its far end is simply blackness with no detail in it at all. Paint it as one large, flat, very dark shape.

The ONLY light touching the crew is cool spill coming in from the street behind the viewer's side, raking across them from the open lane. Nothing lights them from behind or from within the alley.

CHANGE TWO — SION IS ALERT, NOT CASUAL. In image 2 the woman on the right of the group now reads as lounging: her weight is cocked onto one hip, her hand is buried in her pocket and her whole bearing is loose and off-duty. That is wrong for a crew having a careful, covert word before walking into a place they do not trust.

Repaint her ATTENTIVE AND COMPOSED, while keeping the good posture already achieved:
- Her spine stays STRAIGHT and her shoulders level — do not return to the hunch of earlier versions.
- Her weight is now settled EVENLY on both feet, squarely and steadily, rather than slung onto one hip. Feet stay close together, roughly hip-width, with no wide straddle.
- Her shoulders are SQUARED toward the other two, her chest open, her chin level and up. She is engaged in the conversation and watchful, not slouching against anything and not leaning on a wall.
- TAKE HER HAND OUT OF HER POCKET. Instead she folds her arms across her chest — her natural right arm crossed over, her bare steel-grey left cyber forearm resting on top of it. This reads alert and guarded, and it keeps both hands closed and simple with no visible fingers to articulate.
- Her head is turned toward the other two, listening closely, with a trace of wariness rather than ease. She is not smiling and not relaxed.
- She is still NOT pointing and makes no gesture; her hands stay tucked in the fold of her arms.

Keep her design exactly as image 2 has it: ochre utility jacket with the LEFT sleeve absent at the shoulder, black shirt beneath, slim teal neck scarf with short ends and nothing trailing, opaque ruby-red goggles concealing her eyes, dark shoulder-length hair, bare steel-grey left cyber arm, charcoal cargo trousers and black boots. Only her posture and the position of her arms change.

LIGHT AND COLOUR: otherwise unchanged from image 2, except that the alley behind the crew is now unlit and black. No neon, no bloom, no halos, no lens flare, no light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
