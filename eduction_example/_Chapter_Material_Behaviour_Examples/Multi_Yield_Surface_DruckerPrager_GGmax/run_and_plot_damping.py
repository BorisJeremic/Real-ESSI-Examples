# ******************************************
# Function: plot stress-strain
# ******************************************
import numpy as np
import matplotlib.pyplot as plt  

def plot_stress_strain(stress_,strain_,figure_ID):
	essiGamma = [2*item for item in strain_]
	plt.plot(essiGamma, stress_, 'r-*', label=' ESSI')
	plt.legend(loc=2)
	plt.xlabel('Strain / (unitless)')
	plt.ylabel('Stress / (Pa)')
	plt.title('Material Behavior: Stress-Strain')
	plt.grid()
	plt.box()
	plt.savefig('stress-strain'+str(figure_ID)+'.pdf', transparent=True, bbox_inches='tight')
	plt.clf()
	# plt.show()


# ******************************************
# Function: run essi by shell
# ******************************************
from subprocess import call
import shlex as sh
def run_with_strain(strainIN):
	command = "essi -s strainIN=" + str(strainIN) + " -f main_damping.fei"
	call(sh.split(command))

# def collect_stress_strain_figures(Nstep):
# 	command = "mkdir " + str(Nstep) + " && mv stress-strain*.pdf " + str(Nstep)
# 	call(sh.split(command))
# ******************************************
# Function: Damping ratio calculation
# ******************************************
def count_increase(stress_):
	count = 0
	while(stress_[count]<stress_[count+1]):
		count = count + 1
	return count

def calc_damping(stress_, strain_):
	max_x = max(strain_)
	max_y = max(stress_)
	print "max_x = " + str(max_x)
	print "max_y = " + str(max_y)
	# calc Ws
	Ws = 0.5 * max_y * max_x 
	# calc Wd
	min_y = min(stress_)
	start = count_increase(stress_)
	print "start = " + str(start)
	loop_area = 0
	for x in xrange(start, 5*start):
		loop_area = loop_area + (strain_[x+1]-strain_[x]) * (stress_[x] + stress_[x+1] - 2*min_y)/2.
		# print "loop_increment = " + str(  (strain_[x+1]-strain_[x]) * (stress_[x] + stress_[x+1] - 2*min_y)/2.)
	Wd = loop_area
	# calc damping
	print "Wd = " + str(Wd)
	print "Ws = " + str(Ws)
	this_damping = Wd / 4.0 / np.pi / Ws
	return this_damping


# ******************************************
# Function Simulation with NStep
# ******************************************
def start_simulation(Nstep_):
	strain_incre_ = 1E-5
	max_strain = 1E-3
	[start, end] = np.log10([strain_incre_, max_strain])
	the_max_strain_size = np.logspace(start, end, Nstep_)
	print the_max_strain_size
	damping_ret = []
	print "the_damping: "
	for x in xrange(0,Nstep_):
		run_with_strain(the_max_strain_size[x]/2.)
		strain = np.loadtxt("strain.feioutput")
		stress = np.loadtxt("stress.feioutput")
		plot_stress_strain(stress,strain,x)
		the_damping = calc_damping(stress,strain)
		print the_damping
		damping_ret.append(the_damping)
	print "damping_ret: "
	print damping_ret
	# collect_stress_strain_figures(Nstep_)
	return [the_max_strain_size, damping_ret]


# ******************************************
# Start Simulation:
# ******************************************
[InputStrain, InputDamping] = start_simulation(11)
[ESSIStrain, ESSIDamping] = start_simulation(51)


# plot:
fontSIZE = 21
import matplotlib as mpl
label_size = fontSIZE
mpl.rcParams['xtick.labelsize'] = label_size 
mpl.rcParams['ytick.labelsize'] = label_size 

plt.semilogx(ESSIStrain, ESSIDamping,  'b-', label=' ESSI',  linewidth = 5.0 )
plt.semilogx(InputStrain, InputDamping,'r--', label='Input',  linewidth = 5.0 )
plt.legend(loc=2, prop={'size':fontSIZE})
plt.xlabel('Strain / (unitless)',fontsize=fontSIZE)
plt.ylabel('Damping Ratio/ (unitless)',fontsize=fontSIZE)
plt.title('Damping Plot',fontsize=fontSIZE)
plt.grid()
plt.box()
plt.savefig('damping.pdf', transparent=True, bbox_inches='tight')
plt.show()






# plt.title('Material Behavior: Stress-Strain',fontsize=fontSIZE)
# plt.grid()
# plt.box()
# plt.savefig('backbone.pdf', transparent=True, bbox_inches='tight')
# plt.show()





# # *******************************
# # One simulation for debug
# # *******************************
# x=9
# strain_incre = 1E-5
# max_strain = 1E-2
# Nstep =11
# [start, end] = np.log10([strain_incre, max_strain])
# the_max_strain_size = np.logspace(start, end, Nstep)
# print the_max_strain_size[x]/2.
# run_with_strain(the_max_strain_size[x]/2.)
# strain = np.loadtxt("strain.feioutput")
# stress = np.loadtxt("stress.feioutput")
# plot_stress_strain(stress,strain, x)
# the_damping = calc_damping(stress,strain)
# print the_damping

# strain_=strain
# stress_=stress
# max_x = max(strain_)
# max_y = max(stress_)
# # calc Ws
# Ws = 0.5 * max_y * max_x 
# # calc Wd
# loop_area = 0 
# strain_step_len = strain_[1] - strain_[0]
# print strain_step_len

# start = count_increase(stress)
# Num_increase_step =  int(max_x / strain_step_len)
# print Num_increase_step
# min_y = min(stress_)
# print min_y
# loop_area = 0
# for x in xrange(start, 5*start):
# 	loop_area = loop_area + (strain[x+1]-strain[x]) * (stress_[x] + stress_[x+1] - 2*min_y)/2.
# 	# print (strain[x+1]-strain[x]) * (stress_[x] + stress_[x+1] - 2*min_y)/2.

# print loop_area













