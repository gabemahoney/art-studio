# the-rusty-robot v085

User request verbatim: It looks perfect to me except for the scale. The crew are much too large considering how close they are to the cantina. They are in the alley right next to it.
Mode: Edit off v083 (user: 'looks perfect except for the scale'): crew shrunk from ~830 px to ~330 px tall (Graxo), feet kept at the alley mouth.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a1040a-0c9d-7b82-998a-83f4e4a7a84d/exec-94a1cf46-a9cb-4000-b767-3018a9623f65.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v083/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.17 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: PARTIAL: crew shrank from ~830 px to ~575 px (Graxo), but the scene was zoomed in at the same time, so they are still ~2.4x the door's height (door ~240 px). Asked for ~330 px. Poses, likenesses, lighting kept.

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
Image 2 is EDIT TARGET: The scene being revised. Preserve everything the spec does not change.
Image 3 is IDENTITY: The approved crew lineup. Keep the crew's likenesses and clothing matching it.

TASK: Revise this scene: the crew conferring in the dark alley beside the Rusty Robot cantina.

Reproduce image 2 and change ONE thing: the SIZE of the three crew. Keep everything
else as it is — their poses, grouping, likenesses, clothing and lighting, the alley,
the Rusty Robot, the street, the dome.

The crew stand in the alley right beside the cantina, at about the same distance from
the viewer as the cantina's front-left corner. They must be to scale with it:

- In image 2 Graxo, the tallest, is about 830 pixels tall — three times the height of
  the cantina's arched door (about 280 pixels). That is far too big.
- Make Graxo about 330 pixels tall: a little taller than the door, about one third of
  the picture's height. Daxus and Sion shrink in proportion.
- Their feet stay on the alley paving at the alley's mouth, near the bottom of the
  picture; their heads now come only to about the height of the canopy's underside.
- The space above them, freed by shrinking, is the alley's dark interior and the
  cantina's shadowed left side wall.

If unsure, paint them smaller.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
