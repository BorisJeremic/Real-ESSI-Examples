import numpy as np
import matplotlib.pyplot as plt  

# target
userInput1= [0,3.16200000000000e-07,1.00000000000000e-06,3.16227766016838e-06,1.00000000000000e-05,2.23606797749979e-05,5.00000000000000e-05,7.07106781186548e-05,0.000100000000000000,0.000223606797749979,0.000500000000000000,0.000707106781186548,0.00100000000000000,0.00223606797749979,0.00500000000000000,0.00707106781186548,0.0100000000000000];  
userInput2= [1,0.997819460000000,0.995638920000000,0.981193900000000,0.966748880000000,0.919966125000000,0.873183370000000,0.830267645000000,0.787351920000000,0.627273280000000,0.467194640000000,0.393814435000000,0.320434230000000,0.214917680000000,0.109401130000000,0.0864393250000000,0.0634775200000000];
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

# avoid the divide by zero
fontSIZE = 21
import matplotlib as mpl
label_size = fontSIZE
mpl.rcParams['xtick.labelsize'] = label_size 
mpl.rcParams['ytick.labelsize'] = label_size 

stress_plot = [1./4000* x for x in tau]
essi_stress_plot = [1./4000* x for x in stress]
plt.plot(essiGamma, essi_stress_plot, 'b-', label=' ESSI',  linewidth = 5.0 )
plt.plot(gamma, stress_plot, 'r--', label='Input',  linewidth = 5.0 )
plt.legend(loc=2, prop={'size':fontSIZE})
plt.xlabel('Strain / (unitless)',fontsize=fontSIZE)
plt.ylabel('Stress / (kPa)',fontsize=fontSIZE)
plt.title('Material Behavior: Stress-Strain',fontsize=fontSIZE)
plt.grid()
plt.box()
plt.savefig('full-loop.pdf', transparent=True, bbox_inches='tight')
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



