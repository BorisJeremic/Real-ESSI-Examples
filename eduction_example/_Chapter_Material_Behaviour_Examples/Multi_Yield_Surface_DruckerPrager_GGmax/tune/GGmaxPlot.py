import numpy as np
import matplotlib.pyplot as plt  
# #################################
userInput1= [0,1E-6,1E-5,5E-5,1E-4];
userInput2= [1,0.995,0.964,0.863,0.772];
Gmax = 3E8;
poisson = 0.0;
# #################################
gamma = userInput1
GGmax = userInput2
G=[Gmax * item for item in GGmax]

tau = np.zeros(len(gamma))
# for it in xrange(1,len(gamma)):
# 	tau[it] = gamma[it] * G[it-1]

tau = [a * b for a,b in zip(G,gamma)]

ys_size = [item*np.sqrt(3.) for item in tau] ;

H=np.zeros(len(tau)-1)
for it in xrange(1,len(tau)-1):
	H[it-1] = 2 * (tau[it+1] - tau[it])/(gamma[it+1]-gamma[it])

H[-1]=H[-2]/3

H_prime = [1/ ((1/item) - (1/2./Gmax))  for item in H]

# ys_size_ = ys_size.pop(0)
# p_ys_size = ' '.join(str(item) for item in ys_size_)
# p_H_prime = ' '.join(str(item) for item in H_prime)

# p_ys_size
# p_H_prime

x0 = [0, 0.0001, 0.0010, 0.0050, 0.0100, 0.0500, 0.1000, 0.5000, 1.0000] ; 
tau0 = [0, 0.0060, 0.0578, 0.2588, 0.4630, 1.3334, 1.8359, 3.0262, 3.3407];
epsilon12 = [item/100 for item in x0];
tau12 = [item*1E5 for item in tau0];
N_Inc=[0,1,2,3,4,5,6,7];

rang=5
print epsilon12
print tau12
# #################################
strain_stress = np.loadtxt("strain_stress.txt")
# strain = np.loadtxt("strain.feioutput")
# stress = np.loadtxt("stress.feioutput")
strain=strain_stress[:,0]
stress=strain_stress[:,1]
n_active = strain_stress[:,2]
dstress = np.zeros(np.size(stress));
for i in xrange(1,len(stress)):
	dstress[i]=stress[i]-stress[i-1]
plt.subplot(311)
plt.plot(strain, stress,'b-*', label='essi')
plt.plot(epsilon12[:rang] , tau12[:rang] ,'r-^',label='target')
plt.legend(loc=4)
plt.xlabel(' Strain / (unitless)')
plt.ylabel(' Stress / (Pa)')
plt.title('Material Behavior: Stress-Strain')
plt.grid()
plt.box()


plt.subplot(312)
plt.plot(strain, n_active,'b-*', label='essi')
plt.plot(epsilon12[:rang] , N_Inc[:rang] ,'r-^',label='target')
plt.legend(loc=4)
plt.xlabel(' Strain / (unitless)')
plt.ylabel(' N_active ')
plt.grid()
plt.box()

plt.subplot(313)
plt.plot(strain, dstress)
plt.xlabel(' Strain / (unitless)')
plt.ylabel(' dstress / (Pa)')
plt.grid()
plt.box()

plt.savefig('result.pdf', transparent=True, bbox_inches='tight')
plt.show()
