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
from time_integrator_analysis import findpeaks, measure_damping, hht_damping_and_shift

from mycolor_fun import *

h5in_file_name=sys.argv[1]
alpha=sys.argv[2]
alpha=float(alpha)

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

# alpha=0.0
N = node_displ.shape[0]
D = fft(node_displ[:])
f = fftfreq(N, dt)
xi, fs, Ys = measure_damping(f[0:N/2], abs(D[0:N/2]))

# **********************************************
# The measured xi is not accurate by the previous method
# Use the other method to measure xi:
peak_indices=findpeaks(node_displ)
pks = []
for index in peak_indices:
	pks.append(node_displ[index])
deltaSize=len(pks)-1;
delta=np.zeros([deltaSize,1]);

for i in xrange(len(delta)):
	delta[i] =1.0/(i+1.0)*np.log(pks[0]/pks[i+1])
deltaAverage=np.mean(delta);
xi_measure=deltaAverage/2./pi;
# print "old xi = " + str(xi)
# print "new xi = " + str(xi_measure)
# **********************************************

# print fs


peak_index = 0
max_Y = 0
T_system=1.0
for i in arange(len(fs)):
    if (abs(Ys[i]) > max_Y) :
        max_Y = abs(Ys[i])
        peak_index = i        
# xi_measure = xi[peak_index]
measured_period = 1./fs[peak_index]
measured_period_shift=(1./fs[peak_index]-T_system)/T_system



w = 2*pi/T_system

gamma = 0.5*(1.0-2.0*alpha)
beta = 0.25*(1.0 - alpha)**2


wbar, xi_analytic = hht_damping_and_shift(beta, gamma, alpha, w, dt)


T_theory = 2*pi/wbar
T_shift = (T_theory - T_system)/T_system

# xi_measure_error=abs(xi_measure-xi_analytic)/xi_measure
T_error=abs(T_system-T_theory)/T_system



# standard 1
# print  dt, " & ",  gamma, " & ",   "%0.4f" %xi_measure, " & ",  "%0.4f" %xi_analytic, " & ",  "%0.4f" %xi_measure_error, " & ", "\\\\ "
# print  dt, " & ",  gamma, " & ",  "%0.4f" %T_system, " & ",  "%0.4f" %T_theory, " & ",  "%0.4f" %T_error, " & ", "\\\\ "

# standard 2
#                             1 measured xi_measure          2 xi_analytic
xi_analytic=xi_analytic+0
xi_analytic=abs(xi_analytic)
# print  dt, " & ",  alpha, " & ",  "%0.6f" %xi_measure," & ", "%0.6f" %xi_analytic, " & ", "%0.6f" %measured_period_shift, " & ",  "%0.6f" %T_shift,  "\\\\ \\hline"

# new printing
xi_err = abs(xi_analytic - xi_measure)
period_err = abs(T_shift - measured_period_shift)
xi_rel_err = abs(xi_analytic - xi_measure) / xi_analytic
period_rel_err = abs(T_shift - measured_period_shift) / T_shift
if period_rel_err > 1.0:
	period_rel_err = 1.0
if xi_rel_err > 1.0:
	xi_rel_err =1.0
print headrun()          , "-----------Testing results-----------------"
print headstep()         , "dt = " + str(dt) + "   alpha = " + str(alpha)
print headstep()         ,'{0}  {1}     {2}    {3}'.format('Analytic  ','ESSI  ','Absolute_Error ','Relative_Error')
print headDamping()      ,'{0:+0.2e}   {1:+0.2e}        {2:+0.2f}         {3:+0.2f}'.format(xi_analytic, xi_measure, xi_err, xi_rel_err )
print headPeriodShift()  ,'{0:+0.2e}   {1:+0.2e}        {2:+0.2f}         {3:+0.2f}'.format(T_shift, measured_period_shift, period_err, period_rel_err )




# My own method to calculate the theoretical wbar for Newmark method:
# I got the same result with the pre-exi_measuresting one.
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


# xi_measure=0.1

# u_0=0.1
# w_n=2*pi
# w_D=w_n*np.sqrt(1-xi_measure**2)




# u_exact=np.exp(-xi_measure*w_n*time)*(u_0*np.cos(time*w_D)+(xi_measure*w_n*u_0)/w_D*np.sin(w_D*time))


# # print("time")
# # , (comma) cannot be ignored.
# u_essi,=plt.plot(time, node_displ,'ro-')
# u_disp,=plt.plot(time, u_exact,'b^--')
# plt.xlabel('Time')
# plt.ylabel('Displacement')

# plt.legend([u_essi, u_disp], ["ESSI", "Exact"])

# plt.show()






