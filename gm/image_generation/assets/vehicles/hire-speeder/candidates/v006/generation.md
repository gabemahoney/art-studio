# hire-speeder v006

User request verbatim: The stirrups can be just one flat plane.
Mode: Edit off candidate v005 against description v8. Three changes: (1) each stirrup simplified to ONE FLAT PLANE — a single angular plate projecting from the flank, no loop, cage, cradle, bracket assembly or guard plate; (2) the pair nudged forward to sit below and just AHEAD of the saddle rather than below its rear, keeping the forward rake; (3) the ventral skid pod restored — v005 dropped it collaterally when the forward stirrups were removed, and description.md still specifies it. Everything else frozen: five views, rider distribution, straddle posture, saddle proud on the spine, single aft pair only with clean forward flanks, sunset swipe and its widening, rust engine pod with cream collar, no antenna, tidy tail plumbing, grey ground.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-5.6-terra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f09b-c817-7063-a65f-b971deca54df/exec-ed6d3a32-f976-4a0e-9833-db651780df2f.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 IDENTITY: assets/vehicles/hire-speeder/sources/user-geometry-reference-2026-09-29.png
- Image 3 EDIT TARGET: assets/vehicles/hire-speeder/candidates/v005/image.png
- Image 4 IDENTITY: assets/vehicles/hire-speeder/sources/livery-swipe-study-v3.png
Date: 2026-09-29
Status: approved and promoted to reference.png on 2026-09-29. User approval: "Lets just go with 006."
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.74 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: APPROVED AND PROMOTED to reference.png on the user's instruction "Lets just go with 006." Superseding note on the stirrups: an earlier version of this review claimed the flat-plane stirrups were achieved; that claim was wrong and was withdrawn after the user challenged it and the stirrups were re-examined at 400 percent. This candidate's stirrups are BENT BRACKETS — a short arm leaving the flank and turning once at an elbow into a flat foot plate. Candidate v007 was then generated with the single unbroken slab the description had asked for, and the user chose this one over it. That is a deliberate design decision, not an oversight: description.md has been amended to v10 so the written canon describes the bracket this sheet actually shows, and the art and the description agree again. Everything else on this sheet: five views with riders in the three-quarter hero, head-on and ridden study and none in the side elevation or top plan; straddle unambiguous in the head-on with legs either side and both boots on the stirrups; narrow saddle proud on the hull spine in the top plan; exactly one stirrup pair, both aft, with clean forward flanks and prow; ventral skid pod beneath the mid-hull in plain weathered grey; the 1970s sunset swipe running level then sweeping up and widening toward the tail; engine pod in the swipe's rust band with a cream collar; no antenna anywhere; two or three tidy parallel tubes along the boom; prow leading with the engine pod trailing; long low proportions; honest chipped wear; no wheels; plain grey ground; no text or labels.

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
Image 2 is IDENTITY: The GEOMETRY reference for this machine's overall shapes and the order of its parts. Ignore its rendering, and note the deliberate departures: NO antenna, sparse tidy tail plumbing, a STRADDLED saddle, and exactly one aft pair of flat-plate stirrups with clean forward flanks.
Image 3 is EDIT TARGET: The scene baseline: hire-speeder candidate v005. Its five views, single aft stirrup pair, clean forward flanks, straddle posture, saddle, livery, engine pod and grey ground are correct. Change only the stirrups' form and position, and restore the ventral skid pod it lost.
Image 4 is IDENTITY: The LIVERY SWIPE study. Copy the band COLOURS in order (narrow cream, golden yellow, orange, red-orange, dark brown), the SWIPE PATTERN, and the WIDENING toward the tail. The engine pod keeps the fourth band's deep red-orange rust with a cream collar. A flat graphic specification, not a vehicle and not a scene.

TASK: A five-view reference sheet for the Kalagra hire speeder on plain flat mid-grey, with one aft pair of simple flat-plate stirrups raked forward, and a ventral skid pod beneath the hull.

SUBJECT DESIGN (description v8, restated so nothing is invented):
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

   Each stirrup is **ONE FLAT PLANE** — a single flat plate projecting straight out
   from the flank for the boot to stand on, and nothing more. It is a simple
   angular tab, a slab of metal, read as one shape. There is **no loop, no ring,
   no stirrup cage, no three-sided cradle, no bracket arm assembly and no guard
   plate**; nothing wraps around the boot and nothing hangs below it. Keep it as
   plain as a shelf.

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
