# the-rusty-robot v017

User request verbatim: Not just the scale though. The lighting, their postures. v5 was perfect except for the sign.
Mode: Edit off v016, closing the two remaining gaps against v005 that the user named. v016 fixed the scale but is cooler and dimmer than v005, with a small warm pool and most of the street in flat cool grey, and its huddle is compressed into a stiff clump. (1) LIGHT warmed and spread: the door lamps throw further, flooding the full flight of steps and well out across the foreground paving, the cantina wall bathed in warm ochre-gold, the overall key moved warmer and the cool shadow confined to upper walls, alley and far lane — all still painted as flat opaque warm areas with no glow, bloom or rays. (2) POSTURES loosened from the compressed block back toward v005's natural conferring arrangement: still close with overlapping silhouettes but with air between heads and varied individual stances, Daxus leaning easily from the waist, Graxo upright and inclined, Sion turned in with her compact across-the-body point and the corrected hand anatomy preserved. Camera, scale, sign geometry, grey-and-teal buildings, angular lamps, clean paving and black alley all frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f4ca-5ccb-7993-a696-2909042f7f61/exec-4a6f32c6-0916-4993-a97d-c727f3a0aff6.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v016/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.41 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Closest match yet to the v005 target, with the sign fixed. Checked against v005 side by side at matched scale. SCALE: the three figures now read at roughly half the frame's height, matching v005's 48 percent against v015's 61, and the cantina entrance with its full flight of steps is seen whole as one feature of a wider street rather than cropped and filling the frame. A broad sweep of paving runs across the lower third. LIGHT: warm ochre-gold now floods the full flight of steps and spills well out across the foreground paving and onto the cantina wall, with the cool slate shadow confined to the upper walls, the alley and the far end of the lane — the warm-dominant balance v005 had, where v016 was cool and dim with only a small pool. It is still painted as flat opaque warm areas with no glow, bloom or rays. POSTURES: the stiff compressed clump of v015 and v016 is gone; the three stand close with overlapping silhouettes but with air between their heads and individual stances — Daxus leaning easily at the left, Graxo upright and inclined toward the others, Sion turned in with her compact across-the-body point. Their spines stay straight. Sion's corrected hand anatomy survived: index extended alone, the other three curled into one compact fist with the thumb across the front. THE FIXES MADE SINCE v005 ALL SURVIVED THE REBUILD, which was the point of carrying them in the prompt rather than inheriting them: the sign lies flat on the wall above the brow with grey wall all around it and its edges parallel to the wall's horizontals, painted chipped ivory on rusted metal with a flat stencil emblem and no glow; the buildings are grey ferrocrete with muted teal painted bands and no red, orange or pastel; the door lamps are angular machined housings rather than lanterns; the paving is clean with no rocks or rubble; the alley interior is unlit black. Text reads exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals with no other lettering anywhere. File is 2.41 MB, inside the 2.5 MB book-float budget, at 1536x1024 exact 3:2. REMAINING DIFFERENCES FROM v005, both consequences of requested changes rather than faults: the armoured brow is smaller and less dramatic than v005's, because the sign had to come off it and onto the wall to fix the geometry, which changes how the entrance reads; and the lane is grey and teal rather than v005's pastel run of coloured facades, which the user asked for after v005. No outstanding discrepancies against the current brief.

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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v016. Its camera, scale, sign, buildings, lamps and ground are correct. Change only the warmth and spread of the light, and loosen the crew's postures.
Image 3 is IDENTITY: The approved CREW LINEUP — Daxus left, Graxo centre, Sion right. Copy their faces, builds, hair, clothing and equipment. Ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce NONE of its printed numbers or any other text.

TASK: A single 3:2 horizontal evening street shot, warmly lit: a grey ferrocrete cantina with its full flight of steps bathed in golden lamplight under a wall sign reading THE RUSTY ROBOT, three travellers conferring naturally at the alley mouth beside it.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the two things below. Image 3 is the approved CREW LINEUP, for the characters' likenesses and clothing only; ignore its plain background, poses, layout and height chart, and reproduce none of its printed numbers.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers confer at the mouth of a narrow alley, across the lane from the lit door of a cantina called The Rusty Robot.

KEEP FROM IMAGE 2 — UNCHANGED: the CAMERA AND SCALE exactly as they are, with the three figures at about half the frame's height, the cantina entrance and its full flight of steps seen whole and uncropped, and a broad sweep of paving across the lower third; the SIGN flat on the wall above the armoured brow with grey wall all around it, its edges parallel to the wall's horizontals, painted chipped ivory on rusted metal with its FLAT STENCIL robot emblem, lit only by its hooded lamp, reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals; the armoured brow, the round-arched ribbed door, the steps and pipe handrail; the two ANGULAR MACHINED LAMPS with flat downward-facing lit panels; the GREY FERROCRETE buildings with their MUTED TEAL painted bands and NO red, orange or pastel anywhere; the domed tower and stepped rooflines; the dome's ribbed underside overhead; the two distant silhouettes; the CLEAN DRY PAVING with NO rocks, rubble or gravel and NO puddles, sheen or reflections; the PITCH-BLACK alley with no lights inside it; and every item of all three characters' clothing, equipment and likeness. Do not re-frame, do not zoom, do not resize anyone, do not touch the sign, the buildings or the ground.

CHANGE ONE — MAKE THE LIGHT WARMER AND RICHER. Image 2 is too cool and too dim overall: its warm pool is small and most of the street sits in flat cool grey, so the picture reads chilly. Flood it with more warm light.

- The two door lamps throw MUCH MORE light and throw it FURTHER. Their warm ochre pools spill generously down the whole flight of steps, across the landing, and well out over the paving of the lane in front of the cantina, reaching most of the way across the foreground.
- The cantina's own wall around and above the doorway is bathed in that warm light, its grey ferrocrete glowing a rich warm ochre-gold where the light falls, with the colour strongest near the lamps and fading gradually outward.
- The warm light also reaches the crew at the alley mouth and the lower part of the buildings opposite, so a large portion of the picture carries warmth rather than just a small pool.
- The overall key moves WARMER: the lit areas are golden and inviting, deep and saturated rather than pale and washed out.
- The shadows stay cool slate blue-grey by contrast, but there is LESS of them — the balance shifts so warm light dominates the lower and middle of the picture and cool shadow is confined to the upper walls, the alley and the far end of the lane.
- Keep the dome overhead and the distant lane cool and dim; the contrast between the warm foreground and the cold vault above is what should carry the mood.
- Still NO neon, NO bloom, NO halos, NO lens flare and NO light rays. All of this stays painted: flat opaque areas of warm colour with hard edges, not glow.

CHANGE TWO — LOOSEN THE CREW'S POSTURES. In image 2 the three are packed into a stiff compressed clump, their heads jammed together and their bodies squeezed into one block. They should be grouped closely but NATURALLY, standing as real people do when talking.

- They still stand CLOSE, their silhouettes overlapping, as a group plainly in conversation with one another — but with a little air between their heads and a little variety in how they stand. The cluster should look relaxed and unposed, not compressed.
- DAXUS at the left stands with his weight easy, leaning in slightly from the waist and turning his head toward the others to listen, hands down.
- GRAXO at the centre stands tall and upright, his body angled toward Sion, head inclined attentively, cape hanging still.
- SION at the right turns in toward the other two, her natural RIGHT upper arm vertical at her side, elbow bent at her waist, forearm crossing horizontally in front of her torso at chest height and her hand near her opposite flank — a compact point ACROSS HER OWN BODY toward the cantina door. Her index finger is extended ALONE, with the middle, ring and little fingers curled tightly into one compact rounded fist and the thumb folded across its front: one small ball with one finger projecting, never splayed into flat parallel bars. Her steel-grey LEFT cyber arm hangs relaxed at her side.
- Vary their heights and stances naturally — Graxo tallest, Daxus broad, Sion slighter — and let each stand on their own feet rather than merging into one mass. Keep every spine straight: no hunching, no stooping and no slouching.

THEIR LIGHTING: with the warmer key they are clearly and warmly readable in the alley's shade. Daxus's jacket reads pale off-white with its red crosses legible, Sion's jacket reads warm ochre with her teal scarf teal, Graxo's cape reads a deep wine aubergine plainly purple with both antique-gold collar pins catching, and faces are clearly modelled. Sion's ruby goggles read red and her cyber arm takes a bright metallic highlight. They are in shade only relative to the doorway, which stays the brightest thing in the picture.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
