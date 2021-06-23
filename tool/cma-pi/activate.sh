#!/bin/bash
#-------------------------------------
# activate environment for CMA-PI
# Use python environment Anaconda3 installed by wangdp.
#-------------------------------------

set -x
source /g1/u/wangdp/start_anaconda3.sh
conda activate py39-dev
SOKORT_ROOT="/g11/wangdp/project/work/graphics/nwpc-graphics/sokort"
export NWPC_GRAPHICS_CONFIG="${SOKORT_ROOT}/tool/cma-pi/config/config.yaml"

# module load mathlib/ncl_ncarg/6.5.0/gnu

set +x