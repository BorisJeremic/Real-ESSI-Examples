import numpy as np  
import matplotlib.pylab as plt


dis = np.loadtxt('dis.txt')

time = dis[:1900,0]
disp = dis[:1900,1]

plt.figure()
plt.plot(time,disp)
plt.grid()
plt.xlabel("Time (second) ")
plt.xlim([0, 20])
plt.ylabel("Displacements (meter)  ")
plt.savefig('input_motion.pdf',  bbox_inches='tight')



