#!/usr/bin/env bash
# Run ncl script to draw graph for GRAEPS MESO 9KM.
#
# Prepare:
#   1. enter a work directory
#   2. create grapes_meso_date
#   3. link and copy scripts
#
# Environment Variables:
#   GEODIAG_ROOT
#   GEODIAG_TOOLS
#
# Parameters should be passed as environment variables.
#   start_time: YYYYMMDDHH
#   data_path: directory of GRAPES GFS GMF original GRIB2 products.
#   ncl_script_name: ncl script file
#
set -x
set +x
set -e

#---------------
# SECTION: activate anaconda environment for NCL.
#----------------
source ./load_env.sh

#---------------
# ncl script name
#-----------------
file_name=${ncl_script_name}
echo $file_name

#-------------
# SECTION: link and copy script
#cp ${script_dir}/ps2gif_NoRotation_NoPlot.scr .

ncl_lib=${script_dir}/ncllib
ln -sf ${ncl_lib}/gsn_code.ncl .
ln -sf ${ncl_lib}/gsn_csm.ncl .
ln -sf ${ncl_lib}/GFS_T639.ncl .
ln -sf ${ncl_lib}/cn_map_function.ncl .
ln -sf ${ncl_lib}/common.ncl .
ln -sf ${ncl_lib}/data_file_name.ncl .
ln -sf ${ncl_lib}/ncl_variable.ncl .
ln -sf ${ncl_lib}/region.csv .
ln -sf ${ncl_lib}/contributed.ncl .
ln -sf ${ncl_lib}/lib .

#------------------------------
# link and rename data files
#------------------------------
ln -sf ${data_path}/* .
rename tcgra gra ./*.grb2

#------------------
# run ncl script
#------------------
ncl ./${ncl_script_name}

# convert image
#./ps2gif_NoRotation_NoPlot.scr