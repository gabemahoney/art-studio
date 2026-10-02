# the-rusty-robot v003

User request verbatim: Also can we get more sci fi with the Rusty Robot font?
Mode: Edit off v002. Two changes: (1) TYPEFACE — the lettering redrawn as wide, extended, geometric squared capitals with softly rounded corners, uniform stroke weight, flat terminals and squarish counters, in the manner of 1970s spacecraft and station signage, with serif, script, gothic, grunge, ornate and thin faces all explicitly excluded; (2) ALLEY — v002 left the crew standing against the right-hand building faces at the side of the open street rather than inside a slot, so a real alley mouth is now specified, narrow and walled on both sides with its far end in blackness, the crew set back inside it with the near wall overlapping the closest figure. Sign geometry, tube illumination, muted 1970s building palette, dry ground, dome and lighting all explicitly frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f466-8c7b-71a1-b976-7157b9a1d8bb/exec-38e581f1-1ab8-4e20-8176-369e958a110c.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v002/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.27 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Both changes landed. TYPEFACE: the lettering is now a proper retro-futuristic face — wide, extended, geometric capitals built from straight strokes with softly rounded corners, uniform stroke weight, flat terminals and squarish counters, reading as machined hull or station signage of the 1970s rather than v002's generic blocky caps. The text is still exactly "THE RUSTY ROBOT", correctly spelled, and no other lettering appears anywhere in the picture. ALLEY: the crew are now genuinely inside an alley mouth on the right, a narrow slot between two buildings with its near wall overlapping and cropping the closest figure and its depth falling away into blackness behind them — where v002 had merely stood them against the right-hand building faces in the open street. They huddle, heads angled in, conspiratorial, with the lit doorway across the lane from them. Held from v002: the corrected sign geometry flush on the armoured brow with its edges on the building's vanishing point; the lit amber tube lettering and the teal butler-robot emblem, all painted as flat opaque shapes with no bloom, halo or rays; the muted 1970s building palette of faded teal, sage, avocado, mustard, dusty rose, cream and slate with no return to warm sand-and-orange; the armoured brow, arched door, stair and railing; the paired amber door lamps; the dry dusty ground with no puddles or reflections; the dome's ribbed underside overhead; the utility pod at lower left; the two distant silhouettes. File is 2.27 MB, inside the 2.5 MB book-float budget. DISCREPANCIES: (1) the crew occupy about 49 percent of the frame's height against a specified one quarter, and the rightmost figure runs to within roughly 36px of the right frame edge, so the group is both larger and tighter to the crop than intended — they are cropped by the picture's own edge as well as by the alley wall. (2) They are more brightly lit than the "deep shadow, thin cool edge only" the spec asked for; their colours read fairly fully rather than as dark masses with rim light. Both are worth a pass if the user wants them to recede further into the alley.

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

Image 1 is STYLE: Match this image's hand-painted matte rendering technique ONLY. Ignore and do not reproduce its people, clothing, equipment, interior, setting or composition.
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v002. Its street, muted 1970s building colours, corrected sign geometry and electric tube lighting are all correct. Change only the lettering's typeface and the crew's placement.

TASK: A single 3:2 horizontal evening street scene: the crew conferring inside a narrow alley mouth beside a domed-city cantina, its lit sign reading THE RUSTY ROBOT in wide squared retro-futuristic capitals.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the two things below.

SCENE: "The Cantina," exterior. Evening in the low-rent warrens of Kannan, a domed working-class city. The crew of the Antares confer in shadow beside a dockworkers' cantina called The Rusty Robot.

KEEP FROM IMAGE 2 — UNCHANGED: the whole street, its perspective and its framing; the massive wedge-shaped armoured brow over the entrance; the deep round-arched doorway with its circular ribbed door; the stair and pipe railing; the two warm amber door lamps and their pools of light; the muted 1970s building colours — faded teal, dusty sage and avocado, muted mustard, dusty rose, cream and slate — exactly as image 2 has them, with NO return to warm sand-and-orange; the domed tower and stepped rooflines; the grey louvred utility pod at lower left; the DRY dusty ferrocrete ground with NO puddles, wet patches, sheen or reflections; the dome's ribbed underside overhead in place of sky; the two distant anonymous silhouettes; and the warm-amber-against-cool-slate evening light. Do not re-frame, do not zoom, do not rebuild the street, do not recolour the buildings.

KEEP THE SIGN'S GEOMETRY AND ILLUMINATION: the board stays flush on the front face of the armoured brow, its edges parallel to that face and converging on the same vanishing point, with its thickness and cast shadow intact. The lettering stays LIT TUBE lettering in warm amber on the dark rusted board, with the butler-robot emblem beside it in cooler muted teal tube. All of that light stays painted as FLAT OPAQUE shapes with hard edges — no bloom, no halo, no glow, no gradient, no blur, no rays.

CHANGE ONE — GIVE THE LETTERING A SCIENCE-FICTION TYPEFACE. In image 2 the words are set in plain blocky capitals with nothing period about them. Redraw them in a RETRO-FUTURISTIC 1970s SCIENCE-FICTION LETTERFORM — the kind of lettering used on spacecraft hulls, station signage and science-fiction film logos of that era.

The letterforms are:
- WIDE and EXTENDED, noticeably broader than they are tall, with generous horizontal proportions
- GEOMETRIC and SQUARED-OFF: built from rectangles and straight strokes, with SOFTLY ROUNDED CORNERS rather than sharp points — squarish letters with rounded shoulders
- UNIFORM in stroke weight throughout, with flat horizontal terminals and no tapering
- Tight, rectangular counters — the enclosed spaces inside O, R, U and B are squarish rather than circular
- Set in CAPITALS with generous even letterspacing

It should look machined and institutional, like it was stencilled onto a hull: think of the wide squared capitals on 1970s spacecraft and space-station signage. It must NOT be a serif face, NOT a script or handwritten face, NOT gothic or blackletter, NOT a distressed grunge face, NOT ornate or decorative, and NOT a thin delicate face.

THE TEXT IS UNCHANGED and must still read exactly:

THE RUSTY ROBOT

Those three words, spelled exactly that way, in capitals, large and clearly legible as lit amber tubes. NO OTHER TEXT ANYWHERE in the picture — no additional signage, posters, notices, numbers, graffiti or labels, and no nonsense letterforms. This is the only lit sign in the lane.

CHANGE TWO — PUT THE CREW PROPERLY INTO AN ALLEY MOUTH. In image 2 the three stand against the faces of the right-hand buildings, at the side of the open street. They should instead be set back INSIDE a narrow alley.

Open a real ALLEY on the right: a tall, narrow vertical slot between two buildings, barely wide enough for two people abreast, its side walls running back into the picture and its far end lost in blackness. The alley mouth frames the crew on both sides, so there is clearly a wall between them and the street on the near side, and another behind them.

Set the three crew INSIDE that slot, a step or two back from the street line, so that the alley's near wall overlaps and partly crops the nearest of them. They stay in deep shadow: dark simplified masses with only a thin cool edge of street spill catching a shoulder, a cheekbone, the rim of Sion's goggles, the steel of her cyber arm and the gold pins at Graxo's collar. They lean in close together, heads angled toward one another, conspiratorial, with one of them glancing out toward the lit doorway. Keep them at about one quarter of the frame's height.

Only Graxo wears a cape. Sion and Daxus have no cape, cloak or trailing fabric; Sion's teal scarf is a slim neck wrap with short ends and nothing streaming.

LIGHT AND COLOUR: otherwise unchanged from image 2. Apart from the sign's own flat tube lettering, there is no other lit signage and no neon anywhere, and nothing has bloom, halos, lens flare or visible light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
