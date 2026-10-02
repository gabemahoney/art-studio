# the-ride-out v006

User request verbatim: Lets try a real re-framing. It looks a little goofy. I think we're trying to add too much having the raiders. Lets have the shot be more zoomed out, the characters and the speeders less BIG in the frame. Give you more room to make the speeders look interesting. Also, can we find a way to add one of these retro 70s color stripes to them (see the vehicle in the back) / here is an idea for the speeder geometry
Mode: Fresh wide re-framing, abandoning the v001-v005 close-up line. Raiders REMOVED at user direction (overcrowding the frame); camera pulled well back so each speeder spans ~1/5 frame width and riders are under 1/10 frame height. Character IDENTITY sheets deliberately NOT attached — at this scale a face is ~15px, so rules.md's escalation ladder ('full source, crop, or nothing') says nothing, and attaching them drags scale up; crew carried by colour and silhouette in the design text instead. Speeder geometry now from a user-supplied design reference filed at assets/vehicles/hire-speeder/sources/. Retro 70s stripe assembly (brick-red / ivory / teal-cyan / ivory) added per user request, described in words rather than attaching the user's painting screenshot to avoid leaking its characters.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f06b-2c92-7673-9ced-05392fbb2020/exec-90ee335c-f9d9-42b8-bac2-c786a2d391d6.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/vehicles/hire-speeder/sources/user-geometry-reference-2026-09-29.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.71 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: The re-framing works and this is a different and better picture. Scale: the camera is well back and somewhat elevated, the nearest speeder spans roughly a fifth of the frame width, the riders are small enough that no face is attempted, and the land genuinely dwarfs them -- which was the point. Raiders are gone entirely at user direction; exactly three machines and three riders, no pursuers, no figures on any ridge. Speeder geometry came across from the user's design reference closely: long low wedge body, rider seated IN a tub set well back behind a small curved windscreen rather than astride a saddle, slim boom reaching forward to a fat cylindrical engine pod, whip antenna curving up at the front, angular vanes beneath, ventral skid, squared-off transom, and clear daylight and cast shadow under every hull with no wheels anywhere. The retro 1970s stripe assembly landed exactly as asked: a wide brick-red band, ivory pinstripe, teal-cyan band and second ivory pinstripe running the full length of each ivory hull and sweeping over the sloping deck, crisp and flat with no gradient or sheen, the same livery on all three so they read as one hire fleet. Crew read purely by colour and silhouette as intended: Graxo's aubergine cape streaming as a dark purple banner, Sion's ochre jacket and teal scarf, Daxus's off-white. Kannan's dome and spires sit small and pale in the middle distance, the storm mass fills the far horizon with two branching bolts of lightning, and the long raking shadows across the terraces do real compositional work. Discrepancies: (1) the ground still carries an all-over dry-brush hatch rather than the fully quiet interiors asked for, though the large terrace forms are correctly broad and flat -- much improved on v002 but not clean; (2) the storm mass reads somewhat ambiguously as a dark mountain range, and is only clearly weather because of the lightning inside it; (3) each speeder has a red drum at the tail as well as on the forward boom, where the reference has the engine pod only at the front -- it reads fine as twin pods but is an addition; (4) the file is 2.71 MB, over the 2.5 MB book-float budget, and needs recompression before placement. Speeders remain IMPROVISED: the user's geometry reference is filed at assets/vehicles/hire-speeder/sources/ but no asset has been created and no reference.png exists, so nothing here is canonical yet. If the speeder is to recur, it should become a real asset.

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
Image 2 is IDENTITY: The hire speeder's DESIGN REFERENCE, supplied by the user. Copy its geometry: the long low wedge body with the rider's tub set well back under a small windscreen, the slim boom reaching forward to a fat cylindrical engine pod, the vanes and whip antenna at the front, the ventral skid, the squared-off transom. Ignore its rendering entirely — its smooth digital shading, grey studio backdrop, horizon bands and glowing exhaust are not part of this picture.

TASK: A single 3:2 horizontal wide landscape illustration: three small hover speeders crossing an immense empty Kalagra badlands toward the distant domed city of Kannan, the planet-wide storm standing along the whole horizon.

THE MACHINES — three rented hover speeders, and they are the subject of this picture. Image 2 is the DESIGN REFERENCE for their geometry: copy its shapes and its layout, and ignore its rendering entirely — its smooth digital shading, its grey studio backdrop, its horizon bands and its glowing exhaust are not part of this picture.

GEOMETRY, read off image 2 and built from back to front:

- The REAR two thirds is the body: a long, low, wedge-shaped hull whose upper deck slopes down toward the front and whose flat squared-off transom closes the back. It sits deeper than the rest of the machine.
- The RIDER sits in an open tub set into the top of that body, well toward the REAR, with a small curved windscreen blister rising in front of them. They sit IN the machine, not astride it — no straddled saddle, no bicycle handlebars, no upright motorcycle posture.
- From the front of the body a long slim BOOM reaches forward, well out ahead of the rider, carrying a big CYLINDRICAL ENGINE POD slung at its far end like a lance point. That forward pod is the machine's signature: a fat drum with a ribbed collar and small canted fins at its nose.
- Below and ahead, angular VANES and a forked structure hang beneath the boom, with a thin whip ANTENNA curving up and back from the front of the machine.
- Beneath the body runs a flat ventral SKID POD.
- The whole machine hovers a hand's breadth clear of the ground with CLEAR DAYLIGHT AND A CAST SHADOW beneath it. NO wheels, NO tyres, NO rims, NO spokes, NO forks, NO mudguards anywhere in the picture.

Overall the machine is long and lean — roughly four times as long as it is tall — and it reads as a thrown lance with its heavy engine out front and its rider tucked at the back.

THE PAINT — this is the other important part. On the ivory and warm-grey hull each speeder carries a bold RETRO 1970s RACING STRIPE ASSEMBLY, the kind painted down the flank of a science-fiction adventure vehicle on a paperback cover: a set of parallel bands running the FULL LENGTH of the hull, following its taper and sweeping UP AND OVER the sloping deck at the front.

From top to bottom each assembly is: a WIDE BRICK-RED-TO-ORANGE band, a narrow IVORY pinstripe, a narrower TEAL-CYAN band, and a second narrow IVORY pinstripe. The brick-red band covers the sloping upper deck behind the windscreen, as image 2's rust-coloured deck panel does. The forward engine pod wears the same brick-red with one ivory band around its collar.

Keep the bands crisp: flat opaque colour with hard straight edges. No gradients, no airbrushing, no glow, no metallic sheen, no reflections. They are painted graphics, not lighting.

The three machines carry the SAME stripe assembly so they read as one hire fleet, but each is weathered differently: chipped and sand-scoured along the leading edges, one with a mismatched replacement panel interrupting the bands, one with its stripe faded pale. Honest wear on honest paint.

THE RIDERS — three small figures, each recognisable ONLY by colour and silhouette at this distance. Do not attempt facial detail; a face here is a few flat marks at most, and no portrait is possible or wanted.

- GRAXO, in the lead machine's tub: the tallest, in a deep muted AUBERGINE cape — a dusky desaturated purple-brown, never magenta or crimson — streaming straight out behind him over the transom in one long flat shape. That cape is his entire read at this size: a dark purple banner above an ivory shirt. Dark hair.
- SION, in the second: a slimmer figure in a warm OCHRE jacket with a slim TEAL scarf streaming behind her, one bare STEEL-GRAY arm catching a hard pale highlight at the controls. Dark hair blown back.
- DAXUS, in the third: a broader figure in a short OFF-WHITE jacket with a small BURNT-ORANGE wedge at its opening, sitting more upright than the other two.

Their colours — aubergine, ochre and teal, off-white and burnt-orange — are the only saturated notes besides the machines' stripes in a vast ochre and blue-violet landscape, so the three of them read as bright specks strung along the diagonal.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame. THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. It is NOT a 2:1 banner, NOT a panorama, NOT a letterbox strip, NOT a square. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO labels, NO text of any kind. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors, composition or its close-up framing. Image 2 contributes the SPEEDERS' DESIGN ONLY — their geometry and layout; ignore its smooth digital rendering, its grey studio backdrop, its horizon bands and its glowing exhaust, and do not reproduce it as a side-on product view.

SCENE: "The Ride Out." Late afternoon on the barren planet Kalagra. Three riders on hover speeders are crossing an enormous empty badlands toward the distant domed city of Kannan, with the planet-wide storm standing along the horizon the whole way. This is a LANDSCAPE first and a vehicle shot second. The subject is the scale of the crossing: three small bright machines strung out across a vast, indifferent country.

THERE ARE EXACTLY THREE PEOPLE AND THREE MACHINES IN THIS PICTURE. Nobody is chasing them. There are no pursuers, no raiders, no bandits, no gang, no second group of vehicles, no distant riders, no dust plumes from unseen machines, and no figures on any ridge or horizon. Three riders, three speeders, empty country. Nothing else moves.

SCALE AND FRAMING — PULL WELL BACK. The camera is far away and somewhat elevated, looking out across the badlands. The three speeders sit in the MIDDLE DISTANCE, not the foreground:

- Each speeder, being long and lean, spans roughly ONE FIFTH of the frame's width — small enough that the land dwarfs them, large enough that the shape of the hull and its painted stripe read cleanly.
- Each rider is a SMALL FIGURE, well under one tenth of the frame's height. No face is legible at this distance and none should be attempted.
- The three machines together occupy only the lower-middle band of the picture. Everything above them is land, storm and sky; everything below them is open rock running down toward the viewer.
- Do NOT crop in. Do NOT fill the frame with a machine or a rider. No hull touches the edge of the picture.

COMPOSITION: the three speeders run in a loose staggered line on a shallow DIAGONAL from the lower left toward the middle right, heading away from the viewer and into the depth of the picture, so we see them from BEHIND AND SLIGHTLY ABOVE at a three-quarter angle. That angle shows each machine's long lean profile and the top of its deck at once, which is what makes the stripe read. The nearest is at the left and slightly larger; the farthest is toward the centre-right and smaller. Each trails a long, low, flat banner of ochre dust behind it, the banners lying almost parallel to the ground and stretching well back toward the lower left — the clearest signal of speed in the picture.

Keep big quiet areas: a broad calm sky above, a broad calm sweep of rock below, and the detail concentrated in the narrow band where the three machines and their dust cross the middle of the frame.

THE LAND: an immense badlands of flat ochre and warm grey rock, laid out in broad terraces and shelves that step down and away toward the horizon. Flat-topped mesas and buttes stand in the middle and far distance. A dry canyon cuts across the middle ground. Build ALL of it from a FEW LARGE FLAT PLANES of solid colour with hard, crisply angled edges — broad calm fields of warm ochre in the light and broad calm fields of deep slate blue-violet in shadow, meeting along clean seams. Drawing and detail belong ONLY at those seams: the shelf lips, the canyon rim, the mesa crests. The interior of every large plane stays quiet, flat and under-detailed. Do NOT break the ground into a carpet of small chips, facets, pebbles or mosaic tiles.

THE STORM: across the whole far distance stands the planet-wide storm front — an immense dark mass of cobalt and blue-violet like a second mountain range, with a hard angular top edge, sitting low and wide behind everything and filling much of the horizon. Two or three thin branching bolts of pale yellow lightning inside it. It is still far off: the air over the riders is clear and sunlit, with no haze, no rain and no wind-driven murk anywhere near them.

KANNAN: far away in the middle distance, small and pale, the domed city sits in the bowl of its crater — a low pale dome and a few fine spires behind the rim of a vast crater wall, dwarfed by the storm mass behind it. It is the riders' destination and it is plainly still hours away.

LIGHT: late-afternoon daylight from a low searing blue-white sun raking from the left. Every mesa, shelf and machine throws a LONG hard shadow out across the rock to the right — those long shadows are a major part of the design. The lit rock is warm ochre; every shadow is a single flat plane of deep slate blue-violet. The storm mass stays cool and dark against the sunlit ground. The sky above is a clear deep blue, paling toward the horizon, painted as large flat areas. No neon, no bloom, no lens flare, no light rays, no sun disc in frame.

COLOUR: the picture is built from warm ochre and ivory rock against cool cobalt and blue-violet storm and shadow. The only saturated notes are the three machines and their riders: the brick-red-and-teal stripes on ivory hulls, Graxo's aubergine cape, Sion's ochre jacket and teal scarf, Daxus's off-white and burnt-orange. Those specks of colour are what the eye finds in all that emptiness.

This is a quiet, spacious, handsome landscape with three small fast machines crossing it — not an action close-up.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
