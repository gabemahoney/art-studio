# art-studio

A skill and its tooling for building **consistent illustrated scenes** — people,
places, ships and objects persist as files across sessions, and every image is built
from them, so the cast stays recognizable and the rendering never drifts.

It holds no project content. A project's style, style anchor and recurring subjects
live in a **package** somewhere else, and finished scenes go to an **output folder**
somewhere else again. Both are passed to every command as paths:

| | |
|---|---|
| `--package PKG` | `style.md`, the style anchor, `style_versions/`, `presets.json`, `assets/`. Asset work writes here. |
| `--output OUT` | `OUT/<scene>/vNNN/image.png` + `generation.md`. Scene renders write only here, never into the package. |

One package can feed many output folders — the same cast and prompts can render into a
sourcebook and an adventure just by changing `--output`.

## What's here

| | |
|---|---|
| `skills/art-studio/SKILL.md` | The package layout, the six-step loop every image goes through, the rules that are never optional. |
| `skills/art-studio/rules.md` | How generations run. The same for every package. |
| `skills/art-studio/scripts/` | `prompt.py` → `gen.py` → `review.py` → `promote.py`, plus `selftest.py`. Stdlib only, no venv. |
| `skills/art-studio/templates/style.md` | Starting point for a new package's `style.md`. |
| `skills/art-studio/reference/` | Writing prompts, diagnosing a bad image, routing a fix, ImageMagick commands. |

## Installing the skill

Copy or symlink it into the location your agent reads. The scripts travel with it.

```bash
ln -s "$PWD/skills/art-studio" ~/.claude/skills/                  # every project
ln -s "$PWD/skills/art-studio" <project>/.claude/skills/           # one project
```

Needs Python 3, ImageMagick (`magick`), and the `codex` CLI logged in to ChatGPT. The
paid `--backend api` reads its key from `OPENAI_API_KEY` or
`~/.config/art-studio/openai.key` — never from a package or a repo.

## Running the tooling

```bash
python3 -I skills/art-studio/scripts/selftest.py   # every guard, against a throwaway package
python3 -I skills/art-studio/scripts/gen.py --help
```

`selftest.py`'s case list is the authoritative enumeration of what fails closed.
