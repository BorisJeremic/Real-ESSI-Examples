#!/usr/bin/python
import h5py
import matplotlib.pylab as plt
import sys
import numpy as np;


################ Node # 2 Displacement #############################
#######################################
## Analytical Solution
#######################################

finput = h5py.File('Analytical_Solution.feioutput')

plt.figure()

# Read the time and displacement
times = finput["time"][:]
normal_strain = finput["/Model/Elements/Element_Outputs"][6,:]
normal_stress = -finput["/Model/Elements/Element_Outputs"][9,:];

# plt.plot(normal_strain,normal_stress,'-r',Linewidth=4,label='Analytical Solution')
plt.hold(True)

#######################################
## Current Solution
#######################################


# Go over each feioutput and plot each one.  
thefile = "Monotonic_Contact_Behaviour_Adding_Normal_Load.h5.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
normal_strain = finput["/Model/Elements/Element_Outputs"][6,:]
normal_stress = -finput["/Model/Elements/Element_Outputs"][9,:];

# Configure the figure filename, according to the input filename.
outfig=thefile.replace("_","-")
outfigname=outfig.replace("h5.feioutput","pdf")

# Plot the figure. Add labels and titles.
plt.plot(normal_strain,normal_stress,'-k',Linewidth=4,label='Numerical Solution')
plt.xlabel(r"Normal Strain $\epsilon$")
plt.ylabel(r"Normal Stress $\sigma$")
plt.legend()
plt.savefig("Contact_Normal_Interface_Behavour.pdf",  bbox_inches='tight')
# plt.show()
# #####################################################################


