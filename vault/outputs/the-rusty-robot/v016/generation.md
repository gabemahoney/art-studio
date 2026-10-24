# the-rusty-robot v016

User request verbatim: v15 the sizes are all wrong. the characters are way too big. Compare it please to v5 yourself. Your goal is to get something similar in composition to v5 without the broken sign. thats it
Mode: FRESH generation with NO edit target, rebuilding v005's composition. Measured at matched scale: the crew occupy about 48 percent of frame height in v005 against about 61 percent in v015, and v015 crops the stair run and fills the frame with the entrance where v005 shows the cantina as one feature of a wider street. The drift entered at v006, itself a fresh generation that started closer than v005, and eleven subsequent edits preserved it; since repeated 'paint them smaller' edits have failed throughout this scene, the camera is specified numerically in a fresh build instead — figures at 45 to 50 percent of frame height, the entrance and its full flight of steps uncropped, a broad sweep of empty paving across the lower third. Everything the user approved since v005 is carried in the prompt rather than inherited: the sign flat on the wall above the brow with its edges parallel to the wall's horizontals, painted not lit, with a flat stencil emblem; grey ferrocrete with muted teal painted bands and no red, orange or pastel; angular machined lamps rather than lanterns; clean dry paving with no rocks; an unlit black alley; the tight overlapping huddle; Sion's across-the-body point with the corrected hand anatomy; and the v005 light level on the crew.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f4c8-0b0a-7613-818f-8856dc201f54/exec-fabf5b00-43be-460c-8fec-4a83d0e73704.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.44 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
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
Image 2 is IDENTITY: The approved CREW LINEUP — Daxus left, Graxo centre, Sion right. Copy their faces, builds, hair, clothing and equipment. Ignore its plain background, its standing poses, its side-by-side layout and its height chart, and reproduce NONE of its printed numbers or any other text.

TASK: A single 3:2 horizontal evening STREET shot: a grey ferrocrete cantina seen whole with its full flight of steps and its wall sign reading THE RUSTY ROBOT, and three small figures huddled at an alley mouth beside it.

THE CAST — three crew conferring in the lane. Image 2 is the approved CREW LINEUP: Daxus on the left, Graxo in the centre, Sion on the right. Copy their faces, skin tones, builds, hair, clothing and equipment from it. Ignore its plain studio background, its standing poses, its side-by-side arrangement and its height chart, and reproduce NONE of its printed height numbers or any other mark from it.

GRAXO VOSS — the tallest at 6 feet 2. Weathered, elongated, angular face with a long projecting nose whose tip is broad and softly rounded, a neat dark-brown mustache, and dark brown hair swept up with clearly visible silver-grey at both sides and temples. He wears a full-length cape in DEEP WINE AUBERGINE — a dark, heavily greyed-off purple-brown, never magenta, crimson or pink — hanging from a high standing collar with two square antique-gold medallion pins at its front edges, lying across both shoulders and falling down his back with both arms clear of it. Dark olive-charcoal fitted vest, ivory long-sleeved shirt, plum ascot, charcoal trousers and boots, and a holstered blaster at his anatomical right hip.

SION TILL — 5 feet 9, slender, medium warm skin, dark shoulder-length hair. Large dark-framed goggles with OPAQUE MIRRORED RUBY-RED lenses, a single flat red surface with one pale diagonal streak, completely concealing her eyes and eyebrows; never paint eye shapes, pupils or eyebrows on or above them. Worn OCHRE utility jacket over a black shirt, right arm sleeved, LEFT sleeve absent at the shoulder. A SLIM teal scarf wrapped once at her throat with short ends at her upper chest — a narrow band only, never a broad sheet and never trailing. Her anatomical LEFT arm is a bare steel-grey cyber arm from shoulder to five-fingered hand; her right arm is natural skin. Charcoal cargo trousers, black boots.

DAXUS SKYE — 6 feet 0, broad and sturdy, light-to-medium skin, full cheeks, clean-shaven, thin metal-framed glasses, dark brown hair with cropped sides and a neat swept-back wave. Short OFF-WHITE medical jacket with a high collar and a broad inverted-V opening showing a BURNT-ORANGE shirt, orange-red sleeve patches with pale medical crosses, a broad dark-brown bandolier from his right shoulder to his left hip carrying an ivory scanner at the chest, off-white belt, dark brown trousers, worn brown boots.

ONLY GRAXO WEARS A CAPE. Sion and Daxus wear no cape, cloak, mantle, shawl or coat-tail, and nothing broad hangs from either of their shoulders.

HANDS — KEEP THEM SIMPLE AND CLOSED. Do not paint anyone POINTING. No extended index finger, no jabbing gesture, no counting on fingers, no splayed hand held up. Pointing hands have repeatedly come out malformed, with the folded fingers drawn as flat parallel bars instead of curling into the palm. Avoid the problem entirely: each character's hands are either relaxed and closed at their sides, tucked into a pocket, folded across the chest, or resting on a belt. Sion's natural right hand may hook a thumb in her belt; her steel-grey cyber hand hangs relaxed with its fingers loosely together. At this size a hand is two or three flat shapes at most — a simple mitten-like mass with the thumb suggested — never articulated fingers.

THE PLACE — The Rusty Robot, a dockworkers' cantina in the low-rent warrens of Kannan, a city sunk in a crater and sealed under a protective dome. It is evening. The lane is grimy, lived-in and working-class.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no turnarounds, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only, and take nothing else from it. Image 2 is the approved CREW LINEUP, for the three characters' likenesses and clothing only.

SCENE: "The Cantina," exterior. Evening in the low-rent warrens of Kannan, a working-class city sunk in a crater and sealed under a dome. Three travellers huddle at the mouth of a narrow alley, conferring quietly, across the lane from the lit door of a dockworkers' cantina called The Rusty Robot.

THE CAMERA AND THE SCALE — THE MOST IMPORTANT THING IN THIS BRIEF. This is a STREET SHOT with people in it, not a group portrait with a street behind. Stand well back.

- The three figures stand ABOUT HALF the frame's height — roughly 45 to 50 percent, no more. Their heads reach only to about the middle of the picture, with a good depth of wall, sign and architecture above them.
- The cantina's ENTRANCE IS FULLY VISIBLE and reads as one feature of a larger street: the whole run of its steps from bottom tread to top, the complete doorway, the armoured brow above it, and the sign above that — none of it cropped by the figures or the frame.
- A broad sweep of empty dusty paving runs across the lower third of the picture, between the viewer and the buildings. The lane carries on past the cantina into the distance with room to breathe.
- The buildings on both sides rise well above the crew and are seen as whole masses, not as backdrop fragments.
- Do NOT crop in. Do NOT let the figures dominate. If in doubt, stand FURTHER BACK and paint them SMALLER. Nothing in this picture should read as a close-up.

THE LANE AND THE ARCHITECTURE. A street running away from the viewer into depth, hemmed in by heavy blocky buildings. Thick walls, deep-set arched windows, chunky buttresses, plain parapets, external pipework. Down the lane, stepped rooflines and a squat domed tower. Everything stained, patched and worn.

BUILDING COLOUR — GREY CONCRETE WITH PAINTED LINES. The buildings are WEATHERED GREY FERROCRETE — cool bone-grey, slate-grey and dust-grey — and that grey dominates the whole street. Colour appears ONLY as PAINTED MARKINGS on that grey: narrow horizontal bands along parapets and door surrounds, stripes around buttresses, a painted line on the ground. Those markings are a MUTED DUSTY TEAL-GREEN, faded and chipped, with at most a little dull olive as a secondary. NO RED, NO RUST-RED, NO ORANGE, NO BRICK and NO PASTEL FACADES anywhere: no building has a fully coloured wall, and nothing on the architecture echoes the warm cream-and-orange livery worn by the crew's ship and speeders.

THE CANTINA — on the LEFT side of the lane:
- Its front is a tall FLAT WALL of weathered grey ferrocrete, reading as one clean vertical plane.
- A large ROUND-ARCHED DOORWAY is set deep in shadow low in that wall, its door a dark circular slab with heavy radial ribs. A full flight of steps with a plain pipe handrail climbs to it, all of it visible.
- Above the doorway a MASSIVE WEDGE-SHAPED ARMOURED BROW of dark grey metal juts out over the steps like a blunt prow, with panel seams and louvred vents.
- TWO LAMPS flank the doorway. Each is an ANGULAR MACHINED METAL HOUSING — a squat wedge or truncated box with a flat rectangular lit face aimed downward on a short bracket. Hard-edged and utilitarian, like a deck light. They are NOT lanterns: no glass panes in frames, no carriage lamps, no scrolled ironwork, no finials, no gaslight styling.

THE SIGN — FLAT ON THE WALL, WELL ABOVE THE BROW. The sign is a flat rectangular board fixed FLUSH AGAINST THE CANTINA'S FLAT FRONT WALL, clearly ABOVE the armoured brow, with grey wall visible all around it on every side. It is NOT mounted on the brow, NOT on any angled or projecting surface, and NO part of it overhangs or crosses the brow or any other edge. Nothing behind it but wall.

Because it lies flat on that wall it shares the WALL'S perspective exactly: its top and bottom edges run parallel to the wall's own horizontal lines — the parapet, the window heads, the painted band — and converge with them toward the SAME vanishing point. Its left and right ends are identical simple vertical cuts, one merely nearer than the other. It is a plain rectangle in honest perspective, with a small thickness and a shadow cast on the wall behind it. If its edges do not run parallel to the other horizontals of that same wall, it is wrong.

THE SIGN IS PAINTED, NOT LIT. The board is dark rusted metal. The lettering is painted on it in flat CHIPPED IVORY, pale and matte and worn, flaked in places to show rust. Beside the words a painted butler-robot emblem in the same chipped ivory: a FLAT STENCIL silhouette with a rounded dome head, two round eyes, a stiff collar and a bow tie, rust-pitted. The emblem has NO shading, NO rounding, NO gradient and NO volume anywhere inside it — it is described by its outline alone, with flat chipping as the only variation. There is NO glow, NO neon, NO lit tubes and NO light emitted by the sign. A small hooded lamp above it throws a flat hard-edged wash of warm light across its upper part.

THE TEXT must read exactly:

THE RUSTY ROBOT

Those three words, spelled exactly that way, in WIDE, EXTENDED, GEOMETRIC SQUARED CAPITALS — straight strokes, softly rounded corners, uniform stroke weight, flat terminals, squarish counters, generous letterspacing, in the manner of 1970s spacecraft signage. Not serif, not script, not gothic, not ornate, not thin. Large and clearly legible. NO OTHER TEXT ANYWHERE in the picture, and no nonsense letterforms.

THE ALLEY AND THE CREW. At the LEFT, just along from the cantina's steps, a NARROW ALLEY runs back between buildings: a tall dark vertical slot, its sheer walls close together, its far end LOST IN BLACKNESS with NO windows, lamps or glowing openings inside it. The alley's near wall forms the left edge of the picture.

The three crew stand at the MOUTH of that alley, in its shade, close to the lane.

THEY ARE A TIGHT HUDDLE. Their silhouettes OVERLAP so each partly occludes the next and the three read as ONE compact interlocking mass, with no open background showing between any two of them from shoulder to hip. Their shoulders nearly touch. All three angle INWARD toward a shared point between them, forming a closed inward-facing triangle, and their HEADS LEAN IN close together at the top — the gap between their heads is smaller than the gap between their feet. DAXUS presses in at the left, leaning over Graxo's shoulder to listen. GRAXO stands at the centre, inclined toward the others. SION closes in from the right, her shoulder nearly against Graxo's. Their feet are close together and the group occupies a narrow footprint. They read instantly as three people with their heads together over something they do not want overheard. Each keeps a straight spine — the closeness comes from proximity and inward angle, not from stooping.

SION'S GESTURE: her natural RIGHT upper arm hangs vertically against her side, her ELBOW bent at her waist, her FOREARM crossing horizontally in front of her torso at chest height, her hand finishing near her opposite flank — a compact point ACROSS HER OWN BODY toward the cantina door, staying largely within her silhouette. It is a quiet private indication, not a reach into the street. HER HAND: index finger extended ALONE; middle, ring and little fingers curled tightly into the palm as ONE compact rounded fist with the knuckles a simple curved ridge; thumb folded across the front. The silhouette is one small ball with one finger projecting. Do NOT splay the folded fingers into flat parallel bars beside the index, and do not let more than one finger appear to point. Keep the whole hand to two or three flat shapes. Her steel-grey LEFT cyber arm hangs relaxed at her side.

THEIR LIGHTING: they stand in the alley's shade but are CLEARLY AND WARMLY READABLE, not silhouetted. Warm spill from the lane reaches them and lifts their local colour. DAXUS'S medical jacket reads pale off-white with its red cross patches legible. SION'S jacket reads warm OCHRE and her slim teal scarf reads teal. GRAXO'S cape reads a deep WINE AUBERGINE, dark but plainly purple, with both antique-gold collar pins catching. Faces and hair are clearly modelled, Sion's ruby goggles read red, and her cyber arm takes a bright metallic highlight. They are in shadow only RELATIVE to the doorway opposite, which stays the brightest thing in the picture.

AT MOST TWO other people appear, far down the lane as small anonymous dark silhouettes with no faces or detail. No crowd, no patrol.

THE GROUND IS DRY AND CLEAN. Kannan is sealed under a dome and no weather reaches these lanes. The street is dry dusty ferrocrete paving — pale, matte, laid out in a few large quiet flat planes — with drifted dust along the wall feet, a few flat scraps of litter, scuffed traffic-worn patches and the painted teal line. There are NO rocks, NO boulders, NO rubble, NO gravel and NO stone debris anywhere: not on the road, not on the steps, not in the corners. THERE IS ALSO NO RAIN, NO PUDDLES, NO WET PATCHES, NO SHEEN AND NO REFLECTIONS. Light falls on the dust and stops.

ABOVE. No open sky. Far overhead the underside of the city's protective DOME arches across the top of the picture — a dark vault of structural ribs and dim panels catching a faint cold glimmer, with upper storeys and overhanging walkways crowding beneath it. It reads as a lid over the city, not as night sky. No stars, no moon, no clouds.

LIGHT — EVENING, ARTIFICIAL, WARM AGAINST COLD. The two lamps at the cantina door are the heart of the picture, pooling warm ochre light down the steps and across the dust. A few small warm lit windows glow further along the lane and one or two pale downlights hang under the overhangs. Everything beyond their reach falls into a single deep cool slate blue-grey shadow plane. No neon, no bloom, no halos, no lens flare, no light rays.

COMPOSITION: the lane recedes on a clear diagonal; the lit doorway under its armoured brow, with the sign on the wall above, sits as the focal point at left of centre and is seen whole; the huddle of three stands small at the alley mouth beside it; and large quiet areas of plain grey wall and broad dusty paving fill the rest. Concentrate detail at the doorway and the sign, and keep everything else calm.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
