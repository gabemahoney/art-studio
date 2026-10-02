# the-rusty-robot v022

User request verbatim: Can we go back to the pose from v5?
Mode: Edit off v020, abandoning the thumb experiment at the user's direction. Three attempts at thumb orientation (v019 vertical, v020 seventy degrees, v021 retracted to a nub) failed to converge, because at roughly thirty pixels across a thumb reads almost entirely by its angle and that is below this model's reliable control; an extended index finger instead gives a long directional silhouette that survives at small scale, which is why the v018 point read unambiguously. Single change: Sion's hand returns to the v005 index-finger point, specified anatomically — index extended alone as a long tapered shape aimed at the doorway, middle, ring and little curled tightly into the palm as one compact rounded mass, thumb folded across the front and explicitly not the thing pointing, with a two-or-three-shape budget and the failure test that more than one apparent pointing finger is wrong. Arm position, crew shadow depth, light pool, sign, buildings, lamps, ground, alley recess and all postures frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f569-1034-7a30-b046-ee7736b55b57/exec-51509ccb-61e3-42c8-9085-3f33830f6382.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v020/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.96 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Index point restored off v020 as requested, superseded almost immediately by a change of direction: the user has decided to branch from v005 instead and fix its sign and buildings there, so this candidate is a dead end on the v016-v022 line rather than a step toward the final. Not evaluated in detail.

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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v020. Correct in every respect except that Sion's hand makes a thumb gesture instead of pointing with her index finger.

TASK: A single 3:2 horizontal evening street shot: three travellers in an alley recess, one pointing across her body with an extended index finger at the lit door of a cantina whose wall sign reads THE RUSTY ROBOT.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the ONE thing below.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers stand in the shadow of an alley recess at the LEFT, conferring. The cantina's lit doorway is across and to their RIGHT, further down the lane.

IMAGE 2 IS APPROVED AND CORRECT IN EVERY RESPECT BUT SION'S HAND. Keep absolutely everything else exactly as it is: the camera, framing and scale, with the figures at about half the frame's height and the cantina entrance and its full flight of steps seen whole; the concentrated warm pool on the entrance recess, doorway and steps, fanning onto the paving and falling off, with the upper walls, far lane, right-hand buildings and picture edges in cool slate blue-grey; THE CREW'S DEPTH OF SHADOW EXACTLY AS IT IS — do not brighten them and do not darken them, their colours staying just readable with only lane-facing edges catching warm spill; the sign flat on the wall above the armoured brow with grey wall all around it, its edges parallel to the wall's horizontals, painted chipped ivory on rusted metal with its FLAT STENCIL robot emblem, lit only by its hooded lamp, reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals; the armoured brow, the round-arched ribbed door, the steps and pipe handrail; the two angular machined lamps; the grey ferrocrete buildings with their muted teal painted bands and no red, orange or pastel; the domed tower; the dome's ribbed underside; the two distant silhouettes; the clean dry paving with no rocks, rubble, puddles or reflections; the alley recess with its projecting near wall and black interior; and all three characters' positions, postures, clothing, equipment and likenesses — including Sion's ARM exactly where it is: upper arm vertical against her side, elbow bent at her waist, forearm crossing horizontally in front of her torso at chest height, hand near the middle of her chest. Do not re-frame, do not zoom, do not move or re-pose anyone, do not change any lighting.

THE ONE CHANGE — SION POINTS WITH HER INDEX FINGER AGAIN. In image 2 her hand is a closed fist with a thumb gesture, which does not read as indicating anything. Replace it with a clear pointing hand.

Her hand now POINTS WITH THE INDEX FINGER across her own body toward the cantina's lit doorway:

- The INDEX FINGER is fully EXTENDED, straight and clearly separate, projecting from the hand as a long slender tapered shape aimed to the viewer's RIGHT at the doorway. A straight line continued along that finger runs to the cantina's door.
- The MIDDLE, RING and LITTLE fingers are CURLED DOWN AND IN, folded tightly against the palm so their tips touch it, forming ONE compact rounded mass beneath the extended index — a small closed fist, with their knuckles reading as a simple curved ridge.
- Those three fingers do NOT lie flat, do NOT extend, do NOT fan out and do NOT run parallel to the index finger. If more than one finger appears to be pointing, it is wrong.
- The THUMB folds across the front of that closed fist, lying against the curled middle finger. It does NOT stick out and it is NOT the thing doing the pointing.
- The silhouette reads as ONE small compact ball with ONE long slender finger projecting from it, and nothing else.

Keep the whole hand to TWO OR THREE flat shapes at most: a rounded mass for the fist, one tapered shape for the extended finger, and a small mark for the thumb. Do not attempt individual articulated fingers or knuckle detail — fewer shapes read better at this size.

NOTHING ELSE about Sion changes: her forearm, elbow, upper arm, shoulders, head, face, expression, hair, goggles, scarf, jacket and her relaxed steel-grey left cyber arm are all exactly as in image 2. Only the hand changes from a fist to a pointing hand.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
