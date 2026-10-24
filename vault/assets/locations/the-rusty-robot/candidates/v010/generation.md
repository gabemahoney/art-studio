# the-rusty-robot (asset) v010

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User requests verbatim: "The door needs to remain half circular like it was in the first image" / "dude v8 looks horrible" / "the 3/4 view has the sign completely messed up" / "also remove tehe grey box on the right of the door. I don't know what that is."

## Sources

| region | from |
|---|---|
| everything | **v007** (model-drawn sign, not v008's warp) |
| both door portals | **v009** (semicircular brutalist portal), via `mask-doors-from-v009.png` (3/4: polygon 425,562 672,572 672,792 425,792; front: rectangle 1134,372 1310,505; blur 0x3) |
| grey plate beside the door, both views | painted out with wall from directly above it: 3/4 36x36+658+664 → +658+702; front 24x24+1292+400 → +1292+425, feathered |

v007 vs v009 along the door masks' edges: mean difference 6–10 /255, on plain lit wall.

Status: awaiting user evaluation

Review: Arched brutalist doors in place in the three-quarter and front views; grey plate gone; v007's sign restored. A faint trace of the plate's outline may remain at 300% in the three-quarter view. Carries v007's other issues: three storeys in the three-quarter view, blotchy generic surface (user: lost v001's character).
