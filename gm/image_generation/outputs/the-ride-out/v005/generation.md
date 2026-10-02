# the-ride-out v005

User request verbatim: Also the raiders should be on speeders. The speeders could also look a little longer.
Mode: Edit off v004, machines only: crew speeders stretched to ~3x as long as wide with a long prow ahead of the bars and a long tail behind the saddle, width/height/riders unchanged; raider machines rebuilt from compact motorcycle-shaped bikes into long lean open-framed junker hover sleds of the same family, so every vehicle in the picture is one class. Four-raider count, the three hard-won lines of sight, calm ground planes, aubergine cape and no-wheels rule all explicitly frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f065-2fbb-7cd3-ad21-776d8c049f93/exec-3675e618-d73c-43c4-8251-9670d567a3f0.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-ride-out/v004/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.40 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Both machine changes landed and nothing regressed. The three crew speeders are now long and lean -- roughly three times as long as wide, with a long tapering prow reaching out ahead of the handlebars and a long tail running behind the saddle -- so they read as fast standing still instead of as stubby sleds. Width, height and rider positions are unchanged. The raider machines are rebuilt from compact motorcycle-shaped bikes into long open-framed junker hover sleds of the same family: long skeletal spines, saddles set well back, bare nose booms ahead of the riders' hands, scavenged engine blocks slung beneath the tails, patched mismatched panels and exposed pipework. Every vehicle in the picture now plainly belongs to one class of craft, which is what the scene text describes. Verified on a magnified crop: exactly FOUR raiders, matching the enumeration one for one -- leader nearest with rifle raised, second hunched behind and left with a green scarf and no weapon, third higher on the slope with a rifle across his body, fourth cresting the ridgeline -- with the ridge beyond him empty rock and sky. No wheels, tyres, rims, spokes, forks or mudguards anywhere; every machine rides on blunt lift pods with clear daylight and cast shadow beneath it. The three hard-won lines of sight held: Graxo eyes front with his face fully readable, Sion wrenched back over her right shoulder at the pursuit, Daxus chin lifted and tilted up-right toward the cresting raider. Also held: broad calm ochre and blue-violet ground planes, the muted aubergine cape with both gold pins, Sion's opaque ruby goggles and correctly sided cyber arm, Daxus's glasses and cross patches, Kannan's dome and the storm wall with its lightning. File is 1536x1024, exact 3:2 matching scene-meet, scene-jump and scene-pad, 2.40 MB and inside the 2.5 MB book-float budget with no recompression needed. One observation, not a defect: the trailing dust banners are lighter than in earlier passes, so the speed now reads from the long hulls and the diagonal rather than from dust. This candidate is judged finished. Speeders and raiders remain IMPROVISED -- no assets exist for either, so this image establishes nothing canonical about their design.

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
Image 2 is EDIT TARGET: The scene baseline: the-ride-out v004, approved by the user except that the machines are too stubby and the raiders are on bikes rather than speeders.

TASK: A single 3:2 horizontal daytime action illustration: the crew of the Antares running three long lean hover speeders across the Kalagra badlands as four raiders on junker hover speeders come down off a ridge after them.

THE CAST — three riders, each copied from their own identity sheet. Ignore every sheet's layout, its multiple views, its expression busts, its height chart and its plain gray background; take only the person's design.

GRAXO VOSS (description v11) — image 2. Tall, sturdy adult man with a weathered, elongated angular face: long middle and lower face, tall forehead with a loose forelock, heavy brow, deep-set readable eyes, pronounced angular cheekbones, strong jaw with a rounded chin. Long projecting nose with a broad, softly rounded bulbous tip, clearly broader than the bridge. Neat regular dark-brown mustache ending at the mouth corners, no beard. Dark brown hair swept up, with clearly visible silver-gray at both sides and temples. He wears a full-width AUBERGINE cape over both shoulders and back, open at the front, with a high standing collar and two square antique-gold medallion pins, one at each cape edge; the cape falls below the knees and its lining is dusty mauve. Under it a plain dark walnut-brown fitted vest with restrained metallic buttons, an ivory long-sleeved shirt and a compact plum ascot. Charcoal trousers, charcoal boots with metal toe and heel caps. A charcoal molded holster on his anatomical RIGHT hip carries one blaster, wood grip upward and backward, muzzle enclosed downward.

SION TILL (description v1) — image 3. Young adult woman, medium warm skin, slender-to-average build, broad chin and slightly square jaw, full lips, dark shoulder-length hair swept to one side. She wears large dark-framed goggles with OPAQUE MIRRORED RUBY-RED lenses — a continuous red surface with one broad diagonal pale reflection, completely concealing her eyes and eyebrows. Never paint eye shapes, pupils or eyebrows on or above the lenses. Worn OCHRE utility jacket over a plain black shirt: the RIGHT arm is sleeved, and the LEFT sleeve is absent at the shoulder. A slim TEAL scarf loosely wraps her neck, its short ends finishing near the upper chest. Her anatomical LEFT arm is a cyber arm, exposed from shoulder to five-fingered hand: steel-gray shells, dark joints, restrained brass fittings, human proportions, no wires or weapons. Her right arm and hand are natural skin. Relaxed charcoal cargo trousers with thigh flap pockets, sleek black boots.

DAXUS SKYE (description v1) — image 4. Youthful adult man, broad sturdy build, light-to-medium skin, full cheeks, square jaw, straight nose, dark eyebrows, clean-shaven, with thin metal-framed glasses. Dark brown hair, closely cropped sides, neat side part, swept-back voluminous wave on top. He wears a short OFF-WHITE medical jacket with a high collar and rounded front edges flaring toward the hips; a broad inverted-V opening exposes a BURNT-ORANGE shirt across his abdomen, and orange-red sleeve patches carry pale medical crosses. One broad dark-brown bandolier runs from his anatomical RIGHT shoulder down to his LEFT hip, with a flat triangular leather panel at the lower chest carrying one ivory diagnostic scanner. Off-white utility belt, dark brown cargo trousers, worn brown lace-up work boots.

RELATIVE HEIGHT: Graxo is the tallest at 6 feet 2, Daxus 6 feet, Sion 5 feet 9.

THE RAIDERS are original and have no identity sheet: four of them, faces hidden behind wrapped dust scarves and scratched goggles, in mismatched scavenged gear. Keep them as dark, simplified silhouettes — they are a threat, not portraits. Do not give them any of the crew's clothing, colors or equipment.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame. THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. It is NOT a 2:1 banner, NOT a panorama, NOT a letterbox strip. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO labels, NO text of any kind. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors or composition. Image 2 is the SCENE BASELINE: reproduce it faithfully and change only the machines.

SCENE: "The Ride Out." Daytime on the barren planet Kalagra. The crew of the Antares is running three rented hover speeders across open rocky badlands toward the domed city of Kannan, and four raiders have come down off a ridge after them.

Image 2 is APPROVED in every respect except the shape of the machines. Reproduce it exactly — same camera, same framing, same crop, same scale, same colours, same light, same paint handling, same people — and rebuild only what they are riding.

KEEP FROM IMAGE 2 — COMPLETELY UNCHANGED: the whole composition and camera; the positions of all seven riders and the diagonal they run on; every detail of the three crew's faces, clothing and equipment; the broad calm planes of warm ochre rock and deep slate blue-violet shadow, quiet and under-detailed in their interiors with drawing only at the shelf lips and mesa crests; the domed city of Kannan small in the middle distance; the immense dark cobalt and blue-violet storm wall along the far horizon with its pale yellow lightning; the late-afternoon raking sunlight and the long hard shadows. Do not re-frame, do not zoom, do not re-texture the ground.

THE THREE CREW AND THEIR THREE LINES OF SIGHT ARE UNCHANGED — this was hard won, do not disturb it:
- GRAXO, nearest and largest at lower left: eyes FRONT along the line of travel, jaw set, face readable in three-quarter — long projecting nose with a broad bulbous tip, dark mustache, silver-gray at both temples, loose forelock. Muted AUBERGINE cape streaming behind him, deep desaturated purple-brown and never magenta or crimson, with two square antique-gold medallion pins at the collar. Walnut-brown vest, ivory shirt, plum ascot, blaster at his anatomical right hip.
- SION, middle: head and shoulders wrenched BACK over her right shoulder toward the raiders, hair whipping forward across her cheek. Large opaque mirrored RUBY-RED goggles as one flat red shape with a single pale diagonal streak — no eyes, pupils or eyebrows painted on or above them. Ochre jacket, right arm sleeved and LEFT sleeve absent at the shoulder, teal scarf streaming, bare steel-gray LEFT cyber arm on the controls.
- DAXUS, farthest: chin lifted, head tilted UP AND TO THE RIGHT toward the cresting raider, alarmed. Thin metal-framed glasses, off-white medical jacket with a burnt-orange inverted-V opening and orange-red cross patches, dark-brown bandolier to the left hip with an ivory scanner at the chest.

THERE ARE STILL EXACTLY FOUR RAIDERS, in their current positions: the leader nearest at lower right with a long crude rifle raised above his shoulder; the second hunched low behind and to his left, both hands on his controls, no weapon; the third higher on the ridge slope with a rifle across his body; the fourth farthest, just cresting the ridgeline, both hands on his controls. Beyond the fourth the ridge stays EMPTY — bare rock and sky, no further riders, no extra dust plumes, no fifth figure anywhere in the picture. Do not add, remove or move a raider. They stay dark simplified silhouettes in wrapped dust scarves and scratched goggles, carrying none of the crew's colours.

CHANGE ONE — MAKE THE CREW'S SPEEDERS LONGER. In image 2 the three crew machines are stubby and blunt. Stretch each one along its own length so it reads as a long, lean hover speeder: roughly THREE TIMES AS LONG AS IT IS WIDE. Lengthen it fore and aft of the rider — a long tapering prow reaching well out ahead of the handlebars, and a long tail running well out behind the saddle. Keep the width, the height and the rider exactly as they are; only the length grows. The result should look fast standing still: a lance of a machine, not a stubby sled.

Each keeps everything else it already has: a low slabby hull with chipped ivory and ochre paint, brick-red markings, mismatched replacement plates, exposed vents and grab rails, a simple cowl and handlebars, a single saddle, and NO WHEELS — it rides a hand's breadth above the rock with clear daylight and a cast shadow beneath it. Each still throws its low flat wedge of ochre dust straight back. Keep them simple: large flat blocks of colour with hard edges, details suggested, never drawn in full.

CHANGE TWO — PUT THE RAIDERS ON SPEEDERS TOO, NOT BIKES. In image 2 the raider machines are compact and motorcycle-shaped: short, upright, straddled, with the rider sitting high over a stubby frame. Rebuild them as SPEEDERS of the same family as the crew's — long, low, lean hover craft — so that everyone in the picture is plainly riding the same class of vehicle.

Each raider speeder is a long open-framed hover sled, also about three times as long as it is wide: a long skeletal spine with a saddle set well back, a long bare nose boom reaching out ahead of the rider's hands, and a heavy scavenged engine block slung beneath the tail. Blunt downturned lift pods fore and aft hold it a hand's breadth clear of the rock, with CLEAR DAYLIGHT AND CAST SHADOW beneath every machine — nothing touches the ground. NO wheels, NO tyres, NO rims, NO spokes, NO forks, NO mudguards, NO chains anywhere in the picture.

The raiders' speeders are the junk versions of the crew's: the same long lean proportions, but stripped, patched and ugly — mismatched panels in slate, rust-brown and dull green, ragged or missing fairings, welded repairs, exposed pipework and bare frame where plating has been torn off. The riders sit low and forward on them. Each trails its own low flat wedge of ochre dust. Keep them smaller in the frame than the crew's machines, as their distance already makes them, and keep them dark and muted so the crew still reads first.

LIGHT: unchanged from image 2. Late-afternoon daylight raking from the left, long hard shadows across the rock, one bright lit plane along the left side of every rider and machine, every shadow a single flat plane of deep slate blue-violet. No neon, no bloom, no lens flare, no light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
