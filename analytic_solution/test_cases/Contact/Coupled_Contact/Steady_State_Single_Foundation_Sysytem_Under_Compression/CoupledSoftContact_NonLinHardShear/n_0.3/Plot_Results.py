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



# Plot the figure. Add labels and titles.
plt.figure()
ax = plt.subplot(111)
ax.grid()
ax.set_xlabel("Time [s] ")
ax.set_ylabel(r"Stress  [Pa]  ")

# Pore Pressure
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

# pore_pressure
ax.plot(times,upU_p,'b',linewidth=2,label=r'Pore Pressure $p$'); 
ax.hold(True);

# Total Stress 
# #########################################################################

# Read the time and displacement
times = finput["time"][:];
T     = times[len(times)-1]
sigma_zz = 400/T*times

# kinetic energy 
ax.plot(times,sigma_zz,'k',linewidth=2,label=r'Total Stress $\sigma$'); 
ax.hold(True);


# Effective Stress 
# #########################################################################

# Read the time and displacement
times = finput["time"][:];
sigma_zz_ = sigma_zz - upU_p

# kinetic energy 
ax.plot(times,sigma_zz_,'r',linewidth=2,label=r'''Effective Stress $\sigma^{\prime}$'''); 
ax.hold(True);

max_yticks = 5
yloc = plt.MaxNLocator(max_yticks)
ax.yaxis.set_major_locator(yloc)

max_xticks = 5
yloc = plt.MaxNLocator(max_xticks)
ax.xaxis.set_major_locator(yloc)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.35),
          ncol=2, fancybox=True, shadow=True, prop={'size': 24})

pylab.savefig("Coupled_Soft_Contact_Steady_State_SF_Ststem_Under_Compression_Porosity_Effective_Stress_Principle.pdf",  bbox_inches='tight')






# plt.show()
# 

################################### Drainage Condition Verification #############################

ax.hold(False);
fig = plt.figure();
ax = plt.subplot(111)

ax.plot(times,upU_u*1e8,'k',linewidth=3,label=r'$upU\_u$');  ax.hold(True); 
ax.plot(times,upU_U*1e8,'b',linewidth=10,label=r'$upU\_U$');  ax.hold(True);
ax.plot(times,u_u*1e8,'r',linewidth=3,label=r'$u\_u$');  ax.hold(True);
ax.grid()
ax.set_xlabel("Time [s] ")
ax.set_ylabel(r"Displacement $\times 1e^{-8}$ [m]  ")
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25),
          ncol=4, fancybox=True, shadow=True, prop={'size': 24})

max_yticks = 5
yloc = plt.MaxNLocator(max_yticks)
ax.yaxis.set_major_locator(yloc)

max_xticks = 5
yloc = plt.MaxNLocator(max_xticks)
ax.xaxis.set_major_locator(yloc)

pylab.savefig("Coupled_Soft_Contact_Steady_State_SF_Ststem_Under_Compression_Porosity_Undrained_Conditions.pdf",  bbox_inches='tight')

# plt.show()

