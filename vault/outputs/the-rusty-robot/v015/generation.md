# the-rusty-robot v015

User request verbatim: v14 still does not have the same close huddled vibe of the characters from v5.
Mode: Edit off v014. Single change: the three closed into the tight conspiratorial huddle they have in v005, which v014 had lost by standing them abreast with background visible between their bodies. Specified concretely rather than as a mood — silhouettes overlapping so each partly occludes the next with no open gap from shoulder to hip, shoulders nearly touching, all three angled inward toward a shared centre forming a closed triangle, heads leaned in so the gap between their heads is smaller than the gap between their feet, Daxus pressing in over Graxo's shoulder, Sion's shoulder nearly against Graxo's, and the whole group on a narrower footprint. Upright spines retained so the closeness comes from proximity and inward angle rather than from stooping, avoiding a return of the hunch corrected earlier. Sion's across-the-body gesture and corrected pointing hand, the crew's position and light level, and the entire finished world are all frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f4c4-5da5-7961-a960-21a5ed9acfaf/exec-39b57cf3-2249-4045-a0e2-90d564ed7a5d.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v014/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.16 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v014. Its street, sign, lighting, crew position and Sion's gesture are all correct. Change only how closely the three stand together.
Image 3 is IDENTITY: The approved CREW LINEUP — Daxus left, Graxo centre, Sion right. Copy their faces, builds, hair, clothing and equipment. Ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce NONE of its printed numbers or any other text.

TASK: A single 3:2 horizontal evening street scene: three travellers huddled tightly together at the mouth of a dark alley, heads close, one pointing across her body at the lit door of a cantina whose wall sign reads THE RUSTY ROBOT.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the ONE thing below. Image 3 is the approved CREW LINEUP, for the characters' likenesses and clothing only; ignore its plain background, poses, layout and height chart, and reproduce none of its printed numbers.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers huddle at the mouth of a narrow left-hand alley, conferring, across from the lit door of a cantina called The Rusty Robot.

KEEP FROM IMAGE 2 — ABSOLUTELY UNCHANGED: the whole street, its perspective and framing; the SIGN flat on the wall with its chipped ivory lettering reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals and its FLAT STENCIL robot emblem with no shading inside it; the hooded lamp above the board; the armoured brow, the round-arched ribbed door, the steps and pipe handrail; the two ANGULAR MACHINED LAMPS and their warm pools; the GREY FERROCRETE buildings with their MUTED TEAL bands and NO red, orange or pastel; the domed tower; the dome's ribbed underside; the two distant silhouettes; the CLEAN DRY PAVING with NO rocks or rubble; the PITCH-BLACK alley; the crew's position at the alley mouth and their LIGHT LEVEL, with Daxus's jacket pale off-white, Sion's jacket warm ochre, her scarf teal, Graxo's cape readable wine aubergine with both gold pins catching, and faces clearly modelled; and every item of all three characters' clothing and equipment. Do not re-frame, do not zoom, do not darken anyone, do not touch the sign, buildings or ground.

KEEP SION'S GESTURE EXACTLY: her upper arm vertical against her side, elbow bent at her waist, forearm crossing horizontally in front of her torso at chest height, hand near her opposite flank, pointing across her body toward the cantina. Her index finger extended alone, the middle, ring and little fingers curled into one compact rounded fist, thumb folded across the front — one small ball with one finger projecting, with no splayed parallel bars.

THE ONE CHANGE — CLOSE THE THREE INTO A TIGHT HUDDLE. In image 2 the three stand apart from one another with clear gaps of background visible between their bodies, each squarely upright and facing slightly different ways, so they read as three separate people standing in a row. They should instead be packed together in a close, conspiratorial knot.

Bring them PHYSICALLY CLOSER until they almost touch:
- Their SILHOUETTES OVERLAP. Each figure partly occludes the one behind, so the three read as ONE compact interlocking mass rather than three separate shapes. No open gap of background shows between any two of them from shoulder to hip.
- Their SHOULDERS are nearly touching, close enough that they could put a hand on one another without reaching.
- All three ANGLE INWARD toward a shared point between them, their chests and shoulders turned toward the centre of the group rather than out toward the street or the viewer. They form a closed, inward-facing triangle.
- Their HEADS LEAN IN toward one another, brought close together at the top so the three faces are near enough to speak quietly without being overheard. The gap between their heads is smaller than the gap between their feet.
- DAXUS presses in close at the left, leaning forward over Graxo's shoulder to hear, his head low and angled in.
- GRAXO stands at the centre, inclined toward the other two.
- SION closes in from the right, her shoulder nearly against Graxo's, her head turned in toward them while her hand points across her body.
- Their FEET stay close together on the ground, the whole group occupying a NARROWER footprint than in image 2. They are standing in an alley mouth; there is no room to spread out.

The result must read instantly as three people with their heads together, sharing something they do not want overheard — tight, inward and secretive — not as three figures standing abreast.

Keep each character's own upright posture within that: straight spines, no hunching of the back, no slouching. The closeness comes from how near they stand and how they angle toward each other, not from stooping.

LIGHT AND COLOUR: unchanged in every respect. No neon, no bloom, no halos, no lens flare, no light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
