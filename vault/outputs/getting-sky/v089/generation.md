# getting-sky v089

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "in 86 some white cruft go added to the right side of the Antares. Do you see it? Can we remove it?"

## Sources

| region | from |
|---|---|
| everything | **v076** |
| area the Antares left | **v076 shifted down 40 px** (so each vacated pixel takes the background from 40 px above it — never ship pixels), through `mask-vacated-region.png` |
| the Antares and her trails | v076 through `mask-antares-and-trails-tight.png` (her cutout alpha undilated ∪ trail pixels left of x 1080, dilated 3, blur 1), moved down 40 px |
| two beams | as v084/v086 (`beam-draw.sh`) |

v086's cruft came from two things: the gorge-reference fill was far brighter than v076's
rock where her nose had been, and the over-dilated ship mask dragged a band of bright haze
along with her. This version fills from v076 itself and uses a tight mask.

Status: awaiting user evaluation

Review: User: front of the bottom (wingman) ship munged — the vacated-region mask reached x 509 and overwrote its nose and barrels with rock from 40 px above. Fixed in v090.
