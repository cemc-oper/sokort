#!/bin/bash
#-------------------
# Convert ps to png and trim the image using ImageMagick tools
#
# Usage:
#     ./convert_image.sh some.ps
#
# Input: some.ps
# Output: some.png
#-------------------
set -x
INPUT=$1
convert -density 200 "${INPUT[0]}" plot_${INPUT%.*}.png
convert -trim plot_${INPUT%.*}.png trim1_${INPUT%.*}.png
convert -trim trim1_${INPUT%.*}.png ${INPUT%.*}.png
rm plot_${INPUT%.*}.png
rm $INPUT
rm trim1_${INPUT%.*}.png
set +x