# hire-speeder v003

User request verbatim: However, maybe it should be setup so they straddle it instead of sitting inside. Do a study with a generic character riding it too. / remove the antenaa off the back as well / And lets use one of the colors from the swipe for the engine turbine thing. Also, a little less heavy on the tubes going to the back. Like, fewer and a bit less chaotic.
Mode: Edit off candidate v002 against description v5. Four changes: (1) riding posture reversed from seated-in-a-tub to STRADDLING a saddle on the hull spine, legs down each flank, motorcycle posture, no cockpit well; (2) a fifth RIDDEN STUDY view added with one deliberately generic mannequin rider for posture and scale — no cape, no costume, no named-character features; (3) the tail whip antenna removed entirely; (4) the engine pod recoloured to the swipe's fourth band (deep red-orange rust) with a cream collar band so it belongs to the livery, and the boom plumbing cut back to two or three tidy parallel tubes instead of a tangle.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f08f-4619-7f10-97cb-bb7b4850d26a/exec-7d70ed57-cc8f-4c6d-8821-7f20e73b764c.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/vehicles/hire-speeder/sources/user-geometry-reference-2026-09-29.png
- Image 3 EDIT TARGET: assets/vehicles/hire-speeder/candidates/v002/image.png
- Image 4 IDENTITY: assets/vehicles/hire-speeder/sources/livery-swipe-study-v3.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.57 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Four of four requested changes landed. STRADDLE: the new ridden study at lower right shows the posture correctly at last — the rider sits ON the machine astride a saddle, one leg down the near flank with the boot on a footrest, torso upright and leaning forward onto handlebar grips, whole body from the thighs up out in the open air. It reads as riding a motorcycle, not sitting in a car. Note for the record: v002 could not have shown a straddle, as it was generated against description v3 which still specified a seated tub; v003 is the first attempt after the posture was reversed in description v4. GENERIC RIDER: the figure is deliberately anonymous — drab utility jacket, goggles, wrapped dust scarf, no cape, no costume, no insignia, no weapon — and exactly one figure appears on the sheet, the other four views being machine-only. ANTENNA: removed completely, gone from every view. TUBES: the tail plumbing is now two or three clean parallel runs following the boom with simple clamps, instead of v002's dense knot. ENGINE POD: repainted in the swipe's fourth band, the deep red-orange rust, with one narrow cream band at its collar, so it plainly belongs to the livery rather than being a separate bright red. Held from v002: fore/aft order with the prow leading and the pod trailing, the five views consistent with one another, long low proportions, the sunset swipe widening toward the tail, honest chipped wear, no wheels, plain grey ground, no text. ONE INTERNAL INCONSISTENCY TO FIX: the four unridden views still draw the rider's station as a recessed well with a windscreen — most visible in the top plan, where it reads as a sunken tub or bench rather than a narrow saddle sitting proud on the hull spine. The ridden study and the unridden views therefore disagree about what the rider sits on. The saddle should read as a raised narrow saddle in every view, with the deck stepping down either side of it. Not yet approved; do not promote. No reference.png exists, so the speeder remains unapproved and must not be attached as IDENTITY to any scene.

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
Image 2 is IDENTITY: The GEOMETRY reference for this machine, supplied by the user. Copy its overall shapes and the order of its parts. Ignore its rendering entirely, and note two deliberate departures from it: this machine has NO antenna, and its tail plumbing is far sparser — two or three tidy parallel tubes, not a dense tangle.
Image 3 is EDIT TARGET: The approved-so-far sheet: hire-speeder candidate v002. Its four unridden views, geometry, fore/aft order, proportions, widening swipe and grey ground are all correct. Change only what the spec below specifies.
Image 4 is IDENTITY: The LIVERY SWIPE study. Copy the band COLOURS in order (narrow cream, golden yellow, orange, red-orange, dark brown), the SWIPE PATTERN, and the WIDENING toward the tail. The engine pod is painted in the FOURTH band's deep red-orange rust, with one narrow cream band at its collar. It is a flat graphic specification, not a vehicle and not a scene; reproduce no object from it.

TASK: A five-view reference sheet for the Kalagra hire speeder on plain flat mid-grey, four views of the machine alone plus one ridden study with a single generic rider straddling it.

SUBJECT DESIGN (description v5, restated so nothing is invented):
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
3. **Rider.** **Straddles** the machine toward the **rear** of the body, sitting
   *on* it rather than in it. A narrow saddle sits on the spine of the hull where
   the deck steps down behind the body's widest point; the rider sits astride it
   with one leg down each flank and boots on small footrests or pegs set into the
   sides. Ahead of the saddle the deck rises into a low cowl with a small curved
   windscreen, and the rider leans forward onto a set of grips or a short
   handlebar yoke mounted on that cowl. There is **no enclosing tub, no cockpit
   well, no bucket seat and no sunken footwell** — the rider's whole body from the
   thighs up is out in the open air above the hull, the way a motorcyclist rides.
   The long deck stretches away in front of them; there is comparatively little
   hull behind them.
4. **Boom.** From the back of the hull, behind the rider, a slim exposed boom
   reaches **backward** to carry the engine pod. Its plumbing is **sparse and
   orderly**: just **two or three** clean tubes running back alongside the boom,
   roughly parallel, following the same line, with a couple of simple clamps. It
   reads as tidy exposed engineering, not as a tangle. Avoid a dense knot of pipes,
   looping or coiled runs, criss-crossing, bundled cable looms or a chaotic mass of
   hoses.
5. **Engine pod.** At the very **tail**, carried on the end of that boom: a fat
   cylinder with a ribbed collar, mounted low, its open mouth facing backward, away
   from the direction of travel. Angular vanes and a small forked bracket hang
   beneath and behind it. This is the machine's **only** engine pod.

   The pod is painted in a colour **taken from the livery swipe**: the deep
   **red-orange / rust** band, the fourth band down. It is not a separate bright
   red — it is the same rust the flank stripe uses, so the pod plainly belongs to
   the paint scheme. One narrow **cream** band from the swipe rings its collar.

There is **no antenna** anywhere on the machine. Earlier drafts carried a thin whip
antenna curving up from the tail structure; it has been removed and must not
reappear — no whip, no aerial, no mast, no wire, on the tail or anywhere else.

The check: the rider sits astride, high and exposed, looking out over a long bonnet
of hull, and the drum-shaped engine hangs out behind them on its boom like an
outboard motor at the stern of a boat. **The pod is the last thing in the direction
of travel, never the first.**

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

**The swipe pattern matters as much as the colours.** The bands run LEVEL and
narrow along the length of the body, then, toward the **rear**, all sweep UPWARD
together in one smooth continuous curve, finishing high on the tail. The kick is a
gentle S-curve, not a sharp angle and not a chevron. At the front the bands end in
a clean squared termination.

**The bands GROW WIDER through and after the kick.** They are at their thinnest
along the level run at the front and thicken steadily as they rise, so the whole
assembly is noticeably broader at the tail than at the nose — roughly half again
as deep. They stay parallel to one another and keep their relative proportions
while they widen; it is the whole group that swells, not one band.

`sources/livery-swipe-study-v3.png` is the authority on both the colour order and
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
It is NOT a 2:1 banner, NOT a panorama, NOT a square. There is NO landscape, NO
sky, NO ground, NO dust and NO scenery anywhere in this image — the machines sit on
empty grey. Exactly ONE human figure appears on the whole sheet, in the ridden
study described below; every other view is the machine alone. There is NO text, NO
labels, NO callouts, NO arrows, NO dimension lines, NO borders and NO frames.

THE SHEET shows the SAME single machine in FIVE views, evenly spaced and drawn at a
consistent scale, each fully separated from the others by empty grey:

- Upper left, largest: a THREE-QUARTER HERO VIEW from in front, above and to the
  machine's left, showing the prow, the near flank and the top deck at once. No
  rider.
- Upper right: a full SIDE ELEVATION, the machine level and square to the viewer,
  nose to the LEFT and tail engine pod to the RIGHT. No rider. This view is the
  authority on the machine's length, height and the order of its parts.
- Lower left: a TOP-DOWN plan view, nose to the left. No rider.
- Lower centre: a HEAD-ON FRONT view, looking straight at the prow. No rider.
- Lower right: a RIDDEN STUDY — the same machine in side view with ONE generic
  rider aboard, included to establish riding posture and scale.

THE RIDDEN STUDY, in detail. The rider STRADDLES the machine: astride a narrow
saddle on the spine of the hull toward the rear, one leg down each flank, boots on
small footrests set into the sides, leaning forward onto the grips on the cowl
ahead of the saddle. Their whole body from the thighs up is out in the open air
above the hull, exactly as a motorcyclist sits. They are NOT sitting down inside
anything: no tub, no cockpit well, no bucket seat, no sunken footwell, nothing
enclosing their legs.

The rider is a GENERIC FIGURE, present only for posture and scale: an ordinary
adult in plain drab utility clothing, goggles and a wrapped dust scarf, with no
distinctive costume. NO cape, NO cloak, NO armour, NO named-character features, NO
weapons, NO insignia. Do not give them anything memorable — they are a mannequin,
not a person. Exactly ONE rider appears anywhere on this sheet; the other four
views have no people in them at all.

Every view must agree with every other view on the order of the parts, the length,
the height and the placement of the livery.

Keep the machine simple and readable: large flat blocks of colour with hard angular
edges, details suggested rather than drawn in full. No glow, no reflections, no
lens effects, no cast environment.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
