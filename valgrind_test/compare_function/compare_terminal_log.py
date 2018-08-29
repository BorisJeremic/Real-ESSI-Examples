#!/usr/bin/python
import h5py
import sys
import numpy as np
import os
# automatically find the script directory.
cur_dir=os.getcwd()
sep='test_cases'
test_DIR=cur_dir.split(sep,1)[0]
scriptDIR=test_DIR+'compare_function'
sys.path.append(scriptDIR)
# import my own command line color function
from mycolor_fun import *



f_original=open("original.log")
f_new=open("new.log")

log_diff = set(f_original).symmetric_difference(f_new)

bad_words=["[ETA:"]

filtered_log_diff=[]
for line in log_diff:
	if not any(bad_word in line for bad_word in bad_words):
		filtered_log_diff.append(line)

# Version : --NOT FROM GIT REPO--
# Compiled: Jun 26 2016 at 23:18:45
# Time Now: Jun 27 2016 at 23:22:24
# If the three lines above do not match, len(log_diff):=6 .
# So if we have more than 6 differences. This means some other lines have mismatch. 
if len(filtered_log_diff) > 6:
    print headFailed() , "Real ESSI execution terminal output has mismatch!"
    print headFailed() , "Maybe some debug purpose messages are printing!"
else:
	print headOKCASE() 

# print headstart() 





# Remove the line containing this string "[ETA:". 
# Because each the time of ETA in terminal log is different.

# Transient Analysis: Step Number is : 2 out of 15 [ETA: 0 h, 1 m, 10 s]		Transient Analysis: Step Number is : 2 out of 15 [ETA: 0 h, 0 m, 52 s]
# Transient Analysis: Step Number is : 3 out of 15 [ETA: 0 h, 0 m, 51 s]		Transient Analysis: Step Number is : 3 out of 15 [ETA: 0 h, 0 m, 48 s]
# Transient Analysis: Step Number is : 4 out of 15 [ETA: 0 h, 0 m, 43 s]		Transient Analysis: Step Number is : 4 out of 15 [ETA: 0 h, 0 m, 41 s]
# Transient Analysis: Step Number is : 5 out of 15 [ETA: 0 h, 0 m, 40 s]		Transient Analysis: Step Number is : 5 out of 15 [ETA: 0 h, 0 m, 36 s]
# Transient Analysis: Step Number is : 6 out of 15 [ETA: 0 h, 0 m, 35 s]		Transient Analysis: Step Number is : 6 out of 15 [ETA: 0 h, 0 m, 33 s]
# Transient Analysis: Step Number is : 7 out of 15 [ETA: 0 h, 0 m, 31 s]		Transient Analysis: Step Number is : 7 out of 15 [ETA: 0 h, 0 m, 30 s]
# Transient Analysis: Step Number is : 8 out of 15 [ETA: 0 h, 0 m, 28 s]		Transient Analysis: Step Number is : 8 out of 15 [ETA: 0 h, 0 m, 26 s]
# Transient Analysis: Step Number is : 9 out of 15 [ETA: 0 h, 0 m, 24 s]		Transient Analysis: Step Number is : 9 out of 15 [ETA: 0 h, 0 m, 23 s]
# Transient Analysis: Step Number is : 10 out of 15 [ETA: 0 h, 0 m, 21 s]		Transient Analysis: Step Number is : 10 out of 15 [ETA: 0 h, 0 m, 20 s]
# Transient Analysis: Step Number is : 11 out of 15 [ETA: 0 h, 0 m, 17 s]		Transient Analysis: Step Number is : 11 out of 15 [ETA: 0 h, 0 m, 16 s]
# Transient Analysis: Step Number is : 12 out of 15 [ETA: 0 h, 0 m, 13 s]		Transient Analysis: Step Number is : 12 out of 15 [ETA: 0 h, 0 m, 13 s]
# Transient Analysis: Step Number is : 13 out of 15 [ETA: 0 h, 0 m, 10 s]		Transient Analysis: Step Number is : 13 out of 15 [ETA: 0 h, 0 m, 10 s]
# Transient Analysis: Step Number is : 14 out of 15 [ETA: 0 h, 0 m, 7 s]		Transient Analysis: Step Number is : 14 out of 15 [ETA: 0 h, 0 m, 6 s]
# Transient Analysis: Step Number is : 15 out of 15 [ETA: 0 h, 0 m, 3 s]		Transient Analysis: Step Number is : 15 out of 15 [ETA: 0 h, 0 m, 3 s]