import matplotlib.pyplot as plt 
import numpy as np 
import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

# filename1 = "essi_ricker_at_depth_60_acc.txt"
# filename2 = "input_acc.txt"

dat1 = np.loadtxt(filename1)
dat2 = np.loadtxt(filename2)

time1 = dat1[:,0]
acc1 = dat1[:,1]

time2 = dat2[:,0]
acc2 = dat2[:,1]
# acc2 = [item * 10.0  for item in acc2]
plt.plot(time1, acc1, linewidth= 2, label = filename1)
plt.plot(time2, acc2, linewidth= 2, label = filename2)
plt.legend()
plt.xlabel("Time/(second) ")
plt.ylabel("Amplitude/(meter) ")
plt.grid()
plt.savefig("compare_"+filename1 +"_"+filename2 + ".jpg")
plt.show()


