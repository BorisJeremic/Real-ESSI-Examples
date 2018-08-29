#!/usr/bin/python
import h5py
import matplotlib.pylab as plt
import matplotlib as mpl
import sys
import numpy as np;
import matplotlib;
import math;
from matplotlib.ticker import MaxNLocator

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

plt.style.use('grayscale')

###############################################################
## SZ_h = 1e-3 mm
###############################################################
# Go over each feioutput and plot each one.  
thefile = "SZ_h_1e-3/Analytical_Solution_Normal_Stress.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
normal_stress  = -finput["/Model/Elements/Element_Outputs"][9,:];
normal_strain  = -finput["/Model/Elements/Element_Outputs"][6,:];

# Configure the figure filename, according to the input filename.
outfig=thefile.replace("_","-")
outfigname=outfig.replace("h5.feioutput","pdf")

# Plot the figure. Add labels and titles.
plt.figure(figsize=(12,10))

plt.plot(normal_strain,normal_stress/1000,label=r'$SZ_h$ = $1e^{-3} mm$', Linewidth=4, markersize=20)
plt.xlabel(r"Interface Type #")
plt.ylabel(r"Normal Stress $\sigma_n [kPa]$")
plt.hold(True)

###############################################################
## SZ_h = 1 mm
###############################################################
# Go over each feioutput and plot each one.  
thefile = "SZ_h_1/Analytical_Solution_Normal_Stress.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
normal_stress  = -finput["/Model/Elements/Element_Outputs"][9,:];
normal_strain  = -finput["/Model/Elements/Element_Outputs"][6,:];

# Configure the figure filename, according to the input filename.
outfig=thefile.replace("_","-")
outfigname=outfig.replace("h5.feioutput","pdf")

# Plot the figure. Add labels and titles.
plt.plot(normal_strain,normal_stress/1000,label=r'$SZ_h$ = $1 mm$', Linewidth=4, markersize=20)
# plt.xlabel(r"Normal Strain $\epsilon$")
plt.ylabel(r"Normal Stress $\sigma_n [kPa]$")


###############################################################
## SZ_h = 1 m
###############################################################
# Go over each feioutput and plot each one.  
thefile = "SZ_h_1e3/Analytical_Solution_Normal_Stress.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
normal_stress  = -finput["/Model/Elements/Element_Outputs"][9,:];
normal_strain  = -finput["/Model/Elements/Element_Outputs"][6,:];

# Configure the figure filename, according to the input filename.
outfig=thefile.replace("_","-")
outfigname=outfig.replace("h5.feioutput","pdf")

# Plot the figure. Add labels and titles.
plt.plot(normal_strain,normal_stress/1000,label=r'$SZ_h$ = $1 m$', Linewidth=4, markersize=20)
plt.xlabel(r"Normal Strain $\epsilon$")
plt.ylabel(r"Normal Stress $\sigma_n [kPa]$")

###############################################################
## SZ_h = 10 m
###############################################################
# Go over each feioutput and plot each one.  
thefile = "SZ_h_1e4/Analytical_Solution_Normal_Stress.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
normal_stress  = -finput["/Model/Elements/Element_Outputs"][9,:];
normal_strain  = -finput["/Model/Elements/Element_Outputs"][6,:];

# Configure the figure filename, according to the input filename.
outfig=thefile.replace("_","-")
outfigname=outfig.replace("h5.feioutput","pdf")

# Plot the figure. Add labels and titles.
plt.plot(normal_strain,normal_stress/1000,label=r'$SZ_h$ = $10 m$', Linewidth=4, markersize=20)
plt.xlabel(r"Normal Strain $\epsilon$")
plt.ylabel(r"Normal Stress $\sigma_n [kPa]$")

#############################################################
# # # axes = plt.gca()
# # # axes.set_xlim([-7,7])
# # # axes.set_ylim([-1,1])
# outfigname  = "Interface_Test_Normal_Stress.pdf";
# plt.axis([0, 5.5, 90, 101])

# legend = plt.legend()
# legend.get_frame().set_linewidth(0.0)
# legend.get_frame().set_facecolor('none')
plt.legend()
plt.savefig('Normal_Stress.pdf',  bbox_inches='tight')
# plt.show()
