# the-ride-out v003

User request verbatim: keep trying till you like it
Mode: Edit off v002. Five changes: (1) raider count to four, now ENUMERATED individually by position rather than asserted as a total — stating the number three times failed twice; (2) raider machines repainted as wheelless hover bikes, since the text calls them speeder bikes and the crew's machines hover — my own 'long forks' wording caused the motorcycles; (3) Graxo and Sion turned to look back at the pursuit, requested twice and absent twice; (4) ground repainted as few large calm planes against the all-over mosaic texture; (5) cape pushed from magenta to true muted aubergine.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f05f-5e8c-7463-9fb3-2d3794a62f59/exec-60814ac1-eed8-43d3-86d0-e7349131c73a.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-ride-out/v002/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.54 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: Four of five changes landed. RAIDER COUNT FIXED: exactly four raiders, verified on a magnified crop, and they match the enumeration one for one -- leader nearest with rifle raised, second hunched behind and left with no weapon, third higher on the slope with a rifle across his body, fourth cresting the ridgeline with both hands on his bars. The ridge beyond him is empty rock and sky. Describing four specific individuals by position succeeded where asserting the number three times had failed twice; that is the transferable lesson. WHEELS FIXED: every raider machine is now a wheelless hover bike on blunt downturned lift pods with clear daylight and cast shadow beneath it -- no tyres, rims, spokes, forks or mudguards anywhere in the picture, consistent with the crew's own hovering speeders and with the text calling them speeder bikes. GROUND FIXED: the all-over mosaic of chips and dashes is gone, replaced by broad calm planes of warm ochre and deep slate blue-violet meeting along clean angular seams, with drawing concentrated at shelf lips and mesa crests. CAPE FIXED: now a genuinely muted aubergine purple-brown rather than v002's magenta, sitting quietly against the ochre rock, both antique-gold collar pins intact. STILL UNMET: Graxo and Sion are facing forward again rather than glancing back at the pursuit -- the third consecutive failure of that instruction. The likely cause is that turning a head away costs face legibility, and the model is protecting the portrait; the next attempt should ask only Sion to turn, leaving Graxo's face as the lead read. Cast identity otherwise holds: Graxo's elongated face, long broad-tipped nose, mustache, silver temples, plum ascot and vest; Sion's opaque ruby goggles, ochre jacket with the left sleeve absent, teal scarf and bare steel-gray cyber arm on the correct anatomical side; Daxus's glasses, off-white jacket with cross patches, burnt-orange shirt and bandolier. Kannan's dome and the storm wall with its lightning both hold in the middle distance. File is 2.54 MB, marginally over the 2.5 MB book-float budget and needing recompression before placement. Speeders and raiders remain IMPROVISED -- no assets exist for either.

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

Image 1 is STYLE: Match this image's hand-painted matte rendering technique ONLY. Ignore and do not reproduce its people, clothing, equipment, interior or setting.
Image 2 is EDIT TARGET: The scene baseline: the-ride-out v002. Its composition, its three crew riders and its setting are correct; change only what the spec below specifies.

TASK: A single 3:2 horizontal daytime action illustration: the crew of the Antares running three hover speeders across the Kalagra badlands as exactly four raiders on wheelless hover bikes come down off a ridge after them.

THE CAST — three riders, each copied from their own identity sheet. Ignore every sheet's layout, its multiple views, its expression busts, its height chart and its plain gray background; take only the person's design.

GRAXO VOSS (description v11) — image 2. Tall, sturdy adult man with a weathered, elongated angular face: long middle and lower face, tall forehead with a loose forelock, heavy brow, deep-set readable eyes, pronounced angular cheekbones, strong jaw with a rounded chin. Long projecting nose with a broad, softly rounded bulbous tip, clearly broader than the bridge. Neat regular dark-brown mustache ending at the mouth corners, no beard. Dark brown hair swept up, with clearly visible silver-gray at both sides and temples. He wears a full-width AUBERGINE cape over both shoulders and back, open at the front, with a high standing collar and two square antique-gold medallion pins, one at each cape edge; the cape falls below the knees and its lining is dusty mauve. Under it a plain dark walnut-brown fitted vest with restrained metallic buttons, an ivory long-sleeved shirt and a compact plum ascot. Charcoal trousers, charcoal boots with metal toe and heel caps. A charcoal molded holster on his anatomical RIGHT hip carries one blaster, wood grip upward and backward, muzzle enclosed downward.

SION TILL (description v1) — image 3. Young adult woman, medium warm skin, slender-to-average build, broad chin and slightly square jaw, full lips, dark shoulder-length hair swept to one side. She wears large dark-framed goggles with OPAQUE MIRRORED RUBY-RED lenses — a continuous red surface with one broad diagonal pale reflection, completely concealing her eyes and eyebrows. Never paint eye shapes, pupils or eyebrows on or above the lenses. Worn OCHRE utility jacket over a plain black shirt: the RIGHT arm is sleeved, and the LEFT sleeve is absent at the shoulder. A slim TEAL scarf loosely wraps her neck, its short ends finishing near the upper chest. Her anatomical LEFT arm is a cyber arm, exposed from shoulder to five-fingered hand: steel-gray shells, dark joints, restrained brass fittings, human proportions, no wires or weapons. Her right arm and hand are natural skin. Relaxed charcoal cargo trousers with thigh flap pockets, sleek black boots.

DAXUS SKYE (description v1) — image 4. Youthful adult man, broad sturdy build, light-to-medium skin, full cheeks, square jaw, straight nose, dark eyebrows, clean-shaven, with thin metal-framed glasses. Dark brown hair, closely cropped sides, neat side part, swept-back voluminous wave on top. He wears a short OFF-WHITE medical jacket with a high collar and rounded front edges flaring toward the hips; a broad inverted-V opening exposes a BURNT-ORANGE shirt across his abdomen, and orange-red sleeve patches carry pale medical crosses. One broad dark-brown bandolier runs from his anatomical RIGHT shoulder down to his LEFT hip, with a flat triangular leather panel at the lower chest carrying one ivory diagnostic scanner. Off-white utility belt, dark brown cargo trousers, worn brown lace-up work boots.

RELATIVE HEIGHT: Graxo is the tallest at 6 feet 2, Daxus 6 feet, Sion 5 feet 9.

THE RAIDERS are original and have no identity sheet: four of them, faces hidden behind wrapped dust scarves and scratched goggles, in mismatched scavenged gear. Keep them as dark, simplified silhouettes — they are a threat, not portraits. Do not give them any of the crew's clothing, colors or equipment.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame. THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. It is NOT a 2:1 banner, NOT a panorama, NOT a letterbox strip. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO labels, NO text of any kind. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors or composition. Image 2 is the SCENE BASELINE: reproduce its composition, its three crew riders and its setting, and change only what is specified below.

SCENE: "The Ride Out." Daytime on the barren planet Kalagra. The crew of the Antares is running three rented hover speeders across open rocky badlands toward the domed city of Kannan, and a raider gang has come down off a ridge after them.

KEEP FROM IMAGE 2 — UNCHANGED: the whole composition and camera; the three crew speeders running on their diagonal from lower left into the middle distance, at their current sizes and positions; the crew themselves and every detail of their design; the battered ivory-and-ochre hover speeders with their brick-red markings and their low banners of ochre dust; the sunlit badlands with their angular shelves and mesas; the domed city of Kannan small in the middle distance; the immense dark cobalt and blue-violet storm wall along the far horizon with its pale yellow lightning; the late-afternoon raking sunlight, the warm ochre lit planes and the deep slate blue-violet shadows. Do not re-frame, do not zoom, do not move or resize the crew or their machines.

THE CREW ARE UNCHANGED — restated so nothing drifts:
- GRAXO, nearest and largest at lower left: weathered elongated angular face, long projecting nose with a broad softly rounded bulbous tip, neat dark-brown mustache, silver-gray hair at both sides and temples, dark brown hair swept up with a loose forelock. Full-width cape with a high standing collar and two square antique-gold medallion pins, one at each cape edge, streaming out behind him. Dark walnut-brown fitted vest, ivory long-sleeved shirt, compact plum ascot, charcoal trousers, blaster holstered at his anatomical right hip.
- SION, middle: young woman, medium warm skin, dark hair blown back. Large dark-framed goggles with OPAQUE MIRRORED RUBY-RED lenses — one flat red surface with a single pale diagonal streak, completely concealing her eyes and eyebrows; never paint eye shapes, pupils or eyebrows on or above them. Ochre utility jacket, right arm sleeved, LEFT sleeve absent at the shoulder. Slim teal scarf streaming. Her anatomical LEFT arm is a bare steel-gray cyber arm from shoulder to five-fingered hand, human proportions, no wires or weapons; her right arm is natural skin.
- DAXUS, farthest of the three: broad sturdy man, thin metal-framed glasses, dark brown hair with cropped sides and a neat swept-back wave. Short off-white medical jacket with a high collar, a broad inverted-V opening showing a burnt-orange shirt, orange-red sleeve patches with pale medical crosses, and a broad dark-brown bandolier from his right shoulder to his left hip carrying an ivory scanner at the chest.

CHANGE ONE — THERE MUST BE EXACTLY FOUR RAIDERS. Image 2 shows five. Paint four, and paint them as four specific individuals rather than as a crowd. Going from nearest to farthest, these are the only raiders in the picture:

- RAIDER ONE, the leader: nearest of the four, largest, lower right of the raider group, already down off the ridge and onto the flat. He is turned slightly toward the crew, one fist on his handlebar and a long crude rifle raised in his other hand above his shoulder.
- RAIDER TWO: just behind and to the left of the leader, slightly smaller, hunched low over his bars with both hands on them and no weapon showing.
- RAIDER THREE: further back and higher, still on the slope of the ridge, smaller again, a second long crude rifle held across his body.
- RAIDER FOUR: farthest and smallest, at the top of the ridge and only just cresting it, a dark shape against the sky with both hands on his bars.

That is all four. Beyond Raider Four the ridgeline is EMPTY — bare rock and sky, with no further riders, no dust plumes from unseen machines, no silhouettes on the horizon and no fifth figure of any kind anywhere in the picture. Count the riders before you finish: three crew and four raiders, seven people total.

CHANGE TWO — THE RAIDERS' MACHINES HOVER. THEY HAVE NO WHEELS. Image 2 gives them wheeled motorcycles with round rubber tyres, spoked hubs and long front forks. That is wrong for this world: these are speeder bikes, and like the crew's machines they ride on air.

Repaint every raider machine as a skeletal hover bike: a long spine frame with a saddle, a simple handlebar yoke on a short stem, and a heavy exposed engine block slung beneath the middle. Front and rear end in blunt downturned lift pods — stubby armoured shoes a hand's breadth clear of the rock. There is CLEAR DAYLIGHT AND SHADOW between the bottom of every machine and the ground: nothing touches the rock. NO wheels, NO tyres, NO rims, NO spokes, NO forks, NO mudguards, NO chains anywhere in the picture. Each bike trails its own low flat wedge of ochre dust kicked up from beneath its pods.

Keep the raiders looking scavenged and dangerous: mismatched panels in slate, rust-brown and dull green, ragged fairings, welded repairs, exposed pipework. The riders stay dark simplified silhouettes in wrapped dust scarves and scratched goggles, faces hidden, carrying none of the crew's colours or equipment.

CHANGE THREE — GRAXO AND SION LOOK BACK. In image 2 both are facing forward. Turn their heads: Graxo's head and shoulders twist back over his shoulder toward the raiders, his face in three-quarter so the long nose, mustache and silver temples still read clearly; Sion also turns her head back hard toward the pursuit, her red goggles catching the sun. Their bodies stay where they are, still low and driving forward — only the heads and shoulders turn. Daxus, farthest, keeps facing front.

CHANGE FOUR — CALM THE GROUND DOWN. In image 2 the rock and dust are broken into a dense carpet of small chips, dashes and mosaic tiles covering nearly every surface. Repaint the ground as a FEW LARGE FLAT PLANES of solid colour with hard angular edges: broad calm fields of warm ochre in the light and broad calm fields of deep slate blue-violet in shadow, meeting along clean straight or crisply angled seams. Detail and drawing belong ONLY at those seams, at the cliff edges, at the shelf lips and at the crests of the mesas — the interior of every large plane stays quiet, flat and under-detailed. Dry-brush breakup is a light touch at a few edges, never an all-over texture. The same goes for the dust banners: two or three flat opaque shapes each with hard ragged edges, not a spray of speckles.

CHANGE FIVE — THE CAPE IS AUBERGINE. Graxo's cape in image 2 still reads magenta-crimson at its trailing edge. Repaint the whole cape a deep, muted, desaturated purple-brown — the colour of aubergine skin, dusky and dark, sitting quietly against the ochre rock. It is NOT magenta, NOT crimson, NOT scarlet, NOT hot pink, and it does not glow. Its dusty mauve lining may flash where it folds. Keep both antique-gold pins at the collar.

LIGHT: unchanged from image 2. Late-afternoon daylight raking from the left, long hard shadows across the rock, one bright lit plane along the left side of every rider and machine, every shadow a single flat plane of deep slate blue-violet. No neon, no bloom, no lens flare, no light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
