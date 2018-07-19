import numpy as np 
import h5py as h5 
import sys
import os
import matplotlib.pyplot as plt 


# *************************************************************************************
# Plot Freq Parameters
# *************************************************************************************
plotFreq_min = 0.1
plotFreq_max = 20
# # #############################
import matplotlib.pylab as pylab
params = {
'legend.fontsize': 'xx-large',
          'figure.figsize': (20, 10),
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'xx-large',
         'ytick.labelsize':'xx-large'
}
pylab.rcParams.update(params)
# #############################
# *************************************************************************************
# FFT function
# *************************************************************************************
import scipy.fftpack
import math
def FFT(x,dt):
	N = x.size;
	T = N*dt;
	Fs = 1./dt;
	xfft  = scipy.fftpack.fft(x);
	xfreq = np.linspace(0.0, Fs/2, N/2);
	xfftHalf = 2.0/N * np.abs(xfft[:N//2]);
	xfftHalf[0] = xfftHalf[0]/2;
	return xfreq, xfftHalf

# *************************************************************************************
# PreProcess user's arguments
# *************************************************************************************
reference_motion_file = sys.argv[1]
out_motion_file = sys.argv[2]

out_filename = out_motion_file.split('.txt')[0]
# *************************************************************************************


# *************************************************************************************
# Read the File 
# *************************************************************************************
refer_data = np.loadtxt(reference_motion_file)
out_data = np.loadtxt(out_motion_file)
refer_time = refer_data[:,0]
refer_acc = refer_data[:,1]
out_time = out_data[:,0]
out_acc = out_data[:,1]



# *************************************************************************************
# Plot the data in time domain.
# *************************************************************************************
f, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(refer_time, refer_acc, '--k', linewidth=3, label='Soil Surface Motion')
ax1.plot(out_time, out_acc, '-k', linewidth=3, label='Structural Top Motion')
ax1.legend()
ax1.set( xlabel = "Time [s]", ylabel = "Acceleration [m/s^2]", title = "Time Series of Acceleration")
ax1.grid()


# *************************************************************************************
# Plot the data in frequency domain.
# *************************************************************************************
refer_freq, refer_ampl = FFT( refer_acc, refer_time[1]-refer_time[0] )
out_freq, out_ampl = FFT( out_acc, refer_time[1]-refer_time[0] )
ax2.semilogx(refer_freq, refer_ampl, '--k', linewidth=3, label='Soil Surface Motion')
ax2.semilogx(out_freq, out_ampl, '-k', linewidth=3, label='Structural Top Motion')
ax2.legend(loc=2)
ax2.set( xlabel = "Frequency [Hz] ", ylabel = "Acceleration [m/s^2] ", xlim = [plotFreq_min, plotFreq_max] , title = "FFT of Acceleration")
# *****************************
a = np.linspace(0.1,1,10)
b = np.linspace(2,10,9) 
c = np.concatenate((a,b))
plt.xticks(c)
# *****************************
ax2.grid()
plt.savefig( out_filename + "_compare.pdf" )
plt.show()






# # *************************************************************************************
# # Write the data to a txt file
# # *************************************************************************************
# with open(out_filename + '.txt', 'w') as f : 
# 	for i in range(len(time)) :
# 		f.write( str(time[i]) + " \t " + str(target_acc[i]) + "\n")

# print(" Data is written to " + out_filename + '.txt')


