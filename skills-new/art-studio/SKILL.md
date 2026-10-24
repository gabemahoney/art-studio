---
name: art-studio
description: Make, revise and approve illustrations in one consistent visual style. Recurring subjects (people, places, objects) are designed once as approved reference sheets, and scenes are composed from them. Use for all image work in an art-studio project — setting one up, designing an asset, revising one, composing a scene, fixing an image, or approving a candidate.
---

# Art studio

Every recurring subject — person, place, object — lives on disk as a written design
plus one approved picture. Scenes are built from those pictures, so subjects stay
recognizable and the style holds.

Generation goes through four scripts: `prompt.py` → `gen.py` → `review.py` →
`promote.py`. They build the prompt, attach the style anchor, write a receipt per
attempt and record approvals.

## Setup (once per project)

Needs Python 3, ImageMagick (`magick`), and the `codex` CLI logged in to ChatGPT.

1. **Pick two folders**: a *project folder* for text (designs, receipts — keep it in
   git) and an *images folder* for PNGs. They can be the same.
2. **Create the project folder:**
   ```bash
   mkdir -p <project>/bin <project>/style_versions
   cp <this skill>/scripts/*.py <project>/bin/
   cp <this skill>/templates/style.md <project>/style.md
   echo "<images folder>" > <project>/image-root     # absolute, or relative to <project>
   ```
3. **Write the style**: fill in the Style Block in `style.md`, then copy it to
   `style_versions/style-v1.md`.
4. **Add the style anchor**, one image that shows the look:
   ```bash
   mkdir -p <images>/ref_images/style_references <images>/style_versions
   cp anchor.png <images>/ref_images/style_references/canonical_style_reference.png
   cp anchor.png <images>/style_versions/canonical_style_reference-v1.png
   ```
5. **Optional, for `--backend api`** (paid, masked inpainting): set `OPENAI_API_KEY` or
   put the key in `<project>/openai.key`, kept out of version control.

Run commands from `<project>`. Paths are project-relative; the scripts send `.png`
files to the images folder and everything else to the project folder.

### Layout

```
<project>/
  style.md                      the look in words (Style Block + closing lines)
  image-root                    one line: the images folder
  bin/                          the scripts
  style_versions/               frozen copies of each style version
  assets/<type>/<slug>/         one folder per recurring subject
    description.md              the design in words — the source of truth
    description_versions/       a frozen copy per design version
    sources/                    user-supplied originals and crops
    candidates/vNNN/            one folder per attempt: image.png + generation.md
    reference.png + .md         the approved image and its approval record
  outputs/<slug>/               one folder per scene
    vNNN/                       one folder per attempt
    final.png + .md             the approved scene
```

`<type>` is any category: `people`, `places`, `items`. The files are the status: an
asset is approved when `reference.png` exists, a scene is done when `final.png`
exists, the latest attempt is the highest `vNNN`.

## The workflow

Five steps for every image. Scratch files go in `T=$(mktemp -d)`.

### 1. Write the design down

- **New asset** → `assets/<type>/<slug>/description.md`, headed
  `**Description version: v1**`; copy it to `description_versions/description-v1.md`.
- **Revision** → update `description.md`, bump the version, snapshot it. Write the
  design whole ("large rounded nose"), not as a change ("bigger nose").
- **Scene** → a short spec in a scratch file: who, where, action, light, framing.

### 2. Build the prompt

```bash
python3 bin/prompt.py --role STYLE --role IDENTITY \
  --task "A single three-quarter view against a plain background." \
  --design-from assets/<type>/<slug>/description.md \
  --spec-file $T/spec.txt -o $T/prompt.txt
```

One `--role` per attached image, in attach order; image 1 is always STYLE.
`--role ROLE:"text"` overrides the default wording.

| role | what it is |
|---|---|
| `STYLE` | the style anchor — copy its rendering, ignore its content |
| `IDENTITY` | an approved `reference.png` or a `sources/` image — copy its design, ignore its rendering |
| `EDIT TARGET` | the image being changed — keep everything the prompt doesn't change |

### 3. Generate

```bash
python3 bin/gen.py --asset <type>/<slug> --prompt-file $T/prompt.txt \
  --attach ref_images/style_references/canonical_style_reference.png:STYLE \
  --attach assets/<type>/<other>/reference.png:IDENTITY \
  --request "<the user's words>" --mode "<what this attempt changes>"
```

- `--scene <slug>` instead of `--asset` for a scene.
- `--attach path:ROLE`, same order as `--role`; five at most.
- `--dry-run` checks everything without generating.
- `--final-size WxH`, `--flatten <color>`, `--max-mb N` shape the delivered copy.

### 4. Review

Open the image; compare it with `description.md`, the anchor and the base. Zoom every
approved element in the frame to 200% and check it against its reference — not only
the thing this pass changed (see *The core rule: lock what's approved* below). Record it:

```bash
python3 bin/review.py <path>/vNNN --review "<what you see, including misses>"
```

### 5. Show the user

Show the image with its path, and say plainly where it misses. Then:

- **Changes** → back to step 1 or 2. Expect many rounds.
- **Approval** →
  ```bash
  python3 bin/promote.py <path>/vNNN --approval "<their words>"
  ```
  Copies the candidate to `reference.png` or `final.png` and writes the approval
  record (`--replace` to supersede). Then bring `description.md` in line with it.

## The three jobs

| job | step 1 writes | step 3 attaches |
|---|---|---|
| **New asset** | `description.md` v1 | anchor; a user-supplied source as IDENTITY, if any |
| **Revise an asset** | `description.md`, next version | anchor; the baseline as EDIT TARGET |
| **Scene** | a short spec | anchor; the approved scene so far as EDIT TARGET; the reference of every asset in frame as IDENTITY — on every pass |

**Default sheet layouts:** people get front, three-quarter, profile and back views at
one scale plus a few expressions, on plain grey; objects get orthographic views and
details; places get an establishing view, alternate angles and details. Mark invented
details *(provisional)* in `description.md`.

**Scenes need approved assets.** If one is missing, say which to approve first.

---

## The core rule: lock what's approved

The problem this rule exists for: an edit pass does not change "only X". The model
repaints the whole frame, and everything it was not asked about drifts a little toward
its generic default. One pass is barely visible; a chain of passes is not — a
character's mustache fades over three passes, a face becomes a stranger, a staircase
shrinks. Most of what goes wrong in a long session is this. So:

- **Approved parts are locked.** Once the user has approved something in an image — a
  face, a building, a ship — later passes may not change it. After every edit pass,
  keep only the region the pass was meant to change and paste it onto the last
  approved image; everything else stays byte-identical to that image.
- **Every pass that shows an asset attaches its reference.** If a character, building
  or ship is in the frame, its approved `reference.png` goes in as IDENTITY on every
  pass — including passes about something else entirely (adding passersby, changing a
  lamp). Without it, nothing holds the likeness.
- **Review every locked part, not just the change.** In step 4, zoom each approved
  element to 200% and compare it with its reference and with the last approved image:
  faces, distinguishing features (a mustache, goggles, an emblem), part counts.
- **Never take a whole frame from an edit by default.** Take it whole only if the user
  approves that specific result after you have checked the locked parts.

## Best practices

### Fresh for the whole, layered for the parts

1. **Get the look and composition fresh.** Put everything settled into
   `description.md` and the spec, attach the anchor and references, attach no earlier
   candidate, roll two, let the user pick. If the look or layout is wrong, start fresh
   again rather than editing toward it.
2. **Fix small faults by layering**: one edit pass aimed at the fault, then paste only
   the fixed region back onto the approved image (see the core rule). When regeneration
   keeps getting a region wrong, use a masked API call and paste its region back. Each
   composite is its own `vNNN` whose receipt names sources and mask.

**Build scenes in layers.** Approve the location alone first. Then add each subject —
characters, ships, crowds, props — one per pass: paint the subject alone on plain grey
at the pose the scene needs, paste it into the approved scene at the size and angle
wanted, then run one blend pass and keep only the subject's region. Placement, size and
angle come out exactly; nothing already approved moves.

**Keep edit prompts short.** Once the base is right, a few plain sentences ("tuck them
further into the alley, darker") beat a long spec. Long specs full of pixel sizes and
constraints made results worse: the model fixed what was named and drifted the rest.

**Describe the character, not only the fixes.** Put surface, wear, colour and detail
in `description.md`. Fix lists are mostly removals; with nothing protecting the
character, every pass erodes it.

**Reuse a composition from an older image** by attaching it as IDENTITY with
distractions blacked out, copying only camera and framing. It also teaches the *size*
of what's in it — drop it once that scale is wrong.

**Check the framing every pass.** Edits sometimes move the camera or resize the main
subject. Compare with the base side by side.

### Masks and composites

- **Every mask edge lies on a real boundary** — a roofline, a wall edge, a ledge, a
  horizon. A straight cut across open sky or wall leaves a visible break, and
  feathering just smears it. Trace boundaries on a gridded zoom first.
- **Inspect the whole seam at 100–200%** before showing a composite, and show the
  un-composited pass beside it.
- **Don't hand-paint with ImageMagick** — fills, gradients, warped pastes read as
  stickers. Use it to move model-painted pixels, not invent them.

### Choosing a baseline

- **"Close, just fix X"** → that candidate is the baseline: attach it as EDIT TARGET
  and describe the change relatively.
- **"Wrong, try again"** → no baseline; fold the feedback into `description.md` and
  generate fresh.
- **Unclear** → ask "keep this one as the base, or start over?"
- **Edit from the baseline, not the latest attempt.** Ask for all changes since the
  baseline at once.

### Writing specs

- **Say what something is, with numbers.** "Three or four flat tones" beats "no busy
  texture". A prohibition that fails twice becomes a positive, countable statement.
- **Enumerate rather than count**: describe each of the four items, then close the set.
- **Anchor directions and sizes to things in the frame**: "its head level with the
  door lamps" beats "smaller", "parallel to the wall behind it" beats "turned away".
- **State the aspect ratio in the prompt body** — Codex treats `--size` as a hint.

### Choosing attachments

- **Attach the least identity input that carries what text can't**: source, crop, or
  nothing. If a result copies a source's rendering, describe more and attach less.
- **One reference sheet per scene.** Several make the model return a sheet; carry the
  rest in text.
- **Attach approved images**, except a baseline the user picked.

### When the style is wrong but the design is right

Stop at the first that works:

1. **Repaint**: the design-correct image as EDIT TARGET, a prompt for a total repaint
   in the anchor's technique, preserving layout and design.
2. **Fresh** from the anchor and description alone.
3. **Crop assist**: a tight crop of the key detail as IDENTITY.
4. **Converge from the style side**: nudge the best on-style candidate's design in
   small steps.
5. **Degrade then repaint**: `magick in.png -resize 25% -posterize 5 -resize 400%
   sources/flat.png`, then repaint that.

An attached identity image is the usual cause of off-style results — check the
receipt.

### Fixing an existing image

Read `reference/fixing-an-image.md` before spending a generation on a fix;
`reference/imagemagick.md` has the commands.

### Keeping the record trustworthy

- **Candidates are permanent.** Corrections become a new `vNNN`.
- **Approve with `promote.py`.** `gen.py` refuses a `reference.png` that doesn't match
  the candidate its record names.
- **When text and approved image disagree**, the image wins; update the text and tell
  the user.
- **Style changes are versioned**: bump `**Style version**`, add a changelog line,
  freeze `style.md` and the anchor into `style_versions/` as `-v<N>`.
- **Fix drifting designs at the asset**, not by re-describing them in scene prompts.
- **Diagnose at 300–500%.** The user's word says how something reads, not what it is.

### Backends and cost

`--backend codex` (default) uses the ChatGPT subscription. `--backend api` spends
prepaid credits and is the only way to do masked inpainting.

Before every API call, `--dry-run` it, then ask on its own line, e.g. **Approve paid
API call (~$0.09, quality high)? yes/no**, with what it changes and the mask coverage.
Pass the reply with `--approved-by`; `gen.py` refuses a paid call without it. One yes
covers one call.

If Codex returns a 400 saying a model isn't supported, pass another with `--model`.
