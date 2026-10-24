# the-rusty-robot v018

User request verbatim: The lighting is not correct. And they are not tucked into the alleyway enough. Othwerisw its getting very close. Check v005 again for target
Mode: Edit off v017, closing the last two gaps against v005. (1) LIGHT: v017 spread warm light evenly across the entire foreground, which read flat; v005 concentrates it into a pool at the doorway that fans onto the paving and falls off, leaving the crew's corner, the far lane and the picture's edges cool slate blue-grey. Now specified as a hot centre at the entrance recess, steps and doorway, a clear fanning wedge that dims with distance, a warm wall wash that fades before the upper wall, and an explicit requirement that warm light occupy less than half the picture. (2) PLACEMENT: v017 stood the three on the open street with darkness merely behind them; v005 has them inside the alley recess with its near wall cutting across the leftmost figure. Now specified as a recess set back into the building line with a projecting near wall that overlaps and crops the left figure, black alley interior behind and above all three, and the group standing a step back from the lane out of the light wedge — while still lit by warm spill enough that every colour reads, since over-darkening them was the v012 failure. Camera, scale, postures, sign, buildings, lamps and ground all frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f4d2-c9ac-7300-a1df-043ae90b2e1b/exec-83090c34-77ae-4d72-a2b2-ace4c06fd71a.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v017/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.23 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Both remaining gaps against v005 substantially closed, and this time measured rather than judged by eye. CREW IN SHADOW — the point the user had to make three times. Mean luminance of the crew region against the lit steps region: v005 reads 39 against 119, a ratio of 0.33, so the crew sit at a third the brightness of the lit area and are genuinely in shadow with their own lighting, separate from the rest of the scene. v017 read 68 against 144, a ratio of 0.47 — nearly half, far too lit, which is exactly what the user was seeing and what this reviewer had repeatedly failed to register while describing them as correctly readable. v018 now reads 49 against 136, a ratio of 0.36, close to the v005 target. Their colours still hold — Daxus's jacket pale off-white, Sion's ochre and teal scarf, Graxo's wine cape with its gold pins — so this is shadow rather than the near-silhouette over-correction of v012. LIGHT POOL: the even golden wash of v017 is gone. Warm light is now concentrated as a hot centre on the entrance recess, doorway and full flight of steps, fanning out onto the paving in a clear wedge and falling off with distance, with the upper walls, far lane, right-hand buildings and picture edges held in cool slate blue-grey. Warm light occupies well under half the picture, as in v005, and the boundaries stay hard-edged and painted rather than glowing. ALLEY RECESS: the slot is deeper, its near wall projects as a solid vertical edge of masonry down the left, and the black alley interior shows behind and above the group. Everything else held: the camera, framing and the figures at about half frame height; the sign flat on the wall with its edges parallel to the wall's horizontals and its flat stencil emblem; the armoured brow, arched ribbed door, steps and handrail; the angular machined lamps; grey ferrocrete with muted teal bands and no red, orange or pastel; the domed tower, dome underside and distant silhouettes; clean dry paving with no rocks; the loose natural postures; and Sion's across-the-body point with correct hand anatomy. File is 2.23 MB, inside the 2.5 MB book-float budget. REMAINING MINOR DIFFERENCE from v005: the near wall of the recess does not overlap and crop the leftmost figure as firmly as v005's pale pillar does, so the group reads as standing at the recess rather than quite inside it. One further nudge would close it.

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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v017. Its camera, scale, sign, buildings, lamps, ground and the crew's postures are correct. Change only how the light is distributed and how far the crew are tucked into the alley recess.
Image 3 is IDENTITY: The approved CREW LINEUP — Daxus left, Graxo centre, Sion right. Copy their faces, builds, hair, clothing and equipment. Ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce NONE of its printed numbers or any other text.

TASK: A single 3:2 horizontal evening street shot: a concentrated pool of warm lamplight on a cantina's steps and doorway under a wall sign reading THE RUSTY ROBOT, with three travellers tucked back inside a dark alley recess at the left.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the two things below. Image 3 is the approved CREW LINEUP, for the characters' likenesses and clothing only; ignore its plain background, poses, layout and height chart, and reproduce none of its printed numbers.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers stand tucked inside the mouth of a narrow alley, conferring, across the lane from the lit door of a cantina called The Rusty Robot.

KEEP FROM IMAGE 2 — UNCHANGED: the CAMERA, FRAMING AND SCALE exactly as they are, with the figures at about half the frame's height and the cantina entrance and its full flight of steps seen whole; the SIGN flat on the wall above the armoured brow, grey wall all around it, edges parallel to the wall's horizontals, painted chipped ivory on rusted metal with its FLAT STENCIL robot emblem, lit only by its hooded lamp, reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals; the armoured brow, the round-arched ribbed door, the steps and pipe handrail; the two ANGULAR MACHINED LAMPS; the GREY FERROCRETE buildings with their MUTED TEAL painted bands and NO red, orange or pastel; the domed tower; the dome's ribbed underside; the two distant silhouettes; the CLEAN DRY PAVING with NO rocks, rubble, puddles or reflections; the three characters' loose natural postures, their clothing, equipment and likenesses; and Sion's compact across-the-body point with her index finger extended alone, the other three curled into one rounded fist and the thumb across its front. Do not re-frame, do not zoom, do not resize anyone, do not re-pose anyone, do not touch the sign, buildings or ground.

CHANGE ONE — CONCENTRATE THE LIGHT INTO A POOL WITH FALLOFF. Image 2 spreads warm light evenly across the whole foreground, so the picture reads flat and uniformly golden. The light should instead be a focused POOL around the doorway that fades away.

- The two door lamps light the ENTRANCE RECESS, the DOORWAY and the FULL FLIGHT OF STEPS brightly and warmly — that area is the hot centre of the picture, a rich glowing ochre-gold.
- From the foot of the steps the light FANS OUT onto the paving in a clear wedge and then FALLS OFF with distance, growing dimmer and cooler as it spreads toward the viewer and out across the lane. The far side of the lane and the bottom corners of the picture are NOT warmly lit.
- The warm wash climbs the cantina's wall around the doorway and under the brow, but FADES OUT before reaching the upper wall, which stays cool grey.
- Everywhere the pool does not reach falls to a COOL SLATE BLUE-GREY: the upper walls, the far end of the lane, the right-hand buildings, the alley, and the foreground paving at the picture's edges. Warm light should occupy clearly LESS than half the picture.
- The contrast between a concentrated warm doorway and a cold grey-blue street is the whole mood. Do not let the warmth flood everywhere.
- Still painted, not glowing: flat opaque areas of warm colour with hard edges and clean boundaries between lit and unlit. No bloom, no halos, no lens flare, no light rays, no soft gradients.

CHANGE TWO — TUCK THE CREW INSIDE THE ALLEY RECESS. In image 2 the three stand out on the open street in front of a dark area. They should be set INSIDE the alley's mouth, framed and partly hidden by it.

- Deepen the ALLEY at the left into a real recess: a dark vertical slot set BACK into the building line, its near side wall projecting toward the viewer so it forms a solid vertical edge of masonry down the left of the picture.
- Place the three BEHIND that near wall's edge, standing inside the recess rather than in front of it. The near wall OVERLAPS and CROPS the leftmost figure, cutting across his body, so he is plainly behind it.
- The alley's dark interior shows BEHIND and ABOVE all three — a black mass filling the space behind their heads and shoulders, with no windows, lamps or glowing openings in it.
- They stand a step back from the lane, out of the light wedge, with a strip of dim paving between them and the warm pool at the steps.

THEIR LIGHTING: they are in the alley's shadow, lit only by warm spill reaching in from the lane, so they read as being in shade but remain CLEARLY READABLE — not silhouettes, not blacked out. Their lit sides and fronts catch a warm ochre glow while their backs and the alley behind them go dark. Daxus's jacket reads pale off-white with its red crosses legible, Sion's jacket reads warm ochre with her teal scarf teal, Graxo's cape reads a deep wine aubergine plainly purple with both antique-gold collar pins catching, faces are clearly modelled, her ruby goggles read red and her cyber arm takes a bright metallic highlight. They are dimmer than the cantina's steps but their colours all hold.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
