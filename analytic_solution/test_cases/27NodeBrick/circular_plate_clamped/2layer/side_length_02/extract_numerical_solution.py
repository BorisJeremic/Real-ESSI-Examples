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

h5_result_file = sys.argv[1]
# h5_result_file = 't_Fz.h5.feioutput'

disp_at_target_point = find_max_disp(h5_result_file,1)

# Write results to file
f = open('numeric_result.txt','w')
f.write('%.3e' % disp_at_target_point)
f.close()
