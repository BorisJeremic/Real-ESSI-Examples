#!/bin/bash

if [ "$1" != "" ]; then
    if command -v $1 1>/dev/null 2>&1; then
        echo " "
        # echo "$1 is available"
    else
        echo "ERROR! User input argument $1 is not available" 
        echo "$1 is not available" 
        exit
    fi
else
    echo "ERROR! Argument 1 is empty! "
    echo "Please provide the sequential ESSI executable!"
    exit
fi


if [ "$2" == "" ]; then

    echo "ERROR! Argument 2 is empty! "
    echo "Please provide the parallel ESSI executable!"
    exit
fi


essiExe=$1

parallelEssiExe=$2

pwd

$essiExe -f 3D_wave.fei

rm -rf *.feioutput

rm -rf vtk_errors.txt

mpirun -np 10 $parallelEssiExe -f 2D_free_field_model_analysis.fei

python comparison.py


