#!/bin/bash

# This script only change the file name.

cur_dir=${PWD}
scrip_dir=${PWD}/compare_function/
# find and list all the deepest(leaf) directories.
deepest_dir_array=( $(find ./test_cases/ -type d -links 2 ) )

for element in $(seq 0 $((${#deepest_dir_array[@]} - 1)))
do
    cd ${cur_dir}
    cp ./compare_function/update_status.py ${cur_dir}/"${deepest_dir_array[$element]}"    
    cd ${cur_dir}/"${deepest_dir_array[$element]}"
    
    # print the directory
    python update_status.py 
    # make -f run_and_compare run_essi
    # rm the old hdf5 results
    rm -rf *_original.h5.feioutput
    # rename the current hdf5 results to old hdf5 results
    find . -name '*.h5.feioutput' -exec bash -c 'mv $0 ${0/\.h5.feioutput/\_original\.h5.feioutput}' {} \;

    # update the log
    mv new.log original.log
    
    rm update_status.py 
done




