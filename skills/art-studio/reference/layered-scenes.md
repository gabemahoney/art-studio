# Layered scenes

A Layered Scene is stacked from two or more Layers, each made, revised and approved on
its own, so one part can move, change or be locked in while every other part stays
exactly as it was. Each generation still runs `SKILL.md` → *The loop*; this file adds
what differs. `S`, `T`, `PKG` and `OUT` are as in `SKILL.md`, which also lists the
records a Layered Scene keeps (*What each file is for*).

## Terms

- **Layer**: one part of the scene, such as a background, a field of rocks or the ships
  in front. It is transparent wherever it holds nothing, so the Layers beneath show
  through. Its **Layer ID** is a slug that never changes.
- **Layer Plan**: single or layered. A layered plan states the **Frame**, the pixel size
  every Layer, Draft and Combined Image uses, and one **Layer Entry** per Layer, bottom
  to top. A Layer Entry says which parts of the scene the Layer holds, not how they look.
- **Layer Version**: one recorded image of a Layer. It **counts** when its Layer is in
  the current plan, it is the Frame's size, and its Layer Entry says the same as the
  current one; only counting versions are combined by default, kept or approved.
- **Draft**: a whole-scene generation used only to place Layers. It is never approved,
  edited or used for pixels.
- **Combined Image**: Layer Versions stacked by `layers.py combine`, which calls no
  image model.
- **Approved Layer Version**: the version the user approved for a Layer, on its own or
  inside an approved Combined Image.
- **Keep**: the user saying to use a version without approving it.
- **Default Version**: the kept version while its keep lasts, otherwise the Approved
  Layer Version if it counts, otherwise the latest counting version. Combined Images use
  it unless told otherwise, and revisions start from it.

## Planning

Propose the plan before anything is generated, and record it only with the user's
confirmation, because `gen.py` refuses a new scene that has none.

- **Single or layered.** Propose layered when parts of the scene may move, change or be
  approved separately; otherwise propose single, which costs one generation per attempt.
- **What makes a good Layer.** Each holds subjects at one depth that move together. Put
  subjects that may move independently and may overlap in separate Layers, because
  moving one then reveals finished pixels beneath it. Keep a subject that may move
  inside the Frame, or say that moving one the Frame's edge cuts off reveals pixels
  that don't exist.
- **The Frame.** Propose the size of the scene's preset, and say that a Frame of another
  aspect ratio pads every deliverable.
- **Light across Layers.** Combining repaints nothing, so light one Layer casts on
  another, such as a glow on a rock, appears only where some Layer paints it. Plan
  which Layer paints it.

Show the dry run as the proposal, then record the confirmation with the `--based-on`
number it printed:

```bash
python3 $S/layers.py plan --package PKG --output OUT --scene <scene> \
  --frame 1536x1024 --layer "<bottom-id>=<what it holds>" \
  --layer "<top-id>=<what it holds>" --dry-run
python3 $S/layers.py plan --package PKG --output OUT --scene <scene> \
  --frame 1536x1024 --layer "<bottom-id>=<what it holds>" \
  --layer "<top-id>=<what it holds>" \
  --confirmation "<the user's words, verbatim>" --based-on 0
```

A single plan is `--single` instead of `--frame` and `--layer`. Until something is
generated, any change is a new proposal. After that, `plan` refuses a switch between
single and layered or a new Frame, so offer a new scene.

## Making Layers

Make the bottom Layer first, so each later one can be placed against what lies beneath
it. A Draft (`gen.py --draft`) gives the first Layers one composition to place against;
show every Draft with an honest read.

Each later Layer attaches, as PLACEMENT, a Combined Image of the Layers beneath it
(`combine --only` leaves out the Layers above), or the Draft. `rules.md` → *Image input
roles* has every attachment rule. Budget the five slots: the anchor, one or two
PLACEMENT images, the cast crops a Layer's subjects need, and an EDIT TARGET when
editing. A Combined Image carries any number of Layers in one slot.

Write each Layer's prompt as `reference/writing-prompts.md` → *Prompt a Layer so it
separates* says, then generate it at the Frame:

```bash
python3 $S/gen.py --package PKG --output OUT --scene <scene> --layer <layer-id> \
  --prompt-file "$T/prompt.txt" \
  --attach ref_images/style_references/canonical_style_reference.png:STYLE \
  --attach <scene>/vNNN/image.png:PLACEMENT \
  --request "<the user's words, verbatim>" --mode "<what this attempt changes>"
```

Pass no `--preset`, because only Combined Images get deliverables.

`gen.py` checks a Layer's transparency and prints each failure: no alpha, opaque
everywhere, a backdrop left in, a fringe, or glow baked onto dark. Regenerate a Layer
whose final check still fails, because the fault shows in every Combined Image. A
full-frame pale haze can trip the backdrop check, so judge that one in the view. Tell
the user when `gen.py` reports a Layer Version or Draft at the wrong aspect ratio; such
a Layer Version never counts, so show it on its own.

Review every Layer Version, Draft and Combined Image as `SKILL.md` step 4 says, using
`reference/imagemagick.md` → *Viewing transparency*, because a fringe or a partly
transparent area is invisible on a plain viewer.

## Showing each step

After every step that makes or revises Layers, build and show one Combined Image: each
current Layer at its Default Version, except the Layers the step changed, which are at
their new versions. No script checks this, so do it every time.

```bash
python3 $S/layers.py combine --package PKG --output OUT --scene <scene> \
  --use <layer-id>=vNNN --request "<the user's words>" --mode "<the step>"
```

Pass `--use` only for a new version that isn't already its Layer's Default Version.
One step is one Combined Image, so a path-3 fix shows once, after `record`. `combine`
prints each Layer's version and whether it is the Approved Layer Version; name both when
you show it, and pass on every warning it prints. The honest read names misses in every
Layer, including content hidden behind Layers above, and says whether the Layers read
as one picture: scale, perspective, light direction and style. Offer any Layer on its
own. A version the user only asks to see goes in one Combined Image with `--use`, and
the next one returns to the Default Version. A removed Layer goes in with `--insert <layer-id>=vNNN@<position>`, counting
from 1 at the bottom; tell the user where it sits, and ask when that is unclear.

## Keeping and approving

Record a keep or an approval when the user gives it, because nothing else records what
they said. Keep when they say to use a version, or designate it as
`reference/when-it-looks-wrong.md` → *Choosing the baseline* describes:

```bash
python3 $S/layers.py keep --package PKG --output OUT --scene <scene> \
  --layer <layer-id> --version vNNN --words "<the user's words, verbatim>" --dry-run
```

Then run it again with `--based-on N` in place of `--dry-run`. A keep lasts until the
user keeps another version of that Layer or approves one, its Layer Entry changes, or it
is removed. A newer version doesn't end it.

**Ask the keep question.** Before a step that makes or revises Layers, or a plan
change, ask whether to keep a Layer's newest counting version when the step leaves that
Layer alone, the user has seen that version since the Layer's latest approval without
saying whether to keep it, and it isn't the Default Version. `status` flags each Layer
whose newest counting version isn't its Default Version. A later session asks again,
because what the user was shown isn't recorded.

**Ask when a word is ambiguous**, such as "great" while asking for another change:
approve, keep, or neither? Also ask whether an approval covers the whole Combined Image
or one Layer in it.

**Approve** with `promote.py` on the folder, first with `--dry-run`, then with
`--approval "<the user's words, verbatim>"` and `--based-on N`:

```bash
python3 $S/promote.py OUT/<scene>/layers/<layer-id>/vNNN --dry-run
```

- **A Layer Version** (`OUT/<scene>/layers/<layer-id>/vNNN`) becomes its Layer's
  Approved Layer Version. It leaves `final.png` and `final-layers/` alone; when
  `promote.py` notes that the approved image holds another version, tell the user.
- **A Combined Image** (`OUT/<scene>/vNNN`) becomes the scene's approved image, and each
  Layer Version it holds becomes its Layer's Approved Layer Version. Only one holding
  exactly the current Layers, in order, each counting, can be approved; `status` lists
  which can.

When the dry run names approvals this would replace, counting or not, name each to the
user, and pass `--replace` only after they approve superseding them. A Draft is never
approved.

**`--based-on`** is the journal number from the dry run the user saw. When a command
refuses because the journal has moved, show the new state and ask again, because their
answer was about the old one.

## Revising one Layer

Revise only the Layers the user asked to change, starting from each one's Default
Version. Edit from it, or regenerate fresh after a rejection, attaching a Combined
Image without that Layer for placement (`combine --only`). Retry a failed generation
from the step's starting version, not from the failed one, though that is now the
Layer's latest; `gen.py` then warns that the starting version isn't the Default
Version, which is expected here and a mistake anywhere else. Ask when the starting
version is unclear.

Route each fix by `reference/fixing-an-image.md` → *On a Layer*.

**Whole-picture corrections** revise each affected Layer. A linear colour operation
applied to every Layer, such as `-evaluate multiply` on the colour channels, matches
grading the flat picture. A non-linear one, such as `-gamma` or `+level`, differs on
partly transparent content, so measure again on the new Combined Image. Measure tonal
ratios on the Combined Image flattened as a deliverable shows it. Areas no Layer covers
take no grade. Record each graded Layer, then show one Combined Image holding them all.

## Changing the plan

Adding, removing or reordering Layers, changing what a Layer holds, and moving a subject
between Layers are plan changes. Run `plan --dry-run` with the whole new plan, bottom
to top, and show its output as the proposal. It names each approval that would stop or
start counting and each keep that would end. A new Layer takes a new ID, because
`plan` reads a removed Layer's ID as putting that Layer back. To undo a removal or a
changed Layer Entry, list the Layer with `--layer <layer-id>=@N`, which copies its
Layer Entry verbatim from plan record `N` and so restores its earlier versions and
approval, though not its keep.

A two-Layer plan can't drop a Layer, so add the replacement in the same change. Once
recorded, a removal, a reorder or a change whose Layers all have counting versions
builds its Combined Image at once; show it. Otherwise, show the step's Combined Image
once each changed Layer has a version.

## Delivering

Deliverables come from Combined Images only: `combine --preset <name>`, or `gen.py
--refinish` on a Combined Image folder. Areas no Layer covers show the flatten colour.
The `final-layers/` files line up with `final.png`, not with a resized deliverable.

## A later session

Run `layers.py status` before anything else, because it reports the scene's whole state
from the output folder alone. Then ask the keep question for each flagged Layer.
`layers.py rebuild --combined vNNN` checks that a Combined Image still rebuilds from its
receipt.
