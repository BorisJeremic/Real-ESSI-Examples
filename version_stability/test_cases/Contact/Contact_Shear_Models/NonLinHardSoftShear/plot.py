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
thefile = "Gauss_Model_Shear_Load.h5.feioutput";
finput = h5py.File(thefile)

h = 5e-3;

plt.style.use('grayscale')

# Read the time and displacement
times = finput["time"][:]
shear_strain_x = finput["/Model/Elements/Element_Outputs"][4,:]
shear_strain_y = finput["/Model/Elements/Element_Outputs"][5,:]
normal_strain = finput["/Model/Elements/Element_Outputs"][6,:]
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
# plt.figure()
fig = plt.figure(figsize=(12,10))

plt.plot(shear_strain_x,shear_stress_x/normal_stress,Linewidth=4,label='$k_t=1800kPa$')
plt.xlabel(r"Shear Displacement $\Delta_t$ $[mm]$")
plt.ylabel(r"Normalized Shear Stress $\tau/\sigma_n$")

# axes = plt.gca()
# axes.set_xlim([-7,7])
# axes.set_ylim([-1,1])
outfigname  = "Shear_Response.pdf";
# fig.autofmt_xdate();
legend = plt.legend()
legend.get_frame().set_linewidth(0.0)
legend.get_frame().set_facecolor('white')
plt.grid(linestyle='--', linewidth='0.5', color='k')
plt.savefig(outfigname,  bbox_inches='tight')
# plt.show()
