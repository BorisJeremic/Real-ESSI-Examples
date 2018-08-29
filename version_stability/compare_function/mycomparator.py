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

epsilon = 1e-10;

# import my own function for color and comparator
from mycomparator import *
from mycolor_fun import *

epsilon = 1e-10 

def h5diff_disp(h5in_ori_filename,h5in_new_filename):
	# h5in_ori_filename = "imposed_000.h5.feioutput"
	# h5in_new_filename = "imposed_111.h5.feioutput"

	h5_ori_file=h5py.File(h5in_ori_filename,"r")
	h5_new_file=h5py.File(h5in_new_filename,"r")
	# print(h5_ori_file)
	# print(h5_new_file)
	# [()] is a must. Otherwise, result will be a dataset, not an array.
	disp_all_ori_c=h5_ori_file['/Model/Nodes/Generalized_Displacements'][()]
	disp_all_new_c=h5_new_file['/Model/Nodes/Generalized_Displacements'][()]
	# delete the last column
	disp_all_ori=disp_all_ori_c[:,:]
	disp_all_new=disp_all_new_c[:,:]
	# tolerance setting for the overflow and underflow.
	max_rel_tolerance=1e-03
	max_tolerance=1e-03
	print_header_flag=0
	pass_fail_flag=1
	for index, x in np.ndenumerate(disp_all_ori):
		if abs(( np.float32(x) - np.float32(disp_all_new[index]) ) / (np.float32(x) + epsilon) )> max_rel_tolerance or abs( np.float32(x) - np.float32(disp_all_new[index]) ) > max_tolerance:
			pass_fail_flag=0
			if print_header_flag==0:
				print_header_flag=1
				print headwrongstep(), "================================================"
				print headwrongstep(), "|  Generalized_Displacements have mismatches:  | "
				print headwrongstep(), "================================================"
				print headwrongstep(), "|  Location    |Original_value |     New_value | "
			print headwrongstep(), "|",'{:12s}'.format(index) ,"|", '{:+e}'.format(x) ,"|",'{:+e}'.format(disp_all_new[index]) ,"|"

	# print "================================================"

	return pass_fail_flag

def h5diff_Gauss_output(h5in_ori_filename,h5in_new_filename):
	h5_ori_file=h5py.File(h5in_ori_filename,"r")
	h5_new_file=h5py.File(h5in_new_filename,"r")
	outputs_all_ori_c=h5_ori_file['/Model/Elements/Gauss_Outputs'][()]
	outputs_all_new_c=h5_new_file['/Model/Elements/Gauss_Outputs'][()]

	# delete the last column
	outputs_all_ori=outputs_all_ori_c[:,:]
	outputs_all_new=outputs_all_new_c[:,:]
	# tolerance setting for the overflow and underflow.
	max_rel_tolerance=1e-03
	max_tolerance=1e-03
	print_header_flag=0
	pass_fail_flag=1
	for index, x in np.ndenumerate(outputs_all_ori):
		if abs(( np.float32(x) - np.float32(outputs_all_new[index]) ) / (np.float32(x) + epsilon) )> max_rel_tolerance or abs( np.float32(x) - np.float32(outputs_all_new[index]) ) > max_tolerance:
			pass_fail_flag=0
			if print_header_flag==0:
				print_header_flag=1
				print headwrongstep(),"================================================"
				print headwrongstep(),"|Gauss outputs (stress strain) have mismatches: "
				print headwrongstep(),"================================================"
				print headwrongstep(),"|  Location    |Original_value |     New_value | "
			# print "|",index,"|", x ,"|", outputs_all_new[index],"|"
			print headwrongstep(), "|",'{:12s}'.format(index) ,"|", '{:+e}'.format(x) ,"|",'{:+e}'.format(outputs_all_new[index]) ,"|"
	return pass_fail_flag

def h5diff_Element_output(h5in_ori_filename,h5in_new_filename):
	h5_ori_file=h5py.File(h5in_ori_filename,"r")
	h5_new_file=h5py.File(h5in_new_filename,"r")
	outputs_all_ori_c=h5_ori_file['/Model/Elements/Element_Outputs'][()]
	outputs_all_new_c=h5_new_file['/Model/Elements/Element_Outputs'][()]

	# delete the last column
	outputs_all_ori=outputs_all_ori_c[:,:]
	outputs_all_new=outputs_all_new_c[:,:]
	# tolerance setting for the overflow and underflow.
	max_rel_tolerance=1e-03
	max_tolerance=1e-03
	print_header_flag=0
	pass_fail_flag=1
	for index, x in np.ndenumerate(outputs_all_ori):
		if abs(( np.float32(x) - np.float32(outputs_all_new[index]) ) / (np.float32(x) + epsilon) )> max_rel_tolerance or abs( np.float32(x) - np.float32(outputs_all_new[index]) ) > max_tolerance:
			pass_fail_flag=0
			if print_header_flag==0:
				print_header_flag=1
				print headwrongstep(),"================================================"
				print headwrongstep(),"|Element outputs have mismatches:               "
				print headwrongstep(),"================================================"
				print headwrongstep(),"|  Location    |Original_value |     New_value | "
			# print "|",index,"|", x ,"|", outputs_all_new[index],"|"
			print headwrongstep(), "|",'{:12s}'.format(index) ,"|", '{:+e}'.format(x) ,"|",'{:+e}'.format(outputs_all_new[index]) ,"|"
	return pass_fail_flag

def find_max_disp(h5in_file_name,_step):
	h5file_in=h5py.File(h5in_file_name,"r")
	# [()] is a must. Otherwise, disp will be a dataset, not an array.
	dispall=h5file_in['/Model/Nodes/Generalized_Displacements'][()]
	# Select the step.
	disp=dispall[:,_step]
	# axis =0 is a must. Otherwise, disp will be sorted along the first axis.
	disp=np.sort(disp,axis=0)

	# If disp[0] is negative, disp[0] will become the positive value.
	# Elseif disp[0] is positive, disp[0] will be the smaller positive value 
	# in the sorted array. 
	disp[0]=-disp[0]

	# disp[-1] is the last (biggest) element in the sorted array. 
	max_disp=max(disp[0],disp[-1])

	return max_disp

def find_disp_Nstep(h5in_file_name):
	h5file_in=h5py.File(h5in_file_name,"r")
	# [()] is a must. Otherwise, disp will be a dataset, not an array.
	dispall=h5file_in['/Model/Nodes/Generalized_Displacements'][()]
	return dispall.shape[1]




def h5diff_eigen_frequency(h5in_ori_filename, h5in_new_filename):
	# h5in_ori_filename = "imposed_000.h5.feioutput"
	# h5in_new_filename = "imposed_111.h5.feioutput"

	h5_ori_file=h5py.File(h5in_ori_filename,"r")
	h5_new_file=h5py.File(h5in_new_filename,"r")

	# [()] is a must. Otherwise, result will be a dataset, not an array.
	eigen_all_ori=h5_ori_file['/Eigen_Mode_Analysis/frequencies'][()]
	eigen_all_new=h5_new_file['/Eigen_Mode_Analysis/frequencies'][()]
	# tolerance setting for the overflow and underflow.
	max_rel_tolerance=1e-03
	max_tolerance=1e-03
	print_header_flag=0
	pass_fail_flag=1
	for index, x in np.ndenumerate(eigen_all_ori):
		if abs(( np.float32(x) - np.float32(eigen_all_new[index]) ) / (np.float32(x) + epsilon) )> max_rel_tolerance or abs( np.float32(x) - np.float32(eigen_all_new[index]) ) > max_tolerance:
			pass_fail_flag=0
			if print_header_flag==0:
				print_header_flag=1
				print headwrongstep(), "================================================"
				print headwrongstep(), "|  Eigen_Analysis Frequencies have mismatches: |"
				print headwrongstep(), "================================================"
				print headwrongstep(), "|  Location    |Original_value |     New_value | "
			print headwrongstep(), "|",'{:12s}'.format(index) ,"|", '{:+e}'.format(x) ,"|",'{:+e}'.format(eigen_all_new[index]) ,"|"

	# print "================================================"

	return pass_fail_flag



# legacy backup
	# h5in_file_name=sys.argv[1]
	# h5in_file_name="t_1.h5.feioutput"
	# h5in_file_name="0_Fz.h5.feioutput"
