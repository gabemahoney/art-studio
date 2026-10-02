# the-rusty-robot v062

User request verbatim: Where the alley meets the building the geometry gets kind of vague. We need to tight this up. And the overhang below the sign still has strange outcroppings on the top that need to be remove.
Mode: Edit off v061: one straight canopy top edge at the left end (two step-shoulders deleted); alley/cantina corner rebuilt as one corner line with the near wall meeting the pavement, floating slabs deleted.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0fd6c-ba74-7f42-980e-3842fce45fff/exec-368133af-47af-424d-bd3a-dfa1ebd6a57a.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v061/image.png
Date: 2026-10-02
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Review: pending — record with bin/review.py once you have seen it

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
Image 2 is EDIT TARGET: Reproduce this picture and change only what the spec names.

TASK: A single scene illustration: the exterior of the Rusty Robot cantina at night in the domed city of Kannan.

Reproduce image 2 and rebuild TWO things. Everything else stays exactly as it is.

FIRST: THE TOP EDGE OF THE CANOPY, at its LEFT END, where it meets the building.

The canopy is the deep slab above the door and below the sign. Its TOP edge, along
the left end, is currently broken by two small square shoulders that step up out of
it — one just before the slab passes behind the sign, one a little further left.
They read as leftover tabs stuck on the top surface.

Make that top edge ONE unbroken straight line. Count it: from the point where the
canopy meets the building wall on the left, to the point where it disappears behind
the sign board, the top edge is a SINGLE straight run — one edge, one angle, no
steps, no shoulders, no tabs, no nibs. If a shape on that top edge is smaller than
the downlight recess beneath the canopy, it should not be there.

Where a shoulder is deleted, paint the surface that sits behind it — the plain wall
face above the canopy — so no stub, socket, patch or leftover shadow remains.

SECOND: WHERE THE ALLEY WALL MEETS THE FRONT OF THE CANTINA, on the left of the steps.

That junction is currently built from four vertical slabs of similar width standing
side by side at different depths, so the corner reads as a flat stack of bands rather
than as two walls meeting. One dark slab near the foot of the steps floats clear of
the ground entirely.

Rebuild it as a plain masonry corner. Count it:

- EXACTLY ONE vertical corner line where the two walls meet, running from the top of
  the frame down to the pavement, unbroken.
- The near wall — the alley side the crew stands against — is ONE unbroken flat slab
  from top to bottom. Its base meets the pavement in a single straight horizontal
  line, with the paving running up to it and stopping. Nothing floats.
- The far wall — the lit cantina front carrying the door and steps — is ONE flat
  plane running back from that corner line.
- Between them, at the corner, AT MOST ONE stepped buttress: a plain square block,
  taller than it is wide, sitting on the pavement. Not a stack, not a staircase of
  fragments.
- DELETE every loose block at the base: no detached slabs, no floating wedges, no
  rubble chips that touch nothing.

The corner must read so that a person could walk up to it and put a hand flat on
each of the two walls.

FREEZE EVERYTHING ELSE. Unchanged: all four crew members at the left, their poses,
faces, clothing and the robot arm; the sign board and its lettering; the door, its
ironwork and the steps; the downlights and every lit window; the domed city beyond;
the paving and its reflections. There are NO handrails anywhere on the steps and
none may be added.

LIGHTING IS UNCHANGED. The crew stand in deep shadow and the steps are lit: the
crew's region measures 0.298 times the brightness of the lit steps, and it must
still measure 0.298 after this edit. Do not brighten the crew to make them legible.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
