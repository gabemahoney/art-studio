# the-rusty-robot v024

User request verbatim: Looking very good. Can we now fix the lights and the street? Also Graxo's nose is a little too long.
Mode: Edit off v023, the v005 branch. Three changes: (1) LAMPS — the carriage-style lanterns replaced with angular machined metal housings with flat downward-facing lit panels, with an explicit instruction that the light they cast must not change in position, brightness, spread or falloff, since the lighting is the part of v005 the user most wants preserved. (2) STREET — all loose rock, stones, rubble and gravel deleted from road, steps, corners and alley, as a sealed dome admits no weather to wash or blow them in, replaced with drifted dust, a little flat litter and scuffed paving, and the ground restated as a few large quiet flat planes. (3) GRAXO'S NOSE shortened by about a fifth, with his description's defining features explicitly protected — still long and clearly projecting with a broad softly rounded bulbous tip wider than its bridge, and not snub, straight, narrow, pointed or balled. Camera, lighting, crew placement and shadow, sign and building colours all frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f56e-a846-7d62-8787-415125ea279f/exec-4c702865-b608-43dc-9f8a-087829ba6d50.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v023/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.08 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: pending — record with bin/review.py once you have seen it

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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v023. Its camera, lighting, crew, sign and building colours are all correct. Change only the lamp fittings, the stones on the street, and the length of Graxo's nose.
Image 3 is IDENTITY: The approved CREW LINEUP — Daxus left, Graxo centre, Sion right. Use it as the authority on Graxo's face. Ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce NONE of its printed numbers or any other text.

TASK: A single 3:2 horizontal evening street scene: the approved cantina picture with industrial downlights replacing its lanterns, its street swept clean of stones, and the lead character's nose brought into proportion.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the THREE things below. Image 3 is the approved CREW LINEUP, for the characters' likenesses only; ignore its plain background, poses, layout and height chart, and reproduce none of its printed numbers.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers stand in the shadow of an alley at the left, conferring, across from the lit door of a cantina called The Rusty Robot.

KEEP FROM IMAGE 2 — UNCHANGED: the camera, framing and composition; THE LIGHTING, meaning the warm golden pool across the entrance, steps and paving, its fan and falloff, the deep cool blue-grey shadow elsewhere, and the overall warm-against-cold balance — do not brighten, dim, spread or concentrate it; the three crew at their exact positions, sizes, postures and depth of shadow, with Graxo's cape, Sion's ochre jacket, teal scarf, ruby goggles and steel-grey cyber arm, and Daxus's off-white jacket and cross patches; the SIGN flat on the wall above the brow with wall visible around it, its edges parallel to the wall's horizontals, painted chipped ivory on rusted metal with its FLAT STENCIL robot emblem, reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals; the armoured brow, the round-arched ribbed door, the steps and handrails; the GREY FERROCRETE buildings with their MUTED TEAL painted bands and no pastel, red or orange; the domed tower, the dome overhead, the distant figures and the alley. Do not re-frame, do not zoom, do not move or re-pose anyone, do not touch the sign or the buildings.

CHANGE ONE — REPLACE THE DOOR LAMPS WITH INDUSTRIAL FIXTURES. The two lamps flanking the doorway are old-fashioned lanterns: boxy carriage lamps with glass panes in frames and decorative tops. They belong to the wrong century.

Replace each with an INDUSTRIAL, RETRO-FUTURISTIC FIXTURE: a simple ANGULAR METAL HOUSING — a squat wedge or truncated box of painted metal, hard-edged and machined, with its lit face a plain flat rectangular panel aimed DOWNWARD, mounted on a short stubby bracket against the wall. Utilitarian, like a deck light on a ship or a bulkhead lamp. There are NO glass panes in frames, NO carriage-lamp shapes, NO scrolled ironwork, NO finials, NO tapered chimneys and NO Victorian or gaslight styling anywhere.

CRITICALLY: the LIGHT THEY CAST DOES NOT CHANGE. Each fixture throws exactly the same warm golden pool, in the same place, at the same brightness and with the same spread and falloff as in image 2. Only the shape of the housing changes, not the illumination.

CHANGE TWO — CLEAR THE STREET OF STONES. The lane, the steps and the gutters are strewn with loose broken rock: angular chunks of rubble, small stones and scattered stony debris. This is a city sealed under a protective dome, where no weather, wind or erosion reaches the lanes and no rock is washed or blown in. It does not belong.

DELETE every piece of it. There are NO rocks, NO stones, NO boulders, NO rubble piles, NO gravel and NO angular debris anywhere — not on the road, not on the steps, not in the corners, not against the walls, not in the alley.

Leave the ground CLEAN AND FLAT instead: dry, dusty ferrocrete paving, pale and matte, reading as a few large quiet flat planes. What remains is only what a grubby working street would carry — fine DUST and DIRT drifted into soft pale films along the foot of the walls and into the angles of the steps, a few flat scraps of LITTER lying flat, scuffed and stained patches where traffic has worn the surface, and perhaps a thin crack drawn as a single line with no fragments lifting out of it. Keep all of it low-key and flat. The foreground should be one of the calmest, emptiest areas of the picture.

CHANGE THREE — SHORTEN GRAXO'S NOSE A LITTLE. Graxo is the tall man at the centre of the group, with the cape, the mustache and the silver-grey temples. His nose currently projects too far from his face.

Reduce its LENGTH by a modest amount — perhaps a fifth — so it sits in better proportion to his face. This is a small adjustment, not a transformation.

Everything else about his nose and face stays: it is still a LONG nose for a long face, still clearly projecting, and it still ends in a BROAD, SOFTLY ROUNDED, BULBOUS TIP that is noticeably wider than its bridge. Do NOT make it small, snub, straight, narrow or pointed, and do NOT round the tip into a ball. Keep his weathered elongated angular face, his tall forehead and loose forelock, his heavy brow and deep-set eyes, his angular cheekbones, his strong jaw with its rounded chin, his neat dark-brown mustache ending at the mouth corners, and the clearly visible silver-grey at both sides and temples. He must still be unmistakably the same man.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
