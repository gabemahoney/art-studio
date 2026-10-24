# the-rusty-robot v021

User request verbatim: looking sooo close. Sions thumb needs to point to the cantina
Mode: Edit off v020, second attempt at the same detail. v020 rotated the thumb off vertical but left it at roughly seventy degrees, still reading as a raised thumb rather than a sideways indication. Now specified with a measurable target — the thumb within about twenty degrees of horizontal, pointing to the viewer's right along the line to the doorway, with the back of the fist turning upward as the natural consequence of that wrist rotation, and an explicit failure test that if it still looks like a thumbs-up it is wrong. Fist anatomy, arm position, shadow depth, light pool and every other element frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f564-ab6e-79a2-a56d-939b165dd1bd/exec-bcd086fc-0d17-4e39-bf94-5bce4282ca20.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v020/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.94 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Regression on the detail it was meant to fix. Instead of laying the thumb over to horizontal, this pass has largely retracted it: the hand now reads as a plain closed fist with only a small thumb nub, so it indicates nothing at all. v020 at least angled the thumb up and to the right; v021 is worse for legibility. THREE ATTEMPTS AT THE THUMB ANGLE HAVE NOW FAILED in different directions — v019 pointed it straight up as a thumbs-up, v020 reached about seventy degrees from horizontal, and v021 has shrunk it to a nub. The likely cause is scale: Sion's whole hand is roughly thirty pixels across in the finished image, and thumb ORIENTATION at that size is below the level of control this model reliably exercises, which is why each correction lands somewhere different rather than converging. Worth noting for contrast that the INDEX-FINGER point in v018 read unambiguously as indicating the cantina and was anatomically correct when verified at magnification — the extended finger gives a long, directional silhouette that survives at small scale, whereas a thumb is short and reads chiefly by its angle, which is exactly the property that is not holding. Everything else in this candidate is intact and correct: camera, framing and scale; the warm pool on the entrance and steps with its falloff; the crew's depth of shadow; the sign flat on the wall with its chipped ivory lettering and flat stencil emblem; the armoured brow, arched door, steps and handrail; angular machined lamps; grey ferrocrete with muted teal bands; domed tower, dome underside and distant silhouettes; clean dry paving; the alley recess; and all three postures and likenesses. File is 1.94 MB. RECOMMENDATION: rather than a fourth attempt at the thumb, combine the deeper shadow of v019 or v020 with the index-finger point of v018, which already communicated the gesture clearly.

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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v020. Correct in every respect except that Sion's thumb is still raised near-vertical instead of laid sideways at the cantina.

TASK: A single 3:2 horizontal evening street shot: three travellers in an alley recess, one jerking her thumb sideways at the lit door of a cantina whose wall sign reads THE RUSTY ROBOT.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the ONE tiny thing below.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers stand in the shadow of an alley recess at the LEFT, conferring. The cantina's lit doorway is across and to their RIGHT, further down the lane.

IMAGE 2 IS APPROVED AND CORRECT IN EVERY RESPECT BUT THE ANGLE OF ONE THUMB. Keep absolutely everything else exactly as it is: the camera, framing and scale; the warm pool on the entrance, doorway and steps and its falloff across the paving; the cool slate blue-grey upper walls, far lane and picture edges; the crew's DEPTH OF SHADOW exactly as it is — do not brighten or darken them; the sign flat on the wall with its chipped ivory lettering reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals and its flat stencil robot emblem; the armoured brow, arched ribbed door, steps and pipe handrail; the angular machined lamps; the grey ferrocrete buildings with muted teal painted bands and no red, orange or pastel; the domed tower; the dome's ribbed underside; the two distant silhouettes; the clean dry paving; the alley recess with its projecting near wall and black interior; and every position, posture, garment, item of equipment and likeness of all three characters, including Sion's arm — upper arm vertical at her side, elbow bent at her waist, forearm crossing horizontally in front of her torso at chest height — and her closed fist with all four fingers curled into the palm. Do not re-frame, do not zoom, do not move or re-pose anyone, do not change any lighting.

THE ONE CHANGE — LAY SION'S THUMB DOWN FLAT, POINTING SIDEWAYS AT THE CANTINA. In image 2 her thumb still stands up at a steep angle, close to vertical, so the gesture reads as a raised thumb. It must lie over and point SIDEWAYS.

ROTATE HER WRIST so that:
- The thumb lies very close to HORIZONTAL — within about twenty degrees of level. It is NOT vertical, NOT diagonal at a steep angle, and NOT raised. If it still looks like a thumbs-up, it is wrong.
- It points to the VIEWER'S RIGHT, straight across the picture toward the cantina's lit doorway. A straight line continued from the thumb runs to that door.
- The BACK of her closed fist turns to face roughly UPWARD as a result of that rotation, with the knuckles on top, which is what happens naturally when a thumb is laid over sideways.
- The thumb stays SHORT, BLUNT and STUBBY — clearly a thumb, thicker and shorter than a finger.
- All four fingers stay curled into the palm as ONE compact rounded mass. Nothing else projects from the hand.
- Keep the whole hand to TWO flat shapes: a rounded mass for the fist, and a short wedge laid sideways for the thumb.

Think of someone jerking a thumb sideways to say "that place, right there" — the thumb laid over flat and aimed, not held up in approval.

NOTHING ELSE about Sion changes: her forearm, elbow, upper arm, shoulders, head, face, expression and her relaxed steel-grey left cyber arm are all exactly as in image 2. Only the wrist rotates and the thumb lies down.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
