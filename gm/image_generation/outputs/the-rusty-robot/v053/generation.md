# the-rusty-robot v053

User request verbatim: lets remove the handrails. its too complicated
Mode: Both handrails, posts and fixings removed; steps, parapets and pier caps painted bare behind them. Five passes had failed to make the pair symmetrical.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f8c2-84b7-7a60-9d68-d523ace5f236/exec-d8f70dcf-a0a5-492f-96f4-9da03e1e1c5b.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v052/image.png
Date: 2026-10-01
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.98 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
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

## Note on the Forbidden list

Every item in the Style Block's "Forbidden" line names a **rendering tell**, not a
subject: smooth gradients, airbrush, photographic detail, fine linework,
micro-detail, more than three values, granular noise, polygon mosaics, the polished
modern AI look — and, in that same company, **"neon or rim lighting."**

So "neon" there forbids the *look*: saturated glow, bloom, halo, soft falloff, the
lit-from-within sheen of modern digital art. It does **not** forbid lit signage,
lamps, glowing instruments or electric light as subject matter. The world can have
neon in it; the painting must not be rendered like neon.

A lit sign is therefore fine when it is painted the way this style paints
everything else: flat opaque shapes with hard edges, a bright core and at most one
darker band of the same hue, no glow, no gradient, no rays. Recorded 2026-09-30
after the electric sign in `outputs/the-rusty-robot/`, where reading the ban as a
subject prohibition would have blocked a legitimate art direction.

This note sits outside the Style Block and changes none of its text, so it does not
require a style version bump.

Image 1 is STYLE: Match its hand-painted matte rendering only. Ignore its subjects.
Image 2 is EDIT TARGET: Reproduce this picture and change only what the spec names.

TASK: A single scene illustration: the exterior of the Rusty Robot cantina at night in the domed city of Kannan.

Reproduce image 2 and remove ONE set of things: both handrails on the entrance
staircase. Everything else in the picture stays exactly as it is.

REMOVE BOTH HANDRAILS COMPLETELY. Take away the dark metal rail on the left of the
steps and the dark metal rail on the right of the steps, together with every vertical
post that carries them and every base plate or fixing where a post meets the stone.
When you are done there is NO metal railing anywhere on this staircase.

PAINT WHAT IS BEHIND THEM. Where each rail and post used to be, continue the surface
that sits behind it:

- Across the steps, the treads and risers run on unbroken from one side of the flight
  to the other. Every step is one continuous band of stone with nothing standing on it
  and nothing crossing it.
- Along each side, the parapet runs up as one clean unbroken diagonal of stone, its
  crest bare, with no posts rising from it and no fixings in it.
- On each pier at the foot of the flight, the chamfered cap is whole and bare.

Leave NO trace of the railings: no stubs, no sockets, no bolt plates, no patches of
differently coloured stone, no leftover shadows cast by rails or posts, and no gaps
in the step shadows where a post used to stand. The staircase should look as though
it never had a railing.

KEEP THE STAIRCASE ITSELF EXACTLY AS IT IS: the same number of steps with the same
treads and risers, the same two parapets at the same slope, the same two piers with
their chamfered caps, in the same position in the frame and at the same size.

LIGHTING IS UNCHANGED, except that the shadows the rails and posts were casting are
gone with them. The warm pool of light across the steps stays exactly as bright as it
is and falls across the steps the same way; the alley at the left stays as dark as it
is now; the three crew stay in shadow; the cool blue dome light above is unchanged.
Do not brighten anything.

Everything else is unchanged: the sign with its lettering and robot emblem, the canopy
with its two stepped ends and its two downlights, the doorway and its round-arched
door, the swept paving with no rocks or rubble, the three crew at their exact
positions, sizes, postures and depth of shadow, the street, the dome, the distant
figures and the lamps.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
