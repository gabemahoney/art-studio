# art-studio

Tooling and one skill for building consistent illustrated scenes. The vault lives in
`vault/` — personas, locations, items and the style itself persist there
as files, and every image is built from them.

Before touching anything under there, read `vault/CLAUDE.md`, then its
`rules.md` (how generations run) and `style.md` (what this particular project's art
looks like). Images are generated only through `vault/bin/` — never by
calling an image tool directly.
