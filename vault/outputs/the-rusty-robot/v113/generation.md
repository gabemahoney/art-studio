# the-rusty-robot v113

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "Can you try one where she is doing the pointing pose again? Like in v5?"

## Sources (layered rebuild per the skill's core rule)

| region | from |
|---|---|
| everything | **v100** (approved v099 + dark window) |
| alley, x 42–345, y 440–930 | **v101** (edit pass: crew removed), via `mask-alley-from-v101.png` — edges on the alley's left pillar and the cantina corner |
| the crew | **outputs/the-rusty-robot-crew-pose/v003** (crew-pose v002 with Sion pointing as in v005; faces checked at 200%), cut out with `mask-crew-from-pose-v003.png`, stray specks removed (connected components < 5000 px), scaled to 400 px tall, at +38+512 (20 px lower than v102, so their feet stand on the paving in front of the side wall) |

Status: awaiting user evaluation

Review: Supersedes v110 (whose mask carried a stray speck that shrank the crew). Not yet blended.
