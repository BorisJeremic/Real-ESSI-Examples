#!/usr/bin/python
import h5py
import matplotlib.pylab as plt
import sys
import numpy as np;


# Go over each feioutput and plot each one.  
thefile = "Monotonic_Contact_Behaviour_Adding_Normal_Load.h5.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
shear_strain_x = finput["/Model/Elements/Element_Outputs"][4,:]
shear_strain_y = finput["/Model/Elements/Element_Outputs"][5,:]
normal_strain = finput["/Model/Elements/Element_Outputs"][6,:]
shear_stress_x = finput["/Model/Elements/Element_Outputs"][7,:]
shear_stress_y = finput["/Model/Elements/Element_Outputs"][8,:]
normal_stress       = -finput["/Model/Elements/Element_Outputs"][9,:];


# Configure the figure filename, according to the input filename.
outfig=thefile.replace("_","-")
outfigname=outfig.replace("h5.feioutput","pdf")

# Plot the figure. Add labels and titles.
plt.figure()

plt.plot(normal_strain,normal_stress,'-k',Linewidth=4)
plt.xlabel(r"Normal Strain $\epsilon$")
plt.ylabel(r"Normal Stress $\sigma$")

plt.savefig("Contact_Normal_Interface_Behavour.pdf",  bbox_inches='tight')
plt.show()
# #####################################################################