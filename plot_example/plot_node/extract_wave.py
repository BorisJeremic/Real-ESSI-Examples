import numpy as np 
import h5py as h5 
import sys
import matplotlib.pyplot as plt 
# filename = sys.argv[1]
filename = "8NodeBrick_DRM_1D.h5.feioutput"
fileID = h5.File(filename, "r")


dis=fileID['/Model/Nodes/Generalized_Displacements'][()]
acc=fileID['/Model/Nodes/Generalized_Accelerations'][()]
time=fileID['/time'][()]


target_acc = acc[12]
target_dis = dis[12]

plt.plot(time, target_acc)
plt.xlabel("Time/(s)")
plt.ylabel("Acceleration/(m/s^2)")
plt.grid()
plt.savefig("top_acc.jpg")
plt.show()

plt.plot(time, target_dis)
plt.xlabel("Time/(s)")
plt.ylabel("Displacement/(m)")
plt.grid()
plt.savefig("target_dis.jpg")
plt.show()

# target_dis = dis[12]
# plt.plot(time, target_dis)
# plt.show()

with open('top_acc.txt', 'w') as f : 
	for i in range(len(time)) :
		f.write( str(time[i]) + " \t " + str(target_acc[i]) + "\n")

with open('top_dis.txt', 'w') as f : 
	for i in range(len(time)) :
		f.write( str(time[i]) + " \t " + str(target_dis[i]) + "\n")






# dis[42]
# dis[72]
# dis[102]
