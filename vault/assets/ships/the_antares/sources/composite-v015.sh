#!/bin/sh
set -eu
# Run from the_antares asset directory; argument is an existing scratch directory.
scratch_dir="$1"
base=candidates/v013/image.png
donor=candidates/v014/image.png
magick "$base" -crop 300x160+0+0 +repage -resize 402x193! "$scratch_dir/plate.png"
magick "$base" "$scratch_dir/plate.png" -geometry +18+767 -composite "$scratch_dir/rear.png"
# Mounting arms, scaled to the small rear-view drawing.
magick "$donor" -crop 51x52+130+845 +repage -resize 53x39! "$scratch_dir/left-arm.png"
magick "$donor" -crop 47x52+302+845 +repage -resize 53x39! "$scratch_dir/right-arm.png"
magick "$scratch_dir/rear.png" "$scratch_dir/left-arm.png" -geometry +105+846 -composite "$scratch_dir/rear.png"
magick "$scratch_dir/rear.png" "$scratch_dir/right-arm.png" -geometry +277+846 -composite "$scratch_dir/rear.png"
# Central aft body and original generated turbine artwork at matching smaller scale.
magick "$donor" -crop 208x145+137+790 +repage -resize 156x109! "$scratch_dir/body.png"
magick -size 156x109 xc:black -fill white -draw 'polygon 0,42 20,37 35,25 54,21 55,10 66,9 67,6 88,6 90,10 100,10 102,21 120,26 135,38 155,44 155,78 127,85 115,98 98,102 93,107 64,107 58,103 45,101 40,96 31,94 27,86 0,79' "$scratch_dir/body-mask.png"
magick "$scratch_dir/body.png" "$scratch_dir/body-mask.png" -alpha off -compose CopyOpacity -composite "$scratch_dir/body.png"
magick "$scratch_dir/rear.png" "$scratch_dir/body.png" -geometry +139+808 -composite "$scratch_dir/rear.png"
magick "$donor" -crop 109x110+29+810 +repage -resize 76x77! "$scratch_dir/left-turbine.png"
magick "$donor" -crop 108x110+345+810 +repage -resize 76x77! "$scratch_dir/right-turbine.png"
magick -size 76x77 xc:black -fill white -draw 'ellipse 38,39 37,37 0,360' "$scratch_dir/turbine-mask.png"
magick "$scratch_dir/left-turbine.png" "$scratch_dir/turbine-mask.png" -alpha off -compose CopyOpacity -composite "$scratch_dir/left-turbine.png"
magick "$scratch_dir/right-turbine.png" "$scratch_dir/turbine-mask.png" -alpha off -compose CopyOpacity -composite "$scratch_dir/right-turbine.png"
magick "$scratch_dir/rear.png" "$scratch_dir/left-turbine.png" -geometry +33+827 -composite "$scratch_dir/rear.png"
magick "$scratch_dir/rear.png" "$scratch_dir/right-turbine.png" -geometry +326+827 -composite "$scratch_dir/rear.png"
# Restrict rear replacement to the existing rear-view footprint; soften only its boundary.
magick -size 1536x1024 xc:black -fill white -draw 'rectangle 18,767 416,960' -morphology Erode Disk:6 -blur 0x3 -fill black -draw 'rectangle 417,0 1535,1023' -alpha off "$scratch_dir/rear-mask.png"
magick "$base" "$scratch_dir/rear.png" "$scratch_dir/rear-mask.png" -composite "$scratch_dir/rear-composite.png"
# Fixed upper structure behind the open door. Preserve the original raised panel and hinge.
magick -size 1536x1024 xc:black -fill white -draw 'rectangle 1215,731 1500,808' -fill black -draw 'polygon 1251,799 1288,728 1447,706 1456,719 1418,786 1271,814' "$scratch_dir/inset-mask.png"
magick "$scratch_dir/rear-composite.png" "$donor" "$scratch_dir/inset-mask.png" -composite "$scratch_dir/composite.png"
# Include the existing deck/spine above the panel, extending the tight crop upward.
magick "$base" -crop 220x80+600+90 +repage -resize 286x104! "$scratch_dir/upper-hull.png"
magick "$scratch_dir/composite.png" "$scratch_dir/upper-hull.png" -geometry +1214+700 -composite "$scratch_dir/upper-hull-layer.png"
magick -size 1536x1024 xc:black -fill white -draw 'rectangle 1215,702 1499,781' -fill black -draw 'polygon 1251,799 1288,728 1447,706 1456,719 1418,786 1271,814' "$scratch_dir/upper-hull-mask.png"
magick "$scratch_dir/upper-hull-mask.png" -alpha off "$scratch_dir/upper-hull-mask.png"
magick "$scratch_dir/composite.png" "$scratch_dir/upper-hull-layer.png" "$scratch_dir/upper-hull-mask.png" -composite -fill none -stroke '#9daeb2' -strokewidth 1 -draw 'path "M1213,730 L1213,700 L1501,700 L1501,730"' "$scratch_dir/composite.png"
