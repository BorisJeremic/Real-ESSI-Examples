#!/usr/bin/python
import h5py
import matplotlib.pylab as plt
import matplotlib as mpl
import sys
import numpy as np;

plt.rcParams.update({'font.size': 24})

# set tick width
mpl.rcParams['xtick.major.size'] = 10
mpl.rcParams['xtick.major.width'] = 5
mpl.rcParams['xtick.minor.size'] = 10
mpl.rcParams['xtick.minor.width'] = 5
plt.rcParams['xtick.labelsize']=20

mpl.rcParams['ytick.major.size'] = 10
mpl.rcParams['ytick.major.width'] = 5
mpl.rcParams['ytick.minor.size'] = 10
mpl.rcParams['ytick.minor.width'] = 5
plt.rcParams['ytick.labelsize']=20




# Go over each feioutput and plot each one.  
thefile = "Monotonic_Contact_Behaviour_Adding_Normal_Load.h5.feioutput";
finput = h5py.File(thefile)

plt.style.use('grayscale')

# Read the time and displacement
times = finput["time"][:]
normal_disp   =  finput["/Model/Elements/Element_Outputs"][6,:]
normal_stress = -finput["/Model/Elements/Element_Outputs"][9,:];

# plt.figure()
fig = plt.figure(figsize=(10,10))

plt.plot(normal_disp*1e3,normal_stress/1000,Linewidth=4)
plt.xlabel(r"Penetration $\Delta_n$ $[mm]$")
plt.ylabel(r"Normal Stress $\sigma_n$ $[kPa]$")

plt.hold(True)

# axes = plt.gca()
# axes.set_xlim([-7,7])
# axes.set_ylim([-1,1])
outfigname  = "Axial_Response.pdf";
# Make space for and rotate the x-axis tick labels
fig.autofmt_xdate()
plt.grid(linestyle='--', linewidth='0.5', color='k')
plt.savefig(outfigname,  bbox_inches='tight')
# plt.show()