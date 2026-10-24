# the-rusty-robot v013

User request verbatim: If we can fix the robot logo then this is the one!
Mode: Edit off v012 (user-designated): robot emblem only, two separate eyes. Only the emblem regions will be kept; composite onto v012 follows.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10375-bed1-7000-8cbf-f7e270754f41/exec-fe8cca59-9360-4188-96d2-2d86893ada76.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: assets/locations/the-rusty-robot/candidates/v012/image.png
- Image 3 IDENTITY: assets/locations/the-rusty-robot/sources/sign-board-flat-from-v082.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: delivered-1536x1024.png, 1536x1024, sRGB 8-bit PNG-24 no alpha, flattened onto #1b1e26, 1.47 MB; scaled to fit from raw 1536x1024
Review: Emblem fixed: two separate round eyes, bow tie, two buttons, antenna, in both views. Rest of frame lightly repainted; only the emblem regions are used, in v014.

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
Image 2 is EDIT TARGET: The reference sheet being revised. Preserve everything the spec does not change.
Image 3 is IDENTITY: The sign board, flattened: copy its robot emblem's design.

TASK: Revise this architectural reference sheet of the Rusty Robot cantina.

Reproduce image 2, the reference sheet, and change ONE thing: the robot emblem at the
right end of the sign, in the three-quarter view and the front elevation. Everything
else stays exactly as it is.

In image 2 the robot's two eyes have merged into one dark heart-shaped blot. Image 3 is
the sign as it should read: paint the robot emblem exactly as it appears there.

The emblem is a solid ivory silhouette of a butler robot, as tall as the large
capitals:
- a domed head topped by a thin stalk with a small ball antenna;
- TWO round dark eyes, side by side, each a separate small circle, with ivory between
  them;
- below the head, a dark bow tie;
- two round dark buttons, one above the other, down the chest;
- sloping shoulders, the body widening to the board's bottom edge.

It lies flat on the board, in the same plane and perspective as the lettering.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
