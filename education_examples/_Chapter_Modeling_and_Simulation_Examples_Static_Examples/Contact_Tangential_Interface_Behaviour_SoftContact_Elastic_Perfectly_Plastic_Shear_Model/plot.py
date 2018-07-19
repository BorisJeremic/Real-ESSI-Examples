#!/usr/bin/python
import h5py
import matplotlib.pylab as plt
import sys
import numpy as np;


# Go over each feioutput and plot each one.  
thefile = "Monotonic_Contact_Behaviour_Adding_Tangential_Load.h5.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
shear_strain_x = finput["/Model/Elements/Element_Outputs"][4,:]
shear_strain_y = finput["/Model/Elements/Element_Outputs"][5,:]
shear_stress_x = finput["/Model/Elements/Element_Outputs"][7,:]
shear_stress_y = finput["/Model/Elements/Element_Outputs"][8,:]
normal_stress       = -finput["/Model/Elements/Element_Outputs"][9,:];


shear_strain = np.sqrt(shear_strain_x*shear_strain_x + shear_strain_y*shear_strain_y) ;
shear_stress = np.sqrt(shear_stress_x*shear_stress_x + shear_stress_y*shear_stress_y );

shear_stress = shear_stress_x;
shear_strain = shear_strain_x;
# Configure the figure filename, according to the input filename.
outfig=thefile.replace("_","-")
outfigname=outfig.replace("h5.feioutput","pdf")

# Plot the figure. Add labels and titles.
plt.figure()

plt.plot(shear_strain,shear_stress/normal_stress,'-k',Linewidth=4)
plt.xlabel(r"Shear Strain $\gamma$")
plt.ylabel(r"Normalized Shear $\tau/\sigma$")

plt.savefig("Contact_Tangential_Interface_Behavour.pdf",  bbox_inches='tight')
plt.show()
# #####################################################################