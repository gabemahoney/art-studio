# art-studio

An illustration skill for coding agents. It makes characters, places, objects and
scenes in one locked visual style, so a recurring cast stays recognizable across a
whole project.

You ask your agent for a picture; the skill makes it work like an art department
rather than a one-off image generator:

- **Every subject persists on disk** as a written design plus one approved picture,
  and scenes are built only from approved pictures, so the cast never drifts.
- **Every call re-asserts the style**: the style anchor image goes first and the
  written Style Block goes verbatim into every prompt, so the look cannot wander.
- **Every image has a receipt** (`generation.md`) with the full prompt and every
  input, so any image can be explained or replayed.
- **The scripts fail closed.** A malformed call is refused before anything is sent,
  so a mistake costs nothing.

The repo holds no project content. A project's style and subjects live in a
**package**, and scene renders land in an **output folder**; both sit outside this
repo and are passed to every command as `--package` and `--output`. One package can
feed many output folders.

## Install

Symlink or copy `skills/art-studio` into your agent's skills folder. The scripts
travel with it.

```bash
ln -s "$PWD/skills/art-studio" ~/.claude/skills/art-studio            # every project
ln -s "$PWD/skills/art-studio" <project>/.claude/skills/art-studio    # one project
```

You need:

- **Python 3.** The scripts use the standard library only, so no venv.
- **ImageMagick 7** (`magick`), for checks, masks and deliverables.
- **The `codex` CLI**, logged in to ChatGPT. The default backend generates through it
  and bills your subscription. Run it from inside any git repository, because
  `codex exec` refuses to run outside one.
- **Optional: an OpenAI API key**, only for `--backend api` (masked repaints). It
  spends prepaid credits, so every paid call needs `--approved-by "<the user's
  words>"`. Put the key in `OPENAI_API_KEY` or `~/.config/art-studio/openai.key`,
  never in a package or a repo.

## Quick start

Your agent normally runs these steps for you; [`SKILL.md`](skills/art-studio/SKILL.md)
is its full procedure. The commands below show the shape of the work. `S` is the
installed `scripts/` folder, and `PKG` and `OUT` are your package and output folder.

```bash
S=~/.claude/skills/art-studio/scripts
```

### 1. Set up a package

Write the look in words, and pick one image that shows it: the style anchor.

```bash
mkdir -p PKG/ref_images/style_references PKG/style_versions PKG/assets
cp $S/../templates/style.md PKG/style.md            # then write its Style Block
cp anchor.png PKG/ref_images/style_references/canonical_style_reference.png
cp anchor.png PKG/style_versions/canonical_style_reference-v1.png
cp PKG/style.md PKG/style_versions/style-v1.md      # after the Style Block is written
```

### 2. Make an asset

Create the asset's folder and write its design to `description.md` first, then
assemble a prompt, generate one candidate, record what you see, and promote it only
when the user approves.

```bash
mkdir -p PKG/assets/people/alice              # then write description.md
python3 $S/prompt.py --package PKG --role STYLE \
  --task "A character sheet: front, three-quarter, profile and back views." \
  --design-from assets/people/alice/description.md -o prompt.txt
python3 $S/gen.py --package PKG --asset people/alice --prompt-file prompt.txt \
  --attach ref_images/style_references/canonical_style_reference.png:STYLE \
  --request "<the user's words>" --mode "first sheet"
python3 $S/review.py PKG/assets/people/alice/candidates/v001 --review "<what you see>"
python3 $S/promote.py PKG/assets/people/alice/candidates/v001 --approval "<the user's words>"
```

Promotion writes `reference.png`, the only picture a scene may use for that asset.

### 3. Compose a scene

Every new scene starts with a Layer Plan the user confirms: **single** (one image) or
**layered** (separately revisable Layers stacked into one picture). Run the plan with
`--dry-run` first, show it, then record the confirmation with the journal number the
dry run printed.

A single scene:

```bash
python3 $S/layers.py plan --package PKG --output OUT --scene harbour --single --dry-run
python3 $S/layers.py plan --package PKG --output OUT --scene harbour --single \
  --confirmation "<the user's words>" --based-on 0
python3 $S/prompt.py --package PKG --role STYLE --role IDENTITY \
  --task "One illustration of the scene below." --spec-file spec.txt -o scene.txt
python3 $S/gen.py --package PKG --output OUT --scene harbour --prompt-file scene.txt \
  --attach ref_images/style_references/canonical_style_reference.png:STYLE \
  --attach assets/people/alice/reference.png:IDENTITY \
  --request "<the user's words>" --mode "first pass"
```

Then review and promote `OUT/harbour/vNNN` as in step 2; promotion writes
`OUT/harbour/final.png`.

A layered scene names a Frame and its Layers, bottom to top. You generate each Layer
with `gen.py --layer`, stack them with `layers.py combine`, and approve the result
with `promote.py`:

```bash
python3 $S/layers.py plan --package PKG --output OUT --scene quay --frame 1536x1024 \
  --layer sky="Sky and distant hills" --layer boats="The two fishing boats" --dry-run
# record the confirmation as above, then make each Layer:
python3 $S/gen.py --package PKG --output OUT --scene quay --layer boats \
  --prompt-file boats.txt \
  --attach ref_images/style_references/canonical_style_reference.png:STYLE \
  --request "<the user's words>" --mode "first pass"
python3 $S/layers.py combine --package PKG --output OUT --scene quay
python3 $S/layers.py status --package PKG --output OUT --scene quay
```

[`reference/layered-scenes.md`](skills/art-studio/reference/layered-scenes.md) covers
planning, keeping, approving and revising one Layer;
[`reference/writing-prompts.md`](skills/art-studio/reference/writing-prompts.md) covers
Layer prompts (`prompt.py --layer-name`).

Add `--dry-run` to any `gen.py` call to check it for free: nothing is sent and no
candidate number is used.

## What's in the repo

| Path | What it is |
|---|---|
| [`skills/art-studio/SKILL.md`](skills/art-studio/SKILL.md) | The skill: package layout, the six-step loop every image follows, and the rules that are never optional. |
| [`skills/art-studio/rules.md`](skills/art-studio/rules.md) | How generations run: the One Rule, image roles, reference validation, style versioning, backends. |
| [`skills/art-studio/reference/`](skills/art-studio/reference/) | Read when needed: writing prompts, when an image looks wrong, fixing an image, ImageMagick recipes, Layered Scenes. |
| [`skills/art-studio/templates/style.md`](skills/art-studio/templates/style.md) | The starting `style.md` for a new package. |
| `skills/art-studio/scripts/` | The tooling, below. |

| Script | What it does |
|---|---|
| `prompt.py` | Assembles a prompt in the mandated order: Style Block, image roles, task, design, spec, closing style line. |
| `gen.py` | Generates one candidate, scene version, Layer Version or Draft, and writes its receipt. Refuses any call that breaks the rules. |
| `review.py` | Records your assessment on a receipt. |
| `promote.py` | Approves an asset candidate, scene version, Layer Version or Combined Image on the user's words, and verifies the copy byte for byte. |
| `layers.py` | Plans scenes, combines Layers, records keeps and fixes, checks deletions and reports status. Calls no image model. |
| `scene_state.py` | The Scene Journal rules shared by `gen.py`, `promote.py` and `layers.py`. |
| `selftest.py` | Checks that every guard still fails closed. |

`prompt.py`, `gen.py`, `review.py`, `promote.py` and `layers.py` print their full
usage with `--help`.

## Self-test

Run the self-test after any change under `scripts/`. It builds a throwaway package in
a temp folder and stubs the image model, so it generates nothing and bills nothing.

```bash
python3 -I skills/art-studio/scripts/selftest.py
python3 -I skills/art-studio/scripts/selftest.py --exhaustive   # also after changing scene_state.py, layers.py or promote.py
```

`--exhaustive` adds a slower state-space test of the Scene Journal. The self-test's
case list is the authoritative record of what the scripts refuse.

## Contributing

Keep this repo generic: never add project content such as styles, anchors, assets,
presets, receipts or subject names, because every project shares the skill. The
`.gitignore` blocks image files as a backstop.
