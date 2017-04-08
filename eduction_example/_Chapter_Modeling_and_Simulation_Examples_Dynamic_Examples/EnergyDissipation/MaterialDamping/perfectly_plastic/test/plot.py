import numpy as np
import matplotlib.pyplot as plt  
import h5py 

h5in_filename = "brick_5element_freeVibration.h5.feioutput"

h5in=h5py.File(h5in_filename,"r")
outputs_all=h5in['/Model/Elements/Gauss_Outputs'][()]

stress = outputs_all[16 , :-1]
strain = outputs_all[4  , :-1]


plt.plot(strain, stress)
# plt.show()
plt.grid()
plt.xlabel("Strain ")
plt.ylabel("Stress (Pa)  ")
plt.savefig("results.pdf",  bbox_inches='tight')
