# the-rusty-robot v019

User request verbatim: can we try one version with Sion using her thumb to poing? Also, give them a little more shadows, less light
Mode: Edit off v018. Two changes: (1) SION POINTS WITH HER THUMB — arm position unchanged, but the hand becomes a loose closed fist with all four fingers curled into the palm and the thumb alone projecting, short and blunt, cocked toward the doorway; specified as a two-shape silhouette, one rounded ball plus one short wedge, with an explicit test that anything long and slender projecting is wrong. This is a simpler shape than the index point and should fail less. (2) CREW DEEPER INTO SHADOW — measured luminance of the crew region against the lit steps is 0.36 in v018 against 0.33 in v005, and the user wants them darker still, so values drop a further step or two with only lane-facing edges catching spill. Guarded explicitly against the v012 over-correction, which blacked them out and lost all hue: each colour must stay identifiable — Daxus's jacket a dim warm grey still lightest of the three, Sion's a deep muted brown-gold still reading ochre, Graxo's cape a very dark purple with its wine hue just perceptible, faces dim but features discernible. The cantina's own lighting is explicitly frozen so only the crew and their recess darken and the contrast grows.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f55f-06d0-7071-a458-c3b7b6bdcd77/exec-a6d2db3b-d32a-44b6-9a9e-857152c0c993.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v018/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.09 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Both changes landed. THUMB GESTURE, verified at 560 percent: her hand is a closed fist with all four fingers curled into the palm as one rounded mass and the thumb alone projecting as a short blunt shape. No finger extends. The silhouette is one ball with one stubby projection, exactly as specified, and it is cleaner than the index point because there is less to articulate. Her arm position is unchanged — upper arm vertical, elbow bent at the waist, forearm across her torso at chest height. One small observation: the thumb cocks upward and slightly back rather than angling clearly toward the cantina doorway, so it reads as a thumb gesture more than as an unmistakable indication of that building. SHADOW, measured as mean luminance of the crew region against the lit steps region: v019 comes in at 0.28, against 0.36 in v018 and 0.33 in v005. The crew are now in genuinely deeper shade than v018 and their colours survive the drop as required — Daxus's jacket reads a dim pale grey and is still the lightest of the three, Sion's jacket still reads ochre rather than grey with her scarf a dark teal, Graxo's cape is a very dark wine purple rather than flat black, and faces remain discernible. This is shadow rather than the v012 silhouette failure. NOTE ON THE TARGET: the user has since said to use v005 as the reference for the shadows, and v005 measures 0.33 — which sits BETWEEN v018 at 0.36 and this candidate at 0.28. Neither existing version matches it exactly; v019 is modestly darker than v005 and v018 modestly lighter. Landing precisely on the v005 value would need one further pass, or the user may simply prefer one of the two in hand. Everything else held: camera, framing and scale; the concentrated warm pool on the entrance, doorway and steps with its falloff across the paving; cool slate blue-grey upper walls, far lane and picture edges; the sign flat on the wall with its flat stencil emblem; the armoured brow, arched door, steps and handrail; angular machined lamps; grey ferrocrete with muted teal bands and no red, orange or pastel; domed tower, dome underside and distant silhouettes; clean dry paving with no rocks; the alley recess with its projecting near wall and black interior; and the three loose natural postures. File is 2.09 MB, inside the 2.5 MB book-float budget.

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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v018. Its camera, scale, light pool, sign, buildings, lamps, ground and alley recess are correct. Change only Sion's hand and how deeply the crew sit in shadow.
Image 3 is IDENTITY: The approved CREW LINEUP — Daxus left, Graxo centre, Sion right. Copy their faces, builds, hair, clothing and equipment. Ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce NONE of its printed numbers or any other text.

TASK: A single 3:2 horizontal evening street shot: three travellers deep in the shadow of an alley recess, one cocking a thumb toward the lit door of a cantina whose wall sign reads THE RUSTY ROBOT.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the two things below. Image 3 is the approved CREW LINEUP, for the characters' likenesses and clothing only; ignore its plain background, poses, layout and height chart, and reproduce none of its printed numbers.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers stand in the shadow of an alley recess, conferring, across the lane from the lit door of a cantina called The Rusty Robot.

KEEP FROM IMAGE 2 — UNCHANGED: the CAMERA, FRAMING AND SCALE, with the figures at about half the frame's height and the cantina entrance and its full flight of steps seen whole; the CONCENTRATED POOL of warm light on the entrance recess, doorway and steps, fanning onto the paving and falling off, with the upper walls, far lane, right-hand buildings and picture edges in cool slate blue-grey; the SIGN flat on the wall above the armoured brow with grey wall all around it, edges parallel to the wall's horizontals, painted chipped ivory on rusted metal with its FLAT STENCIL robot emblem, lit only by its hooded lamp, reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals; the armoured brow, the round-arched ribbed door, the steps and pipe handrail; the two ANGULAR MACHINED LAMPS; the GREY FERROCRETE buildings with their MUTED TEAL painted bands and NO red, orange or pastel; the domed tower; the dome's ribbed underside; the two distant silhouettes; the CLEAN DRY PAVING with NO rocks, rubble, puddles or reflections; the ALLEY RECESS with its projecting near wall and black interior; the crew's positions, their loose natural postures and all their clothing, equipment and likenesses; and GRAXO and DAXUS exactly as they are. Do not re-frame, do not zoom, do not resize or re-pose anyone, do not touch the sign, buildings, ground or the lighting of the cantina.

CHANGE ONE — SION POINTS WITH HER THUMB. In image 2 she indicates the cantina with an extended index finger. Replace that with a thumb gesture.

Her ARM stays exactly where it is: upper arm vertical against her side, elbow bent at her waist, forearm crossing horizontally in front of her torso at chest height, hand near her opposite flank. Only the HAND changes.

Her hand now makes a LOOSE CLOSED FIST with the THUMB EXTENDED, cocking it toward the cantina's doorway — the casual "that place, over there" gesture people make with a thumb.

- ALL FOUR FINGERS — index, middle, ring and little — are curled down into the palm together, forming ONE compact rounded mass. NO finger is extended. The index finger in particular must NOT stick out.
- The THUMB alone projects, held out from the side of the fist and angled toward the doorway. It is a SHORT, BLUNT, STUBBY shape — clearly a thumb, noticeably shorter and thicker than a finger would be, with a single joint.
- The silhouette is therefore ONE rounded ball with ONE short blunt projection. If anything long and slender projects from that hand, it is wrong.
- Keep the whole hand to TWO flat shapes at most: a rounded mass for the fist and a short wedge for the thumb. Do not attempt knuckle detail or individual fingers.

Her steel-grey LEFT cyber arm stays relaxed at her side. Her body, head, posture and expression are unchanged.

CHANGE TWO — PUT THE CREW DEEPER INTO SHADOW. In image 2 they are still too brightly lit for figures standing in an unlit alley recess. Darken them further.

- Drop every one of their values DOWN a clear step or two. They should read as noticeably DARKER than they do now — the dim pocket of the picture, plainly separate from the warm pool across the lane.
- Only the EDGES facing the lane catch warm spill: a rim along a shoulder, the side of a face, the front of a sleeve, Sion's goggles, her cyber arm, the gold pins at Graxo's collar. The bulk of each figure sits in deep shade.
- BUT THEIR COLOURS MUST STILL BE IDENTIFIABLE — this is shadow, not silhouette. Each hue stays recognisable, just much darker and duller:
  - DAXUS'S medical jacket becomes a DIM WARM GREY, clearly no longer white but still plainly the lightest garment of the three, with his red cross patches still discernible as dark red.
  - SION'S utility jacket becomes a DEEP MUTED BROWN-GOLD, still readable as ochre rather than grey, with her teal scarf a dark teal.
  - GRAXO'S cape becomes a VERY DARK PURPLE, almost black but with its wine hue still just perceptible.
  - Their faces are dim and shadowed, with features still discernible rather than lost.
- Do NOT flatten them into black silhouettes, do NOT lose their hues, and do NOT make them unreadable. The goal is three figures sitting in real shadow whose colours you can still name.

The cantina's doorway, steps and its warm pool stay exactly as bright as they are in image 2 — only the crew and their recess get darker, so the contrast between the lit lane and the dim alley grows.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
