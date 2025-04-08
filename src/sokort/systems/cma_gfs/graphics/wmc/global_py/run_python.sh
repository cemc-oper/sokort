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
#   figure_path:
#   python_script_name: python script file
#   plot_name:
#

set -x
set -e

#---------------
# SECTION: activate anaconda environment for NCL.
#----------------
source ./load_python_env.sh

set -x
#------------------
# params
#------------------
file_name=${python_script_name}
cat <<EOF
file name: ${file_name}
start time: ${start_time}
forecast_hour: ${forecast_hour}
data path: ${data_path}
figure path: ${figure_path}
plot name: ${plot_name}
EOF

#------------------
# run python script
#------------------
python ${file_name} ${start_time} ${forecast_hour} ${data_path} ${figure_path} ${plot_name}
