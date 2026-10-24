# art-studio

A generic illustration skill and its tooling: `skills/art-studio/`. It holds no project
content — a project's style and assets live in a package outside this repo, and scene
renders go to an output folder outside it too. Both are passed as `--package` and
`--output` on every command.

Never add project-specific content (styles, assets, presets, receipts, subject names)
to this repo. After touching anything in `skills/art-studio/scripts/`, run
`python3 -I skills/art-studio/scripts/selftest.py`.
