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
max_rel_tolerance=1e-2
max_tolerance=1e-3

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

	print_header_flag=0
	pass_fail_flag=1
	for index, x in np.ndenumerate(disp_all_ori):
		if not(abs(( np.float32(x) - np.float32(disp_all_new[index]) )/(np.float32(x+epsilon))) < max_rel_tolerance or abs( np.float32(x) - np.float32(disp_all_new[index]) ) < max_tolerance):
			# print abs(( np.float32(x) - np.float32(disp_all_new[index]) )/(np.float32(x+epsilon)));
			# print abs( np.float32(x) - np.float32(disp_all_new[index]) )
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

	print_header_flag=0
	pass_fail_flag=1
	for index, x in np.ndenumerate(outputs_all_ori):
		if  not(abs(( np.float32(x) - np.float32(outputs_all_new[index]) )/(np.float32(x+epsilon))) < max_rel_tolerance or abs( np.float32(x) - np.float32(outputs_all_new[index]) ) < max_tolerance):
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
	Time=h5_new_file['/time'][()]
	NumSteps = len(Time);

	# find out contact elements 
	Element_Class_Tags = h5_new_file['/Model/Elements/Class_Tags'][()];
	Index_to_Element_Outputs = h5_new_file['/Model/Elements/Index_to_Element_Outputs'][()];
	Number_of_Element_Outputs = h5_new_file['/Model/Elements/Number_of_Element_Outputs'][()];
	ElementType = Element_Class_Tags*0; i=0;
	Element_Class_Desc = h5_new_file['/Model/Elements/Element_Class_Desc'][()];
	for i in range(1,len(Element_Class_Tags)):
		ElementType[i] = int(str(Element_Class_Desc[Element_Class_Tags[i]])[:1])

	Discard_Element_Output_Index = [];

	### ElementType == 2 means a contact element 
	for i in range (0,len(Element_Class_Tags)):
		if(ElementType[i]==2):
			index_element_output = Index_to_Element_Outputs[i];
			### strain(3), stress(3), incr_plastic_strain(3)
			### only checking for stress so will remove strain and plastic strain which are very small and depend upon penalty stiffness
			Discard_Element_Output_Index = np.append(Discard_Element_Output_Index,[index_element_output,index_element_output+1,index_element_output+2,index_element_output+6,index_element_output+7,index_element_output+8])

	# print Element_Class_Tags
	# print ElementType
	# print Discard_Element_Output_Index



	# delete the last column
	outputs_all_ori=outputs_all_ori_c[:,:]
	outputs_all_new=outputs_all_new_c[:,:]
	# tolerance setting for the overflow and underflow.
	print_header_flag=0
	pass_fail_flag=1
	for index, x in np.ndenumerate(outputs_all_ori):

		if index[0] in Discard_Element_Output_Index:
			continue;

		if not(abs(( np.float32(x) - np.float32(outputs_all_new[index]) )/(np.float32(x+epsilon))) < max_rel_tolerance or abs( np.float32(x) - np.float32(outputs_all_new[index]) ) < max_tolerance):
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
