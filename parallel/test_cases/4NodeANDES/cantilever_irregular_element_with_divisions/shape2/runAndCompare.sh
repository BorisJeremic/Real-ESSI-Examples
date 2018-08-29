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
    echo "Please provide the parallel-ESSI executable!"
    exit
fi

essiParallelExe=$1

pwd

mpirun -np 4 $essiParallelExe -f main.fei > terminal.log

python extract_numerical_solution.py *.feioutput

python compare_txt.py


