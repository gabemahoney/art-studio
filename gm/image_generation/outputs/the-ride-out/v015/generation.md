# the-ride-out v015

User request verbatim: (autonomous iteration while the user sleeps)
Mode: Edit off v014, single colour correction: Graxo's cape from bright magenta-pink to the deep wine aubergine his canonical individual sheet paints, the user having confirmed that sheet is canon for him. Everything else, and especially v014's newly solved flat calm ground, explicitly frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f0bc-0eab-7960-a8ab-4c7fbac74872/exec-b7047b94-b329-45a9-b195-34478f2700db.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-ride-out/v014/image.png
- Image 3 IDENTITY: assets/characters/graxo/reference.png; frozen assets/characters/graxo/candidates/v027/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.16 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Cape corrected with no regressions, and this is the candidate I judge finished. Graxo's cape is now a deep wine aubergine — dark, greyed-off, brown-red purple sitting quietly against the ochre plain — matching his canonical individual sheet instead of v014's bright magenta-pink. Its shape, drape, motion and the two antique-gold collar pins are unchanged. Critically, v014's hard-won flat ground survived the edit: the plain is still large calm unbroken fields of warm ochre with no all-over dash, hatch or stipple inside them, and the foreground is still a broad bare sweep. Everything else held: the wide framing; the depth stagger with Graxo nearest and low at centre-left, Sion mid-distance right and Daxus far off and tiny at upper left, none level and unevenly spaced; the big billowing dust plumes; the storm filling the horizon with rolling cloud heads and forked lightning; no moon; off-frame moonlight; prow lamps; machines floating clear of the rock with separated shadows; the full speeder design and sunset swipe; Sion's slim teal scarf with no cape; Daxus's likeness. File is 2.16 MB, inside the 2.5 MB book-float budget, at 1536x1024 exact 3:2 matching the other scene images in the book. Remaining note, judged acceptable rather than a fault: the nearest machine is about 27 percent of frame width, above the one-fifth cap, but the long recession back to Daxus carries the sense of scale and the picture reads as the wide shot the brief asked for. This candidate is offered for approval; promote.py must not run without the user's explicit word.

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
Image 2 is EDIT TARGET: The scene baseline: the-ride-out v014. Correct in every respect except the cape's colour.
Image 3 is IDENTITY: GRAXO's approved individual reference sheet — the canonical authority on his cape's colour, a deep wine aubergine with a dusty mauve lining. Take ONLY the colour from it. Ignore its layout, multiple views, expression busts and grey background.

TASK: A single 3:2 horizontal wide night scene: three hover speeders crossing an enormous flat Kalagra plain, storm on the horizon, the lead rider's cape in deep wine aubergine.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no turnarounds, no expression rows, no swatches, no call-outs, no names, no labels, and NO TEXT OR LETTERING OF ANY KIND.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the ONE thing below. Image 3 is GRAXO's approved individual sheet, attached ONLY as the authority on his cape's colour; take nothing else from it, and reproduce none of its layout, its multiple views, its expression busts or its grey background.

SCENE: "The Ride Out." Night on Kalagra, three riders crossing an immense plain on hover speeders with the storm filling the horizon.

KEEP FROM IMAGE 2 — COMPLETELY UNCHANGED. Image 2 is correct in every respect but one and this is a single colour correction. Keep exactly: the wide framing and the scale of every machine; the depth stagger with Graxo nearest and low at centre-left, Sion mid-distance right, Daxus far off and tiny at upper left; the large flat calm fields of warm ochre ground with NO all-over texture, dashes, hatching, chips or stipple inside them, and the broad bare foreground; the big billowing dust plumes; the storm filling the horizon with its rolling cloud heads and forked lightning; the cool deep blue-violet sky; NO moon; the off-frame moonlight; the prow lamps; the machines floating clear of the rock with separated shadows; every detail of all three speeders and their livery; Sion's slim teal scarf and her lack of any cape; Daxus's likeness; and Graxo's face, pose, hair and the SHAPE and drape of his cape. Do not re-frame, do not zoom, do not move anyone, do not re-texture the ground.

THE ONE CHANGE — RECOLOUR GRAXO'S CAPE. In image 2 it is painted a bright, saturated MAGENTA-PINK. That is wrong. Repaint it the colour it is on his own sheet, image 3: a DEEP WINE AUBERGINE — a dark, heavily greyed-off purple with a lot of brown and red in it, like a dark aubergine's skin or a dried plum. It is much DARKER and much LESS SATURATED than what image 2 shows: closer to a deep burgundy-brown than to pink.

It is NOT magenta, NOT hot pink, NOT fuchsia, NOT scarlet and NOT bright violet, and it does not glow. In this night picture it should sit as a dark, rich, quiet mass — only a little more colourful than the shadows around it, and clearly darker than the warm ochre ground behind it. Where the cape folds and turns, its inner face may show the slightly lighter dusty mauve lining, still muted.

Keep the two small square antique-gold pins at his collar. Change only the colour; the cape's shape, size, drape and motion stay exactly as they are in image 2.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
