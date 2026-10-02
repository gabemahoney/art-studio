# the-rusty-robot v013

User request verbatim: [user selected v005] This one. they are dimly lit. the postures are correct.
Mode: Edit off v012. Resolves the ambiguity: the user pointed at v005 and called its crew 'dimly lit', so their sense of dim is v005's level — in shade relative to the doorway but with local colour fully readable — not the near-silhouette v012 produced when I took 'dimly lit' literally. This reviewer had been describing that same v005 treatment as 'lit at close to full value', which is what caused the mismatch. Single change: the crew are stepped forward to the alley mouth and lit back up to v005's level, with Daxus's jacket pale off-white, Sion's ochre reading yellow-brown with her teal scarf visible, Graxo's cape a readable wine aubergine with both gold pins catching, and faces clearly modelled. Poses are already the v005 poses and are held. Sion's corrected pointing hand from v011 is explicitly protected against regressing to the v005 paddle. The finished world around them — sign geometry, flat stencil emblem, angular lamps, grey-and-teal buildings, rock-free paving, unlit black alley — is frozen, since all of that was fixed after v005 and must not come back with the lighting.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f4bf-a3b2-7023-a03e-52761d76cce8/exec-ce618fc6-d55f-4525-948d-344446114827.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v012/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.21 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Crew position and light level now match the v005 treatment the user selected. The three are stepped forward to the alley mouth, level with the building front, and lit so their local colour reads: Daxus's medical jacket is a pale off-white with its red cross patches legible, Sion's utility jacket reads clearly as warm ochre with her teal scarf visible as teal, and Graxo's cape reads as a deep wine aubergine with its purple present rather than blacked out and both antique-gold collar pins catching. Faces, hair and features are modelled and readable, Sion's ruby goggles read red and her steel-grey cyber arm takes a bright metallic highlight. They remain in shade relative to the cantina doorway, which is still by far the brightest thing in the picture. This resolves a misunderstanding worth recording: the user's "dimly lit" meant this v005 level — in shade but fully readable — whereas this reviewer had repeatedly described that same treatment as "lit at close to full value" and flagged it as an unmet request, then produced a near-silhouette in v012 when the instruction was taken literally. The finished world around the crew was successfully frozen: the sign's geometry and flat stencil emblem, the angular machined lamps, the grey ferrocrete with muted teal bands and no pastel or orange, the rock-free dusty paving and the unlit black alley all survived the lighting change, none of which existed in v005. File is 2.21 MB, inside the 2.5 MB book-float budget. OUTSTANDING per the user: Sion's arm is extended outward at shoulder height into the lane, where in v005 she points ACROSS HER BODY — elbow bent, forearm crossing in front of her torso, a compact contained gesture rather than a reach. That is the version the user wants.

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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v012. Its street, sign, lamps, buildings, ground and black alley are all finished and correct. Change only where the crew stand and how brightly they are lit.
Image 3 is IDENTITY: The approved CREW LINEUP — Daxus left, Graxo centre, Sion right. Copy their faces, builds, hair, clothing and equipment. Ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce NONE of its printed numbers or any other text.

TASK: A single 3:2 horizontal evening street scene: three travellers at the mouth of a dark alley, warmly lit in its shade, one pointing across the lane at the lit door of a cantina whose wall sign reads THE RUSTY ROBOT.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the ONE thing below. Image 3 is the approved CREW LINEUP, for the characters' likenesses and clothing only; ignore its plain background, poses, layout and height chart, and reproduce none of its printed numbers.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers stand at the mouth of a narrow left-hand alley, conferring, across from the lit door of a cantina called The Rusty Robot.

KEEP FROM IMAGE 2 — ABSOLUTELY UNCHANGED. The world around the crew is finished and must not be disturbed: the whole street, its perspective and framing; the SIGN flat on the wall above the armoured brow, its edges parallel to the wall's horizontal lines, with grey wall visible all around it, chipped ivory lettering reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals, and its FLAT STENCIL robot emblem with no shading, rounding or gradient anywhere inside it; the hooded lamp above the board; the armoured brow; the round-arched ribbed door, the steps and the pipe handrail; the TWO ANGULAR MACHINED LAMPS with flat downward-facing lit panels — no lanterns, no glass panes, no ironwork — and their warm pools; the GREY FERROCRETE buildings with their MUTED TEAL painted bands and floor line, and NO red, rust, orange or pastel anywhere on the architecture; the domed tower and stepped rooflines; the dome's ribbed underside overhead; the two distant silhouettes; the CLEAN DRY DUSTY PAVING with its drifted dust and few litter scraps and absolutely NO rocks, rubble, gravel or stone debris; and the PITCH-BLACK alley interior with NO windows, lamps or glowing openings inside it. Do not re-frame, do not zoom, do not touch the sign, the buildings, the lamps or the ground.

THE ONE CHANGE — BRING THE CREW FORWARD TO THE ALLEY MOUTH AND LIGHT THEM AS THEY WERE EARLIER. In image 2 the three are set deep back inside the slot and heavily darkened, so their colours have gone out and they read as near-black masses. Move them forward and lift the light back onto them.

POSITION: step all three FORWARD to the MOUTH of the alley, level with the front of the building, standing at the edge of the lane rather than tucked back inside the slot. Being nearer, they become correspondingly LARGER in the frame again. The alley's near wall still overlaps and crops the nearest figure at the picture's left edge, and the black slot still shows behind and above them.

LIGHT LEVEL: they are in the shade of the alley, but they are CLEARLY AND WARMLY VISIBLE, not silhouetted. Their clothing reads in its own colours:
- DAXUS'S medical jacket reads as a pale off-white, plainly the lightest thing among the three, with its red cross patches legible.
- SION'S utility jacket reads as a warm OCHRE, clearly yellow-brown rather than dull grey-brown, with her slim teal neck scarf visible as teal.
- GRAXO'S cape reads as a deep WINE AUBERGINE, dark but with its purple plainly present rather than blacked out, and both antique-gold collar pins catch the light. His ivory shirt reads pale.
- Faces, hair and features are clearly modelled and readable. Sion's ruby goggles read red, and her bare steel-grey cyber arm catches a bright metallic highlight.

They sit in shadow only RELATIVE to the cantina doorway opposite, which stays by far the brightest thing in the picture. Warm spill from the lane reaches them and lifts their local colour; they are not dark silhouettes and not reduced to rim light alone.

POSES — UNCHANGED FROM IMAGE 2, these are correct: Sion turned toward the other two with her natural right arm raised and extended across her body, POINTING at the cantina's lit doorway; Graxo facing her, listening; Daxus leaning slightly in at the left. All three upright, feet close together, no hunching and no slouching.

SION'S POINTING HAND STAYS AS IMAGE 2 DRAWS IT and must not regress: the index finger extended alone, the middle, ring and little fingers curled tightly into the palm as one compact rounded fist, and the thumb folded across the front of it. The silhouette is a single small ball with one finger projecting. Do NOT splay the folded fingers into flat parallel bars alongside the index, and do not let more than one finger appear to point.

Keep every design detail: Sion's ochre jacket with the LEFT sleeve absent at the shoulder, black shirt, slim teal scarf with nothing trailing, opaque ruby goggles, bare steel-grey left cyber arm, charcoal trousers, black boots; Graxo's wine-aubergine cape with two gold collar pins, olive-charcoal vest, ivory shirt, plum ascot; Daxus's glasses, off-white jacket with red cross patches, bandolier and chest scanner. ONLY GRAXO WEARS A CAPE.

LIGHT AND COLOUR: unchanged everywhere else. No neon, no bloom, no halos, no lens flare, no light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
