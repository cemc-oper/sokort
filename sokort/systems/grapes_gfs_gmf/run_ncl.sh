#!/usr/bin/env bash
# Run ncl script to draw graph for GRAEPS GFS GMF.
#
# Prepare:
#   1. enter a work directory
#   2. create grapes_meso_date
#   3. link and copy scripts
#
# Environment Variables:
#   GEODIAG_ROOT
#   GEODIAG_TOOLS
#   GRAPHIC_PRODUCT_LIB_ROOT
#   FORECAST_DATA_FORMAT
#   FORECAST_DATA_CENTER
#
# Parameters should be passed as environment variables.
#   start_time: YYYYMMDDHH
#   min_forecast_time: FFF
#   max_forecast_time: FFF
#   forecast_time_interval: forecast time interval, required by some graph.
#   data_path: directory of GRAPES GFS GMF original GRIB2 products.
#   ncl_script_name: ncl script file
#

set -x
set -e

#---------------
# SECTION: activate anaconda environment for NCL.
#----------------
source ./load_env.sh

#---------------
# ncl script name
#-----------------
file_name=${ncl_script_name}  # GFS_GRAPES_PWAT_SFC_AN_AEA.ncl
echo $file_name

#----------------
# params
#------------------
initial_time=${start_time}
min_forecast_time=${min_forecast_time}
max_forecast_time=${max_forecast_time}
forecast_time_interval=${forecast_time_interval}
graphic_output_home=./  # path of pic

#------------------
# run ncl script
#------------------
ncl initial_time=${initial_time} \
     min_forecast_time=${min_forecast_time} \
     max_forecast_time=${max_forecast_time} \
     forecast_time_interval=${forecast_time_interval} \
     data_path=\"${data_path}\" \
     graphic_output_home=\"${graphic_output_home}\" \
     ${file_name}

# convert image
./ps2gif_NoRotation_NoPlot.src