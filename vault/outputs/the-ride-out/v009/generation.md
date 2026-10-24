# the-ride-out v009

User request verbatim: Ok. So try it again for the Ride Out. The camera is facing the crew. They are riding in a group but dont make it exactly a line. They can be at different distances from each other. It should be a wide shot of them crossing the barren plains with the storm behind them filling the horizon. / Oh and it needs to be night time. The moon is casting enough light to see them.
Mode: Fresh scene pass, and the FIRST to attach an approved speeder: assets/vehicles/hire-speeder/reference.png (= candidates/v006), promoted this session. Every earlier the-ride-out candidate improvised the machine, which is why its fore/aft order and proportions kept drifting. Brief: camera facing the crew, wide shot with the nearest speeder ~1/5 frame width, riders ~1/8 frame height, and a deliberately UNEVEN group — different depths, uneven lateral gaps, no straight line and no level noses. NIGHT, moonlit: a flat pale moon as the only key light, deep slate blue-violet shadow everywhere else, one small flat prow lamp per machine, lightning as the brightest note. Storm restated as cloud filling the full width of the horizon behind them. No raiders. Cape guard retained.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f0a4-003d-78c0-a5c2-abf68e6f8044/exec-47b24f8f-ce90-4a01-987d-9869259f3278.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/vehicles/hire-speeder/reference.png; frozen assets/vehicles/hire-speeder/candidates/v006/image.png
- Image 3 IDENTITY: assets/characters/graxo/reference.png; frozen assets/characters/graxo/candidates/v027/image.png
- Image 4 IDENTITY: assets/characters/sion/reference.png; frozen assets/characters/sion/candidates/v001/image.png
- Image 5 IDENTITY: assets/characters/daxus/reference.png; frozen assets/characters/daxus/candidates/v001/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.46 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: First the-ride-out pass built on an approved speeder, and the machine is finally right. Attaching assets/vehicles/hire-speeder/reference.png carried the design across intact: prow leading with its forward grille, rider STRADDLING a saddle toward the rear with a boot on the flat flank stirrup, slim boom with tidy tubes reaching back to the rust engine pod at the TAIL, ventral skid beneath the hull, no antenna, no wheels, and the 1970s sunset swipe running level and narrow at the front then sweeping up and widening toward the tail. All three machines are consistent with one another and with the sheet. This is the structural problem solved: candidates v001 to v008 all improvised the machine, which is why its fore/aft order and proportions kept sliding between passes. NIGHT landed well and matches the Pad scene for continuity: flat pale moon upper right with simple crater patches, cool moonlight on the upper hulls, shoulders and faces, everything else in deep slate blue-violet, and one flat pale-yellow prow lamp per machine throwing a wedge onto the rock. STORM fills the full width of the horizon and reads unmistakably as cloud — billowing rounded heads, a ragged rain curtain swallowing the plain, several lightning forks as the brightest notes in the picture. GROUP FORMATION as asked: not a line and not a rank — Sion left and mid-distance, Graxo nearest and centre, Daxus far right and smallest, with different depths, uneven lateral gaps and no two noses level. CAST: only Graxo wears a cape; Sion's teal scarf stayed a slim band; Daxus has nothing trailing. Sion's opaque ruby goggles, ochre jacket with the absent left sleeve and steel-gray cyber arm on her anatomical left all correct; Daxus's glasses, cross patches and bandolier correct. DISCREPANCIES: (1) SCALE — the nearest speeder spans roughly 610px of 1536, about 40 percent of frame width, against a specified one fifth and a stated cap of one quarter. The plain and storm still dominate, but this is closer than the wide shot asked for and the same drift that was rejected at 45 and 26 percent in earlier passes. (2) Graxo's cape has drifted warm again, reading crimson-magenta rather than muted aubergine, and his vest reads ochre-gold rather than dark walnut-brown. (3) The ground still carries an all-over dashed dry-brush hatch rather than quiet flat plane interiors — the most persistent style drift in this scene across every pass. (4) The prow lamp wedges carry a slight gradient where flat opaque shapes were specified. File is 2.46 MB, inside the 2.5 MB book-float budget.

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

Image 1 is STYLE: Match this image's hand-painted matte rendering technique ONLY. Ignore and do not reproduce its people, clothing, equipment, interior, setting or its close-up framing.
Image 2 is IDENTITY: The APPROVED REFERENCE SHEET for the Kalagra hire speeder. Copy the machine it shows exactly — prow leading, rider straddling a saddle toward the rear with boots on flank stirrups, boom and engine pod trailing at the tail, ventral skid pod, and the 1970s sunset swipe with its widening kick. Ignore the sheet itself: its grey background, its five-view layout, its panels and its own generic rider.
Image 3 is IDENTITY: GRAXO VOSS. Copy this man's design exactly — face, hair, mustache, silver temples, aubergine cape with its two gold collar pins, walnut-brown vest, ivory shirt and plum ascot. He is the ONLY character who wears a cape. Ignore this sheet's layout, its multiple views, its expression busts and its plain gray background.
Image 4 is IDENTITY: SION TILL. Copy this woman's design exactly — face, hair, opaque ruby goggles, ochre jacket with the missing left sleeve, slim teal scarf and bare steel-gray left cyber arm. She wears NO cape. Ignore this sheet's layout, its multiple views, its expression busts, its height chart and its plain gray background.
Image 5 is IDENTITY: DAXUS SKYE. Copy this man's design exactly — face, glasses, hair, off-white medical jacket with the burnt-orange V and cross patches, bandolier and chest scanner. He wears NO cape. Ignore this sheet's layout, its multiple views, its expression busts, its height chart and its plain gray background.

TASK: A single 3:2 horizontal wide night illustration: the crew of the Antares crossing an immense barren Kalagra plain on three hire speeders under moonlight, riding toward the viewer in a loose scattered group, the planet-wide storm filling the horizon behind them.

THE MACHINES — three Kalagra hire speeders, one per rider, all identical in design. Image 2 is their APPROVED REFERENCE SHEET and is the authority on every part of them. Copy the machine it shows and ignore the sheet itself: ignore its grey background, its five-view layout, its separate panels and its own generic rider.

From that sheet, the machine is: a long, low hover speeder, about three times as long as it is tall. The PROW leads — a blunt, slightly raked nose with a small forward grille — and nothing projects ahead of it. Behind the prow runs the long body, its upper deck carrying the paint. The RIDER STRADDLES the machine toward the REAR, sitting ON a narrow saddle that stands proud of the hull spine, one leg down each flank, each boot resting on a flat angled stirrup bracket that projects from that flank just ahead of the saddle. The rider leans forward onto a short handlebar yoke on a low cowl with a small windscreen. Behind the rider, a slim boom with two or three tidy parallel tubes reaches BACKWARD to a fat cylindrical ENGINE POD at the very TAIL, mouth facing backward, with angular vanes beneath it. A flat grey skid pod runs beneath the mid-hull. Every machine hovers a hand's breadth clear of the ground with clear daylight and a cast shadow beneath it.

NEVER: no wheels, tyres, rims, spokes, forks or mudguards; no antenna or aerial anywhere; no engine pod at the nose; no enclosed cockpit, tub or cabin; nobody sitting down inside the machine.

THE PAINT, from the same sheet: pale cream and ivory hull over a dark brown lower body, with the 1970s sunset swipe along the flank — narrow cream, golden yellow, orange, red-orange and dark brown bands running level and narrow at the front, then sweeping up together toward the rear in one smooth curve and widening as they rise. The tail engine pod is the swipe's deep red-orange rust with one cream band at its collar. Flat opaque colour, hard clean edges, honest chipped and sand-scoured wear.

THE RIDERS — copy each person's design from their own identity sheet and ignore every sheet's layout, multiple views, expression busts, height chart and plain gray background.

GRAXO VOSS (image 3): adult man, weathered elongated angular face, long projecting nose with a broad softly rounded bulbous tip, neat dark-brown mustache, dark brown hair swept up with clearly visible silver-gray at both sides and temples. Deep muted AUBERGINE cape — a dusky desaturated purple-brown, never magenta or crimson — with a high standing collar and two square antique-gold medallion pins, streaming back behind him. Dark walnut-brown vest, ivory long-sleeved shirt, plum ascot.

SION TILL (image 4): young adult woman, medium warm skin, dark shoulder-length hair blown back. Large dark-framed goggles with OPAQUE MIRRORED RUBY-RED lenses — one flat red surface with a single pale diagonal streak, completely concealing her eyes and eyebrows; never paint eye shapes, pupils or eyebrows on or above them. Worn OCHRE utility jacket over a black shirt, right arm sleeved, LEFT sleeve absent at the shoulder. Slim TEAL scarf streaming. Her anatomical LEFT arm is a bare steel-gray cyber arm from shoulder to five-fingered hand; her right arm is natural skin.

DAXUS SKYE (image 5): youthful adult man, broad sturdy build, thin metal-framed glasses, dark brown hair with cropped sides and a neat swept-back wave. Short OFF-WHITE medical jacket with a high collar and a broad inverted-V opening showing a BURNT-ORANGE shirt, orange-red sleeve patches with pale medical crosses, and a broad dark-brown bandolier from his right shoulder to his left hip carrying an ivory scanner at the chest.

ONLY GRAXO WEARS A CAPE. Graxo alone has the aubergine cape streaming behind him. SION HAS NO CAPE and DAXUS HAS NO CAPE — no cape, cloak, poncho, coat-tail or banner trailing behind either of them. Sion's only streaming item is her SLIM TEAL SCARF, a narrow band of cloth at the neck, never widening into a sheet across her back. Daxus's short jacket is close-fitting and ends at the hips; nothing of his trails at all.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame. THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. It is NOT a 2:1 banner, NOT a panorama, NOT a letterbox strip, NOT a square. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO labels, NO text of any kind. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors, composition or its close-up framing. Image 2 contributes the SPEEDER'S DESIGN ONLY — copy the machine, not the sheet: ignore its grey background, its five-view layout, its panels and its own generic rider. Images 3, 4 and 5 contribute their PEOPLE ONLY.

SCENE: "The Ride Out." NIGHT on the barren planet Kalagra. The crew of the Antares are crossing an immense empty plain on three hire speeders, riding hard through the dark, with the planet-wide storm standing along the whole horizon behind them.

THERE ARE EXACTLY THREE PEOPLE AND THREE MACHINES. Nobody is chasing them. There are no pursuers, no raiders, no bandits, no gang, no other vehicles, no distant riders, no dust plumes from unseen machines and no figures anywhere on the horizon. Three riders, three speeders, empty country.

THE CAMERA FACES THEM. The viewer stands ahead of the oncoming riders and low, roughly at the height of the machines. All three come TOWARD the viewer in front three-quarter view: we see their faces and chests, the prow of each hull coming at us, and enough of each machine's near flank that the sunset swipe reads along its length. No rider's back is turned to us and we are not looking down on their decks from above.

THE GROUP — RIDING TOGETHER, BUT NOT IN A LINE. This matters. They are a loose, scattered group, NOT a formation, NOT a rank, NOT three machines evenly spaced across the frame, and NOT three machines strung along one straight diagonal. Break it up:
- Each rider is at a DIFFERENT DISTANCE from the viewer. One is clearly the nearest and largest. One is a good way further back and noticeably smaller. One is somewhere between them — and not at the midpoint of the other two.
- Their lateral spacing is UNEVEN: two of them run closer together, the third set well apart from that pair.
- The gaps between them differ in both depth and width, so no two spacings match.
- They are not aligned on any straight line, and their noses are not level with one another.
- Vary them: one runs slightly ahead and lower, one holds back, one drifts wide. It should look like three people travelling together across open country, each riding their own line, not a parade.

SCALE AND FRAMING — A WIDE SHOT. The land and sky dominate; the riders are small figures crossing a very large country.
- The NEAREST speeder spans about ONE FIFTH of the frame's width. The others are smaller. Do not exceed a quarter for any of them, and if unsure, paint them smaller.
- Each rider is roughly ONE EIGHTH of the frame's height. Faces are small: five to eight flat planes each, no more. Do not enlarge anyone to show their face.
- The three machines occupy a band across the middle of the picture. Above them is a broad sweep of night sky and storm; below them, open plain running down toward the viewer.
- Do NOT crop in. No hull touches any edge of the frame.

THE LAND: an immense barren plain of flat rock, laid out in broad terraces and low shelves stepping away toward the horizon, with a few flat-topped mesas standing in the far distance. Build ALL of it from a FEW LARGE FLAT PLANES of solid colour with hard, crisply angled edges — broad calm fields meeting along clean seams. Drawing and detail belong ONLY at those seams: the shelf lips, the mesa crests. The interior of every large plane stays QUIET, FLAT and UNDER-DETAILED. Do NOT break the ground into a carpet of small chips, facets, pebbles, dashes, hatching or mosaic tiles.

THE STORM, BEHIND THEM, FILLING THE HORIZON: across the entire far distance stands the planet-wide storm front, and it must READ UNMISTAKABLY AS WEATHER, NOT AS MOUNTAINS. Paint it as a towering wall of CLOUD spanning the full width of the picture: a mass of deep cobalt and blue-violet with a soft-shouldered, billowing, rolling top edge made of stacked rounded cloud heads — no rock facets, no strata, no cliff faces, no hard geological silhouette. Its base is a ragged curtain of falling dust that swallows the ground at the far horizon, so the plain disappears INTO it rather than meeting it at a clean line. It is tall: it fills much of the upper half of the picture behind the riders. Several thin branching bolts of pale yellow-white LIGHTNING fork inside it, and they are the brightest things in the image. It is still far off — the air around the riders is clear, with no haze or murk near them.

LIGHT — NIGHT, LIT BY THE MOON. This is a night picture and it must read as one: dark overall, with a small number of clear lit shapes.
- A large pale MOON hangs in the night sky above and to one side, well clear of the storm — a plain flat pale disc with two or three simple darker flat patches for craters, no gradient, no glow around it.
- The moon is the only source of light on the riders. It falls from above and slightly behind the viewer, so the TOPS and FRONTS of the riders and machines catch it: one flat, cool, pale plane along each upper hull, each shoulder, each helmet and face. Everything turned away from it — undersides, far flanks, the ground beneath them — falls into a single deep slate blue-violet shadow plane.
- The ground is dark: cool blue-grey and slate, with only the upward-facing terrace tops catching a muted pale wash of moonlight. There is no warm daylight anywhere.
- Each speeder carries ONE small forward lamp at its prow, painted as a single flat pale-yellow shape throwing a short flat wedge of light onto the rock ahead of it. Painted shapes only: no glow, no bloom, no halo, no soft edges, no light rays, no volumetric beams.
- The sky is a deep blue-black, painted as large flat areas, paling a little toward the storm.
- No neon, no rim lighting, no bloom, no lens flare.

COLOUR: the picture is built from deep slate blue-violet and blue-black, with cool pale moonlight as the only light. Under that moonlight the machines' sunset swipe reads muted — the cream and yellow bands as pale bone, the orange and rust as dull warm notes, the dark brown nearly black — and the riders' colours are likewise dimmed: Graxo's aubergine cape a dark purple mass, Sion's ochre jacket and teal scarf muted, Daxus's off-white the palest thing on any of them. Those muted warm notes, the three small prow lamps and the lightning are the only relief in a cold dark picture.

Give it quiet and distance: three small machines running through the dark across an enormous plain, with a mountain of weather standing over the whole horizon behind them.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
