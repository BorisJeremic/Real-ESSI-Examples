#!/bin/bash

# This script only change the file name.

cur_dir=${PWD}
scrip_dir=${PWD}/compare_function/
# find and list all the deepest(leaf) directories.
deepest_dir_array=( $(find ./test_cases/ -type d -links 2 ) )

for element in $(seq 0 $((${#deepest_dir_array[@]} - 1)))
do
    cd ${cur_dir}/"${deepest_dir_array[$element]}"
    sed -i 's/linear_elastic_isotropic_3d/linear_elastic_isotropic_3d_LT/' main.fei || true

done




