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

# analytic_solution = sys.argv[1]
# numeric_result = sys.argv[2]

analytic_solution = 'analytic_solution.txt'
numeric_result = 'numeric_result.txt'

analytic_sol = np.loadtxt(analytic_solution)
numeric_res  = np.loadtxt(numeric_result)

abs_error = abs(analytic_sol - numeric_res)

rel_error = abs_error/analytic_sol


analytic_sol = float(analytic_sol)
numeric_res = float(numeric_res)
rel_error = float(rel_error)

# print the results
case_flag=1
print headrun()     , "-----------Testing results-----------------"
print headstep()    ,'{0}  {1}     {2}   '.format('analytic_solution  ','numeric_result  ','error[%]')
print headOK()      ,'{0:+e}        {1:+e}        {2:+0.2f}    '.format(analytic_sol, numeric_res, rel_error )


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

