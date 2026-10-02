# the-rusty-robot v007

User request verbatim: That looks good. Sion's stance looks weird. Her legs are too wide and she is hunched. Also, make the paint swaths on the buildings another color, not the Anatares orange.
Mode: Edit off v006, which the user approved. Two changes: (1) SION'S STANCE — feet brought in to roughly hip-width from a wide straddle, weight settled onto one leg with the other knee relaxed, spine straightened and shoulders levelled and set back, with her listening turn moved into the neck rather than a forward hunch of the whole spine; her design, hands and equipment otherwise untouched. (2) PAINTED BANDS RECOLOURED from rust-red and orange to a muted dusty teal-green, with a dull olive or mustard permitted sparingly as a secondary — red, rust, orange and brick now banned outright on every wall, parapet, kerb and floor marking, because that warm family is the Antares and speeder livery and the architecture must not echo it. The grey ferrocrete itself, the sign's rusted board and ivory lettering, and the amber door lamps are all explicitly exempt and unchanged. Editing off v006 is safe here, unlike the earlier passes, because the baseline no longer contains the sign error that was being inherited.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f4aa-2c9f-7d00-a82a-d54431c24e82/exec-ca3f5d29-46a2-4cf2-aca3-7f4d8996a94d.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v006/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.32 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Both changes landed. SION'S STANCE: her feet are now roughly hip-width rather than splayed in a wide straddle, her weight settles onto one leg with the other knee relaxed, her spine is straight and her shoulders level and set back, and her listening turn sits in the neck rather than a forward hunch of the whole spine. Her design is otherwise untouched: ochre jacket with the left sleeve absent, black shirt, slim teal neck scarf, opaque ruby goggles, bare steel-grey left cyber arm, and her natural hand still pocketed with no pointing gesture. PAINTED BANDS RECOLOURED: every painted marking on the architecture — the horizontal bands along walls and parapets, the stripes at door surrounds, and the lines on the ground — is now a muted dusty teal-green, faded and chipped. No red, rust, orange or brick remains on any wall, parapet, kerb or floor marking, so the architecture no longer echoes the Antares and speeder livery. The cool teal against the warm amber lamplight also reads more clearly as paint on concrete than the warm bands did. Correctly exempted and unchanged: the grey ferrocrete itself, which remains the street's dominant colour; the sign's rusted dark board with its chipped ivory lettering and painted robot emblem; and the two amber door lamps. Everything else held from v006: the sign flat on the wall with its edges parallel to the wall's horizontal lines and grey wall visible all around it, reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals, lit only by its hooded lamp and emitting nothing; the armoured brow, arched ribbed door, steps and handrail; the angular machined lamps with flat downward panels; the domed tower; the dome's ribbed underside overhead; the two distant silhouettes; the left alley; only Graxo caped, in deep wine aubergine with both gold collar pins; Daxus's likeness and cross patches. File is 2.32 MB, inside the 2.5 MB book-float budget. DISCREPANCY raised by the user and not yet addressed: loose ROCKS AND RUBBLE are scattered across the street and the steps, which makes no sense inside a sealed dome where no weather or erosion reaches. Dust and dirt are plausible; broken stone is not. Also still outstanding from earlier: the crew are lit at close to full value rather than as dark masses in the alley shadow.

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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v006, approved by the user. Its street, grey ferrocrete buildings, corrected wall-mounted sign, angular lamps and alley are all correct. Change only Sion's stance and the colour of the painted bands.
Image 3 is IDENTITY: The approved CREW LINEUP — Daxus left, Graxo centre, Sion right. Copy their faces, builds, hair, clothing and equipment. Ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce NONE of its printed numbers or any other text.

TASK: A single 3:2 horizontal evening street scene: three travellers conferring in a narrow alley across from a grey ferrocrete cantina marked with muted teal painted bands, its wall sign reading THE RUSTY ROBOT.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the two things below. Image 3 is the approved CREW LINEUP, for the three characters' likenesses and clothing only; ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce none of its printed numbers.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers confer in the shadow of a narrow left-hand alley, across from the lit door of a dockworkers' cantina called The Rusty Robot.

KEEP FROM IMAGE 2 — UNCHANGED: the whole street, its perspective and its framing; the cantina's flat grey front wall; the SIGN exactly as it is — flat on that wall, above the armoured brow, with grey wall visible all around it, its edges parallel to the wall's horizontal lines, painted in chipped ivory on rusted metal with the painted butler-robot emblem, lit only by the hooded lamp above it, emitting no light of its own, reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals; the massive wedge-shaped armoured brow; the deep round-arched doorway with its ribbed circular door; the steps and pipe handrail; the two ANGULAR MACHINED LAMPS with their flat downward-facing lit panels, and their warm pools of light; the weathered GREY FERROCRETE of every building; the domed tower and stepped rooflines; the DRY dusty ground with its painted floor markings and NO puddles, wet patches, sheen or reflections; the dome's ribbed underside overhead; the two distant anonymous silhouettes; the alley at the left and the crew standing in it at their current size and position; Graxo's face and his deep wine-aubergine cape with its two antique-gold collar pins; Daxus's likeness, glasses, off-white jacket and cross patches; and the warm-amber-against-cool-grey evening light. Do not re-frame, do not zoom, do not move anyone, do not touch the sign.

CHANGE ONE — FIX SION'S STANCE. In image 2 the woman on the right of the group stands badly: her feet are planted much too far apart in a wide straddle, and her back is hunched forward with her shoulders rolled and her head pushed down.

Repaint her standing NATURALLY and at ease:
- Her FEET are close together — roughly hip-width apart at most, not shoulder-width and certainly not splayed. One foot may sit slightly ahead of the other. She is standing in a narrow alley; there is no room to straddle.
- Her WEIGHT settles onto one leg, that hip taking the load, with the other knee slightly relaxed and bent — a normal, asymmetric resting stance rather than a braced, symmetrical one.
- Her BACK IS STRAIGHT and her posture upright. Her shoulders are level and settled back, not rolled forward or raised toward her ears. Her neck is long and her head sits upright on it.
- She is listening, so her head turns toward the other two and tips very slightly — but the TURN is in her neck, not a forward hunch of the whole spine. Her chest stays open and her chin does not drop toward it.
- She stays relaxed: her natural right hand remains in her pocket or hooked at her belt and her steel-grey left cyber arm hangs loosely at her side. She is not pointing, not gesturing, and her fingers stay closed and simple.

Keep every part of her design exactly as image 2 has it: ochre utility jacket with the LEFT sleeve absent at the shoulder, black shirt beneath, slim teal neck scarf with short ends and nothing trailing, opaque ruby-red goggles concealing her eyes, dark shoulder-length hair, bare steel-grey left cyber arm, charcoal cargo trousers and black boots. Only her posture changes.

CHANGE TWO — RECOLOUR THE PAINTED BANDS ON THE BUILDINGS. In image 2 the painted stripes and floor markings on the grey ferrocrete are RUST-RED and ORANGE. That is the Antares and speeder livery, and the architecture must not share it.

Repaint every one of those painted markings in a MUTED TEAL-GREEN instead: a dull, dusty blue-green, desaturated and chalky, faded and chipped as before. This applies to all of them — the horizontal bands running along the walls and parapets, the stripes around door surrounds and buttresses, the painted markings on the ground, and any painted panel blocks.

Use ONE secondary accent sparingly alongside it if a second colour is needed: a dull OLIVE or muted MUSTARD, equally faded. Nothing more.

NO RED, NO RUST-RED, NO ORANGE and NO BRICK on any building, wall, parapet, kerb or floor marking anywhere in the picture. If a painted band reads warm, it is wrong. The bands are cool against the warm lamplight, which is what makes them read as paint on concrete rather than as more of the same light.

The GREY FERROCRETE of the buildings themselves is unchanged, and remains the dominant colour of the street. The sign's board keeps its rusted dark metal and chipped ivory lettering — the sign is not a painted building band and is not affected by this change. The two door lamps keep their warm amber light.

LIGHT AND COLOUR: otherwise unchanged from image 2. Warm amber at the doorway, cool slate grey shadow elsewhere, dry dusty ground. No neon, no bloom, no halos, no lens flare, no light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
