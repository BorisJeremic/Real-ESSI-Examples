#!/bin/bash
# Author: Yuan Feng
# Email : ofeng@ucdavis.edu
# Date  : Mon Jun 27 22:53:38 PDT 2016

# This script will go over each leaf directory and 
# compare max displacements in HDF5 results.
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
    cp ./compare_function/compare_HDF5_max.py ${current_dir}/"${deepest_dir_array[$element]}"

    # ===================================================================
    # Execution:
    # ===================================================================
    cd ${current_dir}/"${deepest_dir_array[$element]}"
    # Print the relative path in advance
    python status.py 
    # compare the max displacement of HDF5 output.
    make -f run_and_compare compare_HDF5_max
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
    
    # find . -name 'element.fei' -exec bash -c 'mv $0 ${0/element.fei/add_element.include}' {} \;
    # find . -name 'constraint.fei' -exec bash -c 'mv $0 ${0/constraint.fei/add_constraint.include}' {} \;
    # find . -name 'node.fei' -exec bash -c 'mv $0 ${0/node.fei/add_node.include}' {} \;
    # find . -name 'add_node.fei' -exec bash -c 'mv $0 ${0/add_node.fei/add_node.include}' {} \;
    # find . -name 'elementLT.fei' -exec bash -c 'mv $0 ${0/elementLT.fei/add_elementLT.include}' {} \;

    # sed -i "s/node\.fei/add_node.include/" main.fei
    # sed -i "s/add_node\.fei/add_node.include/" main.fei
    # sed -i "s/element\.fei/add_element.include/" main.fei
    # sed -i "s/elementLT\.fei/add_elementLT.include/" main.fei
    # sed -i "s/constraint\.fei/add_constraint.include/" main.fei


    # find . -name '*_bak.h5.feioutput' -exec bash -c 'mv $0 ${0/\_bak.h5.feioutput/\_original\.h5.feioutput}' {} \;
