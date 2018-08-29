#!/usr/bin/python
import h5py
import matplotlib.pylab as plt
import matplotlib as mpl
import sys
import numpy as np;

plt.rcParams.update({'font.size': 28})

# set tick width
mpl.rcParams['xtick.major.size'] = 10
mpl.rcParams['xtick.major.width'] = 5
mpl.rcParams['xtick.minor.size'] = 10
mpl.rcParams['xtick.minor.width'] = 5
plt.rcParams['xtick.labelsize']=24

mpl.rcParams['ytick.major.size'] = 10
mpl.rcParams['ytick.major.width'] = 5
mpl.rcParams['ytick.minor.size'] = 10
mpl.rcParams['ytick.minor.width'] = 5
plt.rcParams['ytick.labelsize']=24

###############################################################
## Analytical Solution
###############################################################
# Go over each feioutput and plot each one.  
thefile = "Analytical_Displacement.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
disp = finput["/Model/Nodes/Generalized_Displacements"][24,:]

# Plot the figure. Add labels and titles.
plt.figure(figsize=(12,10))

plt.plot(times,disp,'-r',label='Analytical Solution', Linewidth=4)
plt.xlabel("Time [s] ")
plt.ylabel("Displacement [m]  ")

###############################################################
## Numerical Solution
###############################################################

# Go over each feioutput and plot each one.  
thefile = "Frictional_SDOF_freeVibration.h5.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
disp = finput["/Model/Nodes/Generalized_Displacements"][24,:]

# Plot the figure. Add labels and titles.
plt.plot(times,disp,'-k',label='Numerical Solution', Linewidth=4)
plt.xlabel("Time [s] ")
plt.ylabel("Displacement [m]  ")




########################################################
# # axes = plt.gca()
# # axes.set_xlim([-7,7])
# # axes.set_ylim([-1,1])
outfigname  = "Displacement_Response.pdf";
legend = plt.legend()
legend.get_frame().set_linewidth(0.0)
legend.get_frame().set_facecolor('none')
plt.savefig(outfigname,  bbox_inches='tight')
# plt.show()
