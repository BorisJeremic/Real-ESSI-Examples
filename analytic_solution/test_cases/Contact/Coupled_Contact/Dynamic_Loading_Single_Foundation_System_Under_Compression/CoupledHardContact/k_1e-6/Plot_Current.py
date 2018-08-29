#!/usr/bin/env python

#!/usr/bin/python
import h5py
from matplotlib import pylab
import matplotlib.pylab as plt
import sys
from matplotlib.font_manager import FontProperties
import math
import numpy as np

#!/usr/bin/python
import h5py
import matplotlib.pylab as plt
import matplotlib as mpl
import sys
import numpy as np;


plt.rcParams.update({'font.size': 30})

# set tick width
mpl.rcParams['xtick.major.size'] = 10
mpl.rcParams['xtick.major.width'] = 5
mpl.rcParams['xtick.minor.size'] = 10
mpl.rcParams['xtick.minor.width'] = 5
plt.rcParams['xtick.labelsize']=28

mpl.rcParams['ytick.major.size'] = 10
mpl.rcParams['ytick.major.width'] = 5
mpl.rcParams['ytick.minor.size'] = 10
mpl.rcParams['ytick.minor.width'] = 5
plt.rcParams['ytick.labelsize']=28


Pore_Pressure = [];
Solid_Displacement_u   = [];
Solid_Displacement_uPU = [];
Fluid_Displacement_uPU = [];
Time                   = [];

# Plot the figure. Add labels and titles.
plt.figure()
ax = plt.subplot(111)
ax.grid()
ax.set_xlabel("Time [s] ")
ax.set_ylabel(r"Stress  [Pa]  ")

# Loading Stage
# #########################################################################
thefile = "Soil_Foundation_System_Surface_Load.h5.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
upU_p = finput["/Model/Nodes/Generalized_Displacements"][3,:]
upU_u = finput["/Model/Nodes/Generalized_Displacements"][2,:]
upU_U = finput["/Model/Nodes/Generalized_Displacements"][6,:]
u_u = finput["/Model/Nodes/Generalized_Displacements"][79,:]
sigma_zz_ = finput["/Model/Elements/Gauss_Outputs"][14,:]

Pore_Pressure =  np.append(Pore_Pressure,upU_p);
Solid_Displacement_u   = np.append(Solid_Displacement_u  , u_u);
Solid_Displacement_uPU = np.append(Solid_Displacement_uPU, upU_u);
Fluid_Displacement_uPU = np.append(Fluid_Displacement_uPU, upU_U);
Time                   = np.append(Time, times);

# Consolidation Stage
# #########################################################################
thefile = "Soil_Foundation_System_Consolidation.h5.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = times[-1] + finput["time"][:]
upU_p = finput["/Model/Nodes/Generalized_Displacements"][3,:]
upU_u = finput["/Model/Nodes/Generalized_Displacements"][2,:]
upU_U = finput["/Model/Nodes/Generalized_Displacements"][6,:]
u_u = finput["/Model/Nodes/Generalized_Displacements"][79,:]
sigma_zz_ = finput["/Model/Elements/Gauss_Outputs"][14,:]

Pore_Pressure =  np.append(Pore_Pressure,upU_p);
Solid_Displacement_u   = np.append(Solid_Displacement_u  , u_u);
Solid_Displacement_uPU = np.append(Solid_Displacement_uPU, upU_u);
Fluid_Displacement_uPU = np.append(Fluid_Displacement_uPU, upU_U);
Time                   = np.append(Time, times);

##### Start Plotting 
ax.semilogx(Time,Pore_Pressure,'b',linewidth=2,label=r'Pore Pressure $p$'); 
ax.hold(True);

ax.hold(True);

# max_yticks = 5
# yloc = plt.MaxNLocator(max_yticks)
# ax.yaxis.set_major_locator(yloc)

# max_xticks = 5
# yloc = plt.MaxNLocator(max_xticks)
# ax.xaxis.set_major_locator(yloc)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.35),
          ncol=2, fancybox=True, shadow=True, prop={'size': 24})

pylab.savefig("Current_Excess_Pore_Pressure.pdf",  bbox_inches='tight')


##### Drainage Condition #####

ax.hold(False);
fig = plt.figure();
ax = plt.subplot(111)

ax.semilogx(Time,Solid_Displacement_uPU*1e8,'k',linewidth=3,label=r'$upU\_u$');  ax.hold(True); 
ax.semilogx(Time,Fluid_Displacement_uPU*1e8,'b',linewidth=10,label=r'$upU\_U$');  ax.hold(True);
ax.semilogx(Time,Solid_Displacement_u*1e8,'r',linewidth=3,label=r'$u\_u$');  ax.hold(True);
ax.grid()
ax.set_xlabel("Time [s] ")
ax.set_ylabel(r"Displacement $\times 1e^{-8}$ [m]  ")
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25),
          ncol=4, fancybox=True, shadow=True, prop={'size': 24})

# max_yticks = 5
# yloc = plt.MaxNLocator(max_yticks)
# ax.yaxis.set_major_locator(yloc)

# max_xticks = 5
# yloc = plt.MaxNLocator(max_xticks)
# ax.xaxis.set_major_locator(yloc)

pylab.savefig("Current_Displacement_At_Interface",  bbox_inches='tight')

# plt.show()

