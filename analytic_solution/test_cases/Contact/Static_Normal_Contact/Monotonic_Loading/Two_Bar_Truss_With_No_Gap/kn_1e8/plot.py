#!/usr/bin/python
import h5py
import matplotlib.pylab as plt
import sys


################ Node # 2 Displacement #############################
## Analytical Solution
finput = h5py.File('Analytical_Solution.feioutput')

# Read the time and displacement
times = finput["time"][:]
disp = finput["/Model/Nodes/Generalized_Displacements"][3,:]

# Plot the figure. Add labels and titles.
plt.figure()
plt.plot(times,disp,'-r',label='Analytical Solution')
plt.xlabel("Time [s] ")
plt.ylabel("Displacement [m]  ")
plt.hold(True)

## Current Solution
finput = h5py.File('Verification_Of_Static_Normal_Contact_Adding_Normal_Load.h5.feioutput')

# Read the time and displacement
times = finput["time"][:]
disp = finput["/Model/Nodes/Generalized_Displacements"][3,:]

# Plot the figure. Add labels and titles.
plt.plot(times,disp,'-k',label='Numerical Solution')
# plt.grid(b=True, which='major', color='k', linestyle='-')
# plt.grid(b=True, which='minor', color='r', linestyle='-', alpha=0.2)
plt.minorticks_on()
plt.xlabel("Time [s] ")
plt.ylabel("Displacement [m]  ")
plt.legend()
plt.savefig('Node_2_Displacement',  bbox_inches='tight')
#plt.show()


################ Node # 3 Displacement #############################
## Analytical Solution
finput = h5py.File('Analytical_Solution.feioutput')

# Read the time and displacement
times = finput["time"][:]
disp = finput["/Model/Nodes/Generalized_Displacements"][6,:]

# Plot the figure. Add labels and titles.
plt.figure()
plt.plot(times,disp,'-r',label='Analytical Solution')
plt.hold(True)

## Current Solution
finput = h5py.File('Verification_Of_Static_Normal_Contact_Adding_Normal_Load.h5.feioutput')

# Read the time and displacement
times = finput["time"][:]
disp = finput["/Model/Nodes/Generalized_Displacements"][6,:]

# Plot the figure. Add labels and titles.
plt.plot(times,disp,'-k',label='Numerical Solution')
# plt.grid(b=True, which='major', color='k', linestyle='-')
# plt.grid(b=True, which='minor', color='r', linestyle='-', alpha=0.2)
plt.minorticks_on()
plt.xlabel("Time [s] ")
plt.ylabel("Displacement [m]  ")
plt.legend()
plt.savefig('Node_3_Displacement',  bbox_inches='tight')
#plt.show()
