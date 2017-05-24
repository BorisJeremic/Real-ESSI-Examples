import numpy as np
import matplotlib.pyplot as plt  

# target
userInput1= [0,1E-6,1E-5,5E-5,1E-4, 0.0005, 0.001, 0.005, 0.01];  
userInput2= [1,0.99563892,0.96674888,0.87318337,0.78735192,0.46719464,0.32043423,0.10940113,0.06347752];
Gmax = 3E8;
poisson = 0.0;
# #################################
gamma = userInput1
GGmax = userInput2
G=[Gmax * item for item in GGmax]

tau = np.zeros(len(gamma))
for it in xrange(1,len(gamma)):
	tau[it] = gamma[it] * G[it]

print tau

epsilon = [item/2. for item in gamma]

# # ============================================
# # Figure 1
# # Plot the stress-strain
# # ============================================
strain = np.loadtxt("strain.feioutput")
stress = np.loadtxt("stress.feioutput")

essiGamma = [2*item for item in strain]

plt.plot(gamma, tau, 'b-^', label='Input' )
plt.plot(essiGamma, stress, 'r-*', label=' ESSI')
plt.legend(loc=2)
plt.xlabel('Strain / (unitless)')
plt.ylabel('Stress / (Pa)')
plt.title('Material Behavior: Stress-Strain')
plt.grid()
plt.box()
plt.savefig('backbone.pdf', transparent=True, bbox_inches='tight')
plt.show()



# # ============================================
# # Figure 3
# # Plot the G/Gmax
# # ============================================
# # avoid the divide by zero
# stress[0]=stress[1]
# strain[0]=strain[1]
# essiG = [a/b/2. for a,b in zip(stress, strain)]
# essiGGmax = [item/Gmax for item in essiG]

# plt.semilogx(essiGamma, essiGGmax, label='ESSI')
# plt.semilogx(gamma , GGmax , label='Input')

# plt.legend(loc=3)
# plt.title('Multi-Yield-Surface vonMises G/Gmax')
# plt.xlabel('Strain / (unitless)')
# plt.ylabel('G/Gmax / (unitless)')
# plt.grid()
# plt.box()
# plt.savefig('GGmax.pdf', transparent=True, bbox_inches='tight')
# plt.show()



