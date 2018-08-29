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
h5_result_bak = sys.argv[1]
h5_result_new = sys.argv[2]




# The allowable tolerance between the bak_vals and new_vals values.
tolerance=1e-5
machine_epsilon=2.22e-16
bak_vals=[]
new_vals=[]

bak_vals.append(find_max_disp(h5_result_bak,0))
new_vals.append(find_max_disp(h5_result_new,0))

# if multiple steps, compare the max_disp of random steps 
Nstep = find_disp_Nstep(h5_result_bak)
if Nstep>5 :
	for i in xrange(1,4):
		test_step=random.randint(1,Nstep-2)
		bak_vals.append(find_max_disp(h5_result_bak,test_step))
		new_vals.append(find_max_disp(h5_result_new,test_step))

# calculate the errors
errors=[]
for index, x in enumerate(bak_vals):
	if(abs(x))>machine_epsilon:
		errors.append(abs((new_vals[index]-x)/x))
	else:
		errors.append(machine_epsilon)

# compare and form the flags
flags=[]
for item in errors:
	if abs(item)<tolerance:
		flags.append('pass')
	else:
		flags.append('failed')

# print the results
case_flag=1
print headrun()     , "-----------Testing results-----------------"
print headstep()    ,'{0}  {1}     {2}    {3}'.format('Original_value  ','New_value ','error[%]','flag')
for index, x in enumerate(errors):
	if(abs(x)<tolerance):
		print headOK()      ,'{0:+e}   {1:+e}     {2:+0.2f}      {3}'.format(bak_vals[index],new_vals[index], x, flags[index] )
	else:
		case_flag=0
		print headFailed()  ,'{0:+e}   {1:+e}     {2:+0.2f}      {3}'.format(bak_vals[index],new_vals[index], x, flags[index] )

if(case_flag==1):
	print headOKCASE(),"-----------Done this case!-----------------"
	






# legacy backup


# find . -name 'element.fei' -exec bash -c 'mv $0 ${0/element.fei/add_element.include}' {} \;
# find . -name 'constraint.fei' -exec bash -c 'mv $0 ${0/constraint.fei/add_constraint.include}' {} \;
# find . -name 'node.fei' -exec bash -c 'mv $0 ${0/node.fei/add_node.include}' {} \;
# find . -name 'add_node.fei' -exec bash -c 'mv $0 ${0/add_node.fei/add_node.include}' {} \;
# find . -name 'elementLT.fei' -exec bash -c 'mv $0 ${0/elementLT.fei/add_elementLT.include}' {} \;

# sed -i "s/node\.fei/add_node.include/" main.fei
# sed -i "s/add_node\.fei/add_node.include/" main.fei
# sed -i "s/element\.fei/add_element.include/" main.fei
# sed -i "s/elementLT\.fei/add_elementLT.include/" main.fei
# sed -i "s/constraint\.fei/add_constraint.include/" main.fei


# find . -name '*_bak.h5.feioutput' -exec bash -c 'mv $0 ${0/\_bak.h5.feioutput/\_original\.h5.feioutput}' {} \;

