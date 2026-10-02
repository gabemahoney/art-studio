# the-ride-out v007

User request verbatim: The speeders look sick but we should position the camera in front of the characters so we can see them better. / Oh also only Graxo has a cape!
Mode: Fresh generation off the v006 wide direction, camera flipped to FRONT three-quarter so the riders come toward the viewer and their faces read. Scale brought up modestly (speeder ~1/4 frame width, rider ~1/6 frame height) while keeping the landscape dominant. Character IDENTITY sheets re-attached, since faces are now legible and identity matters again. Kannan omitted — the crew ride toward it, so it is behind the camera. Storm moved behind them and respecified as unmistakable CLOUD (billowing rounded heads, ragged rain curtain swallowing the horizon) after v006's read as a rock range. Explicit cape guard: only Graxo has a cape; Sion's teal scarf must stay a slim scarf. Tail engine drum removed — the forward pod is the only engine. Ground restated against the all-over dry-brush hatch.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f06f-d917-7dc1-bfee-926f0615bc50/exec-07d20148-8d74-432d-b772-d8013ace80f7.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
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
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.73 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: Camera flip succeeded and the storm is fixed. The viewer is now ahead of the riders and low: all three come toward us in front three-quarter, faces and chests lit and legible, forward engine pods aimed at the camera, near flanks still angled enough that the full stripe assembly reads down each hull. No rider's back is turned. THE STORM NOW READS AS WEATHER: a towering wall of cobalt and blue-violet cloud with billowing rounded heads and a ragged base that swallows the far horizon, forked with lightning -- unmistakably a front rather than v006's ambiguous rock range. Respecifying it as cloud anatomy (rounded heads, rain curtain, land disappearing INTO it) rather than as a dark mass is what fixed it. CAPE GUARD HELD: only Graxo wears a cape; Sion's teal scarf stayed a slim streaming band and never widened into fabric across her back; Daxus has nothing trailing. Identity verified on a magnified crop of Sion: opaque ruby goggles with no eyes or eyebrows painted, ochre jacket with the left sleeve absent at the shoulder, black shirt beneath, and the bare steel-gray cyber arm on her anatomical LEFT -- appearing to the viewer's right as it must with her facing us. Graxo's elongated face, long broad-tipped nose, mustache, silver temples, both gold collar pins and plum ascot all read; Daxus's glasses, cross patch and bandolier read. Speeder geometry held with the tail drum correctly removed -- a single forward engine pod on its boom, whip antenna, ventral skid, rider seated in the tub behind a windscreen, clear shadow beneath every hull, no wheels. Stripes are crisp and identical across all three machines. DISCREPANCIES: (1) SCALE DRIFT -- the lead speeder spans 690px of 1536, about 45 percent of the frame width, against a specified 25 percent. Moving the camera in front pulled it substantially closer than the wide framing the user asked for two turns ago; the land no longer dwarfs the riders the way it did in v006. This is the main open question and it sits between two user instructions (zoom out, versus see the crew better). (2) The ground still carries an all-over dashed dry-brush hatch instead of quiet flat plane interiors -- the most persistent style drift in this scene across every pass. (3) Graxo's vest reads ochre-mustard rather than the dark walnut-brown his description specifies. (4) File is 2.73 MB, over the 2.5 MB book-float budget, needing recompression before placement. Speeders remain IMPROVISED -- the user's geometry reference is filed at assets/vehicles/hire-speeder/sources/ but no asset exists and no reference.png has been created, so nothing about them is canonical.

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
Image 2 is IDENTITY: The hire speeder's DESIGN REFERENCE, supplied by the user. Copy its geometry: the long low wedge body, the rider's tub set well back under a small windscreen, the slim boom reaching forward to a single fat cylindrical engine pod, the vanes and whip antenna at the front, the ventral skid, the squared-off transom. Ignore its rendering entirely — its smooth digital shading, grey studio backdrop, horizon bands and glowing exhaust — and do not reproduce it as a side-on product view.
Image 3 is IDENTITY: GRAXO VOSS. Copy this man's design exactly — face, hair, mustache, silver temples, aubergine cape with its two gold collar pins, vest, ivory shirt and plum ascot. He is the ONLY character who wears a cape. Ignore this sheet's layout, its multiple views, its expression busts and its plain gray background.
Image 4 is IDENTITY: SION TILL. Copy this woman's design exactly — face, hair, opaque ruby goggles, ochre jacket with the missing left sleeve, slim teal scarf and bare steel-gray left cyber arm. She wears NO cape. Ignore this sheet's layout, its multiple views, its expression busts, its height chart and its plain gray background.
Image 5 is IDENTITY: DAXUS SKYE. Copy this man's design exactly — face, glasses, hair, off-white medical jacket with the burnt-orange V and cross patches, bandolier and chest scanner. He wears NO cape. Ignore this sheet's layout, its multiple views, its expression busts, its height chart and its plain gray background.

TASK: A single 3:2 horizontal wide landscape illustration: three hover speeders bearing down on the viewer across an immense empty Kalagra badlands, the planet-wide storm towering along the horizon behind them.

THE MACHINES — three rented hover speeders. Image 2 is their DESIGN REFERENCE: copy its geometry and layout, and ignore its rendering entirely — its smooth digital shading, its grey studio backdrop, its horizon bands and its glowing exhaust are not part of this picture, and it must not be reproduced as a side-on product view.

GEOMETRY, built from back to front:
- The REAR two thirds is the body: a long, low, wedge-shaped hull whose upper deck slopes down toward the front and whose flat squared-off transom closes the back.
- The RIDER sits in an open tub set into the top of that body, well toward the REAR, with a small curved windscreen blister rising in front of them. They sit IN the machine, not astride it — no straddled saddle, no bicycle handlebars, no upright motorcycle posture.
- From the front of the body a long slim BOOM reaches forward, well out ahead of the rider, carrying a fat CYLINDRICAL ENGINE POD slung at its far end like a lance point: a drum with a ribbed collar and small canted fins at its nose. This forward pod is the machine's signature and it is the ONLY engine pod — there is no second drum at the tail.
- Angular VANES and a forked structure hang beneath the boom, and a thin whip ANTENNA curves up and back from the front.
- A flat ventral SKID POD runs beneath the body.
- Every machine hovers a hand's breadth clear of the ground with CLEAR DAYLIGHT AND A CAST SHADOW beneath it. NO wheels, NO tyres, NO rims, NO spokes, NO forks, NO mudguards anywhere in the picture.

Overall each machine is long and lean, roughly four times as long as it is tall, reading as a thrown lance with its heavy engine out front and its rider tucked at the back.

THE PAINT: on the ivory and warm-grey hull each speeder carries a bold RETRO 1970s RACING STRIPE ASSEMBLY running the FULL LENGTH of the hull, following its taper and sweeping up and over the sloping deck. From top to bottom: a WIDE BRICK-RED-TO-ORANGE band, a narrow IVORY pinstripe, a narrower TEAL-CYAN band, and a second narrow IVORY pinstripe. The brick-red band covers the sloping upper deck behind the windscreen. The forward engine pod wears the same brick-red with one ivory band around its collar. Keep the bands crisp: flat opaque colour, hard straight edges, no gradients, no airbrushing, no glow, no metallic sheen. They are painted graphics, not lighting. All three carry the SAME livery so they read as one hire fleet, each weathered differently — chipped leading edges, one mismatched replacement panel interrupting the bands, one stripe faded pale.

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

SCALE AND FRAMING — still a wide landscape, but close enough to read the crew:
- Each speeder spans roughly ONE QUARTER of the frame's width.
- Each rider's head and torso are clearly legible: a rider is about ONE SIXTH of the frame's height. Faces are small but readable — a face here is five to eight flat planes, no more.
- The three machines occupy the lower-middle band of the picture. Above them is a broad sweep of land, storm and sky; below them is open rock running down toward the viewer.
- Do NOT crop in tight. Do NOT fill the frame with one machine. No hull touches the edge of the picture, and the land still plainly dwarfs the riders.

COMPOSITION: the three speeders come on in a loose staggered line on a diagonal, sweeping from the middle right of the frame toward the lower left as they approach. GRAXO leads, nearest the viewer and largest, at the centre-left. SION follows a little behind and to the right, slightly smaller. DAXUS is farthest, further right again and smallest. Each trails a long, low, flat banner of ochre dust stretching away BEHIND them toward the upper right — the dust runs back into the picture, away from the viewer, since they are coming at us.

Keep big quiet areas: a broad calm sky, a broad calm sweep of rock, and the detail concentrated in the band where the three machines cross the middle of the frame.

THE LAND: an immense badlands of flat ochre and warm grey rock in broad terraces and shelves stepping away toward the horizon, with flat-topped mesas and buttes standing in the middle and far distance. Build ALL of it from a FEW LARGE FLAT PLANES of solid colour with hard, crisply angled edges — broad calm fields of warm ochre in the light and broad calm fields of deep slate blue-violet in shadow, meeting along clean seams. Drawing and detail belong ONLY at those seams: the shelf lips, the canyon rims, the mesa crests. The interior of every large plane stays QUIET, FLAT and UNDER-DETAILED. Do NOT break the ground into a carpet of small chips, facets, pebbles, dashes, hatching or mosaic tiles, and do not cover it in an all-over dry-brush texture.

THE STORM, BEHIND THEM: across the whole far distance, behind the riders, stands the planet-wide storm front. IT MUST READ UNMISTAKABLY AS WEATHER, NOT AS MOUNTAINS. Paint it as a towering wall of CLOUD: a mass of cobalt and blue-violet with a soft-shouldered, billowing, rolling top edge made of stacked rounded cloud heads — no rock facets, no strata, no cliff faces, no scree slopes, no hard geological silhouette. Its base is a dark ragged curtain of falling dust and rain that visibly smudges and swallows the ground at the far horizon, so the land clearly disappears INTO it rather than meeting it at a clean line. Several thin branching bolts of pale yellow lightning fork inside it. It should look immense, soft-edged and advancing — a weather front, plainly a different kind of thing from the hard angular rock in front of it. It is still far off: the air around the riders is clear and sunlit, with no haze, rain or murk anywhere near them.

Do NOT include the domed city of Kannan: the riders are travelling toward it, so it lies behind the viewer and is not in this shot.

LIGHT: late-afternoon daylight from a low searing blue-white sun raking from the left and somewhat toward the viewer, so the fronts of the riders and machines are LIT — faces, chests and hull noses catch the light — while long hard shadows run out across the rock to the right. The lit rock is warm ochre; every shadow is a single flat plane of deep slate blue-violet. The storm mass stays cool and dark against the sunlit ground. The sky above is clear deep blue paling toward the horizon, painted as large flat areas. No neon, no bloom, no lens flare, no light rays, no sun disc in frame.

COLOUR: warm ochre and ivory rock against cool cobalt and blue-violet storm and shadow. The only saturated notes are the three machines and their riders: the brick-red-and-teal stripes on ivory hulls, Graxo's aubergine cape, Sion's ochre jacket and teal scarf, Daxus's off-white and burnt-orange.

The picture should read as three hard-driving riders bearing down on the viewer out of an enormous empty country, with a mountain of weather at their backs.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
