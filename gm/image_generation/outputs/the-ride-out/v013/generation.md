# the-ride-out v013

User request verbatim: v12 is great for the speeders. But again it seems too zoomed in. Also Sion keeps having a cape. / Also I like the dust cloud in the screenshot from v11 better than the dust clouds you did in v12
Mode: Edit off v012. Three changes. (1) SCALE: v012 measured 36 percent of frame width for the nearest machine; hard-capped at one fifth with one sixth preferred and the failure quantified in the prompt. (2) SION'S SCARF, correctly diagnosed at last: the recurring 'cape' is not a cape but her teal scarf painted as a thick bulky cowl trailing a broad sheet of cloth. Targeting the scarf's WIDTH and LENGTH directly — a slim band no wider than her throat with short ends finishing near her upper chest, per description v1 — rather than repeating a no-cape prohibition that was never the actual fault. (3) DUST: the user prefers the big billowing plume in the speeder sheet's ridden panel over v012's thin flat ground streaks, so the flat cut-paper instruction is deliberately relaxed to a full rolling voluminous mass, still painted in broad tonal masses with no speckle or airbrush.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f0b7-f45e-7d03-ad4c-ff09234116fe/exec-4ae0450c-d40d-45eb-803f-3879529261ee.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-ride-out/v012/image.png
- Image 3 IDENTITY: assets/vehicles/hire-speeder/reference.png; frozen assets/vehicles/hire-speeder/candidates/v006/image.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.77 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: All three changes landed and this is the strongest framing of the scene so far. SCALE: the nearest machine now spans about 210px of 1536, roughly 14 percent of frame width, against 36 percent in v012 and a cap of one fifth — inside the brief and close to the preferred one sixth. The plain finally feels enormous and the riders small and alone in it, which was the entire point of the shot. DUST: replaced by large billowing plumes boiling up and back behind each machine, rising well above hull height with rolling lobed silhouettes in warm bone and dusty ochre — the look from the speeder sheet's ridden panel that the user asked for, and far stronger as a signal of speed than v012's thin ground streaks. SION'S SCARF: correctly diagnosed and fixed. The recurring "cape" was never a cape — it was her teal scarf painted as a bulky cowl trailing a broad sheet. It is now a slim band at her throat with a short flick behind, and nothing reads as fabric hanging from her shoulders. Graxo remains the only caped figure. Held from v012: calm unbroken foreground with no chasm, machines floating clear of the rock with separated shadows, Graxo's corrected face, Daxus's light-to-medium skin and cross patches, warm ochre ground sharing the livery family, cool storm filling the horizon with forked lightning, no moon, prow lamps. DISCREPANCIES: (1) the group has flattened — pulling back left the three machines at similar depths and near-even lateral spacing, so it reads more like a rank than the deliberately scattered formation v010 and v012 had; depth variation needs restoring. (2) The ground still carries an all-over dashed dry-brush hatch, and at this wide framing it covers most of the picture, making it the single most visible style drift in the scene. Roughly ten passes have failed to shift it with prohibitions; the next attempt should try a countable positive constraint instead, in the manner of the Style Block's own hard limits. (3) File is 2.77 MB, over the 2.5 MB book-float budget.

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
Image 2 is EDIT TARGET: The scene baseline: the-ride-out v012. Its group, warm ground, storm, night light, machines, Graxo's face and Daxus's likeness are correct. Change only the three things the spec lists.
Image 3 is IDENTITY: The approved speeder sheet, for the machine's design AND for the look of the DUST in its ridden panel — a large billowing plume boiling up behind the machine. Ignore its grey background, its layout, its panels and its own rider.

TASK: A single 3:2 horizontal WIDE night scene: three small hover speeders crossing an enormous barren Kalagra plain toward the viewer with big billowing dust plumes behind them, the storm filling the horizon.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION — a picture of a place with people in it, filling the whole frame.

THIS IS NOT A REFERENCE SHEET. There are NO panels, NO boxes, NO split frames, NO dividing lines, NO borders, NO insets, NO turnaround views, NO orthographic views, NO expression rows, NO colour swatches, NO call-outs, NO title block, NO character names, NO labels, NO captions and NO TEXT OR LETTERING OF ANY KIND. One continuous painted scene, edge to edge.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only what is listed below. Image 3 is the speeder's approved sheet, here for TWO things only: the machine's design, and the look of the DUST in its ridden panel. Ignore its grey background, its layout, its panels and its own rider, and reproduce no sheet format from it.

SCENE: "The Ride Out." Night on Kalagra. The crew of the Antares cross an immense empty plain on three hire speeders, riding toward the viewer, the planet-wide storm filling the horizon behind them.

KEEP FROM IMAGE 2 — UNCHANGED: the loose scattered group with Daxus far left, Graxo nearest and centre, Sion right and mid-distance, in their current arrangement and uneven spacing; the calm unbroken warm ochre plain with no chasm or fissure in the foreground; the machines floating clearly above the rock with a visible gap and a separated shadow beneath each; the cool deep blue-violet night sky; the storm wall filling the horizon with its rolling cloud heads and forked lightning; NO moon anywhere; the off-frame moonlight raking the tops and fronts of the riders; each speeder's pale-yellow prow lamp; Graxo's corrected face and his deep wine-aubergine cape; Daxus's light-to-medium skin, glasses, off-white jacket and cross patches; and every detail of the three speeders — prow leading, rider straddling the saddle toward the rear with a boot on the flank stirrup, boom and rust engine pod trailing at the tail, ventral skid, and the sunset swipe kicking up toward the tail.

CHANGE ONE — PULL THE CAMERA MUCH FURTHER BACK. Image 2's nearest speeder fills about 36 percent of the frame's width. That is far too close and it kills the sense of scale. This must be a WIDE SHOT of an enormous empty country with three small machines crossing it.
- HARD CAP: the NEAREST speeder spans NO MORE than ONE FIFTH of the frame's width — 20 percent. One sixth, about 16 percent, is better. The other two are smaller again.
- Each rider is roughly ONE TENTH of the frame's height or less. Faces will be small and that is correct — do NOT enlarge anyone to show a face.
- Give the land and the storm far more of the picture than the machines. Widen the plain, deepen the distance, let the storm tower. The riders should look small and alone out there.
- If you are unsure how big to make them, make them SMALLER. It is not possible to overshoot this.

CHANGE TWO — SION'S SCARF IS FAR TOO BIG. This is the real fault, not a cape: in image 2 her teal scarf is painted as a thick bulky cowl wrapped round her neck and chest, trailing behind her as a broad sheet of cloth. At a glance it reads as a cape, and that is why it keeps being wrong.

Shrink it drastically. Her scarf is a SLIM, THIN band of teal cloth — a narrow strip no wider than her throat, wrapped once loosely at the neck, with SHORT ends that finish near her upper chest. It is a scarf of the kind you knot at the collar, not a shawl, snood, cowl, wrap, muffler or streamer. Behind her it may show only a short thin flick of cloth, no longer than her head is tall. It must NOT billow, fan, broaden, form folds across her back, or trail any distance behind her.

Sion wears NO cape, cloak, mantle, shawl, poncho or coat-tail. Her ochre utility jacket is short and close-fitting, ends at her hips and does not flare. Behind her shoulders there is open air and her dust plume, and nothing else. EXACTLY ONE character in this picture has anything streaming from their shoulders, and that is Graxo with his cape.

CHANGE THREE — BIGGER, BILLOWING DUST. Image 2's dust is a set of thin flat streaks lying on the ground, which reads weakly. Replace it with the kind of dust shown in image 3's ridden panel: a LARGE, BILLOWING PLUME boiling up and back from behind each machine.

Each plume is a substantial rolling mass of kicked-up sand that rises well above the height of its machine and drifts back and away, rolling and curling with a soft ragged silhouette and irregular lobed edges. Warm pale bone and dusty ochre where the light catches the tops, deeper warm grey-brown in the hollows. Paint it in a handful of broad tonal masses — full and voluminous, not thin — while keeping it painted rather than photographic: no fine speckle, no granular noise, no individual particles, no airbrushed haze, no transparency gradients. The plumes are the clearest signal of speed in the picture and should read instantly. Each machine's plume differs in size and angle from the others.

LIGHT AND COLOUR: unchanged. Warm ochre and grey-brown ground sharing the speeders' livery family, cool deep blue-violet sky and storm, off-frame moonlight as the only light on the riders, prow lamps and lightning the brightest points. No neon, no bloom, no lens flare, no light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
