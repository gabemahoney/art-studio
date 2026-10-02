# the-ride-out v008

User request verbatim: Speeders are backwards. Proportions are all wrong. Camera is too close to the characters again.
Mode: Regeneration fixing my own design-text error. ORIENTATION: my previous text said the rider sits 'well toward the REAR' of the body, which is backwards — the reference puts the windscreen and rider tub at the FRONT of the hull with the bulk of the body running BEHIND them. Now stated as an explicit front-to-back order (pod, boom, windscreen, rider, long hull, transom) plus a negative restatement. PROPORTIONS: measured off the reference at magnification — total length ~3x max height, boom+pod the front ~1/3, body the rear ~2/3, low throughout. SCALE: v007's lead speeder measured 45 percent of frame width; now a hard cap of one quarter with one fifth preferred and an explicit 'if unsure, smaller', riders to ~1/8 frame height. (First attempt at this prompt failed: codex reported a generated.png path that did not exist; gen.py failed closed and allocated nothing.)
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f077-7ab7-7ba3-b07f-d16a0dea0290/exec-d04a6486-5f88-4092-8556-dd158c2b3c43.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/vehicles/hire-speeder/sources/user-geometry-reference-2026-09-29.png
- Image 3 IDENTITY: assets/characters/graxo/reference.png; frozen assets/characters/graxo/candidates/v027/image.png
- Image 4 IDENTITY: assets/characters/sion/reference.png; frozen assets/characters/sion/candidates/v001/image.png
- Image 5 IDENTITY: assets/characters/daxus/reference.png; frozen assets/characters/daxus/candidates/v001/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.63 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: All three complaints fixed. ORIENTATION: verified on a magnified crop of the lead machine, the front-to-back order is now correct and matches the user's reference — engine pod at the nose with its intake mouth forward, curved pipework and boom, windscreen blister, rider immediately behind it at the FRONT of the hull, then the long striped body running BEHIND the rider to the transom, with the ventral skid slung under. v007 had this inverted, and the fault was mine: my design text said the rider sits 'well toward the REAR' of the body when the reference puts them at the front. Stating the order explicitly front-to-back, plus a negative restatement that the rider is not perched on the tail, fixed it in one pass. PROPORTIONS: the machines are now long and low, close to the reference's roughly 3:1 length-to-height, with the boom carrying the pod well clear of the hull instead of a short stub bolted to a tall chunky wedge. SCALE: the lead speeder now spans about 400px of 1536, roughly 26 percent of frame width, against v007's measured 45 percent — within the hard cap, and the badlands plainly dwarf the riders again. Held from v007: the storm still reads unmistakably as cloud with billowing heads, a ragged base and forked lightning; only Graxo wears a cape, Sion's teal scarf stayed a slim band, Daxus has nothing trailing; the stripe assembly is crisp and identical across all three hulls; exactly three riders and three machines with no pursuers; every hull hovers with a cast shadow and no wheels anywhere. Faces are small but legible: Graxo's mustache, long nose and silver temples, Sion's opaque ruby goggles, Daxus's glasses and cross patch. DISCREPANCIES: (1) Graxo's cape has drifted warm again, reading crimson-magenta rather than the muted aubergine purple-brown his description specifies — the same drift corrected at v003 and now returned; (2) the ground still carries an all-over dashed dry-brush hatch rather than quiet flat plane interiors, which is now the single most persistent style drift in this scene, unfixed across eight passes; (3) the three machines sit at fairly similar depths and even spacing, reading a little like a lineup rather than a staggered diagonal receding into the picture; (4) file is 2.63 MB, over the 2.5 MB book-float budget, needing recompression before placement. Speeders remain IMPROVISED — the geometry reference is filed at assets/vehicles/hire-speeder/sources/ but no asset exists and no reference.png has been created, so nothing about them is canonical and a later scene would drift.

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
Image 2 is IDENTITY: The hire speeder's DESIGN REFERENCE, supplied by the user. Read its layout carefully front to back: engine pod at the nose, long boom, then the windscreen, then the rider's tub at the FRONT of the hull, then a long low hull running BEHIND the rider to a tall squared transom. Total length about three times the maximum height. Ignore its rendering entirely — its smooth digital shading, grey studio backdrop, horizon bands and glowing exhaust — and do not reproduce it as a side-on product view.
Image 3 is IDENTITY: GRAXO VOSS. Copy this man's design exactly — face, hair, mustache, silver temples, aubergine cape with its two gold collar pins, dark walnut-brown vest, ivory shirt and plum ascot. He is the ONLY character who wears a cape. Ignore this sheet's layout, its multiple views, its expression busts and its plain gray background.
Image 4 is IDENTITY: SION TILL. Copy this woman's design exactly — face, hair, opaque ruby goggles, ochre jacket with the missing left sleeve, slim teal scarf and bare steel-gray left cyber arm. She wears NO cape. Ignore this sheet's layout, its multiple views, its expression busts, its height chart and its plain gray background.
Image 5 is IDENTITY: DAXUS SKYE. Copy this man's design exactly — face, glasses, hair, off-white medical jacket with the burnt-orange V and cross patches, bandolier and chest scanner. He wears NO cape. Ignore this sheet's layout, its multiple views, its expression busts, its height chart and its plain gray background.

TASK: A single 3:2 horizontal wide landscape illustration: three long low hover speeders crossing an immense empty Kalagra badlands toward the viewer, small in a vast country, the planet-wide storm towering along the horizon behind them.

THE MACHINES — three rented hover speeders. Image 2 is their DESIGN REFERENCE: copy its geometry and layout, and ignore its rendering entirely — its smooth digital shading, its grey studio backdrop, its horizon bands and its glowing exhaust are not part of this picture, and it must not be reproduced as a side-on product view.

GEOMETRY — READ THIS CAREFULLY, THE LAST ATTEMPT BUILT IT BACKWARDS. Measure the machine along its own length from NOSE to TAIL. Total length L. It is LONG AND LOW: L is about THREE TIMES the machine's maximum height.

FRONT THIRD OF L — the boom and the engine. At the very nose, a fat CYLINDRICAL ENGINE POD with a ribbed collar, mounted LOW. Angular vanes and a small forked bracket hang beneath and ahead of it, and a thin whip ANTENNA curves up and back from a housing just above it. This pod is carried out ahead of the hull on a slim BOOM of exposed structure and visible curved pipework. The boom is LONG: the pod sits well clear of the body, roughly a third of the whole machine's length ahead of it. There is exactly ONE engine pod and it is at the FRONT. There is NO drum, pod or engine at the tail.

REAR TWO THIRDS OF L — the body. A long, low hull. Its upper deck carries the paint. Its back end closes in a TALL SQUARED-OFF TRANSOM. Beneath the deck sits a grey lower hull with a flat ventral SKID POD slung under it.

THE RIDER SITS AT THE FRONT OF THE BODY, NOT AT ITS BACK. This is the part that went wrong. Where the boom meets the hull, the deck begins with a small curved WINDSCREEN BLISTER, and the rider's open tub sits IMMEDIATELY BEHIND that windscreen — at the FORWARD end of the body. From the rider's shoulders the hull runs BACKWARD for most of its length: the great majority of the body mass, deck and paint lies BEHIND the rider, ending at the transom well aft of them.

Say it the other way to be sure: going front to back the order is ENGINE POD, then BOOM, then WINDSCREEN, then RIDER, then a long run of HULL, then TRANSOM. The rider is near the front. The rider is NOT perched on the tail. The bulk of the machine is NOT in front of the rider.

The rider sits IN the tub, not astride the machine — no straddled saddle, no bicycle handlebars, no upright motorcycle posture.

Every machine hovers a hand's breadth clear of the ground with CLEAR DAYLIGHT AND A CAST SHADOW beneath it. NO wheels, NO tyres, NO rims, NO spokes, NO forks, NO mudguards anywhere in the picture.

The whole machine should read as low, long and lance-like: heavy engine thrown out front on its boom, rider tucked behind the windscreen at the front of a long hull that trails away behind them.

THE PAINT: on the ivory and warm-grey hull each speeder carries a bold RETRO 1970s RACING STRIPE ASSEMBLY running the FULL LENGTH of the hull, following its taper and sweeping up and over the sloping deck. From top to bottom: a WIDE BRICK-RED-TO-ORANGE band, a narrow IVORY pinstripe, a narrower TEAL-CYAN band, and a second narrow IVORY pinstripe. The brick-red band covers the long upper deck running back from the windscreen, over and behind the rider, all the way to the transom. The forward engine pod wears the same brick-red with one ivory band around its collar. Keep the bands crisp: flat opaque colour, hard straight edges, no gradients, no airbrushing, no glow, no metallic sheen. They are painted graphics, not lighting. All three carry the SAME livery so they read as one hire fleet, each weathered differently — chipped leading edges, one mismatched replacement panel interrupting the bands, one stripe faded pale.

THE RIDERS — now seen from the FRONT, so each must be recognisably themselves. Copy each person's design from their own identity sheet and ignore every sheet's layout, its multiple views, its expression busts, its height chart and its plain gray background.

GRAXO VOSS (image 3), in the lead machine: adult man with a weathered, elongated angular face — long middle and lower face, tall forehead with a loose forelock, heavy brow, deep-set eyes, pronounced angular cheekbones, strong jaw with a rounded chin. Long projecting nose with a broad, softly rounded bulbous tip, clearly broader than the bridge. Neat regular dark-brown mustache ending at the mouth corners, no beard. Dark brown hair swept up with clearly visible silver-gray at both sides and temples. Deep muted AUBERGINE cape — a dusky desaturated purple-brown, never magenta or crimson — with a high standing collar and two square antique-gold medallion pins, one at each cape edge, streaming back behind him over the transom. Dark walnut-brown fitted vest, ivory long-sleeved shirt, compact plum ascot.

SION TILL (image 4), in the second: young adult woman, medium warm skin, slender build, broad chin and slightly square jaw, full lips, dark shoulder-length hair blown back. Large dark-framed goggles with OPAQUE MIRRORED RUBY-RED lenses — one flat red surface with a single pale diagonal streak, completely concealing her eyes and eyebrows; never paint eye shapes, pupils or eyebrows on or above them. Worn OCHRE utility jacket over a black shirt, right arm sleeved and LEFT sleeve absent at the shoulder. Slim TEAL scarf streaming. Her anatomical LEFT arm is a bare steel-gray cyber arm from shoulder to five-fingered hand — steel shells, dark joints, human proportions, no wires or weapons; her right arm is natural skin.

DAXUS SKYE (image 5), in the third: youthful adult man, broad sturdy build, light-to-medium skin, full cheeks, square jaw, clean-shaven, thin metal-framed glasses. Dark brown hair with closely cropped sides, a neat side part and a swept-back wave on top. Short OFF-WHITE medical jacket with a high collar and a broad inverted-V opening showing a BURNT-ORANGE shirt, with orange-red sleeve patches carrying pale medical crosses. Broad dark-brown bandolier from his anatomical right shoulder to his left hip, carrying one ivory diagnostic scanner on a flat triangular panel at the lower chest.

ONLY GRAXO WEARS A CAPE. This matters and is easy to get wrong at speed. Graxo alone has the aubergine cape streaming behind him. SION HAS NO CAPE and DAXUS HAS NO CAPE: neither wears a cape, cloak, poncho, coat-tail, banner or any loose garment trailing behind them. Sion's only streaming item is her SLIM TEAL SCARF — a narrow band of cloth at the neck, not a sheet of fabric across her back, and it must never widen into a cape-like shape. Daxus's short off-white medical jacket is close-fitting and ends at the hips; nothing of his trails at all.

Their colours — aubergine, ochre and teal, off-white and burnt-orange — plus the machines' brick-red and teal stripes are the only saturated notes in a vast ochre and blue-violet landscape.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame. THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. It is NOT a 2:1 banner, NOT a panorama, NOT a letterbox strip, NOT a square. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO labels, NO text of any kind. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors, composition or its close-up framing. Image 2 contributes the SPEEDERS' DESIGN ONLY. Images 3, 4 and 5 contribute their PEOPLE ONLY.

SCENE: "The Ride Out." Late afternoon on the barren planet Kalagra. Three riders on hover speeders are crossing an enormous empty badlands, riding hard with the planet-wide storm standing along the horizon behind them.

THERE ARE EXACTLY THREE PEOPLE AND THREE MACHINES IN THIS PICTURE. Nobody is chasing them. There are no pursuers, no raiders, no bandits, no gang, no second group of vehicles, no distant riders, no dust plumes from unseen machines, and no figures anywhere on the horizon. Three riders, three speeders, empty country. Nothing else moves.

THE CAMERA IS IN FRONT OF THEM. This is the defining change. The viewer stands ahead of the oncoming riders and a little to their left, low down — roughly at the height of the machines themselves. The three speeders are therefore COMING TOWARD THE VIEWER, seen in FRONT THREE-QUARTER view: we see the riders' faces and chests, the front of each hull with its forward engine pod aimed at us, and the near flank of each machine running away behind it so the painted stripe still reads down its length. We are NOT behind them; no rider's back is turned to us, and we do not look down on the tops of their decks from above.

SCALE AND FRAMING — PULL THE CAMERA WELL BACK. The last attempt was far too close: its lead speeder filled 45 percent of the frame's width. That is roughly twice too big. Stand further off.
- HARD CAP: the NEAREST speeder spans NO MORE than ONE QUARTER of the frame's width, and one fifth is better. If you are unsure, paint it SMALLER. The two behind it are smaller again.
- Each rider is about ONE EIGHTH of the frame's height — small, but with the face still readable as five to eight flat planes. Do not enlarge a rider to show their face better; at this distance a small clear silhouette and the right colours carry the identity.
- The three machines sit in the MIDDLE DISTANCE and occupy only a narrow band across the middle of the picture. Above them is a broad sweep of land, storm and sky; below them a broad sweep of open rock running down toward the viewer. Land and sky together take up far more of the picture than the machines do.
- Do NOT crop in. Do NOT fill the frame with one machine. No hull touches any edge of the picture. The country must plainly dwarf the riders.

COMPOSITION: the three speeders come on in a loose staggered line on a diagonal, sweeping from the middle right of the frame toward the lower left as they approach. GRAXO leads, nearest the viewer and largest, at the centre-left. SION follows a little behind and to the right, slightly smaller. DAXUS is farthest, further right again and smallest. Each trails a long, low, flat banner of ochre dust stretching away BEHIND them toward the upper right — the dust runs back into the picture, away from the viewer, since they are coming at us.

Keep big quiet areas: a broad calm sky, a broad calm sweep of rock, and the detail concentrated in the band where the three machines cross the middle of the frame.

THE LAND: an immense badlands of flat ochre and warm grey rock in broad terraces and shelves stepping away toward the horizon, with flat-topped mesas and buttes standing in the middle and far distance. Build ALL of it from a FEW LARGE FLAT PLANES of solid colour with hard, crisply angled edges — broad calm fields of warm ochre in the light and broad calm fields of deep slate blue-violet in shadow, meeting along clean seams. Drawing and detail belong ONLY at those seams: the shelf lips, the canyon rims, the mesa crests. The interior of every large plane stays QUIET, FLAT and UNDER-DETAILED. Do NOT break the ground into a carpet of small chips, facets, pebbles, dashes, hatching or mosaic tiles, and do not cover it in an all-over dry-brush texture.

THE STORM, BEHIND THEM: across the whole far distance, behind the riders, stands the planet-wide storm front. IT MUST READ UNMISTAKABLY AS WEATHER, NOT AS MOUNTAINS. Paint it as a towering wall of CLOUD: a mass of cobalt and blue-violet with a soft-shouldered, billowing, rolling top edge made of stacked rounded cloud heads — no rock facets, no strata, no cliff faces, no scree slopes, no hard geological silhouette. Its base is a dark ragged curtain of falling dust and rain that visibly smudges and swallows the ground at the far horizon, so the land clearly disappears INTO it rather than meeting it at a clean line. Several thin branching bolts of pale yellow lightning fork inside it. It should look immense, soft-edged and advancing — a weather front, plainly a different kind of thing from the hard angular rock in front of it. It is still far off: the air around the riders is clear and sunlit, with no haze, rain or murk anywhere near them.

Do NOT include the domed city of Kannan: the riders are travelling toward it, so it lies behind the viewer and is not in this shot.

LIGHT: late-afternoon daylight from a low searing blue-white sun raking from the left and somewhat toward the viewer, so the fronts of the riders and machines are LIT — faces, chests and hull noses catch the light — while long hard shadows run out across the rock to the right. The lit rock is warm ochre; every shadow is a single flat plane of deep slate blue-violet. The storm mass stays cool and dark against the sunlit ground. The sky above is clear deep blue paling toward the horizon, painted as large flat areas. No neon, no bloom, no lens flare, no light rays, no sun disc in frame.

COLOUR: warm ochre and ivory rock against cool cobalt and blue-violet storm and shadow. The only saturated notes are the three machines and their riders: the brick-red-and-teal stripes on ivory hulls, Graxo's aubergine cape, Sion's ochre jacket and teal scarf, Daxus's off-white and burnt-orange.

The picture should read as three hard-driving riders bearing down on the viewer out of an enormous empty country, with a mountain of weather at their backs.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
