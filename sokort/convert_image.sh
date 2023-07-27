#!/bin/ksh
#-------------------
# Convert ps to png and trim the image using ImageMagick tools
#
# Usage:
#     ./convert_image.sh some.ps
#
# Parameters should be passed as environment variables.
#   load_env_script_name:
#
# Input: some.ps
# Output: some.png
#-------------------
set -x
echo "load env script file..."
. ${load_env_script_name}

INPUT=$1
echo "input file: ${INPUT}"

echo "converting file..."
convert -density 200 "${INPUT}[0]" plot_${INPUT%.*}.png
convert -trim plot_${INPUT%.*}.png trim1_${INPUT%.*}.png
convert -trim trim1_${INPUT%.*}.png ${INPUT%.*}.png

echo "removing temp files..."
rm plot_${INPUT%.*}.png
rm $INPUT
rm trim1_${INPUT%.*}.png
set +x