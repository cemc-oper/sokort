#!/usr/bin/env bash
# Run python script to draw graph for GRAEPS GFS GMF.
#
# Prepare:
#   1. enter a work directory
#   2. link and copy scripts
#
# Parameters should be passed as environment variables.
#   start_time: YYYYMMDDHH
#   forecast_time: FFF
#   data_path: directory of GRAPES GFS GMF original GRIB2 products.
#   python_script_name: python script file
#

set -x
set -e

#---------------
# SECTION: activate anaconda environment for NCL.
#----------------
source ./load_python_env.sh

#---------------
# python script name
#-----------------
file_name=${python_script_name}
echo $file_name

#------------------
# params
#------------------

YYYY=$(echo ${start_time} | cut -c1-4)
MM=$(echo ${start_time} | cut -c5-6)
DD=$(echo ${start_time} | cut -c7-8)
HH=$(echo ${start_time} | cut -c9-10)
echo ${YYYY} ${MM} ${DD} ${HH} ${forecast_hour}

#------------------
# run python script
#------------------
python ${file_name} \
     ${YYYY} ${MM} ${DD} ${HH} ${forecast_hour} \
     ${data_path}

# convert image
#./ps2gif_NoRotation_NoPlot.src