#!/usr/bin/env bash

#---------------
# SECTION: activate anaconda environment for NCL.
#----------------
#export PYENV_ROOT="$HOME/.pyenv"
#export PATH="$PYENV_ROOT/bin:$PATH"
#eval "$(pyenv init -)"
#eval "$(pyenv virtualenv-init -)"
#
#pyenv local anaconda3-2019.10
source /home/wangdp/.pyenv/versions/anaconda3-2019.10/etc/profile.d/conda.sh
conda activate ncl_stable
