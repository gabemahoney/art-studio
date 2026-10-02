# the-ride-out v010

User request verbatim: Maybe zoom out a bit on them? ... And yes to your other fixes. Maybe try feeding the model the source image for kalagra (the cover) as a reference? / Also it feels like we lost the angle of the color swipe / Graxos cape is also going UNDER his right arm. / Also maybe dont show the moon. Just show the storm. / Daxus also looks too big for his scooter / and we should find someway to show movement. maybe dust clouds behind them? / Oh also, Sion has a cape and should not. / And the ground is too blue. It needs to match better the color palette of the speeders so they dont stand out so much.
Mode: Regeneration off v009 with ten fixes. NOTE ON ATTACHMENTS: image_gen caps reference images at FIVE; a six-image attempt (anchor + speeder + Kalagra + three character sheets) was refused with nothing billed. The three character sheets were dropped rather than the Kalagra reference the user asked for — at ~1/10 frame height a face is ~25px, rules.md's escalation ladder permits 'nothing' as an identity input, and carrying the crew in text also removes the likely route by which Graxo's caped sheet kept bleeding a cape onto Sion. Fixes: camera pulled back to a one-fifth hard cap (v009 measured 40 percent); Kalagra cover attached for terrain and storm character with its retired smooth rendering explicitly excluded; swipe's rising kick restored; Graxo's cape re-specified to hang from the collar over both shoulders with arms clear; cape to muted aubergine and vest to walnut-brown; moon removed from frame; rider-to-machine proportion set at machine length about four times seated rider height; long flat dust banners added behind each machine for movement; Sion's no-cape guard hardened after a cape appeared on her; and the ground repalettised from cold blue to warm ochre-brown so the speeders sit in the landscape instead of against it.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f0ad-4ca4-7510-93b7-b070ed78ecde/exec-0a6aee53-ecb9-4fd6-a0b5-1f208c0d38d5.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/vehicles/hire-speeder/reference.png; frozen assets/vehicles/hire-speeder/candidates/v006/image.png
- Image 3 IDENTITY: outputs/kalagra-crater-city-cover/v007/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.72 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: Large step forward; most of the ten fixes landed. WARM GROUND is the big win: the plain is now muted ochre and warm grey-brown with warm shadow, sharing the speeders' livery family, so the machines read as part of the country instead of cut-outs pasted onto cold blue. The cool blues are confined to sky and storm, as asked. MOVEMENT: each machine now trails a long dust banner streaming back toward the storm with a low skirt kicking out beneath its lift pods, and the picture finally reads as three machines travelling at speed rather than parked. NO MOON: the sky holds only storm and dark, with the moonlight coming from off-frame; the crew stay legible under it. SION HAS NO CAPE: her only streaming item is the slim teal scarf, and her ochre jacket ends at the hips — the erroneous cape from v009 is gone. GRAXO'S CAPE HANGS CORRECTLY: from the collar, across both shoulders, down his back and streaming behind, with both arms clear of it and nothing passing under an arm. His vest has also moved toward the dark brown his description specifies. GROUP: Daxus far left, Graxo nearest and centre, Sion right and mid-distance — different depths, uneven gaps, no straight line. SCALE improved from v009's 40 percent to about 29 percent of frame width for the nearest machine, though still above the one-fifth cap that was asked for. DISCREPANCIES: (1) DAXUS'S IDENTITY HAS DRIFTED — his skin reads dark here, where description v1 specifies light-to-medium skin. This is a direct consequence of dropping the three character identity sheets to stay under image_gen's five-reference cap; carrying him in text alone was not enough to hold his likeness. (2) The nearest speeder is still about 29 percent of frame width against a one-fifth cap. (3) Graxo's cape still reads crimson-purple rather than a properly muted aubergine, though closer than v009. (4) The dust banners are billowy and soft-edged where flat opaque shapes with hard torn edges were specified. (5) The ground keeps its all-over dashed dry-brush hatch, now warm rather than blue — improved in colour, unimproved in texture. (6) File is 2.72 MB, over the 2.5 MB book-float budget. The user has since said the Kalagra reference is not needed, which frees the slot to restore all three character sheets and fix the Daxus drift.

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
Image 2 is IDENTITY: The APPROVED REFERENCE SHEET for the Kalagra hire speeder. Copy the machine exactly — prow leading, rider straddling a saddle toward the rear with boots on flank stirrups, boom and engine pod trailing at the tail, ventral skid, and the sunset swipe with its rising kick and widening toward the tail. It is also the authority on how big a rider is relative to the machine. Ignore the sheet itself: its grey background, five-view layout, panels and its own generic rider.
Image 3 is IDENTITY: KALAGRA — the planet's approved cover painting, for TERRAIN AND WEATHER ONLY: the fractured angular strata of its rock, its terraces, ridges and mesas, and the character of its vast dust storm shot through with lightning. IGNORE ITS RENDERING COMPLETELY — it is painted in an older retired style, smooth and airbrushed with fine speckled detail, and none of that belongs here. Do not copy its daylight sky, its crater city, its dome, its spacecraft or its moon.

TASK: A single 3:2 horizontal wide night illustration: the crew of the Antares small against an immense barren Kalagra plain, riding three hire speeders toward the viewer in a loose scattered group with long dust banners streaming behind them, the planet-wide storm filling the whole horizon, no moon in frame.

THE MACHINES — three Kalagra hire speeders, one per rider, all identical in design. Image 2 is their APPROVED REFERENCE SHEET and is the authority on every part of them. Copy the machine it shows and ignore the sheet itself: ignore its grey background, its five-view layout, its separate panels and its own generic rider.

From that sheet, the machine is: a long, low hover speeder, about three times as long as it is tall. The PROW leads — a blunt, slightly raked nose with a small forward grille — and nothing projects ahead of it. Behind the prow runs the long body, its upper deck carrying the paint. The RIDER STRADDLES the machine toward the REAR, sitting ON a narrow saddle that stands proud of the hull spine, one leg down each flank, each boot resting on a flat angled stirrup bracket that projects from that flank just ahead of the saddle. The rider leans forward onto a short handlebar yoke on a low cowl with a small windscreen. Behind the rider, a slim boom with two or three tidy parallel tubes reaches BACKWARD to a fat cylindrical ENGINE POD at the very TAIL, mouth facing backward, with angular vanes beneath it. A flat grey skid pod runs beneath the mid-hull. Every machine hovers a hand's breadth clear of the ground with clear daylight and a cast shadow beneath it.

NEVER: no wheels, tyres, rims, spokes, forks or mudguards; no antenna or aerial anywhere; no engine pod at the nose; no enclosed cockpit, tub or cabin; nobody sitting down inside the machine.

THE PAINT, from the same sheet: pale cream and ivory hull over a dark brown lower body, with the 1970s sunset swipe along the flank — narrow cream, golden yellow, orange, red-orange and dark brown bands.

THE SWIPE MUST KEEP ITS ANGLE. This is its defining feature and the last attempt flattened it out. The bands run LEVEL AND NARROW along the front half of the hull, and then, over the rear half, they all SWEEP UPWARD TOGETHER in one smooth continuous curve, climbing clearly toward the tail and WIDENING as they rise, so the whole band group is noticeably deeper at the back than at the front. It is a rising kick, not a straight horizontal stripe running the length of the machine. If the bands look level from nose to tail, it is wrong. The curve should be obvious at a glance even at small size.

The tail engine pod is the swipe's deep red-orange rust with one cream band at its collar. Flat opaque colour, hard clean edges, honest chipped and sand-scoured wear.

RIDER-TO-MACHINE SCALE — THE MACHINE IS BIG AND THE RIDER DOES NOT DOMINATE IT. The last attempt drew the riders oversized, perched on machines that looked like scooters under them. Fix the proportion:
- The speeder's total length, prow to the back of the tail engine pod, is about FOUR TIMES the rider's seated height measured from the saddle to the top of their head.
- There is a LONG run of hull in front of the rider — the whole prow and body stretch well ahead of their hands — and the boom and engine pod extend well behind them.
- The hull is WIDER than the rider's hips and shoulders: their legs hang down the outside of a body that is broader than they are, and their knees sit well inside the machine's widest point.
- A rider should look like someone riding a long, heavy machine, not someone sitting on a small one. If the figure reads as large relative to the hull, make the figure SMALLER, never the machine bigger.
- All three riders are in correct proportion to their own machines, and the three machines are identical in size to one another.

THE RIDERS — no identity sheets are attached for them, so paint each person from the description that follows. These descriptions are the authority on their faces, hair, clothing and equipment.

GRAXO VOSS below: adult man, weathered elongated angular face, long projecting nose with a broad softly rounded bulbous tip, neat dark-brown mustache, dark brown hair swept up with clearly visible silver-gray at both sides and temples. Ivory long-sleeved shirt, plum ascot, and a fitted vest in DARK WALNUT BROWN — a deep cool brown, NOT ochre, NOT mustard, NOT gold.

HIS CAPE — COLOUR: deep muted AUBERGINE, a dusky desaturated purple-brown, like dark aubergine skin. It is NOT magenta, NOT crimson, NOT scarlet, NOT hot pink, and it does not glow. Under moonlight it reads as a dark, cool purple mass.

HIS CAPE — HOW IT HANGS, which the last attempt got wrong: the cape fastens at his THROAT, at a high standing collar, with the two square antique-gold medallion pins at its front edges, one either side of the collar. From there it lies ACROSS THE TOP OF BOTH SHOULDERS and falls down his BACK, streaming out behind him in the wind.

Both of his arms are IN FRONT OF the cape and completely clear of it. The fabric passes OVER each shoulder and NEVER under an arm, NEVER through an armpit, NEVER beneath an elbow, and NEVER wrapped around or across his chest. No part of the cape crosses in front of his body below the collar, and no part of it emerges from beneath either arm. It is a cloak worn over the shoulders with the arms free — not a sash, not a toga, not a scarf threaded under one arm.

SION TILL below: young adult woman, medium warm skin, dark shoulder-length hair blown back. Large dark-framed goggles with OPAQUE MIRRORED RUBY-RED lenses — one flat red surface with a single pale diagonal streak, completely concealing her eyes and eyebrows; never paint eye shapes, pupils or eyebrows on or above them. Worn OCHRE utility jacket over a black shirt, right arm sleeved, LEFT sleeve absent at the shoulder. Slim TEAL scarf streaming. Her anatomical LEFT arm is a bare steel-gray cyber arm from shoulder to five-fingered hand; her right arm is natural skin.

DAXUS SKYE below: youthful adult man, broad sturdy build, thin metal-framed glasses, dark brown hair with cropped sides and a neat swept-back wave. Short OFF-WHITE medical jacket with a high collar and a broad inverted-V opening showing a BURNT-ORANGE shirt, orange-red sleeve patches with pale medical crosses, and a broad dark-brown bandolier from his right shoulder to his left hip carrying an ivory scanner at the chest.

ONLY GRAXO WEARS A CAPE — AND THE LAST ATTEMPT PUT ONE ON SION, WHICH IS WRONG. Exactly ONE cape exists in this entire picture and it belongs to Graxo.

SION HAS NO CAPE. Nothing hangs from Sion's shoulders. She wears no cape, cloak, cloak-collar, poncho, shawl, mantle, coat-tail, banner or sheet of fabric of any kind, and nothing broad trails behind her back. Her jacket is a short, close-fitting ochre utility jacket that ends at her hips and does not flare, billow or extend past her body. The ONLY thing of hers that streams in the wind is her SLIM TEAL SCARF: a narrow ribbon of cloth at her throat, no wider than her neck, which must never broaden into a sheet, a wing or a cape-like shape behind her. If anything wide is trailing from Sion, it is an error — remove it.

DAXUS HAS NO CAPE either: his short off-white medical jacket is close-fitting, ends at the hips, and nothing of his trails at all.

Do not let Graxo's cape bleed onto either of the others. One cape, one man.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame. THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. It is NOT a 2:1 banner, NOT a panorama, NOT a letterbox strip, NOT a square. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO labels, NO text of any kind. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors, composition or its close-up framing. Image 2 contributes the SPEEDER'S DESIGN ONLY — copy the machine, not the sheet: ignore its grey background, its five-view layout, its panels and its own generic rider. Image 3 contributes KALAGRA'S TERRAIN AND WEATHER ONLY — the shapes of its land and the character of its storm — and NOT its rendering: it is painted in an older, retired style, all smooth airbrushed blending, fine speckled rock detail and glossy highlights, and NONE of that belongs here. Do not copy its finish, its daylight blue sky, its crater city, its dome, its spacecraft or its moon. There are only three reference images. The three riders are described in words below and have no sheet attached; paint them from that description.

SCENE: "The Ride Out." NIGHT on the barren planet Kalagra. The crew of the Antares are crossing an immense empty plain on three hire speeders, riding hard through the dark, with the planet-wide storm standing along the whole horizon behind them.

THERE ARE EXACTLY THREE PEOPLE AND THREE MACHINES. Nobody is chasing them. There are no pursuers, no raiders, no bandits, no gang, no other vehicles, no distant riders, no dust plumes from unseen machines and no figures anywhere on the horizon. Three riders, three speeders, empty country.

THE CAMERA FACES THEM. The viewer stands ahead of the oncoming riders and low, roughly at the height of the machines. All three come TOWARD the viewer in front three-quarter view: we see their faces and chests, the prow of each hull coming at us, and enough of each machine's near flank that the sunset swipe reads along its length. No rider's back is turned to us and we are not looking down on their decks from above.

THE GROUP — RIDING TOGETHER, BUT NOT IN A LINE. This matters. They are a loose, scattered group, NOT a formation, NOT a rank, NOT three machines evenly spaced across the frame, and NOT three machines strung along one straight diagonal. Break it up:
- Each rider is at a DIFFERENT DISTANCE from the viewer. One is clearly the nearest and largest. One is a good way further back and noticeably smaller. One is somewhere between them — and not at the midpoint of the other two.
- Their lateral spacing is UNEVEN: two of them run closer together, the third set well apart from that pair.
- The gaps between them differ in both depth and width, so no two spacings match.
- They are not aligned on any straight line, and their noses are not level with one another.
- Vary them: one runs slightly ahead and lower, one holds back, one drifts wide. It should look like three people travelling together across open country, each riding their own line, not a parade.

SCALE AND FRAMING — A WIDE SHOT, AND THE LAST ONE WAS TOO CLOSE. Its nearest speeder filled about 40 percent of the frame's width, which killed any sense of scale. Stand well back.
- HARD CAP: the NEAREST speeder spans NO MORE than ONE FIFTH of the frame's width — about 20 percent — and one sixth is better. The others are smaller again. If you are unsure, paint them SMALLER. It is not possible to make them too small for this brief.
- Each rider is roughly ONE TENTH of the frame's height. Faces are small: five to eight flat planes each, no more. Do NOT enlarge anyone to show their face — at this distance identity comes from silhouette and colour.
- THE POINT OF THE SHOT IS SCALE: the plain must feel enormous and the riders tiny within it. Give the land and the storm far more of the picture than the machines.
- The three machines occupy a band across the middle of the picture. Above them is a broad sweep of night sky and storm; below them, open plain running down toward the viewer.
- Do NOT crop in. No hull touches any edge of the frame.

MOVEMENT — THEY MUST LOOK LIKE THEY ARE MOVING FAST. The last attempt read as three machines parked in a landscape. Fix it with dust:
- Each speeder throws a long DUST BANNER streaming out BEHIND it, away from the viewer and back toward the storm, low to the ground and stretching a good distance — several machine-lengths — so the eye reads a wake. The three banners are at different lengths and angles, matching each rider's own line.
- Under each machine, where its lift pods press the rock, a low flat skirt of disturbed dust kicks outward to the sides.
- Paint all of it as FLAT OPAQUE SHAPES with hard, ragged, torn edges — two or three tones of pale dusty bone and warm grey per banner, catching the moonlight on their upper edges and falling dark underneath. NO soft clouds, NO airbrushed billows, NO gradients, NO transparency, NO speckled particles.
- The riders lean forward into the run, and Graxo's cape and Sion's scarf stream back hard, in the same direction as the dust.

THE LAND, taking its forms from image 3: an immense barren plain of rock, laid out in broad terraces, shelves and fractured slabs stepping away toward the horizon, cut by dry channels, with jagged ridges and flat-topped mesas standing in the middle and far distance. Kalagra's rock is fractured and angular, splitting along hard strata — take that character from image 3, but paint it in THIS picture's flat planes and night palette, never in image 3's smooth airbrushed finish. Build ALL of it from a FEW LARGE FLAT PLANES of solid colour with hard, crisply angled edges — broad calm fields meeting along clean seams. Drawing and detail belong ONLY at those seams: the shelf lips, the mesa crests. The interior of every large plane stays QUIET, FLAT and UNDER-DETAILED. Do NOT break the ground into a carpet of small chips, facets, pebbles, dashes, hatching or mosaic tiles.

THE STORM, BEHIND THEM, FILLING THE HORIZON — take its character from image 3, where it stands as a vast rolling wall of dust and cloud shot through with lightning. It must READ UNMISTAKABLY AS WEATHER, NOT AS MOUNTAINS. Paint it as a towering wall of CLOUD spanning the full width of the picture: a mass of deep cobalt and blue-violet with a soft-shouldered, billowing, rolling top edge made of stacked rounded cloud heads — no rock facets, no strata, no cliff faces, no hard geological silhouette. Its base is a ragged curtain of falling dust that swallows the ground at the far horizon, so the plain disappears INTO it rather than meeting it at a clean line. It is tall: it fills much of the upper half of the picture behind the riders. Several thin branching bolts of pale yellow-white LIGHTNING fork inside it, and they are the brightest things in the image. It is still far off — the air around the riders is clear, with no haze or murk near them.

LIGHT — NIGHT, MOONLIT, BUT THE MOON ITSELF IS NOT IN FRAME. This is a night picture and it must read as one: dark overall, with a small number of clear lit shapes.
- DO NOT PAINT A MOON. There is no moon, no moon disc, no crescent and no bright orb anywhere in this picture. The sky holds only the storm and the dark. The moonlight comes from off-frame, above and behind the viewer.
- That off-frame moonlight is the only light on the riders. It falls from above and slightly behind the viewer, so the TOPS and FRONTS of the riders and machines catch it: one flat, cool, pale plane along each upper hull, each shoulder, each helmet and face. Everything turned away from it — undersides, far flanks, the ground beneath them — falls into a single deep slate blue-violet shadow plane. The light is generous: this is a dark picture, but the crew and their machines stay clearly legible.
- THE GROUND IS WARM, NOT BLUE. The last attempt made the plain cold blue-grey, which left the machines standing out against it like cut-outs. Kalagra's rock is a WARM DARK ochre-brown even at night: paint the lit terrace tops in muted dusty ochre, bone and warm grey-brown, and put the shadowed faces into a deep warm brown-violet rather than a cold slate blue. The ground should sit in the SAME family of colours as the speeders' cream, yellow, orange and brown livery, so the machines feel like they belong in this landscape instead of being pasted onto it. Keep the cool blues for the SKY and the storm only.
- Each speeder carries ONE small forward lamp at its prow, painted as a single flat pale-yellow shape throwing a short flat wedge of light onto the rock ahead of it. Painted shapes only: no glow, no bloom, no halo, no soft edges, no light rays, no volumetric beams.
- The sky is a deep blue-black, painted as large flat areas, paling a little toward the storm.
- No neon, no rim lighting, no bloom, no lens flare.

COLOUR: a warm dark earth below, a cool dark sky above. The GROUND, the dust and the machines share one warm family — muted ochre, bone, warm grey-brown and dull rust — so the speeders read as part of the country rather than against it. The SKY and the STORM are the cool notes: deep cobalt, blue-violet and blue-black. Under moonlight the machines' sunset swipe is muted — cream and yellow as pale bone, orange and rust as dull warm notes, the dark brown nearly black. The riders are dimmed to match: Graxo's aubergine cape a dark cool purple mass, Sion's ochre jacket muted and her teal scarf the one small cool accent on any rider, Daxus's off-white the palest thing among them. The three small prow lamps and the lightning are the brightest points.

Give it quiet and distance: three small machines running through the dark across an enormous plain, with a mountain of weather standing over the whole horizon behind them.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
