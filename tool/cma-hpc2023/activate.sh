#!/bin/bash
#-------------------------------------
# activate development environment for CMA-HPC2023
# Use python environment Miniconda3 installed by wangdp@CEMC.
#-------------------------------------

set -x
source /g1/u/wangdp/start_miniconda3.sh
conda activate py312-cedar-dev
SOKORT_ROOT="/g4/wangdp/project/work/graphics/cemc-sokort/sokort"
export NWPC_GRAPHICS_CONFIG="${SOKORT_ROOT}/tool/cma-hpc2023/config/config.yaml"

set +x