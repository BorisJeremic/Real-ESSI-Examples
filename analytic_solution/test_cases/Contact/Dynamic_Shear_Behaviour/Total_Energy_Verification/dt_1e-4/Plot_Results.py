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
ax.set_ylabel(r"Energy  [J]  ",fontsize=30)

# #########################################################################
thefile = "Frictional_SDOF_freeVibration.h5.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
disp = finput["/Model/Nodes/Generalized_Displacements"][3,:]
acc  = finput["/Model/Nodes/Generalized_Accelerations"][3,:]


n = len(acc);
dt = times[1] - times[0];
vel  = acc;
vel[0]=0;

for i in xrange(1,n):
	vel[i]=vel[i-1]+(acc[i])*dt;

E_k = 0.5*vel*vel;
E_s = 0.5*100*disp*disp;

# kinetic energy 
ax.plot(times,E_k,'b',linewidth=4,label=r'$E_{kinetic}$'); 
ax.hold(True);

# potential energy 
ax.plot(times,E_s,'k',linewidth=4,label=r'$E_{potential}$'); 
ax.hold(True);

# Contact Energy 
# #########################################################################
# Read the time and displacement
times = finput["time"][:]
Fx = finput["/Model/Elements/Element_Outputs"][5,:]
Deltax = finput["/Model/Elements/Element_Outputs"][8,:]

E_inc_d = Fx*Deltax;
E_inc_d[0] =0;
Deltax[0]=0;
E_d = Fx*Deltax;
E_d[0] =0;

for i in xrange(1,n):
	E_d[i]=E_d[i-1]+ E_d[i];

ax.plot(times,E_d,'r',linewidth=4,label=r'$E_{dis}$'); 
ax.hold(True);

# Total Energy 
# #########################################################################
E_total = E_k +E_s + E_d;

ax.plot(times,E_total,'g',linewidth=4,label=r'$E_{total}$'); 
# ax.hold(True);




ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.155),
          ncol=4, fancybox=True, shadow=True)
# plt.show()


pylab.savefig("Total_Energy_Plot_With_Components.pdf",  bbox_inches='tight')


ax.hold(False);
fig = plt.figure();
ax = plt.subplot(111)
ax.plot(times,E_inc_d*1000,'r',linewidth=4,label=r'$E^{incr}_{dis}$'); 
# ax.plot(times,E_d,'b',linewidth=4,label=r'$E_{dis}$'); 
ax.grid()
ax.set_xlabel("Time [s] ")
ax.set_ylabel(r"Energy  [mJ]  ")
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.24),
          ncol=4, fancybox=True, shadow=True)

pylab.savefig("Incremental_Dissipated_Energy.pdf",  bbox_inches='tight')

# plt.show()
