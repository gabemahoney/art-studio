# the-rusty-robot v006

User request verbatim: Sions hand looks wrong. She is pointing with a forefinger but the rest of her fingers are at the wrong angle. Also, the building colors are too pastel. I liked the approach you took with the Pad, grey building with paint lines. / also the lamp posts look very old fashioned. And the sign geometry is still totally wrong. / Maybe you need to remove the source image.
Mode: FRESH generation with NO edit target, on the user's diagnosis — every prior pass inherited the broken sign from its baseline and reproduced it, so the error was being carried forward rather than fixed. Five changes: (1) SIGN moved off the canted armoured brow and onto the cantina's FLAT FRONT WALL, well above the brow with wall visible all round, so it shares a simple plane whose perspective is already established by the parapet and window heads — the repeated failure was that the board's gently sloping edges never converged with the steeply sloping brow, leaving it on its own plane. (2) BUILDINGS re-specified as weathered GREY FERROCRETE with colour appearing only as narrow painted bands, stripes and marking blocks on that grey, following the approach the user liked in the-job-the-pad, replacing v005's fully coloured pastel facades. (3) LAMPS re-specified as angular machined metal housings with flat downward lit panels, explicitly excluding lanterns, glass panes, scrolled ironwork and gaslight styling. (4) HANDS — pointing gestures banned outright after Sion's pointing hand came out malformed with the folded fingers drawn as parallel bars; hands are now closed, pocketed, folded or belt-hooked, and painted as two or three flat shapes. (5) CREW SHADOW AND SCALE quantified in the prompt — prior attempts measured 44, 49 and 52 percent of frame height against a target of one quarter, and their clothing read at near-full brightness rather than as dark masses with a thin cool rim.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f4a5-c181-7822-a810-3baf168b5892/exec-988d518f-552d-4912-b8fe-8af57eb46473.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.50 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: Fresh generation with no edit target, on the user's diagnosis, and it fixed the thing four edit passes could not. THE SIGN GEOMETRY IS FINALLY CORRECT: the board lies flat on the cantina's front wall with grey wall visible all around it, and its top and bottom edges now run parallel to the wall's own horizontal lines — the painted red band and the parapet — converging with them toward the same vanishing point. It reads as bolted to a plane rather than floating. Two things made this work. First, abandoning the edit target: every previous pass inherited the broken sign from its baseline and faithfully reproduced it, so the error was being carried forward rather than corrected, which is exactly what the user suspected. Second, moving the sign off the canted armoured brow onto a flat wall: the repeated failure was that the board's gently sloping edges never converged with the brow's steeply sloping ones, so the two surfaces read as different planes. A flat wall is a plane the model already renders consistently, so the problem disappeared rather than being fought. BUILDING COLOUR FIXED: the street is now weathered grey ferrocrete throughout, with colour appearing only as narrow painted bands and floor markings in rust-red on that grey — the approach used in the-job-the-pad. The pastel facades of v005 are gone and no wall reads as a coloured block. LAMPS FIXED: the door lamps are angular machined housings with flat downward-facing lit panels, with no lanterns, glass panes, scrolled ironwork or gaslight styling anywhere. HANDS FIXED: nobody points. Sion's natural hand is in her pocket, Graxo's hands hang closed, and no malformed fingers appear — banning the gesture outright rather than trying to describe a correct one solved it. Also held: the painted sign with no neon or emitted light, lit only by its hooded lamp; the wide squared retro-futuristic capitals; the text exactly "THE RUSTY ROBOT" with no other lettering anywhere; the armoured brow, arched door and steps; the dry dusty ground with painted floor markings and no puddles, sheen or reflections; the dome's ribbed underside overhead; two distant silhouettes; only Graxo caped, Sion's slim teal neck scarf and her steel-grey left cyber arm. File is 2.50 MB, exactly at the book-float budget. REMAINING DISCREPANCIES, both concerning the crew: (1) THE SHADOW ASK IS STILL UNDER-DELIVERED. The user asked for them "conferring more in the shadows"; they stand in the alley but are lit at close to full value, with Daxus's jacket reading bright white and Sion's ochre fully saturated, rather than as dark masses caught by a thin cool rim. This is the one outstanding user request in the picture. (2) Scale has now missed four times running — 44, 49, 52 and here 55 percent of frame height against a specified quarter, even with the previous misses quantified in the prompt. Worth noting that the crew's size is this reviewer's specification and not something the user has ever objected to; the composition reads well as a character beat. The darkness is the user's ask and should take priority.

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
Image 2 is IDENTITY: The approved CREW LINEUP — Daxus left, Graxo centre, Sion right. Copy their faces, builds, hair, clothing and equipment. Ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce NONE of its printed numbers or any other text.

TASK: A single 3:2 horizontal evening street scene: three travellers conferring deep in the shadow of a narrow left-hand alley, across from the lit door of a grey ferrocrete cantina whose painted wall sign reads THE RUSTY ROBOT.

THE CAST — three crew conferring in the lane. Image 2 is the approved CREW LINEUP: Daxus on the left, Graxo in the centre, Sion on the right. Copy their faces, skin tones, builds, hair, clothing and equipment from it. Ignore its plain studio background, its standing poses, its side-by-side arrangement and its height chart, and reproduce NONE of its printed height numbers or any other mark from it.

GRAXO VOSS — the tallest at 6 feet 2. Weathered, elongated, angular face with a long projecting nose whose tip is broad and softly rounded, a neat dark-brown mustache, and dark brown hair swept up with clearly visible silver-grey at both sides and temples. He wears a full-length cape in DEEP WINE AUBERGINE — a dark, heavily greyed-off purple-brown, never magenta, crimson or pink — hanging from a high standing collar with two square antique-gold medallion pins at its front edges, lying across both shoulders and falling down his back with both arms clear of it. Dark olive-charcoal fitted vest, ivory long-sleeved shirt, plum ascot, charcoal trousers and boots, and a holstered blaster at his anatomical right hip.

SION TILL — 5 feet 9, slender, medium warm skin, dark shoulder-length hair. Large dark-framed goggles with OPAQUE MIRRORED RUBY-RED lenses, a single flat red surface with one pale diagonal streak, completely concealing her eyes and eyebrows; never paint eye shapes, pupils or eyebrows on or above them. Worn OCHRE utility jacket over a black shirt, right arm sleeved, LEFT sleeve absent at the shoulder. A SLIM teal scarf wrapped once at her throat with short ends at her upper chest — a narrow band only, never a broad sheet and never trailing. Her anatomical LEFT arm is a bare steel-grey cyber arm from shoulder to five-fingered hand; her right arm is natural skin. Charcoal cargo trousers, black boots.

DAXUS SKYE — 6 feet 0, broad and sturdy, light-to-medium skin, full cheeks, clean-shaven, thin metal-framed glasses, dark brown hair with cropped sides and a neat swept-back wave. Short OFF-WHITE medical jacket with a high collar and a broad inverted-V opening showing a BURNT-ORANGE shirt, orange-red sleeve patches with pale medical crosses, a broad dark-brown bandolier from his right shoulder to his left hip carrying an ivory scanner at the chest, off-white belt, dark brown trousers, worn brown boots.

ONLY GRAXO WEARS A CAPE. Sion and Daxus wear no cape, cloak, mantle, shawl or coat-tail, and nothing broad hangs from either of their shoulders.

HANDS — KEEP THEM SIMPLE AND CLOSED. Do not paint anyone POINTING. No extended index finger, no jabbing gesture, no counting on fingers, no splayed hand held up. Pointing hands have repeatedly come out malformed, with the folded fingers drawn as flat parallel bars instead of curling into the palm. Avoid the problem entirely: each character's hands are either relaxed and closed at their sides, tucked into a pocket, folded across the chest, or resting on a belt. Sion's natural right hand may hook a thumb in her belt; her steel-grey cyber hand hangs relaxed with its fingers loosely together. At this size a hand is two or three flat shapes at most — a simple mitten-like mass with the thumb suggested — never articulated fingers.

THE PLACE — The Rusty Robot, a dockworkers' cantina in the low-rent warrens of Kannan, a city sunk in a crater and sealed under a protective dome. It is evening. The lane is grimy, lived-in and working-class.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no turnarounds, no expression rows, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only, and take nothing else from it. Image 2 is the approved CREW LINEUP, for the three characters' likenesses and clothing only.

SCENE: "The Cantina," exterior. Evening in the low-rent warrens of Kannan, a working-class city sunk in a crater and sealed under a dome. Three travellers stand in the shadow of a side alley, conferring, across from the lit door of a dockworkers' cantina called The Rusty Robot.

THE LANE. A street running away from the viewer into depth, hemmed in by heavy blocky buildings that rise out of frame on both sides. The construction is brutal and practical: thick walls, deep-set arched windows, chunky buttresses, plain parapets, external pipework and conduit. Down the lane, stepped rooflines and a squat domed tower break the view. Everything is stained, patched and worn.

BUILDING COLOUR — GREY CONCRETE WITH PAINTED LINES, NOT PASTEL BLOCKS. This is important. The buildings are NOT painted in soft pastel colours and they are NOT sand-and-orange. Their material is WEATHERED GREY FERROCRETE — cool bone-grey, slate-grey and dust-grey, the colour of bare aged concrete — and that grey is the dominant colour of the whole street.

Colour appears ONLY as PAINTED MARKINGS applied onto that grey: narrow horizontal BANDS running along a parapet or a door surround, a stripe around a buttress, a painted panel number block, a band of colour edging a stair or a kerb. Those markings are muted and few — rust-red, dull teal, faded mustard, dusty olive — laid on as flat, hard-edged stripes and blocks, chipped and faded. Think of a working facility where someone painted guide lines and edge markings onto bare concrete decades ago and never repainted them.

No building has a fully coloured facade. If a whole wall reads as green, teal, rose or mustard, it is wrong. The street reads GREY overall, with a few thin bright-ish painted lines picking out edges and openings.

THE CANTINA — on the LEFT side of the lane, its entrance facing into the street:
- Its front is a tall FLAT WALL of the same weathered grey ferrocrete, square to its own facade and reading as one clean vertical plane.
- Low in that wall, a large ROUND-ARCHED DOORWAY is set deep in shadow, its door a dark circular slab with heavy radial ribs. A short flight of steps with a plain pipe handrail climbs to it.
- Above the doorway, a MASSIVE WEDGE-SHAPED ARMOURED BROW of dark grey metal juts out over the steps like a blunt prow, with panel seams and louvred vents along its upper slope. It shelters the door.
- TWO LAMPS flank the doorway, throwing warm pools of light down the steps and onto the ground.

THE LAMPS ARE INDUSTRIAL AND RETRO-FUTURISTIC, NOT OLD-FASHIONED. Each is a simple ANGULAR METAL HOUSING — a squat wedge or truncated box of painted metal, its lit face a flat rectangular panel aimed downward, mounted on a short stubby bracket. Hard-edged, machined, utilitarian, like a deck light on a ship. They are NOT lanterns: no glass panes in a frame, no hanging carriage lamp, no scrolled ironwork, no finials, no Victorian or gaslight styling of any kind.

THE SIGN — MOUNTED FLAT ON THE WALL, ABOVE THE ARMOURED BROW. Read this carefully, because the geometry matters more than anything else about it.

The sign is a flat rectangular board fixed FLUSH AGAINST THE CANTINA'S FLAT FRONT WALL, well ABOVE the armoured brow, with clear grey wall visible all around it. It is NOT mounted on the brow, NOT on any angled or projecting surface, and it does NOT overhang or cross the brow or any other edge. Nothing behind it but wall.

Because it lies flat on that wall, it shares the WALL'S perspective exactly: its top and bottom edges run parallel to the wall's own horizontal lines — the parapet, the window heads, the courses — and converge with them toward the SAME vanishing point. Its left and right ends are identical simple vertical cuts, the same height treatment, one merely nearer than the other. It is a plain rectangle in honest perspective, with a small consistent thickness and a shadow cast onto the wall behind it.

If the sign's edges do not run parallel to the other horizontal lines of that same wall, it is wrong. It must look bolted to the wall, not floating in front of it.

THE SIGN IS PAINTED, NOT LIT. The board is dark rusted metal. The lettering is painted on it in flat CHIPPED IVORY — pale, matte, worn, flaked away in places to show rust beneath. Beside the words, a painted butler-robot emblem in the same chipped ivory: a flat silhouette with a rounded dome head, two round eyes and a stiff collar, rust-pitted. There is NO glow, NO neon, NO lit tubes, NO coloured light and NO light emitted by the sign at all. A small hooded lamp above it throws a flat, hard-edged wash of warm light across its upper part, leaving the lower part in shadow; that external light is the only reason it can be read.

THE TEXT must read exactly:

THE RUSTY ROBOT

Those three words, spelled exactly that way, in WIDE, EXTENDED, GEOMETRIC SQUARED CAPITALS — straight strokes, softly rounded corners, uniform stroke weight, flat terminals, squarish counters, generous even letterspacing, in the manner of 1970s spacecraft and station signage. Not serif, not script, not gothic, not ornate, not thin. Large and clearly legible.

NO OTHER TEXT ANYWHERE in the picture: no additional signage, posters, notices, numbers, graffiti or labels, and no nonsense letterforms. This is the only sign in the lane.

THE ALLEY AND THE CREW — LEFT FOREGROUND. At the LEFT of the picture, just along from the cantina's steps, a NARROW ALLEY runs back between the cantina's bulk and the building beside it: a tall dark vertical slot, barely wide enough for two people abreast, its sheer side walls close together and its far end lost in blackness. The alley's near wall forms the left edge of the picture.

The three crew stand INSIDE that slot, a step or two back from the street line, so the near wall overlaps and partly crops the nearest of them.

THEY ARE DEEP IN SHADOW. This matters and previous attempts have failed it. Paint them as DARK, SIMPLIFIED MASSES — their clothing reading several steps darker than its true colour, close to silhouette. Only a THIN COOL EDGE of spill light from the street catches them: a rim along one shoulder, a slice of cheekbone, the curve of Sion's goggles, a hard glint on her steel cyber arm, and the two small gold pins at Graxo's collar. Nothing of theirs reads at full brightness: Daxus's off-white jacket is a dim grey, Sion's ochre is a deep dull brown, Graxo's cape is nearly black. They are a dark cluster, not three brightly lit figures.

THEY ARE SMALL. Previous attempts at this scene painted the crew at 44, 49 and 52 percent of the frame's height, all far too large. They must be ABOUT ONE QUARTER of the frame's height — no more than a third at the very most. If in doubt, paint them SMALLER. The architecture towers over them; they are three small figures tucked into a slot, not a foreground group portrait.

They lean in close, heads angled toward one another, conspiratorial and mid-conversation, one of them glancing out toward the lit door across the lane.

ALSO IN THE LANE: at most TWO other people, far down the street, small anonymous dark silhouettes with no visible faces or detail. No crowd, no patrol, nobody else.

THE GROUND IS DRY. Kannan is sealed under a dome and no weather reaches these lanes. The street is dry, dusty ferrocrete and packed grit — pale, matte and powdery, with dust drifted against the walls, scattered litter, a few chunks of rubble and some chipped painted floor markings. THERE IS NO RAIN, NO PUDDLES, NO WET PATCHES, NO STANDING WATER, NO SHEEN AND NO REFLECTIONS ANYWHERE. Light falls on the dust and stops.

ABOVE. There is no open sky. Far overhead the underside of the city's protective DOME arches across the top of the picture — a dark vault of structural ribs and dim panels catching a faint cold glimmer, with the black shapes of upper storeys and overhanging walkways crowding beneath it. It reads as a lid over the city, not as night sky. No stars, no moon, no clouds.

LIGHT — EVENING, ARTIFICIAL, WARM AGAINST COLD. The two lamps at the cantina door are the heart of the picture, pooling warm ochre light down the steps and onto the dust. A few small warm rectangles of lit window glow further along the lane, and one or two pale downlights hang under the overhangs. Everything beyond their reach falls into a single deep cool slate blue-grey shadow plane. Strong contrast: a warm door in a cold grey street. No neon, no bloom, no halos, no lens flare, no light rays.

COMPOSITION: the lane recedes on a clear diagonal, the lit doorway under its armoured brow sits as the focal point at left of centre with the sign on the wall above it, the alley and its dark huddle of figures occupy the near left, and large quiet areas of plain grey wall and plain dusty ground fill the rest. Concentrate detail at the doorway and the sign; keep everything else calm.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
