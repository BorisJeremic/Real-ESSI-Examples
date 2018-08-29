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
thefile = "Analytical_Solution_Shear.feioutput";
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
plt.figure(figsize=(12,10))

plt.plot(shear_strain,shear_stress/normal_stress,'-r',label='Analytical Solution', Linewidth=4)
plt.xlabel(r"Shear Strain $\gamma $")
plt.ylabel(r"Normalized Shear Stress $\tau/\sigma_n$")

###############################################################
## Numerical Solution
###############################################################

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
plt.plot(shear_strain,shear_stress/normal_stress,'-k',label='Numerical Solution', Linewidth=4)
plt.xlabel(r"Shear Strain $\gamma $")
plt.ylabel(r"Normalized Shear Stress $\tau/\sigma_n$")




########################################################
# # axes = plt.gca()
# # axes.set_xlim([-7,7])
# # axes.set_ylim([-1,1])
outfigname  = "Normalized_Shear_Stress.pdf";
legend = plt.legend()
legend.get_frame().set_linewidth(0.0)
legend.get_frame().set_facecolor('none')
plt.savefig(outfigname,  bbox_inches='tight')
# plt.show()
