# kalagra-storm-gorge v002

User request verbatim: I am wondering if we should do this in layers. Canyon first, then Antares, then pursuit ships.
Mode: Layer 1: empty storm gorge, diagonal, open air down the middle for the chase. Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a104ed-4dc9-7d62-b8e4-a5323389b7c9/exec-2b2ae057-f152-4efb-97a8-b7c9a70bea05.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.58 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: Empty gorge: deeper and narrower, lightning in the sky gap, sand curtains, more foreground boulders; the gorge runs straight away more than it bends.

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

Image 1 is STYLE: Match its hand-painted matte rendering only. Ignore its subjects.

TASK: A single illustration of an empty storm gorge on Kalagra at night.

SUBJECT DESIGN (description v1, restated so nothing is invented):
A narrow, twisting gorge cut into Kannan's crater wall on Kalagra, at night, inside the
planet-wide storm. The setting for the Antares's escape in "Getting Sky".
*(Provisional throughout.)*

- Towering sheer cliffs of black and dark slate rock, fractured into tall angular
  slabs and ledges, closing in on both sides.
- The gorge twists: it runs from the far distance toward the viewer and bends.
- Wind-driven sand fills the air in grey curtains that streak diagonally; dust boils
  along the gorge floor.
- A strip of churning storm sky between the cliff tops; forks of lightning throw cold
  blue-white light across the cliff faces.
- Palette: dark slate, storm blue and black, lit cold by lightning. No warm light.
- No vehicles, ships, people or structures.

ONE single continuous illustration, a 3:2 horizontal rectangle. No text or frames.
The empty gorge only — no ships, vehicles or people.

The camera is low inside the gorge, looking up its length on a strong diagonal: the
gorge comes from the far distance at upper left, bends, and opens toward the viewer
at lower right. The cliff walls tower on both sides, leaning in. Leave open air down
the middle of the gorge along that diagonal — the space where a chase will fly.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
