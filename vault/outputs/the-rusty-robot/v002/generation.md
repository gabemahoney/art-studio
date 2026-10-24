# the-rusty-robot v002

User request verbatim: It looks sick! But the sign in front of the bar is not geomertrically correct at all. Also, lets put the crew to the side in an alley beside the robot, conferring more in the shadows. / Also color scheme for buildings should not be Antares orange. Can we get some 70s retro sci fi color schemes in there though? But muted. / Also, the sign should be electric or neon.
Mode: Edit off v001. Four changes: (1) SIGN GEOMETRY — v001 drew the board skewed, rotated independently of the building with edges that disagreed with its perspective, so it read as a decal; now specified as a flat rectangular board lying flush on the armoured brow's front face, its edges parallel to that face and converging on the same vanishing point, with thickness and a cast shadow, and the lettering receding with the board. (2) CREW MOVED into a narrow side alley beside the cantina, in shadow, huddled and conspiratorial, reduced to about a quarter of frame height, lit only by a thin cool edge of street spill — which also addresses v001's crew reading at 44 percent of frame height against a specified 25. (3) BUILDINGS RE-COLOURED out of the warm sand-and-ochre family, which duplicated the Antares and speeder livery, into a muted 1970s science-fiction palette of dusty avocado, faded teal, muted mustard, umber, dusty rose, cream and slate, applied as large flat panels building by building. (4) SIGN MADE ELECTRIC — lit tube lettering in warm amber with the robot emblem in muted teal. NOTE: style.md's Style Block lists neon among its forbidden traits, so this is a deliberate user-directed exception; it is mitigated by specifying the light as flat opaque shapes with at most one darker band, explicitly banning glow, bloom, halo, gradient, blur and rays, so the sign stays painted rather than photographic.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f463-fd20-7cd0-a071-0a5b869a828b/exec-420050a4-787a-4df6-aea9-b303a792f100.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v001/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.46 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: All four changes landed and this is a strong candidate. SIGN GEOMETRY FIXED: the board now lies flush on the armoured brow's front face, its top and bottom edges parallel to that face and converging on the same vanishing point as the building, with visible thickness and a cast shadow. It reads as a solid object bolted to the structure rather than v001's decal floating at its own angle, and the lettering recedes with the board instead of staying square to the viewer. ELECTRIC SIGN: the words are now lit tubes in warm amber on the dark rusted board, with the butler-robot emblem beside them picked out in a second, cooler teal tube — and crucially the light is painted as flat opaque shapes with hard edges, with no bloom, halo, gradient or rays, so it stays inside the picture's painted idiom. BUILDINGS RE-COLOURED: the warm sand-and-ochre run is gone and the lane now carries a muted 1970s palette applied building by building — faded teal, dusty sage and avocado, muted mustard, dusty rose, cream and slate, all desaturated and grimy. The architecture no longer echoes the Antares and speeder livery, which was the point. CREW MOVED: the three are now off to the right in shadow against the buildings, huddled and conferring, reduced to roughly a quarter of the frame's height, lit only by a thin cool edge with Sion's cyber arm and goggles and Graxo's collar pins catching it. Only Graxo wears a cape and Sion's teal scarf is a slim neck wrap with nothing trailing. Held from v001: the armoured brow, the deep round-arched door, the stair and railing, the paired amber door lamps, the dry dusty ground with no puddles or reflections, the dome's ribbed underside overhead, the utility pod at lower left, and the two distant silhouettes. Text is exactly "THE RUSTY ROBOT", correctly spelled, and no other lettering appears anywhere. File is 2.46 MB, inside the 2.5 MB book-float budget. DISCREPANCIES: (1) the crew stand against the right-hand building faces rather than set back inside a distinct alley mouth — they read as at the side of the street in shadow, not as tucked into a narrow slot between buildings, so the alley itself never really materialised. (2) The lettering is plain blocky capitals rather than anything period-specific; the user has since asked for a more science-fictional typeface. STYLE NOTE for the record: style.md's Style Block lists "neon or rim lighting" among its forbidden traits, and this sign is a deliberate user-directed exception. Examination of that list shows every item in it is a RENDERING tell — gradients, airbrush, photographic detail, fine linework, micro-detail, more than three values, granular noise, polygon mosaics — so "neon" there means the glow-and-bloom look, not lit signage as subject matter. Painting the tubes as flat opaque shapes satisfies the rule's intent while giving the user the electric sign they asked for.

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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v001. Its street, architecture, entrance, lighting and dry ground are correct. Change the sign's geometry and illumination, the crew's position, and the buildings' colours.
Image 3 is IDENTITY: The approved CREW LINEUP — Daxus left, Graxo centre, Sion right. Copy their faces, builds, hair, clothing and equipment. Ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce NONE of its printed numbers or any other text.

TASK: A single 3:2 horizontal evening street scene: the crew conferring in shadow in a side alley beside a domed-city cantina, its lit electric sign reading THE RUSTY ROBOT above a heavy armoured entrance, the street painted in muted 1970s colours.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no turnarounds, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the two things below. Image 3 is the approved CREW LINEUP, for the three characters' likenesses and clothing only; ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce none of its printed numbers.

SCENE: "The Cantina," exterior. Evening in the low-rent warrens of Kannan, a working-class city sealed under a dome. The crew of the Antares confer in the shadows of a side alley before going into a dockworkers' cantina called The Rusty Robot.

KEEP FROM IMAGE 2 — UNCHANGED: the whole street and its architecture; the massive wedge-shaped armoured brow cantilevered over the entrance with its panel seams and louvred vents; the deep round-arched doorway with its circular radial-ribbed door; the stair and pipe railing up to it; the two warm amber lamps flanking the door and the pools of light they throw; the SHAPES and massing of the buildings with their deep-set arched windows — their forms are correct, only their colours change, see CHANGE THREE; the domed tower and stepped rooflines down the lane; the grey louvred utility pod anchoring the left foreground; the DRY dusty ferrocrete ground with its grit, rubble and drifted dust and NO puddles, wet patches, sheen or reflections anywhere; the dome's ribbed underside arching overhead in place of sky; the two distant anonymous silhouettes far down the lane; and the warm-amber-against-cool-slate evening lighting. Do not re-frame, do not zoom, do not rebuild the street.

CHANGE ONE — FIX THE SIGN'S GEOMETRY. The signboard reading THE RUSTY ROBOT is drawn at the wrong angle: it sits skewed, as though rotated independently of the building, and its edges do not agree with the perspective of the structure it is mounted on. It reads as a sticker floating in front of the wall rather than a solid board bolted to it.

Rebuild it as a FLAT RECTANGULAR BOARD LYING TIGHT AGAINST THE FRONT FACE OF THE ARMOURED BROW, sharing that surface's perspective exactly:
- Its top and bottom edges run PARALLEL TO the top and bottom edges of the brow's front face, converging toward the SAME vanishing point as the rest of the building. Its left and right edges are parallel to each other and vertical in the building's own frame.
- In the picture it is therefore a clean four-sided shape in honest perspective — a rectangle seen at an angle — with no independent tilt, no rotation of its own, no bowing, no warping and no trapezoid that disagrees with the surfaces around it.
- It sits FLUSH on the brow's face, with a small consistent thickness and a shadow cast onto the face behind it, so it plainly has depth and is fixed to the structure.
- The lettering lies flat on the board and follows the board's perspective with it, receding at exactly the same rate. The letters do not stay square to the viewer while the board turns.

THE SIGN IS NOW AN ELECTRIC SIGN — LIT TUBE LETTERING. It is no longer a plain painted board. The words are formed from illuminated tubes mounted on the dark board, switched on and burning in the evening gloom: a period electric sign of the 1970s, a little tired, with one or two tubes dimmer than the rest and a small dark transformer box and conduit running off one end.

THE TEXT IS UNCHANGED and must still read exactly:

THE RUSTY ROBOT

Those three words, spelled exactly that way, in plain blocky capitals, large and clearly legible, formed as glowing tubes. The lit tubes are a warm pale amber-gold, sitting on a dark rusted board so the letters read clearly against it. Beside them the worn butler-robot emblem — rounded dome head, two round eyes, stiff collar — is picked out in a second, cooler tube colour, a muted teal, so the emblem reads as its own lit element.

HOW TO PAINT THE LIGHT — this matters, because it must stay in the picture's style. Paint every lit tube as a FLAT OPAQUE SHAPE of solid bright colour with hard edges: a bright core stroke, and at most ONE slightly darker flat band of the same hue immediately around it. That is all. There is NO soft glow, NO bloom, NO halo, NO corona, NO gradient, NO blur, NO feathered edge, NO transparency and NO light rays anywhere on or around the sign. It may lay ONE flat, hard-edged pool of dim amber onto the metal brow directly beneath it, and nothing more. Think of a painted poster of a lit sign, not a photograph of one.

NO OTHER TEXT ANYWHERE in the picture: no additional signage, posters, notices, numbers, graffiti or labels, and no nonsense letterforms. This is the only lit sign in the lane.

CHANGE TWO — MOVE THE CREW INTO A SIDE ALLEY, IN SHADOW. In image 2 the three crew stand out in the open street at the foot of the cantina steps, in the lamplight. Move them.

Open a NARROW ALLEY beside the cantina — a tall, dark slot between the cantina's bulk and the neighbouring building, running back into the picture. It is a gap barely wide enough for two people to pass, its walls sheer, its far end lost in darkness.

Stand the three crew INSIDE that alley mouth, set back from the street, conferring:
- They are IN SHADOW, out of the amber lamplight. Paint them mostly as dark, simplified masses, with only a thin cool edge of spill light from the street catching a shoulder, a cheekbone, the rim of Sion's goggles, the steel of her cyber arm and the gold pins at Graxo's collar. Their colours are dimmed and muted by the dark, not bright.
- They still read as themselves in silhouette and in those few lit edges: Graxo tallest with his long cape hanging still, Sion slighter with her bare steel-grey cyber arm and her slim teal neck scarf, Daxus broader with his pale jacket the lightest shape among the three.
- They lean in close together, heads angled toward one another, mid-conversation and conspiratorial — a huddle, not a line. One of them glances out toward the lit doorway.
- They are SMALLER in the frame than in image 2, about one quarter of the frame's height, tucked into their alley rather than dominating the street.

The lit cantina entrance remains the brightest and most prominent thing in the picture; the crew are a quiet dark cluster off to one side of it, watching it. The street between them and the door is open and empty.

ONLY GRAXO WEARS A CAPE. Sion and Daxus have no cape, cloak or trailing fabric of any kind; Sion's teal scarf is a slim neck wrap with short ends and nothing streaming.

CHANGE THREE — RE-COLOUR THE BUILDINGS. In image 2 the whole street is painted in warm sand, cream and ochre — the same colour family as the Antares and the crew's speeders. That makes the ship, the machines and the architecture all look like one thing. The buildings of Kannan should be their OWN world.

Repaint the architecture in a MUTED 1970s SCIENCE-FICTION PALETTE — the colours of period paperback covers and film sets, but dusty, greyed-off and worn, never bright or candy. Draw from:
- dusty AVOCADO and olive GREEN
- faded TEAL and dull aqua
- muted MUSTARD and dark harvest gold
- chocolate and burnt UMBER brown
- soft dusty ROSE and faded terracotta-salmon
- pale CREAM and bone as the neutral between them
- cool SLATE grey-blue in the shadowed masses

Apply them as LARGE FLAT PANELS OF COLOUR building by building, so the lane reads as a run of different structures painted at different times by different people: one block in a dulled avocado green, its neighbour in faded teal, another in muted mustard, another in dusty rose, with cream and slate between them. Bands, panels, door surrounds and window recesses can carry a second colour from the list. Keep every one of them DESATURATED and low-key, as though sun-faded and dust-dulled over decades, with grime settled in the corners.

CRITICALLY: the buildings must NOT be warm sand-and-orange. The cream-plus-orange-plus-rust combination belongs to the Antares and to the crew's speeders, and must not be echoed by the architecture. No building may be painted in that livery. The green, teal, mustard and rose notes are what keep the street distinct from the vehicles.

The armoured brow over the entrance stays dark grey metal, the sign stays chipped ivory on rusted dark, and the amber door lamps stay amber — those are lighting and hardware, not building colour.

LIGHT AND COLOUR: otherwise unchanged from image 2. Warm amber at the doorway, cool slate blue-grey shadow everywhere else, dry dusty ground. Apart from the sign's own flat tube lettering described above, there is no other lit signage and no neon anywhere in the picture, and nothing anywhere has bloom, halos, lens flare or visible light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
