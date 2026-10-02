# the-rusty-robot v020

User request verbatim: looking sooo close. Sions thumb needs to point to the cantina
Mode: Edit off v019. Single detail change: Sion's thumb rotated from vertical to roughly horizontal, angled to the viewer's right and slightly up and back past her shoulder so it aims squarely at the cantina doorway — v019 read as a generic thumbs-up rather than an indication. The direction is derived explicitly in the prompt from her position at the left and the doorway's position to her right and behind, with the test that a line continued from the thumb should meet the door. Fist anatomy preserved: all four fingers curled into the palm as one rounded mass, thumb the only projection, two flat shapes total. Only the wrist rotation changes — forearm, elbow, shoulders, head, body, expression and her cyber arm are all frozen, as are the crew's depth of shadow, the light pool, and every other element of the picture.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f562-9d10-7e02-9d42-a3e0df7844bf/exec-db7611c4-d9ef-4d46-af5b-3477f792bf42.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v019/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.03 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Partial. The thumb has rotated off vertical and now angles up and to the right rather than straight up, so it is no longer a plain thumbs-up, but it sits at roughly seventy degrees from horizontal and still reads more as a raised thumb than as a sideways jerk indicating the cantina. The requested direction was roughly horizontal, aimed to the viewer's right and slightly back past her shoulder along the line to the doorway. Fist anatomy is correct and unchanged: all four fingers curled into the palm as one compact rounded mass, the thumb the only projection, short and blunt. Everything else held exactly as frozen: the camera, framing and scale; the concentrated warm pool on the entrance, doorway and steps with its falloff; the crew's depth of shadow unchanged; the sign flat on the wall with its chipped ivory lettering and flat stencil emblem; the armoured brow, arched ribbed door, steps and handrail; the angular machined lamps; grey ferrocrete with muted teal bands; the domed tower, dome underside and distant silhouettes; clean dry paving; the alley recess with its projecting near wall and black interior; and all three postures, positions and likenesses. File is 2.03 MB, inside the book-float budget. Needs one further pass on the thumb angle alone.

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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v019. Correct in every respect except that Sion's thumb points upward rather than at the cantina.

TASK: A single 3:2 horizontal evening street shot: three travellers in an alley recess, one cocking her thumb sideways at the lit door of a cantina whose wall sign reads THE RUSTY ROBOT.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the ONE small thing below.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers stand in the shadow of an alley recess at the LEFT of the picture, conferring. The lit door of the cantina called The Rusty Robot is across and to their RIGHT, further along the lane.

IMAGE 2 IS APPROVED AND CORRECT IN EVERY RESPECT BUT ONE SMALL DETAIL. Keep absolutely everything else exactly as it is: the camera, framing and scale; the concentrated warm pool on the entrance recess, doorway and full flight of steps, fanning onto the paving and falling off, with the upper walls, far lane, right-hand buildings and picture edges in cool slate blue-grey; the DEPTH OF SHADOW on the crew exactly as it is now, with their colours just readable — do not brighten or darken them; the sign flat on the wall above the armoured brow with its chipped ivory lettering reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals and its FLAT STENCIL robot emblem; the armoured brow, the round-arched ribbed door, the steps and pipe handrail; the two angular machined lamps; the grey ferrocrete buildings with their muted teal painted bands and no red, orange or pastel; the domed tower; the dome's ribbed underside; the two distant silhouettes; the clean dry paving with no rocks or reflections; the alley recess with its projecting near wall and black interior; all three characters' positions, postures, clothing, equipment and likenesses; Sion's arm position — upper arm vertical at her side, elbow bent at her waist, forearm crossing horizontally in front of her torso at chest height, hand near the middle of her chest; and her closed-fist hand with all four fingers curled into the palm. Do not re-frame, do not zoom, do not move or re-pose anyone, do not change the lighting.

THE ONE CHANGE — AIM SION'S THUMB AT THE CANTINA. In image 2 her thumb sticks up and slightly backward, so the gesture reads as a generic thumbs-up rather than an indication of anything. It must clearly POINT AT THE CANTINA'S DOORWAY.

Work out the direction from the picture: Sion stands at the LEFT, turned toward her two crewmates. The cantina's lit doorway lies to the RIGHT of her and a little behind her shoulder, further down the lane. Her thumb must aim along that line.

So: ROTATE HER HAND AT THE WRIST so the thumb no longer points upward. The thumb now lies roughly HORIZONTAL, angled toward the viewer's RIGHT and slightly upward and back past her own shoulder, aimed squarely at the lit doorway across the lane. Imagine a straight line continuing from the thumb — it should run directly to the cantina's door.

- The thumb is extended from the side of the closed fist, short, blunt and stubby, clearly a thumb and not a finger.
- It is the only thing projecting from the hand. All four fingers stay curled into the palm as one compact rounded mass. No finger extends.
- The gesture should read instantly as the casual over-the-shoulder "that place, there" jerk of the thumb, not as a thumbs-up and not as a raised fist.
- Keep the whole hand to TWO flat shapes at most: a rounded mass for the fist and a short wedge for the thumb. No knuckle detail, no individual fingers.

Her forearm, elbow, upper arm, shoulders, head, body and expression all stay exactly as they are in image 2 — only the rotation of the wrist and the angle of the thumb change. Her steel-grey LEFT cyber arm stays relaxed at her side.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
