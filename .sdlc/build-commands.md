# Build commands

One code folder: the repo root (`.`). Run every command from the repo root (or the worktree root).

## Compile

- `.`: none: pure Python scripts, no build step and no type checker configured.

## Lint

- `.`: none: the repo configures no linter.

## Unit tests

- `.`: `python3 -I skills/art-studio/scripts/selftest.py`

## Integration tests

- `.`: none: the selftest drives the scripts end to end; real image generation calls a paid API and is
  never run in checks.
