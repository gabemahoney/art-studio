# the-ride-out v017

User request verbatim: I'd like to remove her teal scarf flowing behind her
Mode: Edit off v016, single removal: the streaming tail of Sion's teal scarf deleted, leaving the scarf as a neck wrap only with short ends finishing near her upper chest — what her description v1 actually specifies. Everything else frozen. NOTE ON MODEL: the vault default gpt-5.6-terra and the fallback gpt-5.6-luna both now return 'not supported when using Codex with a ChatGPT account', an upstream account/model change rather than a prompt fault; neither attempt billed anything. Run on gpt-6-sol instead.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-sol — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f380-4c56-72c0-9e17-137dc2109d89/exec-b5a6706d-ab52-4b33-9b35-2e2bde51d9eb.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-ride-out/v016/image.png
Date: 2026-09-30
Status: approved and promoted to final.png on 2026-09-30. User approval: "Looks sick. Do you have the ability to add it to the PDF?"
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.49 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Single removal, clean, no regressions. Verified at 400 percent: the streaming tail of Sion's teal scarf is gone. Her scarf remains as a neck wrap only — a slim band of teal cloth around her throat with a short end at her upper chest — which is what her description v1 actually specifies; the trailing flick was never canon. Nothing whatsoever now trails behind Sion, and Graxo's cape is the only streaming element left in the picture. The area the tail occupied is repainted as the dust plume and sky behind it, with nothing substituted in its place. Everything else held exactly: the tightened central formation with uneven gaps and varied depth, the zoom at about 20 percent of frame width for the nearest machine, the warm ochre plain and its v013 ground treatment, the calm foreground, the storm filling the horizon with forked lightning, no moon, off-frame moonlight, prow lamps, the big billowing dust plumes, machines floating clear with separated shadows, the full speeder design and sunset-swipe livery, Graxo's face and his deep wine aubergine cape with both antique-gold collar pins, and Daxus's likeness. File is 2.49 MB, inside the 2.5 MB book-float budget, at 1536x1024 exact 3:2 matching the other scene images. MODEL NOTE: run on gpt-6-sol. The vault default gpt-5.6-terra and the documented fallback gpt-5.6-luna BOTH now return HTTP 400 "not supported when using Codex with a ChatGPT account" — an upstream account/model availability change, not a prompt fault. Neither failed attempt billed anything, as bin/gen.py fails closed. gpt-6-sol works and produced this candidate with no visible style shift from terra. rules.md's Codex model table is now out of date and bin/gen.py's CODEX_MODEL default will fail on every run until changed.

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
Image 2 is EDIT TARGET: The scene baseline: the-ride-out v016, approved by the user. Correct in every respect except Sion's trailing scarf tail.

TASK: A single 3:2 horizontal wide night scene: three hover speeders crossing an enormous Kalagra plain toward the viewer, storm filling the horizon, with nothing trailing behind the right-hand rider.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no turnarounds, no expression rows, no swatches, no call-outs, no names, no labels, and NO TEXT OR LETTERING OF ANY KIND.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the ONE thing below.

SCENE: "The Ride Out." Night on Kalagra. Three riders cross an immense plain on hover speeders, coming toward the viewer, the storm filling the horizon behind them.

IMAGE 2 IS APPROVED AND CORRECT IN EVERY RESPECT BUT ONE. This is a single small removal. Keep everything else EXACTLY as image 2 has it: the framing and zoom; the tightened group with Daxus left, Graxo nearest at centre and Sion right, at their current sizes, depths and spacing; the warm ochre plain and its exact ground treatment; the calm foreground; the cool deep blue-violet sky; the storm wall filling the horizon with its rolling cloud heads and forked lightning; NO moon; the off-frame moonlight; the prow lamps; the big billowing dust plumes; the machines floating clear of the rock with separated shadows; every detail of all three speeders and their sunset-swipe livery; Graxo's face and his DEEP WINE AUBERGINE cape with its two antique-gold collar pins, at its current colour, shape and drape; and Daxus's likeness, glasses, off-white jacket and cross patches. Do not re-frame, do not zoom, do not move anyone, do not re-texture the ground, do not recolour anything.

THE ONE CHANGE — REMOVE THE TRAILING TAIL OF SION'S SCARF. In image 2, Sion (the rider on the right) has a teal scarf whose end streams out behind her in the wind. Delete that streaming tail completely.

Her scarf REMAINS, but only as a neck wrap: a slim band of teal cloth wrapped loosely once around her throat, sitting close against her neck and collar, with SHORT ends that finish near her upper chest and hang down the front of her. Nothing teal extends past the back of her shoulders. Nothing teal flows, streams, flaps, flicks or trails behind her at all.

Where that trailing tail used to be there is now simply open air and her dust plume — paint that area as the background that lies behind it, matching the surrounding dust and sky. Do not replace the tail with hair, cloth, a strap, a banner or anything else.

She still wears NO cape, cloak, mantle, shawl or coat-tail, and her short ochre jacket ends at her hips without flaring. After this change, NOTHING at all trails behind Sion. Graxo's cape remains the only thing streaming in the wind anywhere in this picture.

LIGHT AND COLOUR: unchanged from image 2 in every respect.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
