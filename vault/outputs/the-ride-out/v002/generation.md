# the-ride-out v002

User request verbatim: Read /Users/gmahoney/projects/system52/rogue-frontier-private/pdf/one-shot.md and come up with a cool image for Scene 4
Mode: Second pass, fresh generation (not an edit — v001's defects are compositional/global). Fixes: (1) 3:2 aspect now demanded in the PROMPT BODY, since the codex backend treats --size as advisory and returned 1774x887 on v001 while every other scene image in the book is 3:2; (2) raider count pinned to exactly four, stated three times — v001 painted six, and the count is mechanically load-bearing in the Challenge block; (3) cape respecified as deep muted aubergine, not the crimson v001 produced; (4) ground restated as few large quiet planes against v001's carpet of small facets; (5) Graxo and Sion now explicitly glancing back at the raiders.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f059-3ac9-7d61-ba3e-9b288e3a2f6d/exec-160ab486-665a-4ce3-8413-2fa8062d0d89.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/characters/graxo/reference.png; frozen assets/characters/graxo/candidates/v027/image.png
- Image 3 IDENTITY: assets/characters/sion/reference.png; frozen assets/characters/sion/candidates/v001/image.png
- Image 4 IDENTITY: assets/characters/daxus/reference.png; frozen assets/characters/daxus/candidates/v001/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.78 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: Aspect defect fixed, count defect not. FIXED: the raw output is 1536x1024, exact 3:2, matching scene-meet, scene-jump and scene-pad in the book — demanding the ratio in the prompt body worked where the --size flag alone did not, which is expected since the codex backend treats requested size as advisory. The cape also moved from v001's crimson toward a deeper aubergine, though its trailing edge still reads more magenta than the muted purple-brown asked for. Cast identity is strong at this larger scale: Graxo's elongated face, long broad-tipped nose, mustache, silver temples, both gold collar pins, plum ascot and vest; Sion's opaque ruby goggles, ochre jacket with the left sleeve absent, teal scarf and steel-gray left cyber arm on the correct anatomical side; Daxus's glasses, neat side part, off-white jacket with cross patches, burnt-orange shirt and bandolier. The domed city of Kannan now reads in the middle distance under the storm, which the scene text supports. STILL WRONG: (1) FIVE raiders are painted, not four, despite the count being stated three times in the prompt — verified on a magnified crop. The adventure's Challenge block makes the count mechanically load-bearing (clearing the gang takes four successes), so this still cannot ship. Repeating a number is evidently not working; the next attempt should enumerate the four riders individually by position rather than assert a total. (2) The raiders ride WHEELED motorcycles with visible tyres and forks. Both the scene text and the Challenge block call them speeders and speeder bikes, and the crew's own machines hover, so wheels are a setting inconsistency introduced by my own prompt wording ("long forks"). (3) The ground is again a dense carpet of small chips and mosaic dashes despite an explicit instruction to keep it few large quiet planes; this is the Style Block's "coarse dry-brush and broken pigment" being over-applied against its own "large areas stay quiet". (4) Graxo and Sion are still facing forward rather than glancing back at the raiders, so the reaction beat asked for in the spec is absent for the second time. Also note the file is 2.78 MB, over the 2.5 MB book-float budget, and needs recompression before placement. Speeders and raiders remain IMPROVISED — no assets exist for either.

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
Image 2 is IDENTITY: GRAXO VOSS. Copy this man's design exactly — face, build, hair, mustache, cape, vest, ascot, boots and holstered blaster. Ignore this sheet's layout, its multiple views, its expression busts and its plain gray background.
Image 3 is IDENTITY: SION TILL. Copy this woman's design exactly — face, build, hair, opaque ruby goggles, ochre jacket with the missing left sleeve, teal scarf, steel-gray left cyber arm, trousers and boots. Ignore this sheet's layout, its multiple views, its expression busts, its height chart and its plain gray background.
Image 4 is IDENTITY: DAXUS SKYE. Copy this man's design exactly — face, glasses, hair, off-white medical jacket with the burnt-orange V and cross patches, bandolier and chest scanner, belt, trousers and boots. Ignore this sheet's layout, its multiple views, its expression busts, its height chart and its plain gray background.

TASK: A single 3:2 horizontal daytime action illustration: the crew of the Antares running three rented land speeders across the Kalagra badlands as four raiders come down off a ridge after them, the planet-wide storm standing dark along the far horizon.

THE CAST — three riders, each copied from their own identity sheet. Ignore every sheet's layout, its multiple views, its expression busts, its height chart and its plain gray background; take only the person's design.

GRAXO VOSS (description v11) — image 2. Tall, sturdy adult man with a weathered, elongated angular face: long middle and lower face, tall forehead with a loose forelock, heavy brow, deep-set readable eyes, pronounced angular cheekbones, strong jaw with a rounded chin. Long projecting nose with a broad, softly rounded bulbous tip, clearly broader than the bridge. Neat regular dark-brown mustache ending at the mouth corners, no beard. Dark brown hair swept up, with clearly visible silver-gray at both sides and temples. He wears a full-width AUBERGINE cape over both shoulders and back, open at the front, with a high standing collar and two square antique-gold medallion pins, one at each cape edge; the cape falls below the knees and its lining is dusty mauve. Under it a plain dark walnut-brown fitted vest with restrained metallic buttons, an ivory long-sleeved shirt and a compact plum ascot. Charcoal trousers, charcoal boots with metal toe and heel caps. A charcoal molded holster on his anatomical RIGHT hip carries one blaster, wood grip upward and backward, muzzle enclosed downward.

SION TILL (description v1) — image 3. Young adult woman, medium warm skin, slender-to-average build, broad chin and slightly square jaw, full lips, dark shoulder-length hair swept to one side. She wears large dark-framed goggles with OPAQUE MIRRORED RUBY-RED lenses — a continuous red surface with one broad diagonal pale reflection, completely concealing her eyes and eyebrows. Never paint eye shapes, pupils or eyebrows on or above the lenses. Worn OCHRE utility jacket over a plain black shirt: the RIGHT arm is sleeved, and the LEFT sleeve is absent at the shoulder. A slim TEAL scarf loosely wraps her neck, its short ends finishing near the upper chest. Her anatomical LEFT arm is a cyber arm, exposed from shoulder to five-fingered hand: steel-gray shells, dark joints, restrained brass fittings, human proportions, no wires or weapons. Her right arm and hand are natural skin. Relaxed charcoal cargo trousers with thigh flap pockets, sleek black boots.

DAXUS SKYE (description v1) — image 4. Youthful adult man, broad sturdy build, light-to-medium skin, full cheeks, square jaw, straight nose, dark eyebrows, clean-shaven, with thin metal-framed glasses. Dark brown hair, closely cropped sides, neat side part, swept-back voluminous wave on top. He wears a short OFF-WHITE medical jacket with a high collar and rounded front edges flaring toward the hips; a broad inverted-V opening exposes a BURNT-ORANGE shirt across his abdomen, and orange-red sleeve patches carry pale medical crosses. One broad dark-brown bandolier runs from his anatomical RIGHT shoulder down to his LEFT hip, with a flat triangular leather panel at the lower chest carrying one ivory diagnostic scanner. Off-white utility belt, dark brown cargo trousers, worn brown lace-up work boots.

RELATIVE HEIGHT: Graxo is the tallest at 6 feet 2, Daxus 6 feet, Sion 5 feet 9.

THE RAIDERS are original and have no identity sheet: four of them, faces hidden behind wrapped dust scarves and scratched goggles, in mismatched scavenged gear. Keep them as dark, simplified silhouettes — they are a threat, not portraits. Do not give them any of the crew's clothing, colors or equipment.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame. THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. This is a hard requirement: it is NOT a wide 2:1 banner, NOT a panorama, NOT a letterbox strip. Compose for that taller 3:2 field, with real sky above the riders and real ground below them. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO labels, NO text of any kind. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors or composition. Images 2, 3 and 4 contribute their PEOPLE ONLY — copy each person's face, build, clothing and equipment, and ignore each sheet's layout, multiple views, expression busts, height chart and plain gray background. There are exactly SEVEN figures in this picture: the three named crew on three speeders, and EXACTLY FOUR raiders on four bikes. Count them: four raiders, no more and no fewer. No one else.

SCENE: "The Ride Out." Daytime on the barren planet Kalagra. The crew of the Antares is running three rented land speeders across open rocky badlands toward the domed city of Kannan, and a raider gang has just come down off a ridge after them. This is the adventure's one big action beat: speed, dust and a hard diagonal.

THE MOMENT: the chase is already joined. The three crew speeders are flat out, low over the rock, throwing long banners of ochre dust. The raiders have crested a ridge behind and to the right and are dropping down the slope to cut them off, their own dust trailing. The crew are REACTING: Graxo and Sion both have their heads turned back over their shoulders toward the raiders, faces angled away from their direction of travel — this is the instant they realize they are being run down. Daxus, farthest, is still facing front.

COMPOSITION — a strong left-to-right diagonal into depth. The three crew speeders occupy the LEFT and CENTRE of the frame, nearest the viewer, running diagonally from lower left toward the middle distance. The raiders come from the UPPER RIGHT, smaller, on and just below the ridgeline. Between and beyond them the badlands open out. Keep large quiet areas of sky and flat rock between the detailed groups.

THE CREW AND THEIR SPEEDERS — three machines in a loose staggered line, the nearest largest and the farthest smallest:

- NEAREST, lower left and largest in frame: GRAXO leads, seen from behind and to one side in three-quarter rear view, his head and shoulders turned back over his shoulder toward the raiders so his face reads clearly in profile-to-three-quarter — the long nose with its broad tip, the mustache, the silver at his temples. His AUBERGINE cape — a deep muted purple-brown, like dark aubergine skin, NOT crimson, NOT magenta, NOT scarlet — streams straight out behind him in the wind, one big flat shape with its dusty mauve lining flashing, the two gold pins at his collar. He grips the speeder's controls with one hand; the holstered blaster sits on his right hip. He is roughly a third of the frame's height.
- MIDDLE, centre-left and slightly farther: SION, low over her machine, turned back hard toward the raiders. Her ruby mirrored goggles catch the sun as one flat red shape with a single pale diagonal streak. Her ochre jacket with its missing left sleeve and her teal scarf whip in the wind, and her bare steel-gray CYBER LEFT ARM is clearly visible gripping the controls, catching a hard pale highlight. Her dark hair is blown back.
- FARTHEST, centre and smallest of the three: DAXUS, sitting more upright, one hand on the controls and the other bracing his med satchel, glasses on, his off-white medical jacket with the burnt-orange V and the orange-red cross patches reading clearly against the ochre dust. His bandolier crosses his chest.

The speeders themselves are battered open-cockpit hover machines from a hire garage: low slabby hulls with blunt prows, a simple cowl and handlebars, a single seat, no wheels — they ride a hand's breadth above the rock. Chipped ivory and ochre paint over dark panels, mismatched replacement plates, a few brick-red markings, exposed vents and grab rails. Keep them simple: large flat blocks of colour, details suggested, never drawn in full. Each throws a low flat wedge of ochre dust straight back from its skirts — flat opaque shapes with hard, ragged edges, never soft clouds, never glowing.

THE RAIDERS — EXACTLY FOUR of them and no more, upper right, cresting and descending a low rocky ridge, clearly smaller than the crew and clearly closing. Their bikes are junkers: exposed engine blocks, scavenged panels in mismatched slate, rust-brown and dull green, ragged fairings, long forks. The riders are dark simplified silhouettes in wrapped dust scarves and scratched goggles, faces hidden; two have cobbled guns raised, long crude things of welded parts. They ride in a ragged line, not a formation. There are FOUR bikes and FOUR riders in total — do not add a fifth, a sixth, or any further riders trailing behind them. Keep them as shapes and threat — no portrait detail, and none of the crew's colours or equipment on them.

THE LAND: open badlands of flat ochre-gray rock, cracked pavement-like ground broken by angular shelves, low mesas and scattered dark boulders, receding to a wide horizon. Build the ground from a FEW LARGE FLAT colour planes with hard angular edges — broad quiet fields of ochre. Do not break the rock into a carpet of small chips, facets, pebbles or mosaic tiles: most of the ground is large, calm and under-detailed, with drawing concentrated only at the edges where one plane meets another.

THE STORM ON THE HORIZON: across the far distance stands the planet-wide storm front as a single immense dark mass — a second mountain range of cobalt and blue-violet with a hard angular top edge, sitting low and wide behind everything. It is still far off and nothing of it has arrived: the air over the chase is clear and sunlit, with no haze, no rain and no wind-driven murk across the riders. One or two thin branching bolts of pale yellow lightning inside the distant mass. Far to one side, the pale rim of a vast crater breaks the horizon — the wall around Kannan, still hours away.

LIGHT: late-afternoon daylight from a searing blue-white sun, low and raking from the left, so the riders and machines carry long hard shadows across the rock and one bright lit plane along their left sides. The lit rock is warm ochre; every shadow is a single flat plane of deep slate blue-violet. The storm mass in the distance is cool and dark, in clear contrast to the sunlit ground. No neon, no bloom, no lens flare, no light rays.

COLOUR: warm ochre and ivory ground and dust against the cool cobalt and blue-violet of the storm and the shadows, with the crew's colours as the bright accents — Graxo's aubergine cape, Sion's ochre jacket and teal scarf and red goggles, Daxus's off-white and burnt-orange. The raiders stay muted and dark so the crew reads first.

Give the picture real speed: hard diagonals, streaming dust, the cape and scarf snapping, bodies leaning into the run.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
