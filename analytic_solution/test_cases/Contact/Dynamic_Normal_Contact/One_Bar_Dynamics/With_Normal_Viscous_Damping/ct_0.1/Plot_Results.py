#!/usr/bin/env python

#!/usr/bin/python
import h5py
from matplotlib import pylab
import matplotlib.pylab as plt
import sys
from matplotlib.font_manager import FontProperties
import math
import numpy as np
import h5py
import matplotlib.pylab as plt
import matplotlib as mpl
import sys
import numpy as np;

plt.rcParams.update({'font.size': 24})


# set tick width
mpl.rcParams['xtick.major.size'] = 10
mpl.rcParams['xtick.major.width'] = 4
mpl.rcParams['xtick.minor.size'] = 5
mpl.rcParams['xtick.minor.width'] = 10
plt.rcParams['xtick.labelsize']=30

mpl.rcParams['ytick.major.size'] = 10
mpl.rcParams['ytick.major.width'] = 4
mpl.rcParams['ytick.minor.size'] = 5
mpl.rcParams['ytick.minor.width'] = 10
plt.rcParams['ytick.labelsize']=30


# Plot the figure. Add labels and titles.
plt.figure(figsize=(12,10))
ax = plt.subplot(111)
ax.grid()
ax.set_xlabel("Time [s] ",fontsize=30)
ax.set_ylabel(r"Displacement $U_z$ [mm]  ",fontsize=30)

#########################################################################
thefile = "One_Bar_Dynamics_Dynamic_Vibration_1e6_1e-3.h5.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
disp = 1000*finput["/Model/Nodes/Generalized_Displacements"][5,:]

ax.plot(times,disp,'k',linewidth=2,label=r'$\Delta t = 1e^{-3}s$'); 
ax.hold(True);


#########################################################################
thefile = "One_Bar_Dynamics_Dynamic_Vibration_1e6_1e-4.h5.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
disp = 1000*finput["/Model/Nodes/Generalized_Displacements"][5,:]

ax.plot(times,disp,'g',linewidth=2,label=r'$\Delta t = 1e^{-4}s$'); 
ax.hold(True);


#########################################################################
thefile = "One_Bar_Dynamics_Dynamic_Vibration_1e6_1e-5.h5.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
disp = 1000*finput["/Model/Nodes/Generalized_Displacements"][5,:]

ax.plot(times,disp,'b',linewidth=3,label=r'$\Delta t = 1e^{-5}s$'); 
ax.hold(True);


#########################################################################
# Analytical Solution
times = np.linspace(0, 5, num=5000);
disp  = 1000*abs(0.01*np.cos(10*times));


ax.plot(times,disp,'r',linewidth=2,label=r'Analytical'); 
ax.hold(True);







ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.08),
          ncol=2, fancybox=True, shadow=True)
# plt.show()


pylab.savefig("One_Bar_Dynamics_No_Damping_Stiff_1e6.pdf",  bbox_inches='tight')



