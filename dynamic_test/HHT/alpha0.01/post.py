#!/usr/bin/python
#Standard python libs
import sys
import os
# import datetime
import numpy as np
import h5py 
import matplotlib.pyplot as plt
from math import *
#Libs related to scipy and matplotlib
from scipy import *
from scipy.fftpack import fft
from scipy.fftpack.helper import fftfreq

sys.path.append("./" )
# time_integrator_analysis was created by Jose.
# Jose's function was used directly here.
from time_integrator_analysis import findpeaks, measure_damping, hht_damping_and_shift

h5in_file_name=sys.argv[1]
gamma=sys.argv[2]
gamma=float(gamma)
h5file_in=h5py.File(h5in_file_name,"r")

# h5file_in=h5py.File("veri_newmark_dynamic.h5.feioutput","r")

disp=h5file_in['/Model/Nodes/Generalized_Displacements'][()]
time=h5file_in['/time'][()]



# The required displacement.
node_displ=disp[6][:]
last=len(node_displ)-1
len_time=len(time)
node_displ=np.delete(node_displ,[last],None)


dt=time[1]-time[0]

peak_indices=findpeaks(node_displ)

measured_period=time[peak_indices[2]]-time[peak_indices[1]]


alpha=0.0
N = node_displ.shape[0]
D = fft(node_displ[:])
f = fftfreq(N, dt)
xi, fs, Ys = measure_damping(f[0:N/2], abs(D[0:N/2]))	

T_system=1.0
w = 2*pi/T_system
beta = 0.25*(0.5 + gamma)**2
wbar, xibar = hht_damping_and_shift(beta, gamma, alpha, w, dt)

T_theory = 2*pi/wbar
T_shift = (T_theory - T_system)/T_system*100

print "gamma=", gamma
print "xi=", xibar
print "T_shift=",T_shift
print "\n"



# My own method to calculate the theoretical wbar for Newmark method:
# I got the same result with the pre-existing one.
# dtw=dt*w
# numerator=dtw*sqrt(1+dtw**2*(beta-0.25*(gamma+0.5)**2))
# denominator=1+dtw**2*(beta-0.5*(gamma+0.5))w
# Phi=arctan(numerator/denominator)
# wbarmy=Phi/dt
# wbarmy





# # time=np.transpose(time)


# print ("%16.8f \n" %len(node_displ))

# print ("%16.8f \n" %len_time)

# print ("%16.8f \n" %node_displ[0])
# print ("%16.8f \n" %node_displ[1])

# print ("%16.8f \n" %time[0])

# print ("%16.8f \n" %time[1])


# xi=0.1

# u_0=0.1
# w_n=2*pi
# w_D=w_n*np.sqrt(1-xi**2)




# u_exact=np.exp(-xi*w_n*time)*(u_0*np.cos(time*w_D)+(xi*w_n*u_0)/w_D*np.sin(w_D*time))


# # print("time")
# # , (comma) cannot be ignored.
# u_essi,=plt.plot(time, node_displ,'ro-')
# u_disp,=plt.plot(time, u_exact,'b^--')
# plt.xlabel('Time')
# plt.ylabel('Displacement')

# plt.legend([u_essi, u_disp], ["ESSI", "Exact"])

# plt.show()






