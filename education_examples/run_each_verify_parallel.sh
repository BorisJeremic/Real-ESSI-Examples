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

if [ "$1" != "" ]; then
    if command -v $1 2>/dev/null; then
        echo "$1 is available"
    else
        echo "ERROR! User input argument $1 is not available" 
        echo "$1 is not available" 
        exit
    fi
else
    echo "ERROR! Argument 1 is empty! "
    echo "Please provide the parallel-ESSI executable!"
    exit
fi

essiParallelExe=$1

# for path in 'find -mindepth 1 -maxdepth 2 -type d'
for path in `find -mindepth 1 -maxdepth 10 -type d` 
do
    cd $current_dir/$path
    if [ -f main.fei ]; then
    	echo "Testing Location:"
    	echo $PWD
    	if [ -f $PWD/require_parallel.hold ] # check if require essi_parallel
    		then
			    mpirun -np 4 $essiParallelExe -f main.fei
    	else
            echo " "
    	fi
    fi
done

