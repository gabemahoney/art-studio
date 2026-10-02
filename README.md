# Rogue Frontier art studio

Skills and tooling for generating illustrations that stay in one locked visual style
across sessions — characters, ships and locations persist as files, and every image is
built from them.

## What's here

| | |
|---|---|
| `skills/` | The skills themselves. Not installed — see below. |
| `gm/image_generation/bin/` | The tooling the skills drive. stdlib only, no venv. |
| `gm/image_generation/rules.md` | How generations run. Read by the code, not just by you. |
| `gm/image_generation/style.md` | What the art looks like. `gen.py` parses this and fails closed if it can't. |
| `gm/image_generation/outputs/`, `assets/` | The written record: one `generation.md` per attempt. |

**Images are not in this repo.** They are large, numerous and regenerable, so they live
in a separate tree you configure — see *Where images live* in `rules.md`. The text here
is the provenance record; a clone needs the image tree synced separately before it can
generate.

## Installing the skills

Nothing is pre-placed. Copy or symlink whichever you want into the location your agent
reads. **Global** makes a skill available in every project; **per-project** keeps it
scoped to one.

| skill | for | what it does |
|---|---|---|
| `art-studio` | Claude Code | How images are *made*: new assets, revisions, scenes, promotion |
| `image-surgery` | Claude Code | How images are *changed*: routing a correction to the cheapest tool that can do it |
| `create_asset` | Codex | Older Codex-side equivalent of `art-studio` |
| `illustrate` | Codex | Older Codex-side scene composition |

### Claude Code

```bash
# per project
mkdir -p <your-project>/.claude/skills
ln -s "$PWD/skills/image-surgery" <your-project>/.claude/skills/

# or globally, for every project
ln -s "$PWD/skills/image-surgery" ~/.claude/skills/
```

Use `cp -R` instead of `ln -s` if you'd rather have an independent copy you can edit
without touching this repo.

### Codex

Same idea, into `.agents/skills/` (per project) or wherever your Codex install reads
skills from.

### This repo's own copies

`.claude/` and `.agents/` here are symlinks back into `skills/`, and both are
gitignored — so working in this repo uses the same files it ships, with no second copy
to drift.

## A caveat on the Codex skills

`create_asset` and `illustrate` predate the move of images out of the repo and still
describe the old layout, where `image.png` sat beside its `generation.md`. The Claude
Code skills and `rules.md` are current. Treat the Codex pair as historical until
updated.

## Running the tooling

Everything runs from `gm/image_generation/`:

```bash
python3 -I bin/selftest.py      # every guard; run this first
python3 -I bin/gen.py --help
```

`bin/selftest.py`'s case list is the authoritative enumeration of what fails closed —
read it rather than trusting a summary.
