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


disp_pass_or_fail=h5diff_disp(h5_result_ori,h5_result_new)
Gauss_pass_or_fail = 1
try:
	Gauss_pass_or_fail=h5diff_Gauss_output(h5_result_ori,h5_result_new)
except KeyError:
	pass

Element_Output_pass_or_fail = 1
try:
	Element_Output_pass_or_fail=h5diff_Element_output(h5_result_ori,h5_result_new)
except KeyError:
	pass

if disp_pass_or_fail and Gauss_pass_or_fail and Element_Output_pass_or_fail:
	print headOK(), "All hdf5 results are the same."
	print headOKCASE(),"-----------Done this case!-----------------"
else:
	if disp_pass_or_fail==0:
		print headFailed(),"-----------Displacement has mismatches!-----------------"
	if Gauss_pass_or_fail==0:
		print headFailed(),"-----------StressStrain has mismatches!-----------------"
	if Element_Output_pass_or_fail==0:
		print headFailed(),"-----------Element output has mismatches!-----------------"	
# # The allowable tolerance between the ori_vals and new_vals values.
# tolerance=1e-5
# machine_epsilon=1e-16
# ori_vals=[]
# new_vals=[]

# ori_vals.append(find_max_disp(h5_result_ori,0))
# new_vals.append(find_max_disp(h5_result_new,0))

# # if multiple steps, compare the max_disp of random steps 
# Nstep = find_disp_Nstep(h5_result_ori)
# if Nstep>5 :
# 	for i in xrange(1,4):
# 		test_step=random.randint(1,Nstep-1)
# 		ori_vals.append(find_max_disp(h5_result_ori,test_step))
# 		new_vals.append(find_max_disp(h5_result_new,test_step))

# # calculate the errors
# errors=[]
# for index, x in enumerate(ori_vals):
# 	if(abs(x))>machine_epsilon:
# 		errors.append(abs((new_vals[index]-x)/x))
# 	else:
# 		errors.append(machine_epsilon)

# # compare and form the flags
# flags=[]
# for item in errors:
# 	if abs(item)<tolerance:
# 		flags.append('pass')
# 	else:
# 		flags.append('failed')

# # print the results
# case_flag=1
# print headrun()     , "-----------Testing results-----------------"
# print headstep()    ,'{0}    {1}     {2}   {3}'.format('back_value  ','new_value  ','error ','flag')
# for index, x in enumerate(errors):
# 	if(abs(x)<tolerance):
# 		print headOK()      ,'{0:e}   {1:e}     {2:0.2f}     {3}'.format(ori_vals[index],new_vals[index], x, flags[index] )
# 	else:
# 		case_flag=0
# 		print headFailed()  ,'{0:e}   {1:e}     {2:0.2f}     {3}'.format(ori_vals[index],new_vals[index], x, flags[index] )

# if(case_flag==1):
# 	print headOKCASE(),"-----------Done this case!-----------------"
	






# legacy backup

# automatically find the script directory.
# sys.path.append("/home/yuan/Dropbox/3essi_self_verification/test_suite/scripts" )
# script_dir=sys.argv[1]

# print headstart()   , "Running test cases..."
# print headlocation(), os.path.dirname(os.path.abspath(__file__))


# file_in=open("ori_vals_values.txt","r")
# Input the 1st line, which is the ori_vals value.
# ori_vals= float(file_in.readline())
# Input the 2nd line, which is the HDF5 output filename.
# new_vals=find_max_disp(file_in.readline());
# file_in.close()