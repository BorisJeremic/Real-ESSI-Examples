#! /usr/bin/env python

import h5py
import scipy as sp
import numpy as np 
import time
import pickle
import sys
import math
import cmath

from os import path
import os, sys

sys.path.append('../../')

from mycolor_fun import *
cwd = os.getcwd()

abs_error_limit = 0.05; 
rel_error_limit = 0.05; 

benchmark_PC_coef = h5py.File('PC_RF1_verified.hdf5')['PC Coefficients']
test_PC_coef = h5py.File('PC_RF1.hdf5')['PC Coefficients']

# print benchmark_PC_coef.shape 

check_component1 = benchmark_PC_coef[1, 1]; 
component1 = test_PC_coef[1, 1]; 

check_component2 = benchmark_PC_coef[2, 3]; 
component2 = test_PC_coef[2, 3]; 

abs_error_x = abs(component1-check_component1); 
abs_error_z = abs(component2-check_component2); 

rel_error_x = abs_error_x/abs(check_component1); 
rel_error_z = abs_error_z/abs(check_component2); 

case_flag = 1; 

print headrun() , "Test directory:: ", cwd;

print headrun() , "-----------Testing results-----------------"; 

print headstep()   ,'{0}  {1}  {2}  {3}'.format('analytic_solution  ','numeric_result  ','absolute error ', 'relative error[%]'); 

if ((abs_error_x < abs_error_limit) and (rel_error_x < rel_error_limit)):

	print headOK() ,'{0:+e}        {1:+e}        {2:+2.3f}            {3:+2.2f} '.format(check_component1, component1, abs_error_x, 100*rel_error_x); 
		
else:

	print headFailed(), '{0:+e}        {1:+e}        {2:+2.3f}            {3:+2.2f} '.format(check_component1, component1, abs_error_x, 100*rel_error_x);

	case_flag = 0; 

if ((abs_error_z < abs_error_limit) and (rel_error_z < rel_error_limit)):

	print headOK() ,'{0:+e}        {1:+e}        {2:+2.3f}            {3:+2.2f} '.format(check_component2, component2, abs_error_z, 100*rel_error_z); 
		
else:

	print headFailed(), '{0:+e}        {1:+e}        {2:+2.3f}            {3:+2.2f} '.format(check_component2, component2, abs_error_z, 100*rel_error_z);

	case_flag = 0; 

if case_flag ==1 :
	
	print headOKCASE(),"-----------Done this case!-----------------"






