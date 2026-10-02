# Antares cockpit v020
User request: now he loks like he is on mth.
Mode: retry from v017 approved gaze/cape baseline, restrained concern without v019 bright eyes
Style: v2
Tool: built-in image_gen (model not exposed)
Inputs (ordered):
- STYLE: ref_images/style_references/canonical_style_reference.png (style v2)
- EDIT TARGET: outputs/antares-cockpit/v017/image.png
Diagnosis: v019 overemphasized sclera/catchlights. Use relaxed lids and muted sclera, no bright catchlights, understated concern.
Status: PROMOTED to final.png 2026-09-30. User approval, verbatim: "yes we need to prompote them too. oops" — retroactive: this candidate had already been placed in the book's PDF by hand, so the approval record was backfilled. This receipt predates the current bin/gen.py format and had no Status line, which is why bin/promote.py could not update it automatically.

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

Image 1 is STYLE: matte gouache paint handling only.
Image 2 is EDIT TARGET: cockpit v017, explicitly approved for gaze, pose and cape. Preserve it.

Use case: identity-preserve. Add subtle human tension and worried concentration to the crew's expressions, especially Graxo and Sion. They are focusing on something concerning outside the front window. Keep their EXACT current head angles, pupil directions, gaze target and body poses. Do not rotate their heads or redirect their eyes.
Graxo: draw his brows slightly inward with a small worried lift at the inner ends, a little tension around the eyes, closed lips gently pressed and jaw held with restrained concern. He looks alert and apprehensive, not angry, blank, smiling, terrified or melodramatic. Preserve facial proportions, nose, mustache and silver temples.
Sion: convey focused concern through subtly tense closed lips, slightly drawn mouth corners and a little tension in cheeks and jaw. Preserve exact goggle position and opacity; do not add visible eyebrows above the goggles or exposed eyes. No smile, pout or open-mouthed fear. Her focus is intense but controlled.
Daxus: a modest crease of concentration in brows and slight lip tension as he studies instruments, preserving his downward gaze, glasses and face.

Keep every other aspect identical: the already approved shared sightline, Graxo's cape draped OVER raised arm, all hands, costumes, equipment, console, lighting, framing and cockpit. Only tiny facial expression changes; preserve likeness and broad flat matte painted planes. No extra fine wrinkles, skin texture or glossy modeling.

Graxo eye refinement: natural understated alertness, not wide-eyed anxiety. Keep his upper lids relaxed and partly covering the tops of the irises. Eye whites are a narrow muted warm-gray sliver, NEVER bright white. Small dark irises/pupils, no added catchlight dots. Do not enlarge the eye openings. Keep the existing gaze direction exactly. Slight inner-brow concern and subtle lower-lid tension should convey attention; avoid raised startled brows, glaring eyes, pinprick highlights, or a strained expression. He is calm but concerned. Preserve all other features and the approved cape.

Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.

## Self-check
Bright eye-white/catchlight emphasis removed; Graxo has relaxed upper lids and restrained concern. Gaze and over-arm cape visually retained. Matte painted treatment preserved. Candidate saved, not finalized.
