# hegemony-assault-ship v008

User request verbatim: v4 is looking correct, direction wise... thrusters pointing backrward... The top down view is the one to save. Then generate the other views from it. / The star should be geometric. Lines, not points. / Hegemony is Black and Red.
Mode: Fresh sheet from v004's top view (IDENTITY), description v4: all pods aft, black/red, line-built star. Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a1043b-f501-7e11-8575-2cfbe7126f79/exec-031a709b-3552-4e92-9fe1-cf483a3c14f7.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/ships/hegemony-assault-ship/sources/top-view-from-v004.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.01 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Same, slightly longer hull and larger pods, open round intakes; side view stacks the two near pods; star line-built. All pods aft.

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
Image 2 is IDENTITY: The ship's top-down plan view. Copy its design exactly; repaint its colours as described.

TASK: A reference sheet of the Hegemony assault ship, a squat armoured space gunship.

SUBJECT DESIGN (description v4, restated so nothing is invented):
The Hegemony's storm-patrol gunship: a two-seat atmospheric interceptor built to hunt
unauthorized flights through Kalagra's planet-wide storm. Two of them chase the
Antares as she climbs out. *(Whole design provisional — first pass.)*

## Exterior

Not an aircraft: a squat, heavily armoured space gunship that flies on thrusters,
with no wings and no tail fins.

**Design authority: `sources/top-view-from-v004.png`**, the top-down plan. Every other
view agrees with it.

- About half the Antares's length, but bulky and heavy: a thick, blunt armoured hull
  shaped like a flattened hexagonal slab, wider than it is tall, with a blunt angled
  prow — no pointed nose.
- A small armoured cockpit set into the top of the prow: a narrow horizontal slit of
  dark glass under a heavy brow, like a visor in a helmet.
- FOUR stubby round thruster pods, one at each corner of the hull on short armoured
  pylons. All four point straight AFT, their axes parallel to the hull's centreline:
  intake rim forward, exhaust behind, glowing hard white-blue.
- A blocky gun turret slung under the prow with two heavy laser barrels, and a
  rack of sensor fins and antennas along the spine.
- Thick overlapping armour plates with straight seams, heavy bolts and vent grilles.

## Colour and marking

- The Hegemony's colours are **black and red**. Hull: matte black armour, weathered
  to charcoal grey on exposed edges by sandstorms.
- Blood-red bands around each thruster pod and a red stripe along each flank.
- **The Hegemony emblem**: a geometric eight-armed star built from straight bars,
  not points — a bold plus sign of thick square-ended bars over a thinner diagonal
  cross of square-ended bars, all meeting at the centre. Red, on the top of the hull
  and on each flank. No lettering, numbers or other insignia.

A single reference sheet on a plain flat mid-grey background, a 3:2 horizontal
rectangle. No text, labels, arrows or frames.

Image 2 is the ship's top-down plan view: the design authority. Copy its outline,
hull panels, cockpit, chin turret and the four corner thruster pods exactly, and build
every other view from it. Repaint its colours to black and red as described.

The same ship in four views at one consistent scale, separated by empty grey:
- LEFT HALF, largest: a three-quarter view from in front, above and to the left, in
  flight. All four thruster pods point straight back, exhausts glowing behind the
  ship.
- Upper right: a side elevation, nose to the left, pods' exhausts to the right.
- Middle right: the top-down plan view, nose to the left, matching image 2.
- Lower right: a head-on front view, the four pods' intake rims facing us.

Squat and heavily armoured: thick, low and wide.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
