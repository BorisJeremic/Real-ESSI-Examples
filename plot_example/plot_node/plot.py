import matplotlib.pyplot as plt 
import numpy as np 
import sys

filename1 = sys.argv[1]

dat1 = np.loadtxt(filename1)

time1 = dat1[:,0]
acc1 = dat1[:,1]

# time2 = dat2[:,0]
# acc2 = dat2[:,1]

plt.plot(time1, acc1, linewidth= 2, label = filename1)
plt.legend()
plt.xlabel("Time/(second) ")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig(filename1 + ".jpg")
plt.show()


