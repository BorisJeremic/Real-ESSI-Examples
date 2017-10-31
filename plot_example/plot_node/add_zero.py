import matplotlib.pyplot as plt 
import numpy as np 
import sys

filename1 = sys.argv[1]
# filename1 = "northridge.dat"

dat1 = np.loadtxt(filename1)

time1 = dat1[:,0]
acc1 = dat1[:,1]

add_time = 0.5 ; 

time_step = time1[1] - time1[0]
Ntime = len(time1)
total_time = time1[Ntime-1]
total_time = total_time + add_time * 2 ; 
time = np.linspace(0, total_time, total_time/time_step+1)
acc_zero = np.zeros(int(add_time/time_step)) ; 

acc = np.concatenate((acc_zero, acc1),axis=0) ; 
acc = np.concatenate((acc, acc_zero), axis=0) ; 




plt.plot(time, acc, linewidth= 2, label = filename1)
plt.legend()
plt.xlabel("Time/(second) ")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig(filename1 + ".jpg")
plt.show()

with open("added_"+filename1,'w') as f:
	for i in range(len(time)):
		f.write(str(time[i]) + " \t " + str(acc[i]) + " \n")

