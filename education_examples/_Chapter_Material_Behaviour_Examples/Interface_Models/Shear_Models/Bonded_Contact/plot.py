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
thefile = "Monotonic_Contact_Behaviour_Adding_Tangential_Load.h5.feioutput";
finput = h5py.File(thefile)

plt.style.use('grayscale')

# Read the time and displacement
times = finput["time"][:]
disp_x        = finput["/Model/Elements/Element_Outputs"][4,:];
disp_y        = finput["/Model/Elements/Element_Outputs"][5,:];
disp_z        = finput["/Model/Elements/Element_Outputs"][6,:];
force_x      = -finput["/Model/Elements/Element_Outputs"][7,:];
force_y      = -finput["/Model/Elements/Element_Outputs"][8,:];
force_z      = -finput["/Model/Elements/Element_Outputs"][9,:];

shear_disp  = np.sqrt(disp_x*disp_x + disp_y*disp_y) ;
shear_force = np.sqrt(force_x*force_x + force_y*force_y );

# Plot the figure. Add labels and titles.
fig = plt.figure(figsize=(10,10))

plt.plot(shear_disp*1e3,shear_force/1000,label='Force_x',Linewidth=4);
plt.xlabel(r"Shear Displacement $\Delta_t$ $[mm]$")
plt.ylabel(r"Shear Force $F_t$ $[kN]$")

outfigname  = "BondedContact_Response.pdf";
# Make space for and rotate the x-axis tick labels
fig.autofmt_xdate()
plt.grid(linestyle='--', linewidth='0.5', color='k')
plt.savefig(outfigname,  bbox_inches='tight')
# plt.show()
