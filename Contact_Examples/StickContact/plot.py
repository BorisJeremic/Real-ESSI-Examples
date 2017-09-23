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
Displacement_x = finput["/Model/Elements/Element_Outputs"][4,:]
Displacement_y = finput["/Model/Elements/Element_Outputs"][5,:]
Displacement_z = finput["/Model/Elements/Element_Outputs"][6,:]
Force_x        = finput["/Model/Elements/Element_Outputs"][7,:]
Force_y        = finput["/Model/Elements/Element_Outputs"][8,:]
Force_z        = finput["/Model/Elements/Element_Outputs"][9,:]

# Plot the figure. Add labels and titles.
plt.figure()

plt.plot(Displacement_x*1000,Force_x/1000,'-k',Linewidth=4)
plt.xlabel(r"Displacement_X $[mm]$")
plt.ylabel(r"Force in x-drection  $[kN]$")

plt.savefig("Stick_Contact_Behaviour.pdf",  bbox_inches='tight')
plt.show()
# #####################################################################