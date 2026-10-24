# the-ride-out v004

User request verbatim: One adjustment, dont have the characters all looking the exact same direction.
Mode: Edit off v003, single change: three distinct lines of sight — Graxo eyes front driving, Sion wrenched fully back over her right shoulder at the raiders, Daxus tilted up and right toward the cresting fourth raider. Asking only Sion for the full turn-back protects Graxo's face as the lead read, which is the likely reason three earlier 'look back' instructions were refused. Four-raider count, hover bikes, calm ground planes and aubergine cape all explicitly frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f062-0592-7461-b48b-000685861a3b/exec-45138a81-8bd2-454b-9f8a-9267ece3e26c.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-ride-out/v003/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.36 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Three distinct lines of sight achieved, after three earlier failures of the same instruction. Graxo alone keeps his eyes front along the line of travel, jaw set, face fully readable in three-quarter; Sion is wrenched back over her right shoulder at the pursuit with her hair whipping forward and her opaque ruby goggles catching the sun as one flat red shape; Daxus has his chin lifted and his head tilted up and to the right toward the cresting fourth raider, alarmed rather than grim. No two head angles match and none of the three looks at the viewer, so the row-of-identical-poses problem is resolved. The working change was asking only Sion for the full turn-back: the earlier blanket instruction appears to have been refused because turning every head away costs face legibility, and leaving Graxo forward-facing as the lead read removed that conflict. Everything frozen held: exactly four raiders in their enumerated positions with the ridge empty beyond the fourth, wheelless hover bikes on lift pods with daylight beneath them, broad calm ochre and blue-violet ground planes, the muted aubergine cape with both gold pins, Kannan's dome and the storm wall with its lightning. File is 2.36 MB, now inside the 2.5 MB book-float budget without recompression. Outstanding per user direction at time of writing: the raider machines still read as compact motorcycle-shaped bikes rather than speeders, and the crew's own speeder hulls are stubbier than intended -- both to be addressed next. Speeders and raiders remain IMPROVISED -- no assets exist for either.

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
Image 2 is EDIT TARGET: The scene baseline: the-ride-out v003, approved by the user except that all three crew look the same direction.

TASK: A single 3:2 horizontal daytime action illustration: the crew of the Antares running three hover speeders across the Kalagra badlands as four raiders on hover bikes come down off a ridge after them, each crew member reacting in a different direction.

THE CAST — three riders, each copied from their own identity sheet. Ignore every sheet's layout, its multiple views, its expression busts, its height chart and its plain gray background; take only the person's design.

GRAXO VOSS (description v11) — image 2. Tall, sturdy adult man with a weathered, elongated angular face: long middle and lower face, tall forehead with a loose forelock, heavy brow, deep-set readable eyes, pronounced angular cheekbones, strong jaw with a rounded chin. Long projecting nose with a broad, softly rounded bulbous tip, clearly broader than the bridge. Neat regular dark-brown mustache ending at the mouth corners, no beard. Dark brown hair swept up, with clearly visible silver-gray at both sides and temples. He wears a full-width AUBERGINE cape over both shoulders and back, open at the front, with a high standing collar and two square antique-gold medallion pins, one at each cape edge; the cape falls below the knees and its lining is dusty mauve. Under it a plain dark walnut-brown fitted vest with restrained metallic buttons, an ivory long-sleeved shirt and a compact plum ascot. Charcoal trousers, charcoal boots with metal toe and heel caps. A charcoal molded holster on his anatomical RIGHT hip carries one blaster, wood grip upward and backward, muzzle enclosed downward.

SION TILL (description v1) — image 3. Young adult woman, medium warm skin, slender-to-average build, broad chin and slightly square jaw, full lips, dark shoulder-length hair swept to one side. She wears large dark-framed goggles with OPAQUE MIRRORED RUBY-RED lenses — a continuous red surface with one broad diagonal pale reflection, completely concealing her eyes and eyebrows. Never paint eye shapes, pupils or eyebrows on or above the lenses. Worn OCHRE utility jacket over a plain black shirt: the RIGHT arm is sleeved, and the LEFT sleeve is absent at the shoulder. A slim TEAL scarf loosely wraps her neck, its short ends finishing near the upper chest. Her anatomical LEFT arm is a cyber arm, exposed from shoulder to five-fingered hand: steel-gray shells, dark joints, restrained brass fittings, human proportions, no wires or weapons. Her right arm and hand are natural skin. Relaxed charcoal cargo trousers with thigh flap pockets, sleek black boots.

DAXUS SKYE (description v1) — image 4. Youthful adult man, broad sturdy build, light-to-medium skin, full cheeks, square jaw, straight nose, dark eyebrows, clean-shaven, with thin metal-framed glasses. Dark brown hair, closely cropped sides, neat side part, swept-back voluminous wave on top. He wears a short OFF-WHITE medical jacket with a high collar and rounded front edges flaring toward the hips; a broad inverted-V opening exposes a BURNT-ORANGE shirt across his abdomen, and orange-red sleeve patches carry pale medical crosses. One broad dark-brown bandolier runs from his anatomical RIGHT shoulder down to his LEFT hip, with a flat triangular leather panel at the lower chest carrying one ivory diagnostic scanner. Off-white utility belt, dark brown cargo trousers, worn brown lace-up work boots.

RELATIVE HEIGHT: Graxo is the tallest at 6 feet 2, Daxus 6 feet, Sion 5 feet 9.

THE RAIDERS are original and have no identity sheet: four of them, faces hidden behind wrapped dust scarves and scratched goggles, in mismatched scavenged gear. Keep them as dark, simplified silhouettes — they are a threat, not portraits. Do not give them any of the crew's clothing, colors or equipment.

OUTPUT FORM — READ FIRST: produce ONE single continuous illustration filling the whole frame. THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. It is NOT a 2:1 banner, NOT a panorama, NOT a letterbox strip. There are NO panels, NO split frames, NO dividing lines, NO borders, NO insets, NO labels, NO text of any kind. Image 1 contributes its PAINTING TECHNIQUE ONLY — do not copy its people, clothing, equipment, interior, colors or composition. Image 2 is the SCENE BASELINE: reproduce it faithfully and change only the ONE thing specified below.

SCENE: "The Ride Out." Daytime on the barren planet Kalagra. The crew of the Antares is running three rented hover speeders across open rocky badlands toward the domed city of Kannan, and four raiders have come down off a ridge after them.

Image 2 is APPROVED and correct in every respect but one: all three crew are looking in the same direction, which makes them read as a row of identical poses. Reproduce image 2 exactly — same camera, same framing, same crop, same scale, same colours, same light, same paint handling — and change only where each of the three is looking.

KEEP FROM IMAGE 2 — COMPLETELY UNCHANGED: the whole composition and camera; the three crew speeders running on their diagonal from lower left into the middle distance, at their current sizes and positions; every detail of the three crew's clothing, equipment and build; the battered ivory-and-ochre hover speeders with their brick-red markings and their low flat banners of ochre dust; the broad calm planes of warm ochre rock and deep slate blue-violet shadow, quiet and under-detailed in their interiors with drawing only at the shelf lips and mesa crests; the domed city of Kannan small in the middle distance; the immense dark cobalt and blue-violet storm wall along the far horizon with its pale yellow lightning; the late-afternoon raking sunlight and the long hard shadows. Do not re-frame, do not zoom, do not move or resize anything, do not re-texture the ground.

THE FOUR RAIDERS ARE UNCHANGED AND THERE ARE STILL EXACTLY FOUR OF THEM: the leader nearest at lower right with a long crude rifle raised above his shoulder; the second hunched low behind and to his left with both hands on his bars and no weapon; the third higher on the ridge slope with a rifle held across his body; the fourth farthest, just cresting the ridgeline, both hands on his bars. Beyond the fourth the ridge stays EMPTY — bare rock and sky, no further riders, no extra dust plumes, no fifth figure anywhere in the picture. Their machines stay wheelless hover bikes on blunt downturned lift pods with clear daylight and cast shadow beneath them: no tyres, rims, spokes, forks or mudguards anywhere. Do not add, remove or move a raider.

THE ONE CHANGE — GIVE THE THREE CREW THREE DIFFERENT LINES OF SIGHT. In image 2 all three face the same way. Turn their heads so each is looking somewhere different, and so the group reads as three people reacting to the same trouble in three different ways. Only heads, necks and shoulders turn — every body stays exactly where it is, still low and driving hard, hands still on the controls.

- GRAXO, nearest and largest at lower left: EYES FRONT. He alone keeps looking ahead, along the line of travel toward the left of the frame, jaw set, driving. He is the one still flying the machine while the others look behind. His face stays fully readable in the three-quarter it already has — the long nose with its broad tip, the mustache, the silver at his temples.
- SION, middle: TWISTED FULLY BACK. Her head and shoulders rotate hard around to her right, over her shoulder, so she is looking BACKWARD past her own dust at the raiders on the ridge behind and to the right. We see her face at a steep three-quarter-to-profile from the front-left, tipped back over her shoulder, with her jaw and chin turned toward the pursuit and her dark hair whipping forward across her cheek. Her large opaque mirrored RUBY-RED goggles catch the sun as one flat red shape with a single pale diagonal streak — no eyes, pupils or eyebrows painted on or above them. Her teal scarf streams. Her bare steel-gray LEFT cyber arm stays on the controls.
- DAXUS, farthest of the three: LOOKING UP AND AWAY to his right, toward the top of the ridge where the fourth raider is cresting — a different target from Sion's, higher and further off, so their two lines of sight clearly diverge rather than run parallel. His chin lifts, his head tilts up and to the right, and his expression is alarmed rather than grim. His thin metal-framed glasses catch a small hard highlight. He does not look at the viewer.

The result must read at a glance as three distinct head angles: one forward and level, one wrenched back over the shoulder, one tilted up and off to the side. No two of them point the same way, and none of the three looks straight out at the viewer.

LIGHT: unchanged from image 2. Late-afternoon daylight raking from the left, long hard shadows across the rock, one bright lit plane along the left side of every rider and machine, every shadow a single flat plane of deep slate blue-violet. No neon, no bloom, no lens flare, no light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
