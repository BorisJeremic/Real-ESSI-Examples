
###########################################################################################################################
#                                                                                                                         #
#                               Wet Contact Modelling in Real ESSI                                                        #
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                                      #
#                                                                                                                         #
#  GITHUB:: https://github.com/SumeetSinha                                                                                #
#                                                                                                                         #
#  Sumeet Kumar Sinha (September,2016)                                                                                    #
#  Computational Geomechanics Group                                                                                       #
#  University of California, Davis                                                                                        #
#  s u m e e t k s i n h a . c o m                                                                                        #
########################################################################################################################### 

from __future__ import print_function
import matplotlib.pylab as plt
import numpy as np
import h5py

f = h5py.File('CoupledContactEffect_Consolidation.h5.feioutput','r')

z_index = 30;

pressure          = f["/Model/Nodes/Generalized_Displacements"][3,:]
zdisp_at_interface = f["/Model/Nodes/Generalized_Displacements"][z_index,:]
# zdisp_at_top = f["/Model/Nodes/Generalized_Displacements"][79,:]
time = f["/time"][:]

# Plot the pressure figure. Add labels and titles.
plt.figure()
plt.plot(time,pressure/1000,'-',linewidth=2.0,)
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Pressure [kPa] ")
plt.savefig("Pressure_Plot.pdf",  bbox_inches='tight')
plt.show()



# Plot the displacementn figure. Add labels and titles.
plt.figure()
plt.plot(time,1000*zdisp_at_interface,label="At Surface",linewidth=2.0,)
# plt.plot(time,1000*zdisp_at_top,label="At Interface",linewidth=2.0,)
plt.grid()
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Displacement [mm] ")
plt.savefig("Displacement_Plot.pdf",  bbox_inches='tight')
plt.show()


f = h5py.File('Saturated_Contact_Modelling_Consolidation.h5.feioutput','r')

pressure          = f["/Model/Nodes/Generalized_Displacements"][3,:]
zdisp_at_interface = f["/Model/Nodes/Generalized_Displacements"][z_index,:]
# zdisp_at_top = f["/Model/Nodes/Generalized_Displacements"][79,:]
time = f["/time"][:]

# Plot the pressure figure. Add labels and titles.
plt.figure()
plt.plot(time,pressure/1000,'-',linewidth=2.0,)
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Pressure [kPa] ")
plt.savefig("Pressure_Plot_2.pdf",  bbox_inches='tight')
plt.show()



# Plot the displacementn figure. Add labels and titles.
plt.figure()
plt.plot(time,1000*zdisp_at_interface,label="At Surface",linewidth=2.0,)
# plt.plot(time,1000*zdisp_at_top,label="At Interface",linewidth=2.0,)
plt.grid()
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Displacement [mm] ")
plt.savefig("Displacement_Plot_2.pdf",  bbox_inches='tight')
plt.show()