# Rogue Frontier image generation

This directory is an image vault, not an app: characters, ships, locations and the
style itself persist as files, and every image is built from them.

**Use the `art-studio` skill for all image work here** — it carries the workflow, the
tooling and the rules. Invoke it before generating, revising or promoting anything.

Images are generated only through `bin/` (`prompt.py` → `gen.py` → `promote.py`),
never by calling an image tool directly. `rules.md` and `style.md` are the contract.
