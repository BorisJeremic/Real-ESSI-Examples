#!/bin/bash
# ***************************************************************************************
# Dynamic Test Cases:
# Since dynamic test cases require more postprocessing, 
# they are placed in this separate folder. 
# The analytic solutions of damping ratios and period shift are calcualted.
# The ESSI results of damping ratios and period shift are measured. 
# ***************************************************************************************

# This script will run all kinds of parameters and time-steps in both Newmark and HHT.

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
    echo "Please provide the ESSI executable!"
    exit
fi

essiExe=$1

for folder in */;
do
	cd ${folder}
	bash runall.sh $essiExe
	cd ..
done