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
#

set -x
set -e

#---------------
# SECTION: activate anaconda environment for NCL.
#----------------
echo "Load env script path is: ${load_env_script_name}"
source ${load_env_script_name}

#---------------
# ncl script name
#-----------------
file_name=${ncl_script_name}  # GFS_GRAPES_PWAT_SFC_AN_AEA.ncl
echo $file_name

#----------------
# params
#------------------


#------------------
# run ncl script
#------------------
ncl ${file_name}

# convert image
#./ps2gif_NoRotation_NoPlot.src