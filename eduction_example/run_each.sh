#!/bin/bash

current_dir=${PWD}
deepest_dir_array=( $(find . -type d -links 2 ) )
# deepest_dir_array=( $(find . -type d -links 3 ) )

for element in $(seq 0 $((${#deepest_dir_array[@]} - 1)))
do
	cd ${current_dir}/"${deepest_dir_array[$element]}"
	
	if [ -f $PWD/require_parallel.hold ] # check if require essi_parallel
		then
			if hash essi_parallel 2>/dev/null; then # check if essi_parallel is available
			    mpirun -np 4 essi_parallel -f main.fei
			else
			    echo "Example 27NodeBrick_DRM_3D require essi_parallel but it's not installed. Skip this example." 
			fi
	else
		essi -f main.fei
	fi

done