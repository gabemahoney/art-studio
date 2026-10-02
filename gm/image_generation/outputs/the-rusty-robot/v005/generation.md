# the-rusty-robot v005

User request verbatim: Also, remove the junk to the left of the building and put the alley there. Put the characters in that alley. And remove the neon. The painting of the robot was better.
Mode: Edit off v004. Three changes: (1) SIGN REVERTED TO PAINTED — the electric tube treatment removed entirely, lettering and butler-robot emblem now flat chipped ivory paint flaking to rusted metal, emitting no light at all and visible only because the hooded lamp above washes it; this also returns the picture to full Style Block compliance, since the Block's forbidden 'neon' was only ever waived at the user's request. (2) LEFT FOREGROUND CLEARED — the grey louvred utility pod and crates deleted and replaced by a narrow alley running back between the cantina and its neighbour, its mouth opening beside the lit steps. (3) CREW RELOCATED from the right-hand side, which returns to empty street, into that left alley, set back behind its near wall, in shadow at about a quarter of frame height. Sign containment geometry, squared retro-futuristic typeface, muted 1970s palette, dry ground, dome and lighting all explicitly frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f4a0-880f-77b3-815c-d973ffedb7c9/exec-3f883eec-deb4-4c51-95b7-a043f176e78c.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v004/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.14 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: All three requested changes landed. SIGN REVERTED TO PAINT: the electric tubes are gone. The lettering and the butler-robot emblem are now flat chipped ivory paint flaking to rusted metal, emitting no light of their own, visible only because the hooded lamp above throws a hard-edged warm wash down the board's upper half. The teal tube emblem is gone and the robot reads as a painted silhouette again, which the user preferred. This also returns the picture to full Style Block compliance, since the Block's forbidden "neon" had only been waived at the user's request. LEFT FOREGROUND CLEARED: the grey louvred utility pod and the crates are deleted, and a narrow alley now runs back between the cantina and its neighbour with its mouth opening beside the lit steps. CREW RELOCATED: the three are out of the right-hand side, which is now plain empty street, and stand instead in the new left alley with its near wall at the picture edge. They huddle, heads angled in, conspiratorial, with the lit doorway beside them. Held from v004: the sign board still wholly contained within the armoured brow's face with metal margin beyond both ends and nothing overhanging; the wide squared retro-futuristic capitals; the muted 1970s building palette; the armoured brow, arched door, stair and railing; the paired amber door lamps; the dry dusty ground with no puddles or reflections; the dome's ribbed underside; the two distant silhouettes. Text remains exactly "THE RUSTY ROBOT", correctly spelled, with no other lettering anywhere and no lit signage in the lane. File is 2.14 MB, inside the 2.5 MB book-float budget. DISCREPANCIES: (1) THE SHADOW ASK IS UNDER-DELIVERED — the user asked for the crew "conferring more in the shadows", and while they are in an alley they are lit almost fully, with their jacket whites, ochres and the cape's wine all reading at close to full value rather than as dark masses caught by a thin cool rim of street spill. This is the one part of the request that did not come through. (2) SCALE: they occupy about 52 percent of the frame's height against a specified one quarter, continuing a pattern across this scene of 44 percent in v001 and 49 percent in v003; the instruction has been ignored three times and the next attempt should quantify the miss in the prompt, which is what worked for the same problem in the-ride-out. (3) The alley reads as a shallow recess rather than a deep slot running back into blackness.

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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v004. Its street, muted 1970s building colours, entrance and contained sign placement are correct. Change the sign's surface treatment, clear the left foreground for an alley, and move the crew into it.
Image 3 is IDENTITY: The approved CREW LINEUP — Daxus left, Graxo centre, Sion right. Copy their faces, builds, hair, clothing and equipment. Ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce NONE of its printed numbers or any other text.

TASK: A single 3:2 horizontal evening street scene: the crew conferring in shadow in a narrow alley at the left, beside a domed-city cantina whose painted sign reads THE RUSTY ROBOT.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the three things below. Image 3 is the approved CREW LINEUP, for the three characters' likenesses and clothing only; ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce none of its printed numbers.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. The crew of the Antares confer in the shadow of an alley beside a dockworkers' cantina called The Rusty Robot.

KEEP FROM IMAGE 2 — UNCHANGED: the street, its perspective and its framing; the massive wedge-shaped armoured brow over the entrance; the deep round-arched doorway with its circular ribbed door; the stair and pipe railing; the two warm amber door lamps and their light pools; the muted 1970s building colours — faded teal, sage, avocado, mustard, dusty rose, cream and slate, with NO return to warm sand-and-orange; the domed tower and stepped rooflines down the lane; the DRY dusty ferrocrete ground with NO puddles, wet patches, sheen or reflections; the dome's ribbed underside overhead; the two distant anonymous silhouettes; and the warm-amber-against-cool-slate evening light. Do not re-frame, do not zoom, do not recolour the buildings.

KEEP THE SIGN'S SHAPE AND PLACEMENT EXACTLY: the board stays shortened and wholly contained within the armoured brow's front face, with bare metal showing above it, below it and beyond both ends; nothing of it overhangs any edge of the brow or has open air behind it; both ends are cut identically; its edges converge with the brow's toward the same vanishing point; it keeps its thickness and cast shadow. Only its surface treatment changes, in CHANGE ONE.

CHANGE ONE — THE SIGN IS PAINTED, NOT LIT. Remove the electric tube lighting entirely. The lettering and the robot are no longer glowing tubes: they are PAINTED onto the board, the way a sign painter would have done it decades ago.

- The words are painted in flat CHIPPED IVORY — pale, matte, worn, with the paint flaked away in places to show the rusted dark metal beneath.
- The butler-robot emblem beside them is likewise PAINTED in the same chipped ivory, a flat silhouette of a rounded dome head, two round eyes and a stiff collar, worn and rust-pitted.
- There is NO glow of any kind: no tubes, no neon, no lit letters, no coloured light, no teal, no halo, no bloom, no gradient and no light spilling from the sign itself. The sign emits nothing.
- It is instead LIT FROM OUTSIDE by the small hooded lamp mounted above it, which throws a flat, hard-edged wash of warm light down across the upper part of the board and leaves the lower part in shadow. That external lamplight is the only reason the sign is visible.

THE TEXT IS UNCHANGED and must still read exactly:

THE RUSTY ROBOT

Those three words, spelled exactly that way, in the same WIDE, EXTENDED, GEOMETRIC SQUARED CAPITALS as image 2 — straight strokes, softly rounded corners, uniform stroke weight, flat terminals, squarish counters, generous letterspacing — large and clearly legible. NO OTHER TEXT ANYWHERE in the picture, and no nonsense letterforms. There is no lit signage anywhere in the lane.

CHANGE TWO — CLEAR THE LEFT FOREGROUND AND OPEN AN ALLEY THERE. Delete the grey louvred utility pod, the crates and the clutter that fill the lower left of image 2. All of it goes.

In their place, open a NARROW ALLEY at the LEFT of the picture, running back between the cantina's bulk and the building next to it. It is a tall, dark vertical slot, barely wide enough for two people abreast, its side walls sheer and close, its floor the same dry dusty ferrocrete, its far end lost in blackness. Its mouth opens onto the street in the near foreground, just left of the cantina's steps, so the alley sits immediately BESIDE the lit entrance. The near wall of the alley forms the left edge of the picture.

CHANGE THREE — PUT THE CREW IN THAT ALLEY. Remove the three crew from the right-hand side of image 2 entirely; that side of the street returns to plain buildings and empty ground, with nobody standing there.

Set the three crew instead INSIDE the new left-hand alley, a step or two back from the street line, so the alley's near wall overlaps and partly crops the nearest of them:
- They are IN SHADOW, out of the amber lamplight — dark, simplified masses, with only a thin cool edge of street spill catching a shoulder, a cheekbone, the rim of Sion's goggles, the steel of her cyber arm and the gold pins at Graxo's collar. Their colours are dimmed by the dark, not full and bright.
- They lean in close, heads angled toward one another, conspiratorial, mid-conversation, with one glancing out toward the lit doorway across from them.
- They stand about ONE QUARTER of the frame's height — small figures tucked in a slot, with the architecture towering over them. Do not enlarge them.
- Keep clear space between them and the left edge of the picture; the alley wall crops the nearest figure, not the frame.

GRAXO is tallest with his deep wine-aubergine cape hanging still, two antique-gold pins at its collar. SION is slighter, with her bare steel-grey LEFT cyber arm, opaque ruby goggles and a SLIM teal neck scarf with short ends and nothing trailing. DAXUS is broader, his off-white medical jacket the palest shape among the three. ONLY GRAXO WEARS A CAPE; neither of the others has any cape, cloak or trailing fabric.

The lit cantina entrance remains the brightest and most prominent thing in the picture; the crew are a quiet dark cluster in the slot beside it.

LIGHT AND COLOUR: otherwise unchanged from image 2, except that the sign no longer emits light. Warm amber at the doorway and from the sign's hooded lamp, cool slate blue-grey shadow everywhere else, dry dusty ground. No neon anywhere, no bloom, no halos, no lens flare, no light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
