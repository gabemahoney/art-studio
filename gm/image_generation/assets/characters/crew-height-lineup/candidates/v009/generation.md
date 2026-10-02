# crew-height-lineup v009

User request verbatim: Oh. You need to regenerate the lineup then. / GRaxo canonical is his indivudal reference.
Mode: Lineup revision following the user's ruling that an asset's own individual reference is canon. The approved lineup disagreed with Graxo's individual sheet on two colours — it painted his cape bright magenta-pink where his sheet shows deep wine aubergine with a dusty mauve lining, and his vest ochre where his sheet shows dark olive-charcoal. Since the lineup is the DERIVED asset, it is the one corrected. Follows the revision rule written into the lineup's own description.md: each depicted character's approved reference.png attached as IDENTITY alongside the baseline. Poses, order, heights, the height chart and Daxus's and Sion's designs all explicitly frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f0c0-3cdf-7d00-a879-ac94392ff94d/exec-08e8a1d0-f299-4f38-9385-bb4aed189b1a.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v008/image.png
- Image 3 IDENTITY: assets/characters/graxo/reference.png; frozen assets/characters/graxo/candidates/v027/image.png
- Image 4 IDENTITY: assets/characters/sion/reference.png; frozen assets/characters/sion/candidates/v001/image.png
- Image 5 IDENTITY: assets/characters/daxus/reference.png; frozen assets/characters/daxus/candidates/v001/image.png
Date: 2026-09-29
Status: approved and promoted to reference.png on 2026-09-30. User approval: "line up v9 is approved"
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.04 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Lineup brought back into agreement with canon. Graxo's cape is now the deep wine aubergine his individual sheet paints, with the dusty mauve inner lining carrying its sparse gold cross motifs, replacing the bright magenta-pink the previous lineup showed. His vest is now the dark olive-charcoal of his sheet rather than the ochre-mustard the previous lineup gave him. Both antique-gold collar pins, the high standing collar, the plum ascot, his belt and holstered blaster, his face with its silver-grey temples and mustache, his pose and his height are all unchanged. Daxus and Sion are untouched and still match their own sheets: Daxus's off-white medical jacket with red cross patches, burnt-orange shirt, bandolier and chest scanner; Sion's ochre jacket with the absent left sleeve, slim teal scarf, bare steel-gray left cyber arm and opaque ruby goggles. Left-to-right order, standing poses, relative heights and the height chart with its foot rules and numbers are all preserved. Background remains the plain cool studio field. This revision exists because the user ruled that an asset's own individual reference is canonical for that asset, which made the LINEUP the wrong party in a conflict it had with Graxo's sheet — the derived asset follows the individual one, never the reverse. It also follows the revision rule already written into this asset's own description.md, which requires each depicted character's approved reference.png to be attached as an IDENTITY input alongside the baseline. Awaiting the user's explicit approval; promote.py must not run without it. Until promoted, the existing reference.png remains the approved lineup and this candidate must not be attached to scenes.

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
Image 2 is EDIT TARGET: The current approved crew lineup. Reproduce it and change only Graxo's cape and vest colours.
Image 3 is IDENTITY: GRAXO's approved individual sheet — CANONICAL for his colours: a deep wine-aubergine cape with a dusty mauve lining carrying gold cross motifs, and a dark olive-charcoal vest. Ignore its layout, multiple views, expression busts and grey background.
Image 4 is IDENTITY: SION's approved individual sheet — her design is already correct in the baseline; use this only to confirm it. Ignore its layout, multiple views, expression busts, height chart and grey background.
Image 5 is IDENTITY: DAXUS's approved individual sheet — his design is already correct in the baseline; use this only to confirm it. Ignore its layout, multiple views, expression busts, height chart and grey background.

TASK: The crew height-comparison sheet: Daxus, Graxo and Sion standing side by side against a height chart, with Graxo's cape and vest corrected to his canonical colours.

OUTPUT FORM — READ FIRST: produce ONE single continuous crew height-comparison sheet. THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the BASELINE — the current approved lineup. Reproduce it faithfully and change only the colours listed below. Images 3, 4 and 5 are the three characters' own approved individual sheets and are the CANONICAL authority on each person's colours and design; where the baseline disagrees with them, they win. Take likeness and colour from them, and reproduce none of their layout, multiple views, expression busts or grey backgrounds.

THE SHEET: the three crew standing side by side at consistent scale against a plain background with a simple height chart behind them — horizontal rules with foot markings up the left edge, soles at zero, each crown at their stated height. Left to right: DAXUS at 6 feet 0, GRAXO at 6 feet 2, SION at 5 feet 9. This is the one sheet in the vault that carries a height chart, so its rules and foot numbers are correct and should be kept.

KEEP FROM IMAGE 2 — UNCHANGED: the left-to-right order, each figure's standing pose and stance, their relative heights and placement against the chart, the height chart itself with its rules and numbers, the plain cool studio background, and every element of Daxus's and Sion's design — Daxus's off-white medical jacket with its high collar, red cross patches, burnt-orange shirt, bandolier and chest scanner, brown trousers and boots; Sion's ochre utility jacket with the absent left sleeve, slim teal scarf, bare steel-gray left cyber arm, charcoal cargo trousers and black boots, and her opaque ruby goggles. Do not re-pose anyone, do not re-frame, do not change the chart.

THE ONE CHANGE — CORRECT GRAXO'S COLOURS TO MATCH HIS OWN SHEET. In image 2 Graxo is painted with the wrong cape and the wrong vest. His individual sheet is canon. Repaint:

HIS CAPE: in image 2 it is a bright, saturated MAGENTA-PINK. That is wrong. It must be a DEEP WINE AUBERGINE — a dark, heavily greyed-off purple with a great deal of brown and red in it, like a dark aubergine's skin or a dried plum. Much darker and far less saturated than the baseline shows: closer to deep burgundy-brown than to pink. It is NOT magenta, NOT hot pink, NOT fuchsia, NOT bright violet. Where the cape opens and turns, its inner face shows a slightly lighter DUSTY MAUVE lining carrying sparse small gold cross motifs, exactly as his sheet paints it. Keep the cape's shape, length and drape, its high standing collar, and the two square antique-gold medallion pins, one at each front edge.

HIS VEST: in image 2 it is OCHRE or mustard. That is wrong. It must be the DARK OLIVE-CHARCOAL his sheet shows — a deep, cool, desaturated grey-green-brown, clearly darker than his ivory shirt and carrying no yellow. Keep its cut, its buttons and its plum ascot above it.

Everything else about Graxo stays as image 2 has it: his face, his hair with its silver-grey temples, his mustache, his ivory shirt, his belt and holstered blaster, his charcoal trousers and boots, his height and his pose.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
