#!/usr/bin/python
import h5py
import sys
import numpy as np
import os
import re
import random
# find the path to my own python function:
cur_dir=os.getcwd()
sep='test_cases'
test_DIR=cur_dir.split(sep,1)[0]
scriptDIR=test_DIR+'compare_function'
sys.path.append(scriptDIR)

# import my own function for color and comparator
from mycomparator import *
from mycolor_fun import *



h5in_ori_filename = "Shear_Box_Full_small_Analysis_self_weight.h5.feioutput"
h5in_new_filename = "Shear_Box_Full_small_Analysis_self_weight_original.h5.feioutput"

h5_ori_file=h5py.File(h5in_ori_filename,"r")
h5_new_file=h5py.File(h5in_new_filename,"r")

eigen_all_ori=h5_ori_file['/Eigen_Mode_Analysis/frequencies'][()]
eigen_all_new=h5_new_file['/Eigen_Mode_Analysis/frequencies'][()]


min_tolerance=1e-08

print_header_flag=0
pass_fail_flag=1

for index, x in np.ndenumerate(eigen_all_ori):
	if ( np.float32(x) - np.float32(eigen_all_new[index]) ) > min_tolerance :
		pass_fail_flag=0
		if print_header_flag==0:
			print_header_flag=1
			print headwrongstep(), "================================================"
			print headwrongstep(), "|  Eigen_Analysis Frequencies have mismatches: |"
			print headwrongstep(), "================================================"
			print headwrongstep(), "|  Location    |Original_value |     New_value | "
		print headwrongstep(), "|",'{:12s}'.format(index) ,"|", '{:+e}'.format(x) ,"|",'{:+e}'.format(eigen_all_new[index]) ,"|"
	else:
		print "good"

