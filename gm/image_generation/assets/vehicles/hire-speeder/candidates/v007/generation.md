# hire-speeder v007

User request verbatim: ah no they arent
Mode: Edit off candidate v006 against description v9. Single change: the stirrups. v006 removed v005's loops and cradles but still built each stirrup as a BENT L-BRACKET — an arm off the flank kinking down at an elbow into a separate foot plate, i.e. two planes meeting at an angle. My v006 review wrongly recorded this as achieved and has been corrected. Description v9 now specifies a single UNBROKEN SLAB with no bend, kink, step, elbow or hook anywhere — a flat plate bolted to the flank and projecting like a shelf, its whole surface in one plane, with the boot simply resting on top. Everything else explicitly frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f09e-9df4-76b3-811b-c39838fa1fc8/exec-57d6e539-3664-4ee4-896a-750fe98b1cc7.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/vehicles/hire-speeder/sources/user-geometry-reference-2026-09-29.png
- Image 3 EDIT TARGET: assets/vehicles/hire-speeder/candidates/v006/image.png
- Image 4 IDENTITY: assets/vehicles/hire-speeder/sources/livery-swipe-study-v3.png
Date: 2026-09-29
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.78 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Stirrups are correct now, verified at 400 percent on both the side elevation and the head-on rather than at full-sheet size, which is how the v006 error slipped through. Each stirrup is a single unbroken slab: a flat plate meeting the flank and projecting outward like a shelf, its whole surface in one plane, no bend, kink, step, elbow or hook anywhere in the silhouette. The head-on shows the pair as two flat plates projecting left and right with the rider's boots simply resting on top of them. The forward rake survived the simplification and the pair still sits below and just ahead of the saddle. Everything else held with no regressions: five views with riders in the three-quarter hero, head-on and ridden study and none in the side elevation or top plan; straddle unambiguous; narrow saddle proud on the spine in the top plan; exactly one stirrup pair with clean forward flanks and prow; ventral skid pod present beneath the mid-hull in plain weathered grey; sunset swipe running level then sweeping up and widening toward the tail; engine pod in the swipe's rust with a cream collar; no antenna; two or three tidy parallel tubes along the boom; long low proportions; honest chipped wear; no wheels; plain grey ground; no text or labels. No discrepancies found against description v9. PROCESS NOTE: this sheet took seven candidates, and the two failures that cost the most were both mine rather than the model's — description v1 put the rider at the rear of the body when the geometry reference put them at the front, and description v8 forbade loops and cradles without forbidding a bend, which let v006 build an L-bracket that technically satisfied every prohibition. Both were holes in the written description, not misreadings of it. Ready to promote to reference.png on the user's explicit approval; promote.py must not run without it.

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
Image 2 is IDENTITY: The GEOMETRY reference for this machine's overall shapes and the order of its parts. Ignore its rendering, and note the deliberate departures: NO antenna, sparse tidy tail plumbing, a STRADDLED saddle, and one aft pair of single-slab stirrups with clean forward flanks.
Image 3 is EDIT TARGET: The scene baseline: hire-speeder candidate v006. Everything in it is correct — five views, rider distribution, straddle posture, saddle, single aft stirrup pair, skid pod, livery, engine pod, grey ground — EXCEPT the shape of the stirrups themselves, which are bent brackets and must become single flat slabs.
Image 4 is IDENTITY: The LIVERY SWIPE study. Copy the band COLOURS in order (narrow cream, golden yellow, orange, red-orange, dark brown), the SWIPE PATTERN, and the WIDENING toward the tail. The engine pod keeps the fourth band's deep red-orange rust with a cream collar. A flat graphic specification, not a vehicle and not a scene.

TASK: A five-view reference sheet for the Kalagra hire speeder on plain flat mid-grey, its stirrups each a single unbent flat slab projecting from the flank.

SUBJECT DESIGN (description v9, restated so nothing is invented):
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
3. **Saddle and stirrups.** The rider **straddles** the machine toward the **rear**
   of the body, sitting *on* it rather than in it.

   The **saddle** is a narrow padded pad sitting **proud on the spine** of the
   hull, raised clearly above the deck around it, with the deck stepping visibly
   **down and away on both sides** of it. It is about as wide as a motorcycle
   seat — much narrower than the hull. It is **not** a bench, **not** a bucket,
   **not** sunk into a well, and there is **no cockpit tub, no cabin and no
   footwell** anywhere on this machine. Seen from above, the saddle is a small
   narrow shape on the centreline with open deck either side of it; seen head-on,
   it is a raised ridge with the hull falling away left and right.

   The **stirrups** are a defining feature and appear in **every view**. There are
   **exactly TWO stirrups on the whole machine — ONE PAIR, one per flank** — and
   they sit in the **rear half** of the hull, below and just ahead of the saddle,
   within easy reach of a rider sitting on it.

   Each stirrup is **ONE FLAT PLANE — a single unbroken slab, with no bend in it
   anywhere.** Picture a flat rectangular plate bolted straight onto the side of
   the hull and sticking out sideways like a shelf or a diving board. Its whole
   surface lies in ONE plane from where it meets the hull to its outer edge.

   **It does not bend, kink, step, elbow or turn a corner.** There is no arm that
   drops down and then turns outward; there is no separate foot pad on the end of
   a bracket; there is no L-shape, no Z-shape and no hook. If the silhouette shows
   two surfaces meeting at an angle, it is wrong — it must read as a single
   straight slab. There is also no loop, ring, cage or cradle, and nothing wraps
   around or hangs below the boot.

   In side view it is a single straight line of metal angled off the hull. The
   boot simply rests on top of it.

   **There is no second pair.** Nothing of this kind appears on the front half of
   the machine: no stirrups, footrests, pegs, steps, loops or cradle brackets
   anywhere near the prow, the nose or the forward flanks. Two stirrups in total,
   both aft, both beside the saddle. The forward flanks and the prow are clean.

   **The stirrup plates rake FORWARD, and this is what makes the machine look
   fast.** Each plate is angled nose-down and set forward, so the boot sits
   toed-forward rather than flat, and the plate reads in side view as a shallow
   diagonal running forward and down from the hull. Position them below and just
   **ahead of** the saddle — forward-set controls, like a chopper's pegs — so the
   rider is stretched forward into the machine with their weight over the front,
   not sitting bolt upright above their own feet. Do not let them drift back
   behind the saddle.

   Where they must be visible: in **side view**, the single near-side plate
   projecting from the flank just ahead of the saddle; in **top plan**, one small
   flat tab sticking out past the hull's outline on each side, both in the rear
   half and nothing similar further forward; in **head-on view**, the pair seen
   edge-on as two short flat plates projecting left and right. Both stirrups are
   symmetrical and identical.

   Ahead of the saddle the deck rises into a low cowl with a small curved
   windscreen, and the rider leans forward onto a short handlebar yoke mounted on
   that cowl. The rider's whole body from the thighs up is out in the open air
   above the hull, the way a motorcyclist rides. The long deck stretches away in
   front of them; there is comparatively little hull behind them.
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
  machine's left, showing the prow, the near flank and the top deck at once. WITH
  a rider aboard.
- Upper right: a full SIDE ELEVATION, the machine level and square to the viewer,
  nose to the LEFT and tail engine pod to the RIGHT. NO rider — this view is the
  authority on the machine's length, its silhouette, the order of its parts and
  how the swipe runs and widens, and a rider would hide all of it.
- Lower left: a TOP-DOWN plan view, nose to the left. NO rider — this view is the
  authority on the deck, the spine and the narrow saddle, and a rider would hide
  them.
- Lower centre: a HEAD-ON FRONT view, looking straight at the prow. WITH a rider
  aboard, legs clearly straddling the hull one to each side.
- Lower right: a RIDDEN STUDY — the same machine in side view with a rider aboard,
  establishing riding posture and scale.

THREE of the five views carry a rider (hero, head-on, ridden study) and TWO do not
(side elevation, top plan). Every view, ridden or not, must show the stirrup
footrests.

THE RIDING POSTURE, in detail, for every ridden view. The rider STRADDLES the
machine: astride a narrow saddle sitting proud on the spine of the hull toward the
rear, one leg down each flank, each boot resting in an open stirrup footrest that
projects from that flank, leaning forward onto the grips on the cowl ahead of the
saddle. Their whole body from the thighs up is out in the open air
above the hull, exactly as a motorcyclist sits. They are NOT sitting down inside
anything: no tub, no cockpit well, no bucket seat, no sunken footwell, nothing
enclosing their legs.

Every rider on this sheet is the SAME GENERIC FIGURE, present only for posture and
scale: an ordinary adult in plain drab utility clothing, goggles and a wrapped dust
scarf, with no distinctive costume. NO cape, NO cloak, NO armour, NO
named-character features, NO weapons, NO insignia. Do not give them anything
memorable — they are a mannequin, not a person. They sit identically in all three
ridden views, and both feet are in the stirrups.

Every view must agree with every other view on the order of the parts, the length,
the height and the placement of the livery.

Keep the machine simple and readable: large flat blocks of colour with hard angular
edges, details suggested rather than drawn in full. No glow, no reflections, no
lens effects, no cast environment.

RESTORE THE VENTRAL SKID POD. Candidate v005 lost it. Slung beneath the mid-hull,
running fore-and-aft along the underside, is a single flat grey SKID POD — a long
low pod or rail, plainly visible in the side elevation below the flank and in the
head-on view beneath the hull. It is painted plain weathered grey, carries none of
the livery, and is separate from the stirrups. One skid pod per machine, on the
centreline underside.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
