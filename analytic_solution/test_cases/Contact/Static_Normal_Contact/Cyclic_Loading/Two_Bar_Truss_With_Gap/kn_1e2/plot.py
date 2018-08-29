#!/usr/bin/python
import h5py
import matplotlib.pylab as plt
import sys
import numpy as np


################ Node # 2 Displacement #############################
#######################################
## Analytical Solution
#######################################


finput = h5py.File('Analytical_Solution_Adding_Normal_Load.feioutput')

DISP = [];
# Read the time and displacement
times = finput["time"][:];
disp  = finput["/Model/Nodes/Generalized_Displacements"][3,:]
DISP  = np.append(DISP,disp);
# Plot the figure. Add labels and titles.
plt.figure()


finput = h5py.File('Analytical_Solution_Removing_Normal_Load.feioutput')
# Read the time and displacement
times = finput["time"][:]
disp = finput["/Model/Nodes/Generalized_Displacements"][3,:]
DISP  = np.append(DISP,disp);

finput = h5py.File('Analytical_Solution_Again_Adding_Normal_Load.feioutput')
# Read the time and displacement
times = finput["time"][:]
disp = finput["/Model/Nodes/Generalized_Displacements"][3,:]
DISP  = np.append(DISP,disp);
plt.plot(DISP,'-r',label='Analytical Solution')
plt.hold(True)


#######################################
## Current Solution
#######################################
finput = h5py.File('Verification_Of_Static_Cycylic_Contact_Adding_Normal_Load.h5.feioutput')

DISP = [];
# Read the time and displacement
times = finput["time"][:];
disp  = finput["/Model/Nodes/Generalized_Displacements"][3,:]
DISP  = np.append(DISP,disp);
# Plot the figure. Add labels and titles.

finput = h5py.File('Verification_Of_Static_Cycylic_Contact_Removing_Normal_Load.h5.feioutput')
# Read the time and displacement
times = finput["time"][:]
disp = finput["/Model/Nodes/Generalized_Displacements"][3,:]
DISP  = np.append(DISP,disp);

finput = h5py.File('Verification_Of_Static_Cycylic_Contact_Again_Adding_Normal_Load.h5.feioutput')
# Read the time and displacement
times = finput["time"][:]
disp = finput["/Model/Nodes/Generalized_Displacements"][3,:]
DISP  = np.append(DISP,disp);
plt.plot(DISP,'-k',label='Numerical Solution')
plt.hold(True)

plt.minorticks_on()
plt.xlabel("Time [s] ")
plt.ylabel("Displacement [m]  ")
plt.legend()
plt.savefig('Node_2_Displacement',  bbox_inches='tight')


################ Node # 2 Displacement #############################
#######################################
## Analytical Solution
#######################################


finput = h5py.File('Analytical_Solution_Adding_Normal_Load.feioutput')

DISP = [];
# Read the time and displacement
times = finput["time"][:];
disp  = finput["/Model/Nodes/Generalized_Displacements"][6,:]
DISP  = np.append(DISP,disp);
# Plot the figure. Add labels and titles.
plt.figure()


finput = h5py.File('Analytical_Solution_Removing_Normal_Load.feioutput')
# Read the time and displacement
times = finput["time"][:]
disp = finput["/Model/Nodes/Generalized_Displacements"][6,:]
DISP  = np.append(DISP,disp);

finput = h5py.File('Analytical_Solution_Again_Adding_Normal_Load.feioutput')
# Read the time and displacement
times = finput["time"][:]
disp = finput["/Model/Nodes/Generalized_Displacements"][6,:]
DISP  = np.append(DISP,disp);
plt.plot(DISP,'-r',label='Analytical Solution')
plt.hold(True)


#######################################
## Current Solution
#######################################
finput = h5py.File('Verification_Of_Static_Cycylic_Contact_Adding_Normal_Load.h5.feioutput')

DISP = [];
# Read the time and displacement
times = finput["time"][:];
disp  = finput["/Model/Nodes/Generalized_Displacements"][6,:]
DISP  = np.append(DISP,disp);
# Plot the figure. Add labels and titles.

finput = h5py.File('Verification_Of_Static_Cycylic_Contact_Removing_Normal_Load.h5.feioutput')
# Read the time and displacement
times = finput["time"][:]
disp = finput["/Model/Nodes/Generalized_Displacements"][6,:]
DISP  = np.append(DISP,disp);

finput = h5py.File('Verification_Of_Static_Cycylic_Contact_Again_Adding_Normal_Load.h5.feioutput')
# Read the time and displacement
times = finput["time"][:]
disp = finput["/Model/Nodes/Generalized_Displacements"][6,:]
DISP  = np.append(DISP,disp);
plt.plot(DISP,'-k',label='Numerical Solution')
plt.hold(True)

plt.minorticks_on()
plt.xlabel("Time [s] ")
plt.ylabel("Displacement [m]  ")
plt.legend()
plt.savefig('Node_3_Displacement',  bbox_inches='tight')

