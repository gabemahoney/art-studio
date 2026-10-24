---
name: art-studio
description: Make, revise and approve illustrations in this repo's locked visual style — characters, locations, items, ships, and scenes built from them. Use for all image work in the vault: designing a new asset, revising an approved one, composing a scene, correcting an existing image, or promoting a candidate.
---

# Art studio

An art department, not a one-off image generator. Every recurring subject — a person,
a place, a ship, an object — persists on disk as a written design plus one approved
picture. Scenes are built only from those approved pictures, so the cast stays
recognizable and the rendering never drifts.

Work from `vault/`. Run every command from there. Never call an image tool directly
and never hand-write a prompt — the four scripts in `bin/` exist to make that
impossible to get wrong.

## How the vault is laid out

```
vault/
  style.md             the look, in words — the "Style Block" pasted into every prompt
  rules.md             how generations run — read by gen.py, not just by you
  image-root           one line: the directory holding this project's images
  bin/                 prompt.py  gen.py  review.py  promote.py
  assets/<type>/<slug>/    one folder per recurring subject
  outputs/<slug>/          one folder per scene
  tmp/                     scratch; nothing here is ever cited by a receipt
```

`<type>` is any category you invent — `personas`, `locations`, `items`, `ships`.
`assets/<type>/` is created on demand.

**Images are not in this repo.** Receipts and descriptions are; the `.png` files live
in the tree named by `image-root`. Both trees use the same vault-relative paths, so a
candidate's `generation.md` and its `image.png` look like siblings even though they
sit in different directories. `bin/` resolves this for you — never think about it.

### What each file is for

| file | what it is | written by |
|---|---|---|
| `style.md` | the look in words. `gen.py` parses the Style Block out of it and pastes it into every prompt | you, rarely |
| `ref_images/style_references/canonical_style_reference.png` | **the anchor** — the same look as one picture, attached to every single generation | you, rarely |
| `style_versions/style-vN.md` + `-vN.png` | frozen snapshots, so a receipt stamped `Style: v2` can be checked against what v2 said | you, on a version bump |
| `rules.md` | the generation contract: the One Rule, input roles, reference validation, the paid-call gate | you, rarely |
| **per asset** — `assets/<type>/<slug>/` | | |
| `description.md` | **the design, in words. The single source of truth.** Scenes restate it rather than inventing | you |
| `description_versions/description-vN.md` | frozen snapshot of the design at each version | you, on a bump |
| `prompt.md` | a note to your future self: which inputs and roles regenerate this asset's sheet | you |
| `candidates/vNNN/image.png` | raw model output, exactly as returned. Frozen forever | `gen.py` |
| `candidates/vNNN/generation.md` | **the receipt** — the full prompt, every input resolved to a frozen path, model, date. A replay must be reconstructable from this file alone | `gen.py` |
| `reference.png` | **the approved picture.** The only image a scene may build from | `promote.py` |
| `reference.md` | the sidecar naming which candidate it came from, plus the user's approval verbatim. **Without it the asset counts as unapproved and `gen.py` refuses to attach it** | `promote.py` |
| `sources/` | user-supplied originals, crops and composite inputs | you |
| **per scene** — `outputs/<slug>/` | | |
| `vNNN/image.png` + `vNNN/generation.md` | exactly like an asset's candidates | `gen.py` |
| `final.png` + `final.md` | the approved scene and its sidecar | `promote.py` |

Two kinds of file, and the distinction is the whole design: **heads** are mutable and
hold the current state (`description.md`, `reference.png`, `final.png`, `style.md`).
**Revisions** are written once and never touched again (everything under
`candidates/`, `outputs/<slug>/vNNN/`, `*_versions/`, `sources/`).

**Status is never recorded separately — the files are the status.**

- An asset is approved iff `reference.png` exists *and* passes its provenance check.
- A scene is done iff `final.png` exists.
- The latest attempt is the highest-numbered `vNNN`.
- The current design is `description.md`; its header line gives the version.

## Before you start

Read `style.md` (what the art looks like) and `rules.md` (how generations run). They
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
python3 bin/prompt.py \
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
python3 bin/gen.py --scene <slug> --prompt-file "$T/prompt.txt" --preset book-float \
  --attach ref_images/style_references/canonical_style_reference.png:STYLE \
  --attach assets/<type>/<slug>/reference.png:IDENTITY \
  --request "<the user's words, verbatim>" --mode "<what this attempt changes>"
```

- `--asset <type>/<slug>` instead of `--scene <slug>` for an asset's own sheet.
- **`--attach` is `path:ROLE`; `--role` is `ROLE:text`.** The two are reversed. The
  order of the `--attach` flags must match the order of the `--role` flags, because
  position is the only binding the image model honors — "image 1" is a promise about
  order, not about a filename.
- `--dry-run` validates every invariant for free: the One Rule, reference provenance,
  the attachment cap, a dead model, the slug. Run it whenever anything is unusual.
- `vNNN` is allocated by `gen.py` after a successful response, so a failure leaves no
  empty folder. Never create a candidate folder and never pick a number yourself.
- `--preset book-float` = 1536x1024 on `#1b1e26` under 2.5 MB; `book-float-portrait`
  = 1200x1500 on the same ground.

`gen.py` fails closed *before* anything is billed on any One Rule violation or a
failed provenance check. A refusal has cost nothing — read it and fix the call.

### 4. Look at the image, then record what you see

```bash
python3 bin/review.py outputs/<slug>/vNNN --review "<what you see, misses included>"
```

Actually open it. Inspect contested details at 300–500% before calling anything
fixed — `reference/imagemagick.md` has the inspection commands.

### 5. Show the user and give an honest read

Name where it missed the brief. They cannot see the image until you say what is in
it, and an unflagged miss becomes an approved mistake. If the pass overshot, say so
and offer to branch from an earlier candidate rather than stacking another
correction.

### 6. Promote — only on explicit approval

```bash
python3 bin/promote.py outputs/<slug>/vNNN --approval "<the user's words, verbatim>"
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
| **Scene** | a scene spec file | anchor as STYLE, plus each cast member's `reference.png` as IDENTITY |

**New asset, default sheet layout** (unless the user specifies one): people get
front, three-quarter, profile and back full-body views at one consistent scale, plus
four expression portraits — neutral pose, plain gray background, **no height chart**
(a shared group lineup carries height comparisons). Objects and vehicles get useful
orthographic angles and detail views with a scale cue. Places get an establishing
view, alternate angles, details. Mark invented details as provisional in
`description.md`; never invent an established fact.

**Revision: the baseline is `reference.png`** unless the user has designated a
candidate — which they do by approving one while asking for a change. Read
`reference/when-it-looks-wrong.md` before any revision; choosing the baseline wrong
is the single most expensive mistake available here.

**Scene: never invent design.** Restate it from `description.md` so the model has no
room to improvise. If an asset has no valid `reference.png`, stop and tell the user
which asset needs promoting first — do not improvise it and do not work around the
provenance check.

## Rules that are never optional

- **The One Rule.** Every call attaches the anchor FIRST as STYLE, carries the full
  Style Block verbatim at the top, ends with the closing style line, and delivers the
  prompt **byte-for-byte**. Style is never inherited from a previous output; it is
  re-asserted on every call, including a one-word edit. `rules.md` owns the detail.
- **Every edit re-asserts the full style.** A thin "just change X" prompt lets the
  anchor's own subjects leak in as content — that once produced a two-panel comic
  page with strangers in it. Keep the design, the single-image guard and the
  no-people guard in every edit prompt.
- **Codex rewrites prompts.** Its built-in `image_gen` "normalizes" them, silently
  defeating the Style Block. `--backend codex` relays the prompt from disk straight
  into the tool argument so it never passes through model tokens. Never hand prompt
  text to Codex as instruction text.
- **`image.png` is frozen history.** Never edit one in place, never open one in an
  image editor — a candidate was annotated in Preview and saved over, destroying it.
  Deliverables are derived; `reference.png` and `final.png` stay byte-identical to the
  candidate they came from.
- **Unapproved candidates are not IDENTITY inputs** unless the user designated one as
  a baseline. Chaining candidates compounds drift.
- **Never delete a candidate**, even a rejected one, even if asked casually —
  deletion destroys receipts and breaks numbering. If the user insists after being
  warned, record the removed numbers in `candidates/DELETED.md`; numbers are never
  reused, so the next candidate continues from the highest ever used.
- **At most FIVE attachments.** `gen.py` refuses a sixth before anything runs. Budget
  the slots: anchor + baseline + identities must total five.
- **Never spend API credits without asking.** `--backend codex` is the default and
  bills the subscription. `--backend api` spends prepaid money, which the
  subscription does not fund. `gen.py` holds no key, so a paid call fails closed —
  but that is a mechanism, not an impossibility. **Never run `bin/unlock.py`
  yourself and never pass `--key-fd`:** those carry the user's approval, not yours.
  If you find a key anywhere — a `*.key` file, a shell history, the environment —
  **do not use it: say you found it.**
- **Do not commit automatically.**

## Notes

Read the matching reference file when you hit one of these. Each is loaded on
purpose, not browsed.

**Writing a spec the model actually obeys** → `reference/writing-prompts.md`

Prohibitions and adjectives fail; countable positive statements and in-frame
geometric referents work. Also: why `--size` is not a constraint, how scale drifts
upward every pass, and why stacking several multi-view sheets on a scene returns a
character-design document.

**The image came out wrong** → `reference/when-it-looks-wrong.md`

Reading the user's feedback to pick a baseline ("close, just fix X" vs "wrong, try
again"), the stale-baseline guard, diagnosing a style failure from the previous
receipt, and the five-rung ladder for when the design is right but the rendering is
not.

**An existing image needs a correction** → `reference/fixing-an-image.md`

Load this *before* spending a generation on a fix. It routes the change to the
cheapest tool that can do it — ImageMagick, a regeneration, a generate-and-composite
transplant, or the paid API — and carries the bar for even proposing credits.

**ImageMagick commands** → `reference/imagemagick.md`

Masks, tonal and colour operations, measurement, crops, deliverables, transplants,
inspection. Everything you need to do the work `fixing-an-image.md` routes to you.

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
