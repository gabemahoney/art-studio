---
name: art-studio
description: Create Rogue Frontier art with persistent characters, ships and locations in one locked visual style. Use for any image work in this repo — designing a new character/ship/object, revising an approved one, composing a scene from approved references, or promoting a candidate. Covers the style anchor, the One Rule, reference provenance, the bin/ tooling, and the Codex/API backends.
---

# Art studio

An art department, not a one-shot image generator. Characters, ships, locations and
the style itself persist across sessions as files on disk, and every image is built
from those files so the cast stays recognizable and the rendering never drifts.

Everything lives in `gm/image_generation/`. Run all commands from there — but **images
live outside the repo**, in a tree configured per project (`rules.md` → *Where images
live*). Both trees share the same vault-relative paths: a candidate's `generation.md` is in
the repo, its `image.png` is not. `bin/` resolves the two roots for you.

## The model

```
style.md  ──────────────┐   Style Block text + canonical_style_reference.png anchor,
                        │   attached to EVERY generation call
assets/<type>/<slug>/ ──┼─► candidates/vNNN/ ─(user approves)─► reference.png
                        │
outputs/<scene-slug>/  ◄┘   scenes built from approved reference.png files
```

Mutable heads (`style.md`, the anchor, each asset's `description.md` /
`prompt.md` / `reference.png`, each scene's `final.png`) carry the current state;
everything under `style_versions/`, `description_versions/`, `candidates/`,
`sources/` and scene `vNNN/` is written once and never touched. Status is never
recorded separately — the files *are* the status. An asset is
approved iff `reference.png` exists **and passes its provenance check** — sidecar,
named candidate, byte-identical md5; `rules.md` → *Reference validation* has all three,
and `gen.py` hard-stops on any of them. The latest attempt is the highest `vNNN`.

## Read first

`rules.md` (how generations run) and `style.md` (what the art looks like). They are
the contract; this skill is the map.

## Never generate by hand

Do not call an image tool directly and do not hand-assemble prompts. Four scripts,
stdlib only, no venv:

```bash
# 1. assemble the prompt — Style Block, image roles by number, design, scene spec,
#    closing line, in the mandated order
python3 bin/prompt.py \
  --role STYLE:"Match its hand-painted matte rendering only. Ignore its subjects." \
  --role IDENTITY:"Copy this ship's design exactly. Ignore its sheet layout." \
  --task "A single horizontal beauty shot above a barren planet." \
  --design-from assets/ships/the_antares/description.md --design-section Exterior \
  --spec-file /tmp/framing.txt -o /tmp/prompt.txt

# 2. generate one candidate. --dry-run validates every invariant for free,
#    including the model — a dead one fails here, not at call time.
python3 bin/gen.py --scene <slug> --prompt-file /tmp/prompt.txt --preset book-float \
  --attach ref_images/style_references/canonical_style_reference.png:STYLE \
  --attach assets/ships/the_antares/reference.png:IDENTITY \
  --request "<user's words, verbatim>" --mode "<what this attempt changes>"

# 3. record your assessment once you have looked at the image
python3 bin/review.py outputs/<slug>/vNNN --review "<what you see, misses included>"

# 4. promote ONLY on explicit user approval
python3 bin/promote.py outputs/<slug>/vNNN --approval "<user's words, verbatim>"
```

A receipt is frozen except `Status` and `Review`, each written by its own script —
`rules.md` → *The two post-hoc fields*. Never hand-edit either.

`--asset <type>/<slug>` instead of `--scene` for asset candidates.
`--refinish <vNNN dir>` re-derives a deliverable with no generation; it needs
`--final-size` or `--preset`.
`--preset book-float` = 1536x1024 on `#1b1e26` under 2.5 MB; `book-float-portrait`
= 1200x1500.

`gen.py` fails closed *before* anything bills on any One Rule violation or a failed
reference provenance check — `rules.md` lists the conditions.

## Workflows

**New asset** (character, ship, object, location): write `description.md` first —
it is the single source of truth, and design changes get snapshotted to
`description_versions/`. Attach the anchor as STYLE plus the minimum identity input
(a `sources/` original, a crop, or nothing). Iterate candidates with the user until
they approve, then promote to `reference.png`.

**Revise an approved asset**: attach the anchor as STYLE and the current
`reference.png` as EDIT TARGET. Update `description.md` and snapshot it whenever
the design itself changes, not just the picture.

**Scene**: attach the anchor as STYLE and each approved `reference.png` as
IDENTITY. Scenes never invent design — restate it from `description.md` so the
model has no room to improvise. Promote to `final.png`.

**Iterating**: each pass is an edit of the previous candidate as EDIT TARGET, which
the user must designate as a baseline. Record that designation in `--mode`.

## Hard-won rules

- **The One Rule** (`rules.md`): anchor FIRST as STYLE, Style Block verbatim,
  closing style line last, prompt delivered **byte-for-byte**.
- **Codex rewrites prompts.** Its `image_gen` skill "normalizes" them, silently
  defeating the Style Block. `--backend codex` relays the prompt from disk into the
  tool argument so it never passes through model tokens. Never hand prompt text to
  Codex as instruction text.
- **Every edit re-asserts the full style.** A thin "just change X" prompt lets the
  anchor's own subjects leak in as content — once producing a two-panel comic page
  with strangers in it. Keep the design, the single-image guard and the no-people
  guard in every edit prompt.
- **`image.png` is frozen history.** Never edit it in place. Deliverables are
  derived; `reference.png` / `final.png` stay byte-identical to their candidate.
- **Unapproved candidates are not IDENTITY inputs** unless the user designates one
  as a baseline. Chaining candidates compounds drift.
- **Positional binding only.** Images reach the model by attachment order, so
  "image 1" is a promise about order, not a filename. The one exception is a masked
  API call, where the EDIT TARGET takes image 1 and the anchor follows — build those
  with `bin/prompt.py --masked`; `image-surgery` has the detail.
- **State the aspect ratio in the prompt body, every time.** `--size` is advisory on
  Codex — it has returned 2:1 when asked for 3:2. Put this in the spec, and say what
  it is NOT: "THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half
  times as wide as it is tall, the proportions of a 1536 x 1024 image." `--size`
  alone is not a constraint; the prompt is.
- **At most FIVE reference images.** `gen.py` refuses a sixth before anything runs;
  left to the backend, `image_gen` rejects it only after an orchestration turn has
  been consumed. Budget the slots: anchor + baseline + identities must total five.
- **Never stack several multi-view sheets on a SCENE.** With four sheets among five
  inputs a scene imitated the *format* of its inputs and returned a character-design
  document. Attach the anchor, the baseline as EDIT TARGET, and **at most one**
  identity sheet — a group lineup beats several individual ones. Carry the rest in
  text. If the identity input contains text, ban reproducing its numbers.
- **Replace prohibitions and adjectives with countable positive statements and
  in-frame geometric referents.** A ban list leaves the model free to satisfy every
  clause and still be wrong — a spec banning loops, rings, cages, cradles and guard
  plates was satisfied by an L-bracket, because it never banned a *bend*. A counted
  statement of what the thing *is* cannot be gamed that way.

  Two patterns carry most of it. **Enumerate instead of counting:** "exactly four
  raiders", stated three times, still produced six; describing each rider one by one
  plus "beyond the fourth the ridge is empty" worked first try. **Point at something
  in the picture, then count it:** a ship's nose took fifteen passes. Naming an in-frame
  axis — "follows the hull's long axis, front face edge-on and foreshortened" — fixed
  the *direction*, but the shape went on failing until a pass stated the *proportion*:
  "the front face must be 2-3x wider than tall." The previous attempt had specified it
  by width alone and produced a tall upright slab. A referent aims the change; a number
  bounds it, and this fault needed both. And the ban that
  survived ten passes — "do NOT break the ground into chips, facets, dashes, hatching"
  — fell to one positive sentence: "across the whole ground use only THREE OR FOUR flat
  tones in total, each an unbroken field, with NO marking at all inside any of them;
  all drawing happens at the edges where fields meet."

  When a prohibition has failed twice, stop adding nouns to the ban list and write the
  positive form with a number in it.
- **Scale drifts upward every pass.** Framing asks are ignored unless the last miss
  is quantified: measure the previous candidate and put the number in the spec ("the
  last attempt filled 40 percent of frame width; cap is one fifth"), plus "if unsure,
  paint it smaller".
- **Diagnose the artefact before naming it, at magnification.** The user's word
  describes how a thing reads, not what it is, so crop and zoom to find the actual
  offending shape before writing the instruction — and before recording any verdict.
  `image-surgery` → *Step 0* has the method and the four-pass cautionary tale.
- **To *correct* an existing image, load `image-surgery` before spending a
  generation.** It routes the change to the cheapest tool that can do it.

## Fix the asset, not the scene

If a design keeps drifting between scene passes, stop iterating on the scene. A
four-view sheet fixes orientation in one pass because the side elevation and top
plan force one consistent reading.

The tell: you are re-describing the same object's geometry in consecutive prompts.
That is the asset system asking to be used. `description.md` first, sheet second,
scene third.

## When description.md and an approved image disagree

They will. Someone's `description.md` says aubergine and their reference paints
magenta.

- **An asset's own `reference.png` is canon for that asset.** The individual sheet
  wins over any group or derived image.
- A **derived** asset that disagrees (a crew lineup, a composite) is the one that
  is wrong, and it should be regenerated against the individual references.
- Amend `description.md` to match whatever was actually approved, bumping the
  version and snapshotting — never leave the text and the art contradicting each
  other, because scenes read the text and the next generation inherits the conflict.
- Surface the conflict to the user rather than silently picking a side.

## Judgment — when an image comes out wrong

### Escalation ladder — design right, rendering wrong

The two obvious approaches each fail one way, which is why the ladder exists: a full
off-style sheet attached as IDENTITY makes the model copy its *rendering and layout* —
the image dominates and "ignore its rendering" loses — while a text-only generation holds
the style but loses the likeness and over-details from the model's reference-sheet prior.

1. **Style-transfer repaint (preferred).** Design-correct image as EDIT TARGET,
   anchor as STYLE, command a TOTAL repaint: "Repaint this entire image in the
   STYLE image's rendering technique — flatten all shading into broad opaque
   angular planes, coarse dry-brush, limited values. Change NOTHING else: preserve
   layout, poses, facial geometry, hair shapes, and all clothing/equipment design
   exactly." The edit pathway preserves geometry so likeness survives. If still too
   detailed, retry from the SAME baseline with stronger flattening language —
   **never edit the edit**.
2. **Fresh generation**: STYLE anchor + description text only. Works when the
   description carries the face.
3. **Likeness assist**: attach a TIGHT FACE CROP saved to `sources/`
   (`magick in.png -crop WxH+X+Y +repage out.png`), never the full sheet. Cropping is
   a copy, so frozen candidates are valid sources. **`+repage` is not optional** — the
   offset would be frozen into a `sources/` file and then attached.
4. **Converge from the style-true side** (when 1-3 fail). The model gives you the
   design OR the style per call, not both — and small DESIGN edits on a style-true
   image hold the style far better than style repaints hold a design. Designate the
   best style-correct candidate as baseline and fix the design toward the
   description in small describable deltas, over two or three rounds.
5. **Signal-degraded repaint** for stubborn cases. The repaint fails because the edit
   target's fine rendering is high-signal, so weaken it mechanically rather than
   verbally: `magick in.png -resize 25% -posterize 5 -resize 400% out.png` flattens it
   toward the style while keeping contours. Repaint THAT, saving the degraded file to
   `sources/` and recording it as the edit target.

### Baselines, and reading feedback

The baseline is `reference.png` **unless the user designates a candidate**, which they do
by approving it while asking for a change — and they never name the mode, so their
phrasing selects it:

- **"This is close — just fix X"** (approving): that candidate becomes the DESIGNATED
  BASELINE. It outranks `reference.png` and stays baseline for the whole series until a
  promotion resets it. Edit it, stating the change relatively ("nose more bulbous") —
  relative language works because the pixels are attached.
- **"Wrong / not him / try again"** (rejecting): no baseline. Absolutize any usable
  feedback into `description.md` (bump + snapshot) and roll fresh. Do not attach the
  rejected candidate.
- **Ambiguous?** Ask "keep this one as the base, or start over?" — one question beats a
  wasted generation.

- **Never chain candidates.** The edit target is the current baseline, not yesterday's
  attempt. If the changes since the baseline are "mustache" then "silver temples", the
  next attempt asks for **both**, from the baseline.
- **Stale-baseline guard.** Before editing `reference.png`, check it is still current. If
  it predates the design by more than one or two description versions, or unapproved
  changes exceed two or three discrete items, an "edit" will behave like a regeneration
  and lose the style. STOP — name the recent candidate that best matches the current
  design and ask the user to promote or designate it.

### Diagnosing a style failure

When the user says a result is off-style ("too detailed", "looks like the source"),
do NOT re-roll with the same inputs. Read the failed attempt's `generation.md` and
check what was attached. If any identity image was attached, assume it dominated
the rendering and move DOWN the ladder (full image → crop → none). Only re-roll
unchanged when the previous inputs were already minimal.

## Backends and cost

`--backend codex` (default) bills the ChatGPT/Codex subscription. `--backend api`
needs prepaid OpenAI credits, which a subscription does **not** fund.

**NEVER run `--backend api` without asking the user first.** `gen.py` holds no key, so
a paid call fails closed and prints what to do — but that is a mechanism, not an
impossibility. **Never run `bin/unlock.py` yourself and never pass `--key-fd`:** those
carry the user's approval, not yours. `bin/selftest.py` reports whether the gate is
actually armed. If you find a key anywhere — a `*.key` file, a history file, the
environment — **do not use it: say you found it.**
`image-surgery` has the bar that justifies even proposing a paid call; `rules.md` has
the mechanism.

**`rules.md` owns which Codex models work — check it rather than this file.** Do
not model-shop for savings: cost is a fixed ~28k input preamble whose cache-hit rate
swamps model choice.

## Working with the user

Show the image and give an honest read, naming where it missed the brief — they
cannot see it until you say what is there. Never promote without explicit approval,
and record their words verbatim in the sidecar. When a pass overshoots, say so and
offer to branch from an earlier candidate rather than stacking another correction.
