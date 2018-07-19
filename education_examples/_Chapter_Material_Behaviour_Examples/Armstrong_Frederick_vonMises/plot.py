import numpy as np
import matplotlib.pyplot as plt  

# ===========================================
# Font size
# ===========================================
import matplotlib
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}
matplotlib.rc('font', **font)
# ===========================================

strain = np.loadtxt("strain.feioutput")
stress = np.loadtxt("stress.feioutput")

stress_p = [ val/1000 for val in stress]
strain_p = [ val*100 for val in strain]

plt.figure(figsize=(10,8))
plt.plot(strain_p, stress_p,'k', linewidth=2)
plt.xlabel('Strain [%]')
plt.ylabel('Stress [kPa]')
plt.title('Material Behavior: Stress-Strain')
plt.grid()
plt.box()
plt.savefig('result.pdf', transparent=True, bbox_inches='tight')
plt.show()
