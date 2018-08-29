#! /usr/bin/env python

import h5py
import scipy as sp
import numpy as np 
import time
import pickle
import sys
import math
import cmath

with h5py.File('DRMinput.hdf5',  "a") as f:
    
    bool_tag = "Time" in f; 

    if bool_tag:

    	del f['Time']; 
    
    bool_tag = "Accelerations" in f;
    
    if bool_tag:

    	del f['Accelerations']; 

    bool_tag = "Displacements" in f; 
    
    if bool_tag: 

	    del f['Displacements']; 

# print "hdf5 input file cleaned!";  