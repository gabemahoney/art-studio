# the-rusty-robot v014

User request verbatim: But I want Sion pointing the way she does in v5. across her body.
Mode: Edit off v013. Single change: Sion's pointing arm brought in from the extended shoulder-height reach of v011-v013 to the compact across-the-body gesture she has in v005 — upper arm hanging vertically against her side, elbow bent to a right angle at her waist, forearm crossing horizontally in front of her torso at chest-to-stomach height, hand finishing near her opposite flank and largely within her own silhouette, so the point reads as a quiet private indication between the three rather than a theatrical reach into the street. The corrected hand anatomy from v011 is explicitly protected against regressing to the v005 paddle. Crew position and light level, Graxo and Daxus, and the entire finished world around them are frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f4c1-b1bb-7b22-94c1-a93320971021/exec-aea06512-d459-4835-930b-e701bbd12c6e.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v013/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.18 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Gesture corrected and, in this reviewer's judgement, the scene is finished. Sion's arm is brought in from the shoulder-height reach of v011-v013 to the compact across-the-body point she has in v005: upper arm hanging vertically against her side, elbow bent at her waist, forearm crossing horizontally in front of her torso at chest height, hand finishing near her opposite flank and staying largely within her own silhouette. It reads as a quiet, private indication between the three of them rather than a theatrical gesture flung across the street, which is what the user asked for. THE HAND IS CORRECT, verified at 520 percent: the index finger extends alone, the middle, ring and little fingers are curled tightly into the palm as one compact rounded mass, and the thumb folds across the front. The silhouette is a single small ball with one finger projecting, with no splayed parallel bars and no second apparent pointing finger. This is the v005 gesture with the v005 hand fault removed — the user wanted the pose back but had separately rejected that hand, and both are now satisfied together. Everything else held exactly: the crew at the alley mouth at the v005 light level, with Daxus's jacket pale off-white and its red crosses legible, Sion's jacket warm ochre and her scarf teal, Graxo's cape a readable wine aubergine with both antique-gold collar pins catching, and all three faces clearly modelled; Graxo and Daxus in their unchanged poses; her upright posture, straight spine, level shoulders and close feet; her steel-grey left cyber arm relaxed at her side. The finished world is intact: the sign flat on the wall with its edges parallel to the wall's horizontals, chipped ivory lettering reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals, and its flat stencil robot emblem with no shading; the hooded lamp; the armoured brow, arched ribbed door, steps and handrail; the two angular machined lamps; the grey ferrocrete with muted teal bands and no red, orange or pastel; the domed tower; the dome's ribbed underside; the two distant silhouettes; the clean dry paving with no rocks; the pitch-black alley. File is 2.18 MB, inside the 2.5 MB book-float budget, at 1536x1024 exact 3:2 matching the other scene images in the book. No outstanding discrepancies. Offered for approval; promote.py must not run without the user's explicit word.

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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v013. Its street, sign, lamps, buildings, ground, alley, crew position and crew lighting are all correct. Change only Sion's pointing arm.
Image 3 is IDENTITY: The approved CREW LINEUP — Daxus left, Graxo centre, Sion right. Copy their faces, builds, hair, clothing and equipment. Ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce NONE of its printed numbers or any other text.

TASK: A single 3:2 horizontal evening street scene: three travellers at the mouth of a dark alley, the woman pointing compactly across her own body toward the lit door of a cantina whose wall sign reads THE RUSTY ROBOT.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the ONE thing below.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers stand at the mouth of a narrow left-hand alley, conferring, across from the lit door of a cantina called The Rusty Robot.

KEEP FROM IMAGE 2 — ABSOLUTELY UNCHANGED: the whole street, its perspective and framing; the SIGN flat on the wall with its chipped ivory lettering reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals and its FLAT STENCIL robot emblem with no shading inside it; the hooded lamp above the board; the armoured brow, the round-arched ribbed door, the steps and pipe handrail; the two ANGULAR MACHINED LAMPS and their warm pools; the GREY FERROCRETE buildings with their MUTED TEAL bands and NO red, orange or pastel; the domed tower; the dome's ribbed underside; the two distant silhouettes; the CLEAN DRY PAVING with NO rocks or rubble; the PITCH-BLACK alley with no lights in it; the crew's POSITION at the alley mouth and their current LIGHT LEVEL, with Daxus's jacket pale off-white, Sion's jacket warm ochre, her scarf teal, Graxo's cape readable wine aubergine with both gold pins catching, and all their faces clearly modelled; GRAXO and DAXUS exactly as they are, in their current poses; and all other lighting. Do not re-frame, do not zoom, do not darken anyone, do not move Graxo or Daxus, do not touch the sign, buildings or ground.

THE ONE CHANGE — SION POINTS ACROSS HER BODY, NOT OUT INTO THE LANE. In image 2 her right arm is raised and extended outward at about shoulder height, reaching away from her toward the doorway. That is too open and too far. Bring the whole gesture IN and DOWN so it is compact and held close to her.

The corrected arm:
- Her UPPER ARM hangs down close against her side, roughly vertical. It is NOT raised, NOT lifted to shoulder height and NOT held away from her ribs.
- Her ELBOW is bent to about a right angle, tucked in near her waist.
- Her FOREARM runs roughly HORIZONTALLY ACROSS THE FRONT OF HER TORSO, at about chest-to-stomach height, crossing her own body rather than reaching into the open air.
- Her HAND finishes near the far side of her own torso — just about at or barely past her opposite flank. The whole gesture stays close in front of her chest and belly, largely WITHIN her own silhouette.
- Her INDEX FINGER points across her body, aimed toward the cantina's doorway, but the pointing reads as a small, contained, almost private indication between the three of them — a quiet "that one, there" made close to the chest, not a broad theatrical gesture flung out across the street.

This is a subtle, understated movement. The arm does not extend, does not straighten, and does not project out beyond her body into the lane.

THE HAND MUST KEEP ITS CORRECT ANATOMY, exactly as image 2 draws it: the index finger extended alone; the middle, ring and little fingers curled tightly into the palm as ONE compact rounded fist with their knuckles reading as a simple curved ridge; the thumb folded across the front of that fist. The silhouette is one small ball with one finger projecting. Do NOT splay the folded fingers into flat parallel bars alongside the index, and do not let more than one finger appear to point. Keep the whole hand to two or three flat shapes.

Her BODY and HEAD stay as they are: turned toward Graxo and Daxus, upright with a straight spine and level shoulders, feet close together, no hunch and no slouch. Her bare steel-grey LEFT cyber arm stays relaxed at her side with its fingers loosely closed.

Keep her design exactly: ochre utility jacket with the LEFT sleeve absent at the shoulder, black shirt, slim teal neck scarf with short ends and nothing trailing, opaque ruby-red goggles, dark shoulder-length hair, charcoal cargo trousers, black boots.

LIGHT AND COLOUR: unchanged in every respect. No neon, no bloom, no halos, no lens flare, no light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
