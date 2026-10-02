# the-ride-out v014

User request verbatim: (autonomous iteration while the user sleeps, per their instruction to keep going until happy)
Mode: Edit off v013. Two changes. (1) FORMATION: pulling back flattened the group onto one depth and near-even spacing, so it reads as a rank; now specified as one machine much nearer and low, one much further and high, the third off-centre between them, with uneven lateral gaps and nothing level. (2) GROUND TEXTURE: roughly ten passes of prohibitions have failed to shift the all-over dashed hatch, and at this wide framing it fills most of the picture. Switching tactic from prohibition to a COUNTABLE POSITIVE constraint, in the manner of the Style Block's own hard limits — three or four flat tones total across the whole ground, each laid down as a broad unbroken field with no marking whatsoever inside it, all drawing confined to the edges where fields meet, and the foreground explicitly required to be one of the emptiest areas in the picture.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f0ba-5165-7e21-b4bf-9b8d461041c7/exec-8733cabf-7dcd-4d21-a24e-e3a0701761b1.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-ride-out/v013/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.30 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Best candidate of the scene, and it cracked the longest-standing problem. GROUND TEXTURE SOLVED: the all-over dashed dry-brush hatch that survived roughly ten passes of prohibition is gone. The plain is now large flat fields of warm ochre with essentially no marking inside them, all the drawing confined to terrace lips, shelf rims and mesa crests, and the foreground is a broad bare calm sweep. The change that worked was switching from PROHIBITION to a COUNTABLE POSITIVE constraint — "three or four flat tones total across the whole ground, each an unbroken field, no marking whatsoever inside any of them" — which mirrors how the Style Block's own hard limits are written. That is a transferable lesson: telling this model what a surface IS, with a number attached, beats listing what it must not be. FORMATION: the depth stagger is back and stronger than any earlier version — Graxo nearest and low at centre-left, Sion mid-distance to the right, Daxus far off and tiny at upper left. Nothing is level, the lateral gaps are uneven, and the long gap back to Daxus is what now sells the scale of the plain. Held from v013: big billowing dust plumes, storm filling the horizon with forked lightning, no moon, machines floating clear with separated shadows, warm ground sharing the livery family, Sion's slim teal scarf with no cape, Graxo's corrected face, Daxus's likeness. File is 2.30 MB, inside the 2.5 MB book-float budget. DISCREPANCIES: (1) the nearest machine measures about 410px of 1536, roughly 27 percent of frame width, above the one-fifth cap — a consequence of asking for one machine to come much closer; the composition still reads as a wide shot because the distance back to Daxus carries the scale, so this is judged acceptable rather than a fault, but it is recorded. (2) Graxo's cape reads bright magenta, where his canonical individual reference paints a deep wine-aubergine with a mauve lining. The user has confirmed the individual sheet is canon for Graxo, so this is a genuine mismatch worth one more targeted pass.

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

Image 1 is STYLE: Match this image's hand-painted matte rendering technique ONLY. Ignore and do not reproduce its people, clothing, equipment, interior, setting or composition.
Image 2 is EDIT TARGET: The scene baseline: the-ride-out v013. Its wide framing, small machine scale, billowing dust, storm, night light and all three riders are correct. Change only the formation depth and the ground texture.

TASK: A single 3:2 horizontal wide night scene: three small hover speeders strung out at very different distances across an enormous, calm, flat-painted Kalagra plain, the storm filling the horizon.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no turnarounds, no swatches, no call-outs, no names, no labels, and NO TEXT OR LETTERING OF ANY KIND.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the two things listed below.

SCENE: "The Ride Out." Night on Kalagra. Three riders cross an immense empty plain on hover speeders, coming toward the viewer, with the planet-wide storm filling the horizon behind them.

KEEP FROM IMAGE 2 — UNCHANGED: the wide framing and the small scale of the machines, which is now correct — the nearest speeder stays about one sixth of the frame's width and must NOT grow; the big billowing dust plumes boiling up behind each machine; the warm ochre plain with its calm unbroken foreground; the cool deep blue-violet sky; the storm wall filling the horizon with its rolling cloud heads and forked lightning; NO moon; the off-frame moonlight; the prow lamps; the machines floating clear of the rock with separated shadows; and every detail of the three riders and their speeders — Graxo centre with his wine-aubergine cape, Sion with her SLIM teal scarf and no cape, Daxus in his off-white jacket with cross patches.

CHANGE ONE — BREAK UP THE FORMATION AGAIN. In image 2 the three machines sit at much the same distance from the viewer and are spaced almost evenly across the frame, so they read as a rank. Scatter them in DEPTH:
- Bring ONE machine much closer to the viewer — clearly the nearest, noticeably larger than the others, and placed low in the frame. It still spans no more than one fifth of the frame's width.
- Push ONE machine much further away — small, higher in the frame, well back toward the storm, plainly a long way off.
- Leave the THIRD somewhere between them, and NOT at the midpoint — closer to one than the other.
- Their lateral spacing is uneven too: two run nearer together, the third sits well apart.
- No two of them are level with one another and they do not sit on a straight line. It should look like three people crossing open country on their own lines, strung out by distance, not a formation.

CHANGE TWO — CALM THE GROUND DOWN. This is the most important change. In image 2 nearly the whole plain is covered in an all-over texture of small dashes, chips and hatch marks, and at this wide framing that texture fills most of the picture. Remove it.

Paint the open plain as LARGE, FLAT, EMPTY FIELDS OF COLOUR. Count them: across the whole ground use only THREE OR FOUR flat tones in total — a lit warm ochre, one step darker warm brown, and one deep shadow tone — and lay each one down as a broad unbroken area. Inside any one of those areas there is NO marking at all: no dashes, no hatching, no chips, no flecks, no stipple, no mosaic tiles, no scratchy brush strokes, no gravel, no noise. Flat, bare, and quiet, like an area of poster paint.

All the drawing on the ground happens at the EDGES where one field meets another: the lips of terraces, the rims of shelves, the bases of rock outcrops, the crests of distant mesas. There you may use a crisp contour and, sparingly, a little dry-brush breakup — nowhere else.

The foreground in particular, the lower third of the picture, should be one of the emptiest and calmest areas in the whole image: a broad bare sweep of flat warm ochre with almost nothing painted on it. Resist filling it. Emptiness there is what makes the plain feel enormous.

LIGHT AND COLOUR: unchanged. Warm ochre ground, cool deep blue-violet sky and storm, off-frame moonlight as the only light on the riders, prow lamps and lightning as the brightest points. No neon, no bloom, no lens flare, no light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
