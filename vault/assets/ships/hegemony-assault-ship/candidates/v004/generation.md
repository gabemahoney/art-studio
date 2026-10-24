# hegemony-assault-ship v004

User request verbatim: Looks too much like a jet.
Mode: Fresh sheet, description v2: wingless armoured hex-slab gunship on four thruster pods. Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10437-44bb-7e00-883b-c085aac4419e/exec-16fffd02-d9e4-4fa0-baf4-f1490ff785fe.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.95 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Same design, longer and lower, larger pods, chin turret more prominent; four views agree.

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

TASK: A reference sheet of the Hegemony assault ship, a heavy armoured space gunship — not an aircraft.

SUBJECT DESIGN (description v2, restated so nothing is invented):
The Hegemony's storm-patrol gunship: a two-seat atmospheric interceptor built to hunt
unauthorized flights through Kalagra's planet-wide storm. Two of them chase the
Antares as she climbs out. *(Whole design provisional — first pass.)*

## Exterior

Not an aircraft: a heavy armoured space gunship that hovers and flies on thrusters,
with no wings and no tail fins.

- About half the Antares's length, but bulky and heavy: a thick, blunt armoured hull
  shaped like a flattened hexagonal slab, wider than it is tall, with a blunt angled
  prow — no pointed nose.
- A small armoured cockpit set into the top of the prow: a narrow horizontal slit of
  dark glass under a heavy brow, like a visor in a helmet.
- FOUR stubby round thruster pods, one at each corner of the hull on short
  armoured pylons, each able to swivel; their exhausts glow hard white-blue.
- A blocky gun turret slung under the prow with two heavy laser barrels, and a
  rack of sensor fins and antennas along the spine.
- Thick overlapping armour plates with straight seams, heavy bolts and vent grilles.

## Colour

- Dark gunmetal grey hull, matte, weathered by sandstorms.
- One thin blood-red stripe along each flank from nose to tail, and a red band
  around the engine housing — the Hegemony's marking.
- No lettering, numbers or insignia text.

A single reference sheet on a plain flat mid-grey background, a 3:2 horizontal
rectangle. No text, labels, arrows or frames.

The same ship in four views at one consistent scale, separated by empty grey:
- LEFT HALF, largest: a three-quarter view from in front, above and to the left, in
  flight, its engine glowing.
- Upper right: a side elevation, nose to the left.
- Middle right: a top-down plan view, nose to the left.
- Lower right: a head-on front view.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
