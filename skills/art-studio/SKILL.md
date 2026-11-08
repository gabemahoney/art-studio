---
name: art-studio
description: Make, revise and approve illustrations in one locked visual style — characters, locations, items, vehicles, and scenes built from them — so a recurring cast stays consistent across a project. Works against a package (the style and its recurring subjects) and an output folder (where scenes land), both given as paths. Use for any illustration or image-generation request, even when the skill is not named: setting up a package or style anchor, designing or revising a character or asset sheet, composing a scene, fixing or touching up a generated image, deleting or promoting a candidate. Not for charts, diagrams, UI mockups or edits to images unrelated to illustration work.
---

# Art studio

An art department, not a one-off image generator. Every recurring subject — a person,
a place, a ship, an object — persists on disk as a written design plus one approved
picture. Scenes are built only from those approved pictures, so the cast stays
recognizable and the rendering never drifts.

Never call an image tool directly and never hand-write a prompt, because the
scripts in this skill's `scripts/` folder enforce what a hand-made call gets wrong.
Below, `S` is that folder's absolute path, and `T` is a scratch directory you make once
per session with `mktemp -d`, so intermediates never land in the package or the output
folder.

## Two locations, always given

The skill holds no project content. Every command is told where to work:

- **`--package PKG`** — one project's look and its recurring subjects. Ask the user for
  it, or find it from the project's own README or CLAUDE.md. Never guess one.
- **`--output OUT`** — where scene renders land. One package can feed many output
  folders (a sourcebook and an adventure can share one cast); the user says which.

Asset work writes into the package. **A scene render never writes into the package** —
`gen.py` refuses an output folder inside it.

```
PKG/
  style.md                 the look, in words — the "Style Block" pasted into every prompt
  presets.json             optional named delivery specs
  ref_images/style_references/canonical_style_reference.png    the anchor
  style_versions/          frozen style-vN.md + canonical_style_reference-vN.png
  assets/<type>/<slug>/    one folder per recurring subject
OUT/
  <scene>/vNNN/            image.png + generation.md (+ any delivered-WxH.png), one per attempt
  <scene>/final.png        the approved scene, + final.md
```

`<type>` is any category you invent — `personas`, `locations`, `items`, `ships`.
You create `assets/<type>/<slug>/` for a new asset; `gen.py` refuses an asset folder
that does not exist. `rules.md` (beside this file) is the generation
contract and is the same for every package.

### What each file is for

| file | what it is | written by |
|---|---|---|
| `style.md` | the look in words. `gen.py` parses the Style Block out of it and pastes it into every prompt | you, rarely |
| `ref_images/style_references/canonical_style_reference.png` | **the anchor** — the same look as one picture, attached to every single generation | you, rarely |
| `style_versions/style-vN.md` + `-vN.png` | frozen snapshots, so a receipt stamped `Style: v2` can be checked against what v2 said. `gen.py` refuses to run if `style.md` or the anchor has drifted from them | you, on a version bump |
| `presets.json` | named delivery specs: `{"name": {"final_size": "WxH", "flatten": "#rrggbb", "max_mb": 2.5}}` | you |
| **per asset** — `PKG/assets/<type>/<slug>/` | | |
| `description.md` | **the design, in words. The single source of truth.** Scenes restate it rather than inventing | you |
| `description_versions/description-vN.md` | frozen snapshot of the design at each version | you, on a bump |
| `prompt.md` | a note to your future self: which inputs and roles regenerate this asset's sheet | you |
| `candidates/vNNN/image.png` | raw model output, exactly as returned. Frozen forever | `gen.py` |
| `candidates/vNNN/generation.md` | **the receipt** — the full prompt, every input resolved to a frozen path, model, date. A replay must be reconstructable from this file alone | `gen.py` |
| `candidates/DELETED.md` | the deletion log: one `vNNN` per candidate removed at the user's insistence (see *Rules that are never optional*) | you |
| `reference.png` | **the approved picture.** The only image a scene may build from | `promote.py` |
| `reference.md` | the sidecar naming which candidate it came from, plus the user's approval verbatim. **Without it the asset counts as unapproved and `gen.py` refuses to attach it** | `promote.py` |
| `sources/` | user-supplied originals, crops and composite inputs | you |
| **per scene** — `OUT/<scene>/` | | |
| `vNNN/image.png` + `vNNN/generation.md` | exactly like an asset's candidates | `gen.py` |
| `DELETED.md` | the deletion log, as for an asset | you |
| `final.png` + `final.md` | the approved scene and its sidecar | `promote.py` |

Two kinds of file, and the distinction is the whole design: **heads** are mutable and
hold the current state (`description.md`, `reference.png`, `final.png`, `style.md`).
**Revisions** are written once and never touched again (everything under
`candidates/`, `OUT/<scene>/vNNN/`, `*_versions/`, `sources/`), except the deletion
log `DELETED.md`, which is appended to.

**Status is never recorded separately — the files are the status.**

- An asset is approved iff `reference.png` exists *and* passes its provenance check.
- A scene is done iff `final.png` exists.
- The latest attempt is the highest-numbered `vNNN`.
- The current design is `description.md`; its header line gives the version.

### Setting up a new package

Needs Python 3, ImageMagick (`magick`), and the `codex` CLI logged in to ChatGPT.

```bash
mkdir -p PKG/ref_images/style_references PKG/style_versions PKG/assets
cp $S/../templates/style.md PKG/style.md            # then write its Style Block
cp anchor.png PKG/ref_images/style_references/canonical_style_reference.png
cp anchor.png PKG/style_versions/canonical_style_reference-v1.png
cp PKG/style.md PKG/style_versions/style-v1.md      # after the Style Block is written
```

`codex exec` refuses to run outside a git repository, so the directory you run from
must be inside one (any repo works; it is read-only to Codex).

## Before you start

Confirm the package and, for a scene, the output folder. Read the package's `style.md`
(what the art looks like) and this skill's `rules.md` (how generations run). They
are the contract; this skill is the procedure. Then confirm which of three jobs you
are doing — they share one loop and differ only in what goes into steps 1 and 3.

## The loop

Every image, without exception, is made this way.

### 1. Write the text first

Nothing is invented at generation time. Before a prompt exists:

- **New asset** → write `description.md`. Header it `**Description version: v1**` and
  copy it to `description_versions/description-v1.md`.
- **Revising an asset** → merge the change into `description.md`, bump the version
  header, snapshot the new version. Write the design **absolutely**, as if from
  scratch: the user says "nose more bulbous", the file says "large rounded bulbous
  nose tip". A fresh generation has no "before", so a delta in the description is a
  sentence the model cannot use. Relative wording belongs only in the prompt, and
  only when an edit target is attached.
- **Scene** → read each cast member's `description.md` and write a scene spec to a
  scratch file: action, pose, expression, setting, light, framing, aspect ratio.

### 2. Assemble the prompt

```bash
python3 $S/prompt.py --package PKG \
  --role STYLE:"Match its hand-painted matte rendering only. Ignore its subjects." \
  --role IDENTITY:"Copy this asset's design exactly. Ignore its sheet layout." \
  --task "A single horizontal three-quarter view against a plain background." \
  --design-from assets/<type>/<slug>/description.md --design-section Exterior \
  --spec-file "$T/spec.txt" -o "$T/prompt.txt"
```

It emits the sections in the one mandated order — Style Block, image roles by number,
task, design, spec, closing style line — and refuses a role list whose image 1 is not
STYLE. One `--role` per attachment, **in attachment order**; drop the text after the
colon to get the standard wording. Omit `--design-from` for a scene and put the
per-asset identity summaries in the spec file instead (2–3 sentences each: face,
build, clothing, equipment with body sides).

### 3. Generate one candidate

```bash
python3 $S/gen.py --package PKG --output OUT --scene <scene> \
  --prompt-file "$T/prompt.txt" --preset <name> \
  --attach ref_images/style_references/canonical_style_reference.png:STYLE \
  --attach assets/<type>/<slug>/reference.png:IDENTITY \
  --request "<the user's words, verbatim>" --mode "<what this attempt changes>"
```

- `--asset <type>/<slug>` instead of `--scene <scene>` (and no `--output`) for an
  asset's own sheet; the candidate goes into the package's `candidates/`.
- Relative `--attach` paths resolve against the package, then the output folder. Use an
  absolute path for anything else (a user's source image, say).
- **`--attach` is `path:ROLE`; `--role` is `ROLE:text`.** The two are reversed. The
  order of the `--attach` flags must match the order of the `--role` flags, because
  position is the only binding the image model honors — "image 1" is a promise about
  order, not about a filename.
- `--dry-run` validates the invariants for free: the One Rule checks, reference
  provenance, the attachment cap, a dead model, the slug. It skips the `--approved-by`
  check a real `--backend api` call makes. Run it whenever anything is unusual.
- `vNNN` is allocated by `gen.py` after a successful response, so a failure leaves no
  empty folder. Never create a candidate folder or pick a number yourself, except for a
  kept local composite (`reference/fixing-an-image.md` → *Guardrails*).
- `--preset <name>` picks a delivery spec from the package's `presets.json`.

`gen.py` fails closed *before* anything is billed on the One Rule checks it can make
(`rules.md` → *Tooling*) or a failed provenance check. A refusal has cost nothing — read it and fix the call.

### 4. Look at the image, then record what you see

```bash
python3 $S/review.py OUT/<scene>/vNNN --review "<what you see, misses included>"
```

For an asset, pass its `candidates/vNNN` directory here and in step 6. Actually open it, and inspect contested details at 300–500% before calling anything
fixed (see *Two habits worth building* below; `reference/imagemagick.md` → *Inspection*
has the commands).

### 5. Show the user and give an honest read

Name where it missed the brief. They cannot see the image until you say what is in
it, and an unflagged miss becomes an approved mistake. If the pass overshot, say so
and offer to branch from an earlier candidate rather than stacking another
correction.

### 6. Promote — only on explicit approval

```bash
python3 $S/promote.py OUT/<scene>/vNNN --approval "<the user's words, verbatim>"
```

Copies `image.png` to `final.png` (scenes) or `reference.png` (assets), writes the
sidecar, re-verifies byte-identity, and stamps the candidate's receipt. It refuses to
overwrite an existing head without `--replace`; pass that only when the user approved
superseding the current one.

Never copy these files by hand. A `reference.png` without a verified `reference.md`
is one `gen.py` will reject on every future generation, from any agent, forever.
Then confirm `description.md` and `prompt.md` match what was actually approved.

**Approval is rare and revision is the normal case.** Expect to run steps 2–5 many
times per approval. That loop is where nearly all the time goes.

## The three jobs

What changes between them is only step 1's text and step 3's attachments.

| | step 1 writes | step 3 attaches |
|---|---|---|
| **New asset** | `description.md` v1 | anchor as STYLE, plus the *minimum* identity input: a `sources/` original, a crop, or nothing |
| **Revise an asset** | `description.md` bumped + snapshotted | anchor as STYLE, plus the baseline as EDIT TARGET |
| **Scene** | a scene spec file | anchor as STYLE, plus **at most one** cast `reference.png` or group lineup as IDENTITY, with the rest of the cast in text (`reference/writing-prompts.md`) |

**New asset, default sheet layout** (unless the user specifies one): people get
front, three-quarter, profile and back full-body views at one consistent scale, plus
four expression portraits — neutral pose, plain gray background, **no height chart**
(a shared group lineup carries height comparisons). Objects and vehicles get useful
orthographic angles and detail views with a scale cue. Places get an establishing
view, alternate angles, details. Mark invented details as provisional in
`description.md`; never invent an established fact.

**Revision: read `reference/when-it-looks-wrong.md` → *Choosing the baseline* first**,
because a wrong baseline is the most expensive mistake available here. It is
`reference.png` unless the user designated a candidate by approving it while asking
for a change.

**Scene: never invent design.** Restate it from `description.md` so the model has no
room to improvise. If an asset has no valid `reference.png`, stop and tell the user
which asset needs promoting first — do not improvise it and do not work around the
provenance check.

## Rules that are never optional

- **The One Rule.** Every call attaches the anchor FIRST as STYLE, carries the full
  Style Block verbatim at the top, ends with the closing style line, and delivers the
  prompt **byte-for-byte**, because style re-asserted on every call cannot drift.
  `rules.md` owns the detail and the one masked-call exception.
- **Every edit re-asserts the full style.** Keep the design, the single-image guard and
  the no-people guard in every edit prompt, because a thin "just change X" prompt lets
  the anchor's own subjects leak in — that once produced a two-panel comic page with
  strangers in it.
- **Never hand prompt text to Codex as instruction text**, because its `image_gen`
  rewrites prompts and silently defeats the Style Block; `gen.py` relays the prompt
  from disk instead (`rules.md` → *Why #4 exists*).
- **`image.png` is frozen history.** Never edit one in place or open one in an image
  editor, because a candidate annotated in Preview and saved over was lost for good.
  `reference.png` and `final.png` stay byte-identical to the candidate they came from.
- **Unapproved candidates are not IDENTITY inputs** unless the user designated one as
  a baseline, because chaining candidates compounds drift.
- **Never delete a candidate**, even a rejected one, even if asked casually, because
  deletion destroys receipts. If the user insists after being warned, log each removed
  attempt as `vNNN` with three or more digits (`v003`; `v3` is ignored) in
  `candidates/DELETED.md` for an asset or `OUT/<scene>/DELETED.md` for a scene, and
  list no other `vNNN` there, because `gen.py` numbers past every logged one.
- **At most FIVE attachments**, so budget anchor + baseline + identities to five;
  `gen.py` refuses a sixth before anything runs.
- **Never spend API credits without asking.** `--backend codex`, the default, bills
  the subscription; `--backend api` spends prepaid money and needs `--approved-by
  "<the user's words>"` for each call, which only the user can give (`rules.md` →
  *Paid calls need the user's approval*).
- **Do not commit automatically.**

## Notes

Read the matching reference file when you hit one of these, rather than browsing them
all.

- **Writing the `--task` line or spec file** → `reference/writing-prompts.md`: countable
  positive statements instead of bans, aspect ratio in the body, scale drift, and the
  one-identity-sheet limit for scenes.
- **The image came out wrong, before any revision** → `reference/when-it-looks-wrong.md`:
  picking the baseline from the user's words, the stale-baseline guard, diagnosing a
  style failure, and the ladder for right design with wrong rendering.
- **An existing image needs a correction, before spending a generation on it** →
  `reference/fixing-an-image.md`: routes the change to the cheapest tool and sets the
  bar for proposing credits.
- **ImageMagick commands** → `reference/imagemagick.md`: masks, tonal work, measurement,
  crops, deliverables, transplants, inspection.

### Two habits worth building

**Diagnose the artefact before naming it, at magnification.** The user's word
describes how a thing *reads*, not what it *is*. A garment reported as the wrong one
is often the right garment painted badly, and every instruction aimed at the reported
noun fails while the real shape goes untouched. Crop and zoom to find the actual
offending geometry before writing the instruction — and before recording a verdict.

**Fix the asset, not the scene.** If a design keeps drifting between scene passes,
stop iterating on the scene. The tell is that you are re-describing the same object's
geometry in consecutive prompts. That is the asset system asking to be used: a
four-view sheet fixes orientation in one pass, because a side elevation and a top
plan together force one consistent reading. `description.md` first, sheet second,
scene third.

### When the description and the approved image disagree

They will — someone's `description.md` says aubergine and their reference paints
magenta.

- **An asset's own `reference.png` wins for that asset.** The individual sheet
  outranks any group or derived image.
- A **derived** image that disagrees (a group lineup, a composite) is the one that is
  wrong; regenerate it against the individual references.
- **Amend `description.md` to match what was actually approved**, bumping and
  snapshotting. Never leave the text and the art contradicting each other — scenes
  read the text, so the next generation inherits the conflict.
- Surface it to the user rather than silently picking a side.
