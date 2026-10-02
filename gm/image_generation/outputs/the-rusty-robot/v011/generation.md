# the-rusty-robot v011

User request verbatim: Use the pose sion had from v005. Turning towards the team, and pointing towards the cantina.
Mode: Edit off v010. Single change: Sion re-posed from folded arms back to the v005 gesture the user preferred — torso and head turned toward Graxo and Daxus, natural right arm raised and extended across her body to point at the cantina's lit doorway, cyber arm relaxed at her side. The pointing hand is specified anatomically this time rather than banned, because the v005 failure was precise and reproducible: the folded fingers were drawn as flat parallel bars aimed the same way as the index, making the hand read as a stiff paddle. Now stated as index extended alone, middle/ring/little curled tightly to the palm forming one compact rounded fist with knuckles as a curved ridge, thumb folded across the front, and an explicit test that if more than one finger appears to point it is wrong — plus a shape budget of two or three flat shapes total, since fewer shapes fail less at this scale. Upright posture and close feet retained from v010 so neither the earlier hunch nor the later slouch returns.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f4b3-534a-7b10-807f-904d580b257a/exec-042c571a-3fd5-43eb-872c-890d9a908195.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v010/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.07 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Pose restored and the hand is right this time, verified at 500 percent. Sion's torso and head turn toward Graxo and Daxus while her natural right arm lifts and extends across her body to point at the cantina's lit doorway, with her bare steel-grey cyber arm relaxed at her side — the v005 gesture the user asked for. THE POINTING HAND IS CORRECT: the index finger extends alone, the middle, ring and little fingers are curled tightly into the palm as one compact rounded mass, and the thumb folds across the front of that fist. The silhouette reads as a single ball with one finger projecting, which is exactly the test the prompt set. This is the same gesture that failed in v005, where the folded fingers were drawn as flat parallel bars aimed the same way as the index and the hand read as a stiff paddle. What fixed it was describing the anatomy explicitly — which fingers curl, where their tips go, where the knuckles face, where the thumb lies — together with a shape budget of two or three flat shapes and an explicit failure test that more than one apparent pointing finger is wrong. Banning the gesture was the earlier workaround; specifying it properly turned out to be achievable. Her upright posture held: spine straight, shoulders level, feet close together, no hunch and no slouch. Her design is untouched. Graxo and Daxus are unchanged, as are the sign with its flat stencil emblem, the armoured brow, arched door, steps, angular lamps, grey ferrocrete with muted teal bands, domed tower, dome underside, distant silhouettes, black alley and clean dusty paving. File is 2.07 MB, inside the 2.5 MB book-float budget. OUTSTANDING and now explicitly requested by the user: the crew should be set further BACK into the alley and DIMLY LIT, as they were in v005. They currently stand close to the street line and are lit at close to full value, which is the same shadow gap flagged in every review of this scene since v005.

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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v010, approved by the user. Change only Sion's pose; everything else in it is correct.
Image 3 is IDENTITY: The approved CREW LINEUP — Daxus left, Graxo centre, Sion right. Copy their faces, builds, hair, clothing and equipment. Ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce NONE of its printed numbers or any other text.

TASK: A single 3:2 horizontal evening street scene: three travellers in a dark alley, the woman turning to the other two and pointing across the lane at the lit door of a cantina whose wall sign reads THE RUSTY ROBOT.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the ONE thing below. Image 3 is the approved CREW LINEUP, for the characters' likenesses and clothing only; ignore its plain background, poses, layout and height chart, and reproduce none of its printed numbers.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers confer in the shadow of a narrow left-hand alley, across from the lit door of a cantina called The Rusty Robot.

KEEP FROM IMAGE 2 — UNCHANGED: the whole street, its perspective and framing; the sign flat on the wall above the armoured brow, its edges parallel to the wall's horizontal lines, with its chipped ivory lettering reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals and its FLAT STENCIL robot emblem with no shading or rounding anywhere in it; the hooded lamp above the board; the armoured brow, the round-arched ribbed door, the steps and pipe handrail; the two angular machined lamps and their warm pools; the grey ferrocrete buildings with their muted teal painted bands and NO red, rust or orange; the domed tower and stepped rooflines; the dome's ribbed underside overhead; the two distant silhouettes; the PITCH-BLACK alley behind the crew with no lights in it; the clean dry dusty paving with no rocks or rubble; GRAXO and DAXUS exactly as they are, in their current positions, poses and clothing; the crew's overall size and placement; and all of the lighting. Do not re-frame, do not zoom, do not touch the sign, the ground, Graxo or Daxus.

THE ONE CHANGE — REPOSE SION: TURNING TO THE TEAM AND POINTING AT THE CANTINA. In image 2 she stands squared up with her arms folded. Replace that with an active gesture.

HER BODY AND HEAD: she TURNS TOWARD THE OTHER TWO, her torso and shoulders rotating to face Graxo and Daxus on her left, her head turned to them and her chin level. She is speaking to them, alert and businesslike. Keep her posture UPRIGHT — spine straight, shoulders level and settled, no hunching forward and no slouching. Her feet stay close together, roughly hip-width, with no wide straddle, and her weight stays balanced.

HER ARM: her natural RIGHT arm — the sleeved one, not the metal one — lifts and extends ACROSS her body to POINT toward the cantina's lit doorway on the far side of the lane. The arm is raised to about chest or shoulder height, the elbow slightly bent rather than locked straight, and the whole limb angles away from her toward the door. Her bare steel-grey LEFT cyber arm stays down and relaxed at her side, its fingers loosely closed.

HER POINTING HAND — DRAW THIS CAREFULLY. A previous attempt got this wrong by splaying the folded fingers out as flat parallel bars aimed the same way as the index finger, which made the hand read as a stiff paddle. It must be built like a real pointing hand:

- The INDEX FINGER alone is extended, straight and clearly separate, aimed at the doorway.
- The MIDDLE, RING and LITTLE fingers are CURLED DOWN AND IN, folded tightly against the palm so their tips touch it. They form a COMPACT ROUNDED MASS beneath the index finger — a small closed fist. Their knuckles face outward toward the viewer as a simple curved ridge.
- Those three fingers do NOT lie flat, do NOT extend, do NOT fan out and do NOT run parallel to the index finger. If more than one finger appears to be pointing, it is wrong.
- The THUMB folds across the front of that closed fist, lying against the curled middle finger, not sticking out.
- The silhouette therefore reads as ONE small compact ball with ONE finger projecting from it — nothing else.

At this size keep it SIMPLE: the whole hand is two or three flat shapes at most — a rounded mass for the fist, one tapered shape for the extended finger, and a small mark for the thumb. Do not attempt individual articulated fingers or knuckle detail. Fewer shapes will read better and go wrong less.

Keep her design exactly as image 2 has it: ochre utility jacket with the LEFT sleeve absent at the shoulder, black shirt beneath, slim teal neck scarf with short ends and nothing trailing, opaque ruby-red goggles concealing her eyes, dark shoulder-length hair, bare steel-grey left cyber arm, charcoal cargo trousers and black boots. Only her pose and her arms change.

LIGHT AND COLOUR: unchanged from image 2 in every respect. No neon, no bloom, no halos, no lens flare, no light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
