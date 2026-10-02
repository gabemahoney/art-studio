# Antares v013

User request: "Yes" to direct compositing of the corrected orthographic hull regions onto v010, preserving the hero, engine positions, and cargo details.
Mode: user-authorized direct image composite; no new image generation
Tool: ImageMagick 7.1.2-27 Q16-HDRI
Style: v2 (inherited from source images; no style repaint)
Design: description.md (v8 = description_versions/description-v8.md)
Inputs:
- BASE: candidates/v010/image.png
- ORTHOGRAPHIC HULL DONOR: candidates/v011/image.png
- MASK: sources/composite-v013-mask.png
Output: candidates/v013/image.png (1536 x 1024)
Status: candidate; not promoted.

## Operation

Composite the selected front, top, and rear hull areas of v011 onto v010. Preserve all pixels outside the mask. The mask includes the orthographic bodies and small mounting-joint cleanup areas, with a narrow transition at patch boundaries. Engine regions are excluded. The hero, side profiles, and both cargo insets remain the original v010 pixels.

Run from the asset directory:

```sh
magick candidates/v010/image.png candidates/v011/image.png sources/composite-v013-mask.png -composite candidates/v013/image.png
```

The frozen mask is sufficient to replay the composite exactly; it is grayscale with alpha disabled. There is no new image-generation prompt.

## Mask construction

Main SVG (1536 x 1024):
```svg
<svg xmlns="http://www.w3.org/2000/svg" width="1536" height="1024" viewBox="0 0 1536 1024">
<rect width="1536" height="1024" fill="black"/>
<path d="M1221 20 H1406 V191 H1495 V449 H1135 V191 H1221 Z" fill="white"/>
<rect x="162" y="545" width="350" height="195" fill="white"/>
<rect x="151" y="770" width="129" height="180" fill="white"/>
</svg>
```

Join-cleanup SVG (1536 x 1024):
```svg
<svg xmlns="http://www.w3.org/2000/svg" width="1536" height="1024">
<rect width="1536" height="1024" fill="black"/>
<rect x="157" y="582" width="30" height="35" fill="white"/>
<rect x="492" y="582" width="26" height="35" fill="white"/>
</svg>
```

Rasterize main SVG with alpha off and grayscale. Erode with Disk:5, blur 0x3, and multiply by the original hard mask. Rasterize the join SVG with alpha off and grayscale, erode Disk:1, blur 0x0.8. Combine masks using Lighten. Save the resulting mask as sources/composite-v013-mask.png.

## Verification

Visual inspection: orthographic hull flare reduced; original hero silhouette, single low-hinged cargo door, clean hull band, ramp, three crew, layout, and palette retained. No new painting or style generation.

Maximum absolute pixel difference from v010 is zero in every protected region below:
- Hero: 1120x540+0+0
- Cargo insets: 611x309+925+715
- Port profile: 823x170+680+540
- Starboard profile: 505x170+417+770
- Front left engine: 127x146+28+560
- Front right engine: 115x146+532+560
- Top left engine: 88x171+1133+20
- Top right engine: 96x171+1407+20
- Rear left engine: 123x136+28+799
- Rear right engine: 128x136+281+799

Difference check: composite base and output using Difference, crop each listed region, and inspect %[fx:maxima].
