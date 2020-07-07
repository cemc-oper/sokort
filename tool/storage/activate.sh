#!/bin/bash
#-------------------------------------
# activate environment for Storage Server
#-------------------------------------

set -x
source /home/wangdp/start_anaconda3.sh
conda activate nwpc-data
export NWPC_GRAPHICS_CONFIG="/home/wangdp/project/graphics/nwpc-graphics/tool/storage/config/config.yaml"

set +x