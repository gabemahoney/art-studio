# the-ride-out v016

User request verbatim: No, v13 is the best. Can you make a version of that where they are a little tighter in formation and maybe zoomed in just a little bit?
Mode: Edit off v013, the user's chosen best version — NOT off v014/v015. Three changes: (1) lateral gaps closed by about a third so the three read as one travelling party occupying the centre of the frame, while keeping uneven spacing and varied depth so tightening does not flatten them into a rank; (2) a modest zoom, nearest machine to a little under one fifth of frame width from v013's measured 14 percent, with the plain and storm still dominant; (3) Graxo's cape recoloured from magenta-pink to the deep wine aubergine of his canonical individual sheet, per the user's earlier ruling that the individual reference is canon. v013's ground treatment is deliberately left untouched — the flat-field ground fix developed in v014 is NOT applied here, since the user chose v013 over v015 and that treatment may be part of why.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f36f-3f26-72f1-844c-7b2404250a8a/exec-b02fdabe-8897-438c-a5c9-f75c0747fb20.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-ride-out/v013/image.png
- Image 3 IDENTITY: assets/characters/graxo/reference.png; frozen assets/characters/graxo/candidates/v027/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.63 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: Built from v013 at the user's direction after they chose it over v014 and v015. All three changes landed. FORMATION: the lateral gaps are closed and the three now sit in the central portion of the frame with open plain to left and right, reading as one travelling party rather than three separated specks. The tightening did not flatten them into a rank — the gaps remain uneven at roughly 280px and 460px, and Graxo sits nearer the viewer than the other two, so no two are level. ZOOM: the nearest machine now spans about 310px of 1536, roughly 20 percent of frame width, up from v013's 14 percent — the modest step the user asked for, with the plain and storm still dominating and the riders still small in a very large country. CAPE: recoloured from bright magenta-pink to the deep wine aubergine of Graxo's canonical individual sheet, dark and greyed-off against the ochre ground, with both antique-gold collar pins and the cape's shape, drape and motion unchanged. Held from v013: the big billowing dust plumes, the storm filling the horizon with forked lightning, no moon, off-frame moonlight, prow lamps, machines floating clear with separated shadows, the full speeder design and sunset swipe, Sion's slim teal scarf with no cape, Daxus's likeness. DELIBERATELY NOT CHANGED: v013's ground treatment. The flat-field ground developed in v014 — which fixed the long-standing all-over dry-brush hatch — is NOT applied here, because the user picked v013 over v015 and that treatment may be part of the reason. It remains available as a separate option. File is 2.63 MB, over the 2.5 MB book-float budget and needing recompression before placement.

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
Image 2 is EDIT TARGET: The scene baseline: the-ride-out v013, which the user selected as the best version. Its wide framing, ground treatment, dust plumes, storm and riders are correct. Change only the formation width, the zoom and the cape colour.
Image 3 is IDENTITY: GRAXO's approved individual sheet — the canonical authority on his cape's colour, a deep wine aubergine. Take ONLY the colour from it. Ignore its layout, multiple views, expression busts and grey background.

TASK: A single 3:2 horizontal wide night scene: three hover speeders in a tighter loose group crossing an enormous Kalagra plain toward the viewer, storm filling the horizon.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no turnarounds, no expression rows, no swatches, no call-outs, no names, no labels, and NO TEXT OR LETTERING OF ANY KIND.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only what is listed below. Image 3 is GRAXO's approved individual sheet, attached ONLY as the authority on his cape's colour; take nothing else from it and reproduce none of its layout, views, busts or background.

SCENE: "The Ride Out." Night on Kalagra. Three riders cross an immense empty plain on hover speeders, coming toward the viewer, the planet-wide storm filling the horizon behind them.

KEEP FROM IMAGE 2 — UNCHANGED: the wide open composition and its sense of an enormous plain; the warm ochre ground and its treatment exactly as image 2 paints it; the calm unbroken foreground with no chasm; the cool deep blue-violet sky; the storm wall filling the horizon with its rolling cloud heads and forked lightning; NO moon anywhere; the off-frame moonlight; each speeder's pale-yellow prow lamp; the big billowing dust plumes boiling up behind each machine; the machines floating clear of the rock with separated shadows; and every detail of the three speeders — prow leading, rider straddling the saddle toward the rear with a boot on the flank stirrup, boom and rust engine pod trailing at the tail, ventral skid, and the sunset swipe kicking up toward the tail. Keep Sion's SLIM teal scarf and her complete absence of any cape, and keep Daxus's likeness, glasses, off-white jacket and cross patches.

CHANGE ONE — TIGHTEN THE FORMATION. In image 2 the three machines are spread widely apart across the frame, almost to its edges. Bring them CLOSER TOGETHER as a group, so they read as three riders travelling as one party rather than three separate specks.

Close the lateral gaps between them by roughly a third, drawing all three in toward the middle of the picture. The group as a whole should occupy the central portion of the frame, with open empty plain to the left and right of them.

They are tighter, but NOT a rank: keep their spacing UNEVEN, with two running nearer each other and the third set a little apart, and keep them at DIFFERENT DISTANCES from the viewer so no two are level and they do not sit on a straight line. Tightening the group must not flatten it into a row.

CHANGE TWO — ZOOM IN A LITTLE. Come slightly closer than image 2, but only slightly. The nearest machine should span a little under one fifth of the frame's width — a modest step up from image 2, not a close-up. The plain and the storm must still dominate the picture and the riders must still read as small figures in a very large country. Do NOT crop in tight, do NOT let any hull approach the edge of the frame, and do NOT lose the open sweep of empty ground in the foreground.

CHANGE THREE — GRAXO'S CAPE COLOUR. In image 2 his cape is a bright, saturated MAGENTA-PINK. Repaint it the colour his own sheet shows, image 3: a DEEP WINE AUBERGINE — a dark, heavily greyed-off purple with a lot of brown and red in it, like a dark aubergine's skin or a dried plum. Much darker and far less saturated than image 2: closer to deep burgundy-brown than to pink. NOT magenta, NOT hot pink, NOT fuchsia, NOT bright violet, and it does not glow; in this night picture it sits as a dark rich quiet mass. Keep the two square antique-gold pins at his collar and keep the cape's shape, size, drape and motion exactly as image 2 has them. Colour only.

LIGHT AND COLOUR: otherwise unchanged from image 2. Warm ochre ground, cool deep blue-violet sky and storm, off-frame moonlight as the only light on the riders, prow lamps and lightning the brightest points. No neon, no bloom, no lens flare, no light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
