# the-ride-out v019

User request verbatim: Can we vary the distress marks on the vehciles so they dont all look identical?
Mode: Edit off v018 (centred). Single change: each machine given its own pattern of wear, enumerated one by one rather than asked for as generic 'variety' — centre machine chipped raw at the prow, left machine sand-scoured and faded along the flank, right machine carrying a mismatched grey replacement panel and rust at the engine collar — with an explicit rule that no mark may repeat in the same place on two machines. Also codified upstream: assets/vehicles/hire-speeder/description.md bumped to v11 with a standing 'every machine wears differently' rule, so future scenes inherit it. Centring, spacing, depth, ground, cape, scarf and livery layout all frozen. Run on gpt-6-astra, the only model still available on this account today.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f3e5-e5c9-7652-bf0c-918af0f5fd77/exec-14904b65-5e66-4a4e-aeef-ae93cc8f0986.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-ride-out/v018/image.png
Date: 2026-09-30
Status: approved and promoted to final.png on 2026-09-30. User approval: "I think thats a winner. Add it to the PDF."
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.51 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: Wear is now individual, verified on magnified crops of all three machines rather than at full-sheet size. LEFT (Daxus): the stripe bands are faded chalky and scoured thin along the mid-flank, washed out to pale, while the prow paint stays comparatively intact — the sun-and-sand treatment asked for. CENTRE (Graxo, nearest): the opposite — prow and upper nose chipped raw with broad ragged patches of bare pale grey where the paint has broken away, and the flank stripe still strong behind it. RIGHT (Sion): the least damaged, its stripe bands crisp and unbroken, distinguished instead by a clear rust-brown bloom around the tail engine collar, which neither of the others has. No mark, chip, scrape or faded area repeats in the same place on two machines, and the three no longer read as stamped copies. Enumerating the three treatments one by one, rather than asking for "variety", is what produced this in a single pass — the same approach that fixed the raider count earlier in the session. Also codified upstream so future scenes inherit it: assets/vehicles/hire-speeder/description.md is bumped to v11 with a standing rule that every machine in the fleet wears differently and identical distress between two machines in one image is an error; v10 is snapshotted. Everything else held: the centred trio with its uneven gaps and depth spread, the camera and zoom, the warm ochre plain and its ground treatment, the calm foreground, the storm filling the horizon with forked lightning, no moon, off-frame moonlight, prow lamps, the big billowing dust plumes, machines floating clear with separated shadows, the hull shape and sunset-swipe layout, Graxo's deep wine aubergine cape with both gold collar pins, Sion's neck-wrap teal scarf with nothing trailing and no cape, and Daxus's likeness. File is 2.51 MB, marginally over the 2.5 MB book-float budget. Run on gpt-6-astra, the only model still available on this account.

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
Image 2 is EDIT TARGET: The scene baseline: the-ride-out v018, the centred version. Correct in every respect except that all three machines carry identical wear.

TASK: A single 3:2 horizontal wide night scene: three individually battered hover speeders centred in the frame, crossing an enormous Kalagra plain toward the viewer, storm filling the horizon.

SUBJECT DESIGN (description v11, restated so nothing is invented):
A hire fleet, worn honestly: chipped and sand-scoured leading edges, mismatched
replacement panels interrupting the bands, stripes faded pale in places. The paint
is old; the machine still works.

**Every machine wears differently.** These are separately abused rentals, not a
matched set, so whenever two or more appear together each one must carry its OWN
pattern of damage — different marks, in different places, of different kinds. One
might be chipped raw along the prow, another faded and scoured pale across the
mid-hull, another mostly sound but carrying a crude replacement panel or a rust
bloom at the engine collar. Never paint the same scuffs on two machines in the same
image: identical distress is the clearest tell that they were stamped rather than
used.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no turnarounds, no expression rows, no swatches, no call-outs, no names, no labels, and NO TEXT OR LETTERING OF ANY KIND.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the ONE thing below.

SCENE: "The Ride Out." Night on Kalagra. Three riders cross an immense plain on hover speeders, coming toward the viewer, the storm filling the horizon behind them.

IMAGE 2 IS APPROVED AND CORRECT IN EVERY RESPECT BUT ONE. Keep everything else EXACTLY as image 2 has it: the camera, the zoom and the CENTRED placement of the trio in the frame; each rider's position, size and distance; the uneven gaps between them; the warm ochre plain and its exact ground treatment; the calm foreground; the cool deep blue-violet sky; the storm filling the horizon with its rolling cloud heads and forked lightning; NO moon; the off-frame moonlight; the prow lamps; the big billowing dust plumes; the machines floating clear of the rock with separated shadows; the hull SHAPE and the sunset-swipe livery layout on all three machines; Graxo's face and his deep wine aubergine cape with its two antique-gold collar pins; Sion's neck-wrap teal scarf with nothing trailing and no cape; and Daxus's likeness, glasses, off-white jacket and cross patches. Do not re-frame, do not zoom, do not move or resize anyone, do not re-texture the ground.

THE ONE CHANGE — GIVE EACH MACHINE ITS OWN PATTERN OF WEAR. In image 2 all three speeders carry the same scuffs and chips in the same places, which makes them look stamped out rather than separately used. These are three battered rentals from a hire garage, each abused by different people over different years. Repaint the damage so no two machines match.

Treat them one by one. The wear differs in KIND, in PLACE and in AMOUNT:

- THE CENTRE MACHINE, the nearest one carrying the caped rider: the worst-knocked of the three at the FRONT. Its prow and the leading edges of its nose are chipped raw, the paint broken back to bare pale grey metal in a ragged band around the front, with a few deep dings. Behind that the flank paint is comparatively sound and its stripe still strong.

- THE LEFT-HAND MACHINE: barely chipped at the nose, but SUN- AND SAND-SCOURED along the middle of its flank, where the stripe has faded pale and gone chalky and thin, as though it has crossed a great deal of open desert. A long shallow scrape runs back along that flank. Its prow paint is largely intact.

- THE RIGHT-HAND MACHINE: the patched one. Its paint is mostly sound, but one rectangular REPLACEMENT PANEL low on the flank is a plain mismatched grey that interrupts the stripe bands and does not line up with them, plainly a cheap repair. Add a bloom of rust-brown staining around its tail engine collar. Almost no chipping at the nose.

No mark, chip, scrape, patch or faded area may appear in the same place on two of the machines. If the same damage reads twice, it is wrong.

Keep all of it restrained and painted: flat opaque marks with hard edges, a few clear shapes per machine, in the muted night palette. This is honest wear on working machines, not battle damage, not rust-bucket decay, and not fine speckled grime. Do not change the hull shape, the livery colours or the layout of the stripe bands — only where and how the paint is worn.

LIGHT AND COLOUR: unchanged from image 2 in every respect.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
