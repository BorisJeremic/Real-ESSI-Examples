
import numpy as np 

data = np.loadtxt('Cerro237_US_all_001_9Hz_clean.dat')

time = data[:,0]
acce = data[:,1]
velo = data[:,2]
disp = data[:,3]


with open('acce.txt','w') as f:
	for x in range(len(time)):
		f.write( str(time[x]) + ' \t ' + str(acce[x]) + ' \n')


with open('velo.txt','w') as f:
	for x in range(len(time)):
		f.write( str(time[x]) + ' \t ' + str(velo[x]) + ' \n')



with open('disp.txt','w') as f:
	for x in range(len(time)):
		f.write( str(time[x]) + ' \t ' + str(disp[x]) + ' \n')


