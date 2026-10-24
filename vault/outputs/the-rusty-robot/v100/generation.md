# the-rusty-robot v100

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "Also, there is one window lit above the Rusty Robot in that scene image. Can you try making it look dark like the others?"

## Sources

| region | from |
|---|---|
| everything | **v099** (final) |
| lit right pane of the window above the sign (x 598–611, y 117–158) | the same window's dark left pane, `-crop 13x36+583+117` pasted at +598+117; remaining orange pixels at the pane's foot (r>0.55, r−b>0.25, box 596–613 × 140–160) set to the pane's own dark colour srgb(27%,21%,14%) |

Status: awaiting user evaluation

Review: Window now dark like its neighbours; sill and frame unchanged. Only pixels in the box above changed.
