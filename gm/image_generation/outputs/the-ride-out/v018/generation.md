# the-ride-out v018

User request verbatim: Could we do one more pass where we center the trio in the frame?
Mode: Edit off v017 (the promoted final). Single compositional change: trio measured +47px right of frame centre with 330px of open plain left against 236px right; shifted left until margins are roughly equal and the group midpoint sits on the centreline, with the right-hand rider brought in slightly since the centre-to-right gap measured 460px against 280px. Uneven spacing and varied depth preserved. MODEL NOTE: run on gpt-6-astra. gpt-5.6-terra and gpt-5.6-luna became unavailable on this ChatGPT account on 2026-09-30, and gpt-6-sol — which successfully produced v017 earlier the same day — was refused with the same 400 on this run. Account model availability appears to be changing during the session. No refused attempt billed anything.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f389-a87e-7841-9ba9-f98578a3de7c/exec-2f4c396e-ff29-4484-be28-5349967f40ea.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-ride-out/v017/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.51 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: Centring achieved and measured. The group now spans x=270..1240 with its midpoint at 755 against the frame centre of 768 — off by 13px, down from 47px right in v017. Left and right margins are 270px and 296px, close to equal, where v017 had 330px against 236px. The right-hand rider has also been brought in: centre-to-centre gaps are now 320px and 375px, against v017's lopsided 280px and 460px. The gaps remain unequal, so the trio still reads as a loose party rather than an evenly spaced rank. Depth variation survives the move but is now subtler — machine widths measure 330px for Graxo nearest, 290px for Daxus and 260px for Sion furthest — so the three are closer to a common distance than in v017 and the recession is less pronounced. That is the one cost of centring; it still reads as three riders travelling together rather than a row, but if the user wants the depth spread back, one rider should be pushed further off. Everything else held exactly: the camera and zoom with the nearest machine at about one fifth of frame width, the warm ochre plain and its ground treatment, the calm foreground, the storm filling the horizon with forked lightning, no moon, off-frame moonlight, prow lamps, the big billowing dust plumes, machines floating clear of the rock with separated shadows, the full speeder design and sunset-swipe livery, Graxo's deep wine aubergine cape with both antique-gold collar pins, Sion's neck-wrap teal scarf with nothing trailing and no cape, and Daxus's likeness. File is 2.51 MB, marginally over the 2.5 MB book-float budget. MODEL NOTE: run on gpt-6-astra. Over the course of 2026-09-30 this account lost gpt-5.6-terra, then gpt-5.6-luna, then gpt-6-sol — the last of which had successfully produced v017 barely twenty minutes earlier. Availability is changing live during the session; astra is the only verified model still working. No refused attempt billed anything.

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
Image 2 is EDIT TARGET: The scene baseline: the-ride-out v017, the promoted final. Correct in every respect except that the trio sits right of centre in the frame.

TASK: A single 3:2 horizontal wide night scene: three hover speeders centred in the frame, crossing an enormous Kalagra plain toward the viewer, storm filling the horizon.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no turnarounds, no expression rows, no swatches, no call-outs, no names, no labels, and NO TEXT OR LETTERING OF ANY KIND.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the ONE thing below.

SCENE: "The Ride Out." Night on Kalagra. Three riders cross an immense plain on hover speeders, coming toward the viewer, the storm filling the horizon behind them.

IMAGE 2 IS APPROVED AND CORRECT IN EVERY RESPECT BUT ONE. This is a single compositional adjustment. Keep everything else EXACTLY as image 2 has it: the camera and zoom, with the nearest machine at about one fifth of the frame's width; the warm ochre plain and its exact ground treatment; the calm foreground; the cool deep blue-violet sky; the storm wall filling the horizon with its rolling cloud heads and forked lightning; NO moon; the off-frame moonlight; the prow lamps; the big billowing dust plumes; the machines floating clear of the rock with separated shadows; every detail of all three speeders and their sunset-swipe livery; Graxo's face and his DEEP WINE AUBERGINE cape with its two antique-gold collar pins; Sion's neck-wrap teal scarf with NOTHING trailing behind her and no cape; and Daxus's likeness, glasses, off-white jacket and cross patches. Do not re-frame, do not zoom, do not re-texture the ground, do not recolour anything, do not resize any machine.

THE ONE CHANGE — CENTRE THE TRIO IN THE FRAME. In image 2 the three riders sit noticeably right of centre: there is a wide stretch of empty plain on the LEFT and a much narrower one on the RIGHT, and the group's midpoint falls to the right of the picture's midline. It looks off-balance.

Shift the whole group LEFT so that it is CENTRED horizontally in the picture:
- The open plain to the LEFT of the leftmost machine and the open plain to the RIGHT of the rightmost machine should be ROUGHLY EQUAL in width. Neither side should have obviously more empty ground than the other.
- The midpoint of the group as a whole sits on the vertical centreline of the picture.
- Move all three together, keeping their positions relative to one another and keeping every machine at its current size.

Also close the group up slightly on its right: in image 2 the gap between the centre rider and the right-hand rider is much larger than the gap between the left-hand rider and the centre one, which stretches the trio rightward. Bring the right-hand rider IN toward the other two so the two gaps are closer in size — but do NOT make them equal.

The group must stay a loose scattered party, NOT a rank: keep the spacing UNEVEN, keep the three at DIFFERENT DISTANCES from the viewer so no two are level, and do not line them up on a straight line. Centring the group is about where the group sits in the frame, not about making the riders evenly spaced.

LIGHT AND COLOUR: unchanged from image 2 in every respect.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
