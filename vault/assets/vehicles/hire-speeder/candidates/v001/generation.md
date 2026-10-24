# hire-speeder v001

User request verbatim: these are the stripes. 70s swipe. / not just the color, the swipe pattern too. if possible
Mode: First candidate for NEW asset vehicles/hire-speeder, against description v2. Four-view sheet (3/4 hero, side elevation, top plan, head-on) on plain grey, machine only. Fore/aft order stated explicitly — prow leads, rider toward the rear, boom and engine pod TRAILING at the tail — after two scene attempts were rejected as reversed. Livery is the 1970s Dodge Tradesman sunset swipe read off the user's photos, but supplied as a synthetic flat graphic generated here (sources/livery-swipe-study-v2.png) carrying both the band order and the level-then-kick-up curve, so no van bodywork or road scene reaches the model. The user's photos are filed in sources/ for provenance only and are NOT attached.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f08a-6940-7ec2-9da6-dddd2fe743db/exec-2234641d-a00e-49bf-ad82-71f0823d0f65.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/vehicles/hire-speeder/sources/user-geometry-reference-2026-09-29.png
- Image 3 IDENTITY: assets/vehicles/hire-speeder/sources/livery-swipe-study-v2.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.64 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: First candidate for the new asset and a strong one. THE ORIENTATION PROBLEM IS SOLVED: all four views agree that the prow leads (blunt raked nose with its forward grille), the long body runs back from it, the rider's open tub sits toward the REAR behind a small windscreen, and the boom with its curved pipework carries the cylindrical engine pod at the TAIL with vanes and whip antenna back there. This is the layout description v2 specifies and the reverse of what two scene attempts produced. Building it as a four-view sheet is what fixed it: the side elevation and top plan force a single consistent fore/aft reading in a way a single scene view never did. Sheet structure is correct: three-quarter hero upper left, side elevation upper right, top plan lower left, head-on front lower right, all on plain flat grey, machine only, with no people, no landscape, no text and no labels. Proportions match the brief at roughly three times as long as tall, low throughout, with the boom carrying the pod well clear of the hull. LIVERY: the 1970s sunset swipe landed — cream, golden yellow, orange, red-orange and dark brown in the right order, running level along the flank and sweeping upward together toward the rear in one continuous curve, and it reads on the hero, side and top views consistently. Supplying it as a synthetic flat graphic worked: no van bodywork, wheels or road scene leaked in. Ground clearance, ventral skid pods, absence of wheels, and honest chipped sand-scoured wear all present. OUTSTANDING per user direction at time of writing: the swipe bands should GROW WIDER after the kick, thickening as they sweep up toward the tail, as they do on the reference van; the current study holds them at constant thickness and the candidate inherited that. Not yet approved; do not promote. No reference.png exists, so the speeder is still unapproved and must not be attached as IDENTITY to any scene.

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
Image 2 is IDENTITY: The GEOMETRY reference for this machine, supplied by the user. Copy its shapes and the order of its parts. Ignore its rendering entirely — its smooth digital shading, grey studio backdrop, horizon bands and glowing exhaust are not part of this sheet.
Image 3 is IDENTITY: The LIVERY SWIPE study. Copy TWO things from it and nothing else: the band COLOURS in order (narrow cream, golden yellow, orange, red-orange, dark brown) and the SWIPE PATTERN — bands running level, then sweeping upward together in one smooth continuous curve toward the rear, staying parallel and keeping their thickness through the rise. It is a flat graphic specification, not a vehicle and not a scene; reproduce no object from it.

TASK: A four-view reference sheet for the Kalagra hire speeder on a plain flat mid-grey background, machine only, no people and no landscape.

SUBJECT DESIGN (description v2, restated so nothing is invented):
A battered single-seat hover speeder of the kind rented out by remote landing-pad
operators on Kalagra. Three of them appear in "The Ride Out." Built for hard use on
open rock by people who are not their owners.

## Layout — front to back

The machine's order along its own length, from the leading end to the trailing end:

1. **Prow.** The leading end is the body itself: a low, blunt, slightly raked nose
   with a small forward grille or intake. Nothing projects ahead of it — no pod, no
   boom, no drum, no cylinder, no lance point.
2. **Body.** A long, low hull running back from the prow, its upper deck carrying
   the livery. This is the machine's largest single mass and it lies *ahead of the
   rider*.
3. **Rider.** Seated toward the **rear** of the body in an open tub behind a small
   curved windscreen blister. The long deck stretches away in front of them; there
   is comparatively little hull behind them. The rider sits *in* the machine, never
   astride it — no straddled saddle, no bicycle handlebars, no upright motorcycle
   posture.
4. **Boom.** From the back of the hull, behind the rider, a slim exposed boom of
   open structure and curved pipework reaches **backward**.
5. **Engine pod.** At the very **tail**, carried on the end of that boom: a fat
   cylinder with a ribbed collar, mounted low, its open mouth facing backward, away
   from the direction of travel. Angular vanes and a small forked bracket hang
   beneath and behind it, and a thin whip antenna curves up from the structure back
   there. This is the machine's **only** engine pod.

The check: the rider looks out over a long bonnet of hull, and the drum-shaped
engine hangs out behind them on its boom like an outboard motor at the stern of a
boat. **The pod is the last thing in the direction of travel, never the first.**

## Proportions

Long and low. Nose to pod, total length is about **three times** the maximum
height. The body is the front two thirds; the boom and pod are the rear third.
Nothing about the machine is tall, chunky or stubby.

## Ground clearance

It hovers a hand's breadth clear of the ground, with clear daylight and a cast
shadow beneath it. There are **no wheels, tyres, rims, spokes, forks or
mudguards** — not anywhere, not on any variant.

## Livery

Pale cream and ivory upper body over a dark brown lower body.

Along the flank runs a **1970s van "sunset swipe"** — a set of parallel bands in a
warm graduated sequence. Top to bottom the order is:

1. a **narrow cream** separator band
2. **golden yellow**
3. **orange**
4. **red-orange / rust**
5. **dark brown**, the widest, merging into the dark lower body

**The swipe pattern matters as much as the colours.** The bands run LEVEL along the
length of the body, then, toward the **rear**, all sweep UPWARD together in one
smooth continuous curve, staying parallel and keeping their thickness through the
rise, finishing high on the tail. The kick is a gentle S-curve, not a sharp angle
and not a chevron. At the front the bands end in a clean squared termination.

`sources/livery-swipe-study-v2.png` is the authority on both the colour order and
the swipe geometry. `sources/livery-van-reference-a.png` and
`-b.png` are the user's source photographs of the 1977 Dodge Tradesman livery this
is drawn from; they are recorded for provenance and are **not** attached to
generations, so no van bodywork or road scene can leak into the speeder's design.

The bands are painted graphics: flat opaque colour, hard clean edges, no gradients,
no airbrushing, no glow, no metallic sheen.

## Wear

A hire fleet, worn honestly: chipped and sand-scoured leading edges, mismatched
replacement panels interrupting the bands, stripes faded pale in places. The paint
is old; the machine still works.

## Open question

The **fore/aft orientation above is the corrected reading** of the user's geometry
reference (`sources/user-geometry-reference-2026-09-29.png`). Two scene attempts
placed the engine pod at the nose and were rejected as reversed. If the reference
sheet comes back with the pod leading again, this section is where the error lives.

OUTPUT FORM — READ FIRST: produce ONE single continuous reference sheet on a plain
flat mid-grey background. THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly
one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image.
It is NOT a 2:1 banner, NOT a panorama, NOT a square. There are NO people, NO
figures, NO riders, NO landscape, NO sky, NO ground, NO dust and NO scenery
anywhere in this image — the machine alone, on empty grey. There is NO text, NO
labels, NO callouts, NO arrows, NO dimension lines, NO borders and NO frames.

THE SHEET shows the SAME single machine in FOUR views, evenly spaced and drawn at a
consistent scale, each fully separated from the others by empty grey:

- Upper left, largest: a THREE-QUARTER HERO VIEW from in front, above and to the
  machine's left, showing the prow, the near flank and the top deck at once.
- Upper right: a full SIDE ELEVATION, the machine level and square to the viewer,
  nose to the LEFT and tail engine pod to the RIGHT. This view is the authority on
  the machine's length, height and the order of its parts.
- Lower left: a TOP-DOWN plan view, nose to the left.
- Lower right: a HEAD-ON FRONT view, looking straight at the prow.

Every view must agree with every other view on the order of the parts, the length,
the height and the placement of the livery.

Image 1 is STYLE: the rendering anchor. Match its hand-painted matte technique only.
Image 2 is the GEOMETRY reference for this machine's shapes and layout. Image 3 is
the LIVERY study: copy the stripe assembly's colours, their order and their relative
widths, and nothing else — it is a flat colour specification, not a vehicle and not
a scene.

Keep the machine simple and readable: large flat blocks of colour with hard angular
edges, details suggested rather than drawn in full. No glow, no reflections, no
lens effects, no cast environment.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
