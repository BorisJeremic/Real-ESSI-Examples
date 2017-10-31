#!/bin/bash

python clean_dataset.py

essi -f deconvolution2DRM.fei

# python plot.py decon_at_depth_60_acc.txt
# python plot.py decon_at_depth_60_vel.txt
# python plot.py decon_at_depth_60_dis.txt

essi -f DRM_simulation.fei

python extract_wave.py

python plot2.py origin_northridge_acc.dat top_acc.txt

