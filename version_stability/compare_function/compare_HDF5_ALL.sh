#!/bin/bash
# Author: Yuan Feng
# Email : ofeng@ucdavis.edu
# Date  : Mon Jun 27 22:53:38 PDT 2016

# This script will go over each leaf directory and 
# compare all the stress, strain, and displacements in HDF5 results.
# This script should be called one directory upper.
current_dir=${PWD}
compare_function_dir=${PWD}/compare_function/
essi_dir="$(dirname "$current_dir")"

cd ${current_dir}
# find and list all the deepest(leaf) directories.
deepest_dir_array=( $(find ./test_cases/ -type d -links 2 ) )

# loop over the leaf directories.
for element in $(seq 0 $((${#deepest_dir_array[@]} - 1)))
do
    # ===================================================================
    # Preparation:
    # Copy the comparator function 
    # ===================================================================
    cd ${current_dir}
    cp ./compare_function/status.py ${current_dir}/"${deepest_dir_array[$element]}"
    cp ./compare_function/compare_essi_version.py ${current_dir}/"${deepest_dir_array[$element]}"
    # =====================================================
    # Copy the default Comparator if no compare_HDF5_ALL.py is provided. 
    # =====================================================
    cd ${current_dir}/"${deepest_dir_array[$element]}"
    # =====================================================
    if [ -f $PWD/compare_HDF5_ALL.py ]
        then
            :
    else
       cp ${compare_function_dir}/compare_HDF5_ALL.py ${current_dir}/"${deepest_dir_array[$element]}"
    fi
    # =====================================================


    # ===================================================================
    # Execution:
    # ===================================================================
    cd ${current_dir}/"${deepest_dir_array[$element]}"
    # Print the relative path in advance
    python status.py 
    # compare the all the stress, strain, and displacements
    make -f run_and_compare compare_HDF5_ALL
done

# print the ESSI verision information in the log 
flag=1
# call once only
for element in $(seq 0 $((${#deepest_dir_array[@]} - 1)))
do
    cd ${current_dir}/"${deepest_dir_array[$element]}"
    if [[ ${flag} -eq 1 ]]; then
        python compare_essi_version.py
    fi
    break
done

















# legacy script backup
    # cd ${current_dir}/"${deepest_dir_array[$element]}"
    # rm original.log
    # mv new.log original.log
    # # sed -i "s/node\.fei/add_node.include/" main.fei
    # # sed -i "s/element\.fei/add_element.include/" main.fei
    # # sed -i "s/constraint\.fei/add_constraint.include/" main.fei
    # # sed -i "s/elementLT\.fei/add_elementLT.include/" main.fei
    # sed -i "s/add_add_node\.include/add_node.include/" main.fei