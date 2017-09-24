#!/bin/bash
# ********************************************************************
# Author: Yuan Feng
# Date: Sun Sep 24 12:00:55 PDT 2017
# Comments: 
# 	1. This file is used to cooperate with the automatic verification
#      script in Real-ESSI root folder. 
#   2. When run_all_verification is used in Real-ESSI root folder,
#      Real-ESSI-Examples will be downloaded. And this script will
#      be called to run each example.
# ********************************************************************

current_dir=${PWD}
deepest_dir_array=( $(find . -type d -links 2 ) )
# deepest_dir_array=( $(find . -type d -links 3 ) )

for element in $(seq 0 $((${#deepest_dir_array[@]} - 1)))
do
	cd ${current_dir}/"${deepest_dir_array[$element]}"
	echo "Testing Location:"
	echo $PWD
	if [ -f $PWD/require_parallel.hold ] # check if require essi_parallel
		then
			if hash essi_verify_parallel 2>/dev/null; then # check if essi_verify_parallel is available
			    mpirun -np 4 essi_verify_parallel -f main.fei
			else
			    echo "Example 27NodeBrick_DRM_3D require essi_parallel but it's not installed. Skip this example." 
			fi
	else
		if hash essi_verify 2>/dev/null; then # check if essi_verify is available
		    essi_verify -f main.fei
		fi
	fi

done