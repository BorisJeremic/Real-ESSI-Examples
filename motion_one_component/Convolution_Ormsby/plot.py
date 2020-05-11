import scipy as sp
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib 
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as ticker
from scipy.fftpack import fft
from scipy.signal import butter, lfilter, freqz

axial_label_font = FontProperties()
axial_label_font.set_family('sans-serif')
axial_label_font.set_style('normal')
axial_label_font.set_weight('bold')
# axial_label_font.set_size('x-large')
axial_label_font.set_size(20)


legend_label_font = FontProperties()
legend_label_font.set_family('sans-serif')
legend_label_font.set_style('normal')
legend_label_font.set_weight('normal')
# legend_label_font.set_size('large')
legend_label_font.set_size(16)

numbercol = 1; 

surface_acc = np.loadtxt('z_at_depth_0_acc.txt'); 

acc_depth12 = np.loadtxt('Ormsby_depth_12_acc.txt');   

fig = plt.figure()

ax = fig.add_subplot(111)



ax.plot(surface_acc[:, 0], surface_acc[:, 1], '-r', label='Convolution motion @ surface', linewidth= 2.0); 

ax.plot(acc_depth12[:, 0], acc_depth12[:, 1], '-k', label='Input motion @ 12m depth', linewidth= 1.0); 

plt.gca().set_ylim([-20,20]); 

# plt.gca().get_xaxis().set_ticks(np.arange(0, 60.1, 10))

# plt.gca().get_yaxis().set_ticks(np.arange(-15, 3.1, 3))

plt.gca().get_yaxis().set_major_formatter(ticker.FormatStrFormatter('%0.2f'))

plt.gca().get_xaxis().set_tick_params(direction='in',labelsize='x-large')

plt.gca().get_yaxis().set_tick_params(direction='in',labelsize='x-large')

plt.xlabel('Time [s]', fontproperties=axial_label_font); 

plt.ylabel('Acc. [$m/s^2$]', fontproperties=axial_label_font); 

plt.grid(True); 

plt.legend(ncol= numbercol, loc='upper right', prop=legend_label_font); 

plt.savefig('acc_convolution.pdf', bbox_inches='tight'); 

plt.show(); 


