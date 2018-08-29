#!/usr/bin/python
#Standard python libs
import sys
import os
# import datetime
import numpy as np
import h5py 
import matplotlib.pyplot as plt
from math import *

h5in_file_name=sys.argv[1]

h5file_in=h5py.File(h5in_file_name,"r")


disp=h5file_in['/Model/Nodes/Generalized_Displacements'][()]
time=h5file_in['/time'][()]

# The required displacement.
disp_node=disp[6][:]
last=len(disp_node)-1
len_time=len(time)
disp_node=np.delete(disp_node,[last],None)
# np.delete(time,[len_time],None)

# time=np.transpose(time)

# print ("%16.8f \n" %len(disp_node))

# print ("%16.8f \n" %len_time)

# print ("%16.8f \n" %disp_node[0])
# print ("%16.8f \n" %disp_node[1])

# print ("%16.8f \n" %time[0])

# print ("%16.8f \n" %time[1])


xi=0.1

u_0=0.1
w_n=2*pi
w_D=w_n*np.sqrt(1-xi**2)




u_exact=np.exp(-xi*w_n*time)*(u_0*np.cos(time*w_D)+(xi*w_n*u_0)/w_D*np.sin(w_D*time))


# print("time")
# , (comma) cannot be ignored.
u_essi,=plt.plot(time, disp_node,'ro-')
u_disp,=plt.plot(time, u_exact,'b^--')
plt.xlabel('Time')
plt.ylabel('Displacement')

plt.legend([u_essi, u_disp], ["ESSI", "Exact"])

plt.show()






