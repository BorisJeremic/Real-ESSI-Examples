#!/bin/bash
# ***************************************************************************************
# Dynamic Test Cases:
# Since dynamic test cases require more postprocessing, 
# they are placed in this separate folder. 
# The analytic solutions of damping ratios and period shift are calcualted.
# The ESSI results of damping ratios and period shift are measured. 
# ***************************************************************************************

# This script will run all kinds of parameters and time-steps in both Newmark and HHT.

for folder in */;
do
	cd ${folder}
	bash runall.sh
	cd ..
done