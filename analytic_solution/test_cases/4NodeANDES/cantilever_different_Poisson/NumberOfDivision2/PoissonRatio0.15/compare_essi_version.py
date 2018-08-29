#!/usr/bin/python
import h5py
import sys
import numpy as np
import os
# automatically find the script directory.
# script_dir=sys.argv[1]
cur_dir=os.getcwd()
sep='test_cases'
test_DIR=cur_dir.split(sep,1)[0]
scriptDIR=test_DIR+'compare_function'
sys.path.append(scriptDIR)

# import my own command line color function
# from essi_max_disp_fun import find_max_disp
from mycolor_fun import *

print headblankline()
print headblankline()
print headstart(), "Original ESSI version information:"


fin=open("original.log")
for line in fin:
    if 'Version' in line:
        print headstep(), line,
    if 'Compiled' in line:
        print headstep(), line,
    if 'Time Now' in line:
        print headstep(), line,
    if not line: break


print headblankline()
print headstart(), "New ESSI version information:"
fin=open("new.log")
for line in fin:
    if 'Version' in line:
        print headstep(), line,
    if 'Compiled' in line:
        print headstep(), line,
    if 'Time Now' in line:
        print headstep(), line,
    if not line: break

print headstart()
print headblankline()