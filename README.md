# art-studio

Skills and tooling for building **consistent illustrated scenes** — personas,
locations, items, buildings and other assets persist as files across sessions, and
every image is built from them, so the cast stays recognizable and the rendering never
drifts.

The tool is project-agnostic. A project supplies its own style guide, its own style
anchor image and its own asset categories; nothing in `skills/` or `bin/` knows what
you are illustrating. The vault checked in here happens to hold one such project.

## What's here

| | |
|---|---|
| `skills/` | The skills themselves. Not installed — see below. |
| `vault/bin/` | The tooling the skills drive. stdlib only, no venv. |
| `vault/rules.md` | How generations run. Read by the code, not just by you. |
| `vault/style.md` | What the art looks like. `gen.py` parses this and fails closed if it can't. |
| `vault/outputs/`, `assets/` | The written record: one `generation.md` per attempt. |

**Images are not in this repo.** They are large, numerous and regenerable, so they live
in a separate tree you configure — see *Where images live* in `rules.md`. The text here
is the provenance record; a clone needs the image tree synced separately before it can
generate.

## Installing the skill

There is one skill, `art-studio`, and nothing is pre-placed. Copy or symlink it into
the location your agent reads. **Global** makes it available in every project;
**per-project** keeps it scoped to one.

```bash
# per project
mkdir -p <your-project>/.claude/skills
ln -s "$PWD/skills/art-studio" <your-project>/.claude/skills/

# or globally, for every project
ln -s "$PWD/skills/art-studio" ~/.claude/skills/
```

Use `cp -R` instead of `ln -s` if you'd rather have an independent copy you can edit
without touching this repo. For Codex, same idea into `.agents/skills/` or wherever
your install reads skills from.

Its shape:

| | |
|---|---|
| `SKILL.md` | The vault layout and what each file is for, the six-step loop every image goes through, the rules that are never optional. |
| `reference/writing-prompts.md` | Writing a spec the model actually obeys. |
| `reference/when-it-looks-wrong.md` | Choosing a baseline, diagnosing a failure, the re-style ladder. |
| `reference/fixing-an-image.md` | Routing a correction to the cheapest tool that can do it. |
| `reference/imagemagick.md` | The commands that routing picks. |

`SKILL.md` names the step at which each reference file applies, so none of them is
loaded until it is needed.

### This repo's own copy

`.claude/skills/art-studio` here is a symlink back into `skills/`, and `.claude/` is
gitignored — so working in this repo uses the same file it ships, with no second copy
to drift.

## Running the tooling

Everything runs from `vault/`:

```bash
python3 -I bin/selftest.py      # every guard; run this first
python3 -I bin/gen.py --help
```

`bin/selftest.py`'s case list is the authoritative enumeration of what fails closed —
read it rather than trusting a summary.
