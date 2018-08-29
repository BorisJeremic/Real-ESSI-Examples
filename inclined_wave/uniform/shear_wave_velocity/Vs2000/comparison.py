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

# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

sys.path.append('../../../')

from mycolor_fun import *

cwd = os.getcwd()

def node_response_extraction_parallel(node_ID, master_file_dir, postfix, middle_name_less_than_ten, num_DOF):

	master_file_name = master_file_dir + postfix; 

	h5_master = h5py.File(master_file_name, 'r'); 

	subdomain_partition_ID = int(h5_master['Model/Nodes/Partition'][node_ID]);

	if subdomain_partition_ID<10:

		middle_name = '.' + middle_name_less_than_ten + str(int(subdomain_partition_ID)); 

	else:

		middle_name = '.' + str(int(subdomain_partition_ID));

	partioned_file_name = master_file_dir + middle_name + postfix ;

	h5_file = h5py.File(partioned_file_name, 'r'); 	

	displacement_index = int(h5_file['Model/Nodes/Index_to_Generalized_Displacements'][node_ID]);

	displacement_component = h5_file['Model/Nodes/Generalized_Displacements'][int(displacement_index):int(displacement_index+num_DOF), :];

	acceleration_component = h5_file['Model/Nodes/Generalized_Accelerations'][int(displacement_index):int(displacement_index+num_DOF), :]; 

	for x1 in xrange(0,num_DOF):

		displacement_component[x1,:] = displacement_component[x1,:]-displacement_component[x1,0]; ### in case self weight loading stage, get relative displacement 

	return displacement_component, acceleration_component;


def get_amplitude(No_omitted_time_step, dis):   ### Note: dis here is a row vector 

	num_step = dis.shape[0]; 

	num_step = num_step - No_omitted_time_step; 

	peak=[]; 

	for i in xrange(0,num_step-1):
	 	
	 	if  (dis[No_omitted_time_step+i]>dis[No_omitted_time_step+i-1]) and (dis[No_omitted_time_step+i]>dis[No_omitted_time_step+i+1]) and (dis[No_omitted_time_step+i]>0) and (dis[No_omitted_time_step+i-1]>0) and (dis[No_omitted_time_step+i+1]>0) :
	 		
	 		peak.append(dis[No_omitted_time_step+i]);

	peak_min = min(peak); 

	peak_max = max(peak); 

	mag = 0.5*(peak_min+peak_max); 

	return mag, peak; 



### Node tag 150 is located at the center of free field model with coordinates (150, 0, 0)

node_ID = 150; 

HDF5_master_Dir_prefix = '2D_free_field_model_SV_wave_layering.h5'; 

analytical_output_file = 'analytical_result.txt'; 

postfix = '.feioutput'; 

num_DOF = 3; 

No_omitted_time_step = 500; 

master_file = HDF5_master_Dir_prefix + postfix; 

abs_error_limit = 0.05; 

rel_error_limit = 0.05; 

################### End Usr Input ################################

test_partitioned = HDF5_master_Dir_prefix + '.1' + postfix;  

test_partitioned1 = HDF5_master_Dir_prefix + '.01' + postfix;


if path.exists(test_partitioned):

	middle_name_less_than_ten = '';

elif path.exists(test_partitioned1): 

	middle_name_less_than_ten = '0';

else: 

	print "File does not exists";  


displacement_component, acceleration_component = node_response_extraction_parallel(node_ID, HDF5_master_Dir_prefix, postfix, middle_name_less_than_ten, num_DOF); 

mag_x, peak_x = get_amplitude(No_omitted_time_step,displacement_component[0, :]);

mag_z, peak_z = get_amplitude(No_omitted_time_step,displacement_component[2, :]);

analytical_mag = sp.loadtxt(analytical_output_file); 

analytical_mag_x = analytical_mag[0]; 

analytical_mag_z = analytical_mag[1];

abs_error_x = abs(mag_x-analytical_mag_x); 

abs_error_z = abs(mag_z-analytical_mag_z); 

rel_error_x = abs_error_x/abs(analytical_mag_x); 

rel_error_z = abs_error_z/abs(analytical_mag_z); 

case_flag = 1; 

print headrun() , "Test directory:: ", cwd;

print headrun() , "-----------Testing results-----------------"; 

print headstep()   ,'{0}  {1}  {2}  {3}'.format('analytic_solution  ','numeric_result  ','absolute error ', 'relative error[%]'); 

if ((abs_error_x < abs_error_limit) and (rel_error_x < rel_error_limit)):

	print headOK() ,'{0:+e}        {1:+e}        {2:+2.3f}            {3:+2.2f} '.format(analytical_mag_x, mag_x, abs_error_x, 100*rel_error_x); 
		
else:

	print headFailed(), '{0:+e}        {1:+e}        {2:+2.3f}            {3:+2.2f} '.format(analytical_mag_x, mag_x, abs_error_x, 100*rel_error_x);

	case_flag = 0; 

if ((abs_error_z < abs_error_limit) and (rel_error_z < rel_error_limit)):

	print headOK() ,'{0:+e}        {1:+e}        {2:+2.3f}            {3:+2.2f} '.format(analytical_mag_z, mag_z, abs_error_z, 100*rel_error_z); 
		
else:

	print headFailed(), '{0:+e}        {1:+e}        {2:+2.3f}            {3:+2.2f} '.format(analytical_mag_z, mag_z, abs_error_z, 100*rel_error_z);

	case_flag = 0; 

if case_flag ==1 :
	
	print headOKCASE(),"-----------Done this case!-----------------"






