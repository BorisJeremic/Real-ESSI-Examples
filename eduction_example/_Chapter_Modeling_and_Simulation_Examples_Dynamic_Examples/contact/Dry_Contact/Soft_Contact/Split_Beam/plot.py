#!/usr/bin/python
import h5py
import matplotlib.pylab as plt
import sys

# Go over each feioutput and plot each one.  
thefile = "Split_Beam_Analysis_Free_Vibration.h5.feioutput";
finput = h5py.File(thefile)

# Read the time and displacement
times = finput["time"][:]
disp = finput["/Model/Nodes/Generalized_Displacements"][505,:]

# Configure the figure filename, according to the input filename.
outfig=thefile.replace("_","-")
outfigname=outfig.replace("h5.feioutput","pdf")

# Plot the figure. Add labels and titles.
plt.figure()
plt.plot(times,disp)
plt.grid(b=True, which='major', color='k', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='-', alpha=0.2)
plt.minorticks_on()
plt.xlabel("Time [s] ")
plt.ylabel("Displacements in y-direction [m]  ")
plt.savefig(outfigname,  bbox_inches='tight')
plt.show()


