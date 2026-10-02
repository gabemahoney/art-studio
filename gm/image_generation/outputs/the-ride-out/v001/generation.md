# the-ride-out v001

User request verbatim: Read /Users/gmahoney/projects/system52/rogue-frontier-private/pdf/one-shot.md and come up with a cool image for Scene 4
Mode: Fresh scene, first pass. Scene 4 'The Ride Out' — the only scene in the one-shot lacking an image. Chase beat: three crew speeders running left-to-right on a hard diagonal with four raiders cresting a ridge upper-right, storm wall as a distant second mountain range, late-afternoon raking sun. Cast: Graxo v11, Sion v1, Daxus v1, all three references validated. Speeders and raiders are improvised — no assets exist for them.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024, actual 1774x887
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f055-ad03-76c2-9b51-5d55add93ca9/exec-7aeb6d01-c3c9-4c49-aa74-1728d5570e4a.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/characters/graxo/reference.png; frozen assets/characters/graxo/candidates/v027/image.png
- Image 3 IDENTITY: assets/characters/sion/reference.png; frozen assets/characters/sion/candidates/v001/image.png
- Image 4 IDENTITY: assets/characters/daxus/reference.png; frozen assets/characters/daxus/candidates/v001/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1774x887 (raw model output, frozen)
Delivered: delivered-1536x1024.png, 1536x1024, sRGB 8-bit PNG-24 no alpha, flattened onto #1b1e26, 2.06 MB; scaled to fit from raw 1774x887  [raw aspect 1774:887 != target 1536:1024 — padded, not cropped; regenerate at the target aspect for a full-bleed image]
Review: Strong first pass on composition and cast, two objective defects. Cast reads well and matches the sheets: Graxo's elongated face, long broad-tipped nose, mustache, silver temples, streaming cape with both gold collar pins, ivory shirt, vest, plum ascot and the holstered blaster; Sion's opaque ruby goggles as one flat red shape with a single pale streak, ochre jacket with the left sleeve absent, teal scarf and the bare steel-gray left cyber arm on the correct anatomical side; Daxus's glasses, neat side part, off-white medical jacket with cross patch, burnt-orange shirt and chest scanner. Raiders read as dark silhouetted threat in wrapped scarves and goggles on junker bikes, carrying none of the crew's colours. Badlands, angular shelves, warm ochre against blue-violet shadow, distant storm mass with lightning, and the pale crater rim with the dome on the far left horizon all landed. DEFECT 1: the raw output is 1774x887, aspect 2:1, not the requested 1536x1024. The codex backend treats requested size as advisory and ignored it. Every other scene image in the book (scene-meet, scene-jump, scene-pad) is 3:2, so this cannot ship as-is; the derived deliverable had to be padded with bars top and bottom. DEFECT 2: six raiders are painted, not four. The adventure text and its Challenge block both specify four armed raiders, and the count is mechanically load-bearing -- clearing the gang takes four successes -- so this is a canon error, not a detail. Lesser issues: the cape reads crimson-magenta rather than aubergine; the rock is covered in dense small facets against the Style Block's instruction that large areas stay quiet; and the crew are not glancing back at the raiders as the spec asked, which costs a little of the reaction beat. Speeders and raiders are IMPROVISED -- no assets exist for either, so this image establishes nothing about their design.

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

TASK: A single horizontal daytime action illustration: the crew of the Antares running three rented land speeders across the Kalagra badlands as a raider gang comes down off a ridge after them, the planet-wide storm standing dark along the far horizon.

THE CAST — three riders, each copied from their own identity sheet. Ignore every sheet's layout, its multiple views, its expression busts, its height chart and its plain gray background; take only the person's design.

GRAXO VOSS (description v11) — image 2. Tall, sturdy adult man with a weathered, elongated angular face: long middle and lower face, tall forehead with a loose forelock, heavy brow, deep-set readable eyes, pronounced angular cheekbones, strong jaw with a rounded chin. Long projecting nose with a broad, softly rounded bulbous tip, clearly broader than the bridge. Neat regular dark-brown mustache ending at the mouth corners, no beard. Dark brown hair swept up, with clearly visible silver-gray at both sides and temples. He wears a full-width AUBERGINE cape over both shoulders and back, open at the front, with a high standing collar and two square antique-gold medallion pins, one at each cape edge; the cape falls below the knees and its lining is dusty mauve. Under it a plain dark walnut-brown fitted vest with restrained metallic buttons, an ivory long-sleeved shirt and a compact plum ascot. Charcoal trousers, charcoal boots with metal toe and heel caps. A charcoal molded holster on his anatomical RIGHT hip carries one blaster, wood grip upward and backward, muzzle enclosed downward.

SION TILL (description v1) — image 3. Young adult woman, medium warm skin, slender-to-average build, broad chin and slightly square jaw, full lips, dark shoulder-length hair swept to one side. She wears large dark-framed goggles with OPAQUE MIRRORED RUBY-RED lenses — a continuous red surface with one broad diagonal pale reflection, completely concealing her eyes and eyebrows. Never paint eye shapes, pupils or eyebrows on or above the lenses. Worn OCHRE utility jacket over a plain black shirt: the RIGHT arm is sleeved, and the LEFT sleeve is absent at the shoulder. A slim TEAL scarf loosely wraps her neck, its short ends finishing near the upper chest. Her anatomical LEFT arm is a cyber arm, exposed from shoulder to five-fingered hand: steel-gray shells, dark joints, restrained brass fittings, human proportions, no wires or weapons. Her right arm and hand are natural skin. Relaxed charcoal cargo trousers with thigh flap pockets, sleek black boots.

DAXUS SKYE (description v1) — image 4. Youthful adult man, broad sturdy build, light-to-medium skin, full cheeks, square jaw, straight nose, dark eyebrows, clean-shaven, with thin metal-framed glasses. Dark brown hair, closely cropped sides, neat side part, swept-back voluminous wave on top. He wears a short OFF-WHITE medical jacket with a high collar and rounded front edges flaring toward the hips; a broad inverted-V opening exposes a BURNT-ORANGE shirt across his abdomen, and orange-red sleeve patches carry pale medical crosses. One broad dark-brown bandolier runs from his anatomical RIGHT shoulder down to his LEFT hip, with a flat triangular leather panel at the lower chest carrying one ivory diagnostic scanner. Off-white utility belt, dark brown cargo trousers, worn brown lace-up work boots.

RELATIVE HEIGHT: Graxo is the tallest at 6 feet 2, Daxus 6 feet, Sion 5 feet 9.

THE RAIDERS are original and have no identity sheet: four of them, faces hidden behind wrapped dust scarves and scratched goggles, in mismatched scavenged gear. Keep them as dark, simplified silhouettes — they are a threat, not portraits. Do not give them any of the crew's clothing, colors or equipment.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame, horizontal. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO labels, NO text of any kind. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors or composition. Images 2, 3 and 4 contribute their PEOPLE ONLY — copy each person's face, build, clothing and equipment, and ignore each sheet's layout, multiple views, expression busts, height chart and plain gray background. There are exactly SEVEN figures in this picture: the three named crew on three speeders, and four raiders on four bikes. No one else.

SCENE: "The Ride Out." Daytime on the barren planet Kalagra. The crew of the Antares is running three rented land speeders across open rocky badlands toward the domed city of Kannan, and a raider gang has just come down off a ridge after them. This is the adventure's one big action beat: speed, dust and a hard diagonal.

THE MOMENT: the chase is already joined. The three crew speeders are flat out, low over the rock, throwing long banners of ochre dust. The raiders have crested a ridge behind and to the right and are dropping down the slope to cut them off, their own dust trailing. The crew are looking back, reacting — this is the instant they realize they are being run down.

COMPOSITION — a strong left-to-right diagonal into depth. The three crew speeders occupy the LEFT and CENTRE of the frame, nearest the viewer, running diagonally from lower left toward the middle distance. The raiders come from the UPPER RIGHT, smaller, on and just below the ridgeline. Between and beyond them the badlands open out. Keep large quiet areas of sky and flat rock between the detailed groups.

THE CREW AND THEIR SPEEDERS — three machines in a loose staggered line, the nearest largest and the farthest smallest:

- NEAREST, lower left and largest in frame: GRAXO leads, seen from behind and to one side in three-quarter rear view, his head and shoulders turned back over his shoulder toward the raiders so his face reads clearly in profile-to-three-quarter — the long nose with its broad tip, the mustache, the silver at his temples. His AUBERGINE cape streams straight out behind him in the wind, one big flat shape with its dusty mauve lining flashing, the two gold pins at his collar. He grips the speeder's controls with one hand; the holstered blaster sits on his right hip. He is roughly a third of the frame's height.
- MIDDLE, centre-left and slightly farther: SION, low over her machine, turned back hard toward the raiders. Her ruby mirrored goggles catch the sun as one flat red shape with a single pale diagonal streak. Her ochre jacket with its missing left sleeve and her teal scarf whip in the wind, and her bare steel-gray CYBER LEFT ARM is clearly visible gripping the controls, catching a hard pale highlight. Her dark hair is blown back.
- FARTHEST, centre and smallest of the three: DAXUS, sitting more upright, one hand on the controls and the other bracing his med satchel, glasses on, his off-white medical jacket with the burnt-orange V and the orange-red cross patches reading clearly against the ochre dust. His bandolier crosses his chest.

The speeders themselves are battered open-cockpit hover machines from a hire garage: low slabby hulls with blunt prows, a simple cowl and handlebars, a single seat, no wheels — they ride a hand's breadth above the rock. Chipped ivory and ochre paint over dark panels, mismatched replacement plates, a few brick-red markings, exposed vents and grab rails. Keep them simple: large flat blocks of colour, details suggested, never drawn in full. Each throws a low flat wedge of ochre dust straight back from its skirts — flat opaque shapes with hard, ragged edges, never soft clouds, never glowing.

THE RAIDERS — four, upper right, cresting and descending a low rocky ridge, clearly smaller than the crew and clearly closing. Their bikes are junkers: exposed engine blocks, scavenged panels in mismatched slate, rust-brown and dull green, ragged fairings, long forks. The riders are dark simplified silhouettes in wrapped dust scarves and scratched goggles, faces hidden; two have cobbled guns raised, long crude things of welded parts. They ride in a ragged line, not a formation. Keep them as shapes and threat — no portrait detail, and none of the crew's colours or equipment on them.

THE LAND: open badlands of flat ochre-gray rock, cracked pavement-like ground broken by angular shelves, low mesas and scattered dark boulders, receding to a wide horizon. Build the ground from a few large flat colour planes with hard angular edges — broad quiet fields of ochre, not a carpet of small facets or pebbles.

THE STORM ON THE HORIZON: across the far distance stands the planet-wide storm front as a single immense dark mass — a second mountain range of cobalt and blue-violet with a hard angular top edge, sitting low and wide behind everything. It is still far off and nothing of it has arrived: the air over the chase is clear and sunlit, with no haze, no rain and no wind-driven murk across the riders. One or two thin branching bolts of pale yellow lightning inside the distant mass. Far to one side, the pale rim of a vast crater breaks the horizon — the wall around Kannan, still hours away.

LIGHT: late-afternoon daylight from a searing blue-white sun, low and raking from the left, so the riders and machines carry long hard shadows across the rock and one bright lit plane along their left sides. The lit rock is warm ochre; every shadow is a single flat plane of deep slate blue-violet. The storm mass in the distance is cool and dark, in clear contrast to the sunlit ground. No neon, no bloom, no lens flare, no light rays.

COLOUR: warm ochre and ivory ground and dust against the cool cobalt and blue-violet of the storm and the shadows, with the crew's colours as the bright accents — Graxo's aubergine cape, Sion's ochre jacket and teal scarf and red goggles, Daxus's off-white and burnt-orange. The raiders stay muted and dark so the crew reads first.

Give the picture real speed: hard diagonals, streaming dust, the cape and scarf snapping, bodies leaning into the run.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
