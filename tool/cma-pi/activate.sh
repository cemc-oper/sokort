#!/bin/bash
#-------------------------------------
# activate environment for CMA-PI
#-------------------------------------

set -x
source /g1/u/wangdp/start_anaconda3.sh
conda activate nwpc-data
export NWPC_GRAPHICS_CONFIG="/g11/wangdp/project/work/graphics/nwpc-graphics/sokort/tool/cma-pi/config/config.yaml"

#module load mathlib/ncl_ncarg/6.5.0/gnu

set +x