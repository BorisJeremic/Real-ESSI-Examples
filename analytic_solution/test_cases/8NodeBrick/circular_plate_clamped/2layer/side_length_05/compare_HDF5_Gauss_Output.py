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

# the real essi hdf5 results
h5_result_new = sys.argv[1]
h5_result_ori = sys.argv[2]


Gauss_pass_or_fail = 1
try:
	Gauss_pass_or_fail=h5diff_Gauss_output(h5_result_ori,h5_result_new)
except KeyError:
	pass

if Gauss_pass_or_fail:
	print headOK(), "All hdf5 results are the same."
	print headOKCASE(),"-----------Done this case!-----------------"
else:
	if Gauss_pass_or_fail==0:
		print headFailed(),"-----------StressStrain has mismatches!-----------------"

