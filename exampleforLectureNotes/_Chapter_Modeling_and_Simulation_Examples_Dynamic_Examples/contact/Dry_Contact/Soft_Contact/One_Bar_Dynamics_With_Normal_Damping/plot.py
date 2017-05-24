#!/usr/bin/python
import h5py
import matplotlib.pylab as plt
import sys

thefile = "One_Bar_Dynamics_Dynamic_Vibration.h5.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
disp = finput["/Model/Nodes/Generalized_Displacements"][5,:]

# Configure the figure filename, according to the input filename.
outfig=thefile.replace("_","-")
outfigname=outfig.replace("h5.feioutput","pdf")

# Plot the figure. Add labels and titles.
plt.figure()
plt.plot(times,disp)
plt.grid()
plt.xlabel("Time [s] ")
plt.ylabel("Displacement [m]  ")
plt.savefig(outfigname,  bbox_inches='tight')
plt.show()

