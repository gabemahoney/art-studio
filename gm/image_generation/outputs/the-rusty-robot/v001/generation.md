# the-rusty-robot v001

User request verbatim: Ok lets work on Scene 5. I want it to be an outside shot of the Rusty Robot. Dont send this in as a reference image, but analyze it yourself and turn it into the english prompt. This shot should show the characters conferring with each other before entering. Also, it should have a sign saying The Rusty Robot. / The streets shoudl not be wet though. They should be dry since the city is domed.
Mode: Fresh scene, first pass: Scene 5 exterior, The Rusty Robot. The user's photoreal reference was analysed and translated into English prose rather than attached, at their request, so its smooth rendering could not override the Style Block — the architectural read taken from it is the wedge-shaped armoured brow over a recessed round-arched door, twin flanking stair-ramps with pipe rails, paired amber door lamps, sand-plaster and grey concrete massing with deep-set arched windows and a domed tower beyond, a louvred utility pod anchoring the left foreground, and a deep receding lane. Two deliberate departures from that reference: no rain and no wet ground, because Kannan is sealed under a dome and wet streets would contradict Scenes 3, 4 and 6; and the open sky replaced by the dome's underside. Sign text 'THE RUSTY ROBOT' specified exactly with a butler-robot emblem, and all other lettering explicitly banned to prevent invented signage. Cast carried by the single approved crew lineup rather than three individual sheets, per the lesson that stacking multi-view sheets on a scene makes the model imitate the sheet format. Run on gpt-6-astra, the only model still reachable on this account.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f433-299a-72f1-bec6-e4f6b14318a7/exec-6f0f0dc3-e11d-426c-9cc0-f7f63e519eb8.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.56 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: Strong first pass. THE SIGN WORKED, verified at magnification: "THE RUSTY ROBOT" spelled exactly, in blocky chipped ivory capitals on a rusted dark metal board lit by a small lamp, with the butler-robot emblem beside it — rounded dome head, two round eyes, stiff collar, worn and rusted. No other lettering anywhere in the picture; the red shape in the upper-left corner is a painted wall marking and a pipe run, not stray text, and no nonsense letterforms appear. Banning all other signage explicitly is what kept the picture clean. ARCHITECTURE translated from the user's reference without attaching it: the massive wedge-shaped armoured brow cantilevered over the entrance with its panel seams and louvred vents, the deep round-arched doorway with a circular radial-ribbed door, the stair climbing to the door platform with pipe railing, the paired warm amber lamps flanking it, the sand-plaster and grey concrete massing with deep-set arched windows, the domed tower down the lane, and the louvred grey utility pod anchoring the left foreground. The photoreal rendering of the reference did not leak: the picture is flat, angular and matte per the Style Block. THE TWO DELIBERATE DEPARTURES BOTH HELD. The ground is dry — pale dusty ferrocrete with grit, rubble and drifted dust, with no rain, no puddles, no sheen and no reflections anywhere — correct for a city sealed under a dome. And there is no open sky: the underside of the dome arches overhead as a dark vault of structural ribs and dim panels with upper storeys crowding beneath it, reading as a lid over the city rather than as night sky. CREW: the three confer convincingly — Daxus left listening with glasses catching a gleam, Graxo centre mid-sentence with one hand raised, Sion right with arms folded and her steel-grey cyber arm on the correct anatomical side catching a highlight. Only Graxo wears a cape; Sion's teal scarf is a slim neck wrap with nothing trailing. Two anonymous silhouettes occupy the far lane and no crowd appeared. DISCREPANCIES: (1) the crew occupy about 44 percent of the frame's height against a specified one quarter, so they read as a foreground character beat rather than three small figures dwarfed by the lane; this works dramatically but is not the scale asked for, and the architecture towers less than intended. (2) Daxus's shirt reads red rather than the burnt orange his description specifies. (3) A single stair climbs to the door rather than the twin flanking stair-ramps described. (4) File is 2.56 MB, marginally over the 2.5 MB book-float budget.

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
Image 2 is IDENTITY: The approved CREW LINEUP — Daxus left, Graxo centre, Sion right. Copy their faces, skin tones, hair, clothing and equipment. Ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce NONE of its printed height numbers or any other text from it.

TASK: A single 3:2 horizontal evening street scene: the crew of the Antares conferring in a dry, dusty domed-city lane outside a dockworkers' cantina, beneath a heavy armoured entrance brow and a weathered sign reading THE RUSTY ROBOT.

THE CAST — three crew conferring in the lane. Image 2 is the approved CREW LINEUP: Daxus on the left, Graxo in the centre, Sion on the right. Copy their faces, skin tones, builds, hair, clothing and equipment from it. Ignore its plain studio background, its standing poses, its side-by-side arrangement and its height chart, and reproduce NONE of its printed height numbers or any other mark from it.

GRAXO VOSS — the tallest at 6 feet 2. Weathered, elongated, angular face with a long projecting nose whose tip is broad and softly rounded, a neat dark-brown mustache, and dark brown hair swept up with clearly visible silver-grey at both sides and temples. He wears a full-length cape in DEEP WINE AUBERGINE — a dark, heavily greyed-off purple-brown, never magenta or crimson — hanging from a high standing collar with two square antique-gold medallion pins at its front edges, lying across both shoulders and falling down his back with both arms clear of it. Dark olive-charcoal fitted vest, ivory long-sleeved shirt, plum ascot, charcoal trousers and boots, and a holstered blaster at his anatomical right hip.

SION TILL — 5 feet 9, slender, medium warm skin, dark shoulder-length hair. Large dark-framed goggles with OPAQUE MIRRORED RUBY-RED lenses, a single flat red surface with one pale diagonal streak, completely concealing her eyes and eyebrows; never paint eye shapes, pupils or eyebrows on or above them. Worn OCHRE utility jacket over a black shirt, right arm sleeved, LEFT sleeve absent at the shoulder. A SLIM teal scarf wrapped once at her throat with short ends at her upper chest — a narrow band only, never a broad sheet and never trailing. Her anatomical LEFT arm is a bare steel-grey cyber arm from shoulder to five-fingered hand; her right arm is natural skin. Charcoal cargo trousers, black boots.

DAXUS SKYE — 6 feet 0, broad and sturdy, light-to-medium skin, full cheeks, clean-shaven, thin metal-framed glasses, dark brown hair with cropped sides and a neat swept-back wave. Short OFF-WHITE medical jacket with a high collar and a broad inverted-V opening showing a BURNT-ORANGE shirt, orange-red sleeve patches with pale medical crosses, a broad dark-brown bandolier from his right shoulder to his left hip carrying an ivory scanner at the chest, off-white belt, dark brown trousers, worn brown boots.

ONLY GRAXO WEARS A CAPE. Sion and Daxus wear no cape, cloak, mantle, shawl or coat-tail, and nothing broad hangs from either of their shoulders.

THE PLACE — The Rusty Robot, a dockworkers' cantina in the low-rent warrens of Kannan, a city sunk in a crater and sealed under a protective dome. It is evening. The lane is grimy, lived-in and working-class.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no turnarounds, no expression rows, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only, and take nothing else from it. Image 2 is the approved CREW LINEUP, for the three characters' likenesses and clothing only.

SCENE: "The Cantina," exterior. Evening in the low-rent warrens of Kannan, a working-class city sunk in a crater and sealed under a protective dome. The crew of the Antares stand in a grimy back lane outside a dockworkers' cantina called The Rusty Robot, conferring quietly before they go in.

THE LANE AND THE ARCHITECTURE. A narrow street running away from the viewer into depth, hemmed in by heavy, blocky buildings that rise out of frame on both sides. The construction is brutal and practical: broad masses of sand-coloured plaster and weathered grey concrete, thick walls, small deep-set arched windows, chunky buttresses and plain parapets. Further down the lane, beyond the cantina, a squat domed tower and stepped rooflines break the skyline. Everything is stained, patched and dusty — a district that works for a living.

THE CANTINA ENTRANCE — the focal point, set on the LEFT side of the lane, roughly a third of the way in from the left edge and occupying the middle band of the picture:
- A MASSIVE WEDGE-SHAPED ARMOURED BROW of dark grey metal juts out over the doorway like a heavy blunt prow, cantilevered from the building face, with panel seams, rivet lines and a row of louvred vents along its upper slope. It is the building's signature and it dominates the entrance.
- Beneath and behind that brow, a large ROUND-ARCHED DOORWAY is set deep into the wall in shadow, its door a dark circular slab with a radial pattern of heavy ribs.
- TWO STAIR-RAMPS flank the entrance, climbing from the lane up to the door platform from left and right, with simple metal pipe railings and worn treads.
- ONE WARM AMBER LAMP is mounted on each side of the doorway, throwing a pool of warm light down the steps and across the ground below — the brightest thing at street level.

THE SIGN — REQUIRED, AND THE ONLY TEXT IN THE PICTURE. Mounted on the building face above the armoured brow, or fixed to the brow's front edge, is a battered signboard reading exactly:

THE RUSTY ROBOT

Those three words, spelled exactly that way, in plain blocky capitals, on one or two lines, large and clearly legible. The board is weathered painted metal with chipped ivory or pale letters on a dark ground, lit by a small lamp. Beside the words, a simple painted emblem of an old-fashioned butler robot's head and shoulders — a rounded dome head, two round eyes, a stiff collar — rusted and worn.

NO OTHER TEXT ANYWHERE. Do not invent any additional lettering, shop names, posters, notices, numbers, graffiti, labels, logos or background signage. Every other surface in this picture is free of writing. Do not produce scribbles or nonsense letterforms that imitate text.

THE CREW — three figures standing together in the lane at the FOOT of the stairs, in the near middle distance, just outside the amber lamplight. They are conferring: heads turned in toward one another in a loose triangle, mid-conversation, not posing and not looking at the viewer. GRAXO faces the other two with one hand raised slightly as he speaks, his cape hanging still. SION stands half-turned, arms folded, her steel-grey cyber arm catching a hard highlight. DAXUS leans in slightly, listening, glasses catching a small flat gleam. They are the only people who read as individuals, standing about one quarter of the frame's height, close enough that their faces and clothing are clear but small enough that the lane towers over them.

AT MOST TWO other people appear, far down the lane as small anonymous dark silhouettes going about their business, with no visible faces or detail. No crowd. No patrol. Nobody else.

FOREGROUND. Low and to the LEFT, a big grey armoured UTILITY POD squats against the wall — a rounded service module or parked hauler with louvred grilles and access hatches, mostly in shadow, framing the left edge of the picture and leading the eye toward the entrance.

THE GROUND IS DRY. Kannan is sealed under a dome and no weather reaches these lanes. The street is dry, dusty ferrocrete and packed grit: pale, matte and powdery, with drifts of fine dust against the walls, scattered litter, a few loose chunks of rubble and some scuffed painted markings. THERE IS NO RAIN, NO PUDDLES, NO WET PATCHES, NO STANDING WATER, NO SHEEN, NO SLICK SURFACES, AND NO REFLECTIONS ON THE GROUND ANYWHERE. Light falls on the dust and stops; it does not mirror.

ABOVE. There is no open sky. Far overhead, the underside of the city's protective DOME arches across the top of the picture — a dark vault of structural ribs and dim glass panels, catching a faint cold glimmer, with the black shapes of upper storeys and overhanging walkways crowding in below it. It should read as a lid over the city, not as night sky and not as clouds. No stars, no moon, no storm.

LIGHT — EVENING, ARTIFICIAL, WARM AGAINST COLD. The two amber lamps at the cantina door are the heart of the picture, pooling warm ochre light down the steps and onto the dust. A few small warm rectangles of lit window glow further along the lane, and a couple of pale recessed downlights hang under the overhangs above. Everything beyond their reach falls into a single deep cool slate blue-grey shadow plane. Strong contrast: a warm, inviting doorway in a cold, dim street. No neon, no bloom, no halos, no lens flare, no light rays or visible beams.

COLOUR: warm sand, ochre and dusty bone in the lit areas and on the ground, against cool slate blue-grey and near-black in the shadowed masses and the dome above. The crew's colours are the accents — Graxo's dark wine cape, Sion's ochre jacket and teal scarf, Daxus's off-white and burnt-orange.

COMPOSITION: the lane recedes on a clear diagonal, the armoured brow and its lit doorway sit as the focal mass at left of centre, the three crew stand small beneath it in the lamplight's edge, and the foreground utility pod anchors the bottom left. Keep large quiet areas of plain wall and plain ground; concentrate detail at the entrance and on the crew.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
