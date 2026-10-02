# the-rusty-robot v004

User request verbatim: The geomtry of the sign is still incorrect. The left side and right side are different shapes.
Mode: Edit off v003. Single change, and a corrected diagnosis: the board's perspective was not the fault — its PLACEMENT was. The board was longer than the armoured brow it is mounted on, so its left portion lay against metal while its right portion overhung the brow's edge into open air, silhouetted against the background buildings with its conduit box unsupported. One end backed by metal and the other by sky is why the two ends read as different shapes. Fix: the board is shortened so it sits wholly inside the brow's front face with a visible margin of bare metal above, below and beyond BOTH ends; nothing belonging to the sign may cross any edge of the brow or have open air behind it; both ends cut identically; all four corners on the brow's plane with edges converging on the building's vanishing point. Lettering scales down with the board but keeps the wide squared retro-futuristic face and the amber tube treatment. Everything else in the picture explicitly frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f49e-5bb2-76c1-ac76-4f7967e59b93/exec-1c1450a9-646b-479d-ac7e-b2c225b3584c.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v003/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.12 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Sign geometry resolved. The board is now shortened and sits wholly inside the armoured brow's front face, with a visible margin of bare metal above it, below it and beyond BOTH ends. Nothing belonging to the sign — board, frame, brackets, lamp or conduit — crosses any edge of the brow or has open air behind it, so no part of it is silhouetted against the background buildings or the dome. Both ends are cut identically and all four corners lie on the brow's plane with the edges converging toward the building's vanishing point. The earlier diagnosis was wrong and is worth recording: the fault was never the board's perspective, which was already reasonable, but its PLACEMENT — the board was longer than the surface it was mounted on, so its left half lay against metal while its right half overhung into open air. One end backed by metal and the other by sky is what made the two ends read as different shapes. Containing the board within its mounting surface fixed it in one pass, where two earlier attempts at "correct the perspective" had not. Everything else held: the street and its framing, the armoured brow, the arched door, the stair and railing, the paired amber door lamps, the muted 1970s building palette, the domed tower, the dry dusty ground with no puddles or reflections, the dome's ribbed underside, the two distant silhouettes, and the crew in their alley mouth. Text remains exactly "THE RUSTY ROBOT" in the wide squared retro-futuristic capitals, correctly spelled, with no other lettering anywhere. File is 2.12 MB, inside the 2.5 MB book-float budget. Superseded immediately by user direction: the neon tube treatment is to be reverted to a painted sign, the left-hand utility pod and crates are to be replaced by an alley, and the crew moved into it.

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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v003. Correct in every respect except that the sign board overhangs the armoured brow it is mounted on.

TASK: A single 3:2 horizontal evening street scene: a domed-city cantina whose lit sign reading THE RUSTY ROBOT sits wholly within the face of its armoured entrance brow, the crew conferring in an alley opposite.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the ONE thing below.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. The crew confer in an alley beside a dockworkers' cantina called The Rusty Robot.

IMAGE 2 IS CORRECT IN EVERY RESPECT BUT ONE. Keep everything else EXACTLY as it is: the whole street, its perspective and framing; the massive wedge-shaped armoured brow over the entrance; the deep round-arched doorway with its circular ribbed door; the stair and pipe railing; the two warm amber door lamps and their light pools; the muted 1970s building colours — faded teal, sage, avocado, mustard, dusty rose, cream and slate, with NO return to warm sand-and-orange; the domed tower and stepped rooflines; the grey louvred utility pod at lower left; the DRY dusty ground with NO puddles, wet patches, sheen or reflections; the dome's ribbed underside overhead; the two distant silhouettes; the crew in their alley mouth on the right; and the warm-amber-against-cool-slate light. Do not re-frame, do not zoom, do not move anyone, do not recolour anything.

THE ONE CHANGE — THE SIGN MUST SIT ENTIRELY ON THE FACE OF THE ARMOURED BROW. The fault in image 2 is not the board's perspective but its PLACEMENT: the board is too long for the surface it is mounted on. Its left portion lies against the metal brow, while its right portion overhangs past the brow's right edge and hangs in open air, silhouetted against the background buildings, with its conduit box floating clear of any structure. Because one end is backed by metal and the other is backed by sky and distant buildings, the two ends read as belonging to different objects on different planes.

Fix it by making the board SMALLER AND FULLY CONTAINED:

- SHORTEN the board so it fits comfortably INSIDE the brow's front face. It must be clearly narrower and shorter than that face.
- A visible MARGIN OF BARE METAL from the brow shows all the way around the board — above it, below it, and beyond BOTH its left and right ends. The brow's own surface frames the sign on every side.
- NO PART of the board, its frame, its mounting brackets, its lamp or its conduit may cross or overhang ANY edge of the brow. Nothing belonging to the sign is silhouetted against the background buildings, the street, the dome or the sky. If any part of the sign has open air behind it, it is wrong.
- All four of the board's corners lie flat on the brow's front face. Its top edge runs parallel to the brow's top edge and its bottom edge parallel to the brow's bottom edge, converging with them toward the same vanishing point. Its left and right ends are cut identically — the same simple vertical edge, the same thickness, the same treatment — so the two ends are plainly the same shape, one merely nearer than the other.
- The board has a small consistent thickness and casts a soft-edged shadow onto the metal behind it, so it reads as a solid plate bolted flat to the brow.

Because the board is smaller, the lettering is smaller with it. THE TEXT IS UNCHANGED and must still read exactly:

THE RUSTY ROBOT

Those three words, spelled exactly that way, in the same WIDE, EXTENDED, GEOMETRIC SQUARED CAPITALS as image 2 — straight strokes, softly rounded corners, uniform stroke weight, flat terminals, squarish counters, generous letterspacing — set as lit amber tubes on the dark rusted board, with the butler-robot emblem beside them in cooler muted teal tube. Keep the letters large enough within the board to stay clearly legible.

All of that light stays painted as FLAT OPAQUE shapes with hard edges: a bright core and at most one darker band of the same hue. No bloom, no halo, no glow, no gradient, no blur, no rays. NO OTHER TEXT ANYWHERE in the picture, and no nonsense letterforms.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
