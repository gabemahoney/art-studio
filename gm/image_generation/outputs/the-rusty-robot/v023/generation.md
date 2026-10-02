# the-rusty-robot v023

User request verbatim: Honestly I still like v5 the best, Could we branch off that and try to fix the sign and buildings?
Mode: NEW BRANCH off v005 at the user's direction, abandoning the v006-v022 line. v005 is the composition, lighting, crew placement and posture the user prefers, and sixteen passes of rebuilding never fully recovered it, so the remaining faults are being fixed on v005 itself instead. Two changes only: (1) THE SIGN — moved off the canted armoured brow, where it overhung into open air and its edges never converged with anything, onto the cantina's flat front wall above the brow with wall visible all round and nothing overhanging, taking the wall's perspective so its edges run parallel to the parapet and window heads; kept painted rather than lit, with the robot emblem respecified as a flat stencil and the lettering as wide squared retro-futuristic capitals. (2) THE BUILDINGS — repainted from pastel facades to weathered grey ferrocrete with colour only as narrow muted teal painted bands, removing both the pastel blocks and the warm cream-and-orange notes that duplicated the Antares and speeder livery. Deliberately NOT touched in this pass, despite being earlier user complaints: the scattered rocks, the lantern-style door lamps, and Sion's malformed pointing hand — the point of branching from v005 is to disturb it as little as possible, and those can be layered on afterwards.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f56b-42fc-70e3-aa22-542b63d66e8c/exec-b60aeeb3-c97b-4b84-bcc0-1686df285a6f.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v005/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.24 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v005, the version the user prefers. Its camera, lighting, crew placement and postures are all correct and must be preserved. Change only the sign and the buildings' colour.

TASK: A single 3:2 horizontal evening street scene: the approved cantina picture with its signboard rebuilt flat on the wall and its pastel buildings repainted as grey ferrocrete with muted teal painted bands.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it faithfully and change only the TWO things below.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers stand in the shadow of an alley at the left, conferring, across from the lit door of a dockworkers' cantina called The Rusty Robot.

IMAGE 2 IS THE APPROVED PICTURE AND ALMOST EVERYTHING IN IT IS CORRECT. Reproduce it as closely as you can. In particular, keep ALL of the following EXACTLY as image 2 has them, unchanged in every respect:

- THE CAMERA, FRAMING AND COMPOSITION: the viewing angle, the distance, the perspective of the lane, where every element sits in the frame.
- THE LIGHTING, which is the heart of the picture: the warm golden pool thrown by the door lamps across the entrance, the steps and the paving, its fan and its falloff, the deep cool blue-grey shadow everywhere else, and the overall warm-against-cold balance. Do not brighten it, do not dim it, do not spread it or concentrate it. Match it.
- THE THREE CREW: their exact positions at the alley mouth, their sizes in the frame, their postures and the angles of their heads and limbs, the way they huddle together, and the DEPTH OF SHADOW they stand in with their colours just reading. Do not move them, do not resize them, do not re-pose them, do not relight them.
- The armoured brow over the entrance, the round-arched ribbed door, the steps and the handrails.
- The door lamps and their fittings.
- The ground, its dust, its scattered stones and debris exactly as they lie.
- The alley, the dome overhead, the distant figures, and every other element of the street.

CHANGE ONE — FIX THE SIGN. In image 2 the signboard is mounted on the slanted front face of the armoured brow, it is longer than that surface, and its right-hand portion overhangs the brow's edge and hangs in open air against the background buildings. Its edges do not agree with the perspective of anything around it, so it reads as a flat panel floating in front of the building rather than a board fixed to it.

Rebuild it:
- MOVE the board OFF the armoured brow and onto the cantina's FLAT FRONT WALL, mounting it on the wall ABOVE the brow, with clear wall visible all the way around it — above, below and beyond BOTH of its ends.
- NO part of the board, its frame, its fixings or its lamp may cross or overhang the brow or any other edge, and no part of it may have open air or background buildings behind it. Everything behind the sign is wall.
- Because it now lies flat against that wall, it takes the WALL'S perspective exactly: its top and bottom edges run PARALLEL to the wall's own horizontal lines — the parapet, the window heads, any course or band — and converge with them toward the SAME vanishing point. Its left and right ends are identical simple vertical cuts, one merely nearer than the other.
- Give it a small consistent thickness and a shadow cast onto the wall behind it, so it plainly reads as a solid plate bolted flat to the building.
- Keep it reasonably large and clearly legible, but sized so it fits comfortably within the wall with margin around it.

The sign stays PAINTED, as in image 2: a dark rusted metal board with the lettering painted on it in flat CHIPPED IVORY, pale and matte and worn, flaked in places to show rust beneath. It emits NO light — no neon, no lit tubes, no glow. A small hooded lamp above it washes its upper part with warm light.

Beside the words, keep the painted butler-robot emblem in the same chipped ivory, but paint it as a FLAT STENCIL: a silhouette of a rounded dome head, two round eyes, a stiff collar and a bow tie, with NO shading, NO rounding, NO gradient and NO sense of volume anywhere inside it. It is described by its outline alone, with flat chipping to bare rust as the only variation.

THE TEXT must read exactly:

THE RUSTY ROBOT

Those three words, spelled exactly that way, in WIDE, EXTENDED, GEOMETRIC SQUARED CAPITALS — straight strokes, softly rounded corners, uniform stroke weight, flat terminals, squarish counters, generous letterspacing, in the manner of 1970s spacecraft and station signage. Not serif, not script, not gothic, not ornate, not thin. NO OTHER TEXT ANYWHERE in the picture and no nonsense letterforms.

CHANGE TWO — RECOLOUR THE BUILDINGS. In image 2 the buildings down the lane are painted in soft PASTEL blocks — whole facades in pale green, blue, cream, salmon, yellow and red. That is wrong for this world, and the warm cream-and-orange notes among them duplicate the livery of the crew's ship and speeders.

Repaint the architecture as WEATHERED GREY FERROCRETE. Cool bone-grey, slate-grey and dust-grey — the colour of bare aged concrete — becomes the dominant colour of every building and of the whole street.

Colour then appears ONLY as PAINTED MARKINGS applied onto that grey: narrow horizontal BANDS running along parapets, door surrounds, string courses and kerbs, a stripe around a buttress, a painted panel block. Those markings are a MUTED DUSTY TEAL-GREEN — desaturated, chalky, faded and chipped — with at most a little dull olive as a secondary. They are flat, hard-edged stripes, as though guide lines were painted onto bare concrete decades ago and never refreshed.

NO building has a fully coloured facade. If a whole wall reads as green, blue, salmon, yellow, cream or red, it is wrong. There is NO RED, NO RUST-RED, NO ORANGE, NO BRICK and NO PASTEL anywhere on the architecture. The street reads GREY overall, with a few thin teal lines picking out edges and openings.

Keep the buildings' SHAPES, masses, windows, rooflines and the domed tower exactly as image 2 has them — only their colour changes. The sign's rusted board, the warm lamplight and the crew's own colours are not affected by this change.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
