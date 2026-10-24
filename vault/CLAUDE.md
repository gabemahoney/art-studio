# The art vault

This directory is an image vault, not an app: personas, locations, items, buildings and
the style itself persist as files, and every image is built from them.

**Use the `art-studio` skill for all image work here** — it carries the workflow, the
tooling and the rules. Invoke it before generating, revising or promoting anything.

Images are generated only through `bin/` (`prompt.py` → `gen.py` → `review.py` → `promote.py`),
never by calling an image tool directly. `rules.md` and `style.md` are the contract:
`rules.md` is the same for any project, `style.md` is this one's.
