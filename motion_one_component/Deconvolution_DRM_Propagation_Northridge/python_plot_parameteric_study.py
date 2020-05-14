import scipy as sp
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib 
import sys 
import matplotlib.lines as lines
import h5py
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as ticker
from scipy.fftpack import fft

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


def node_response_extraction_sequential(node_ID, file_name, num_DOF): 

    h5_file = h5py.File(file_name, 'r');

    Time = h5_file['time'][:]; 

    displacement_index = int(h5_file['Model/Nodes/Index_to_Generalized_Displacements'][node_ID]);

    displacement_component = h5_file['Model/Nodes/Generalized_Displacements'][int(displacement_index):int(displacement_index+num_DOF), :]; 

    acceleration_component = h5_file['Model/Nodes/Generalized_Accelerations'][int(displacement_index):int(displacement_index+num_DOF), :]; 

    for x1 in xrange(0,num_DOF):

        displacement_component[x1,:] = displacement_component[x1,:]-displacement_component[x1,0]; ### in case self weight loading stage, get relative displacement 

    return Time, displacement_component, acceleration_component;


numbercol = 1; 

surface_node_ID = 252;  ##  252, 250, 249, 251 

node_ID = [252, 212, 172, 132, 92, 52, 12];  ## node ID from surface to bottom 

depth = [0, 2, 4, 6, 8, 10, 12]; 

bottom_node_ID = 6;   ## node just beyond DRM layer 


file_name = 'Motion1C_DRM_propagation.h5.feioutput'  ## 

parameteric_case = 'Motion1C_Northridge' ## 

### ==========================================================================

postfix = '.feioutput'; 

middle_name_less_than_ten = '0'; 

num_DOF = 3; 

Time, displacement_component_surface, acceleration_component_surface = node_response_extraction_sequential(surface_node_ID, file_name, num_DOF); 

Time, displacement_component_bottom, acceleration_component_bottom = node_response_extraction_sequential(bottom_node_ID, file_name, num_DOF); 

# surface_acc = np.loadtxt('Kobe_acc.txt'); 

# surface_disp = np.loadtxt('Kobe_disp.txt'); 

surface_acc = np.loadtxt('scaled_northridge_acc.dat'); 

surface_disp = np.loadtxt('scaled_northridge_dis.dat'); 

########################################################################################
#######===== Print acceleration of nodes ===== ######
########################################################################################

fig = plt.figure()

ax = fig.add_subplot(111)

ax.plot(surface_acc[:, 0], surface_acc[:, 1], '-r', label='surface analytical', linewidth= 1.5); 

ax.plot(Time[200:]-2.0, acceleration_component_surface[0, 200:], '-k', label='DRM propagation', linewidth= 0.5); 


plt.gca().set_xlim([0,38]); 

# plt.gca().set_ylim([-10,10]); 

# plt.gca().get_xaxis().set_ticks(np.arange(0, 60.1, 10))

# plt.gca().get_yaxis().set_ticks(np.arange(-15, 3.1, 3))

plt.gca().get_yaxis().set_major_formatter(ticker.FormatStrFormatter('%0.2f'))

plt.gca().get_xaxis().set_tick_params(direction='in',labelsize='x-large')

plt.gca().get_yaxis().set_tick_params(direction='in',labelsize='x-large')

plt.xlabel('Time [s]', fontproperties=axial_label_font); 

plt.ylabel('Acc. [$m/s^2$]', fontproperties=axial_label_font); 

plt.grid(True); 

plt.legend(ncol= numbercol, loc='upper right', prop=legend_label_font); 

filename = 'acc_check_'+ parameteric_case + '.pdf'

plt.savefig(filename, bbox_inches='tight'); 

plt.show(); 

# # # ########################################################################################
# # # #######======================== Print Time series response along the depth  ===== ######
# # # ########################################################################################

# print "Plot acceleration records along depth!"; 

# fig = plt.figure()

# ax = fig.add_subplot(111)

# # scale_meter = 7; 

# # plt.gca().text(32.7, 1.25, '$1g$', fontsize=20)

# # l1 = lines.Line2D([32, 32], [0.5, 0.5+10/scale_meter], color='k', linewidth=2.0)

# # l2 = lines.Line2D([31.7, 32.3], [0.5, 0.5], color='k', linewidth=0.5)

# # l3 = lines.Line2D([31.7, 32.3], [0.5+10/scale_meter, 0.5+10/scale_meter], color='k', linewidth=0.5)


# # plt.gca().add_line(l1); 

# # plt.gca().add_line(l2);

# # plt.gca().add_line(l3);


# PGA_depth = sp.zeros(len(depth)); 

# for x in xrange(0,len(node_ID)):

#     current_node = node_ID[x];

#     current_depth = depth[x];

#     Time, current_displacement_component, current_acceleration_component = node_response_extraction_sequential(current_node, file_name, num_DOF); 

#     plot_current_acceleration = current_depth + current_acceleration_component/15.0;  ## scale acceleration    

#     PGA_depth[x] = max(abs(current_acceleration_component[0, :])); 

#     ax.plot(Time, plot_current_acceleration[0, :], '-k', linewidth= 1);


# plt.gca().set_ylim([-1,13]); 

# plt.gca().invert_yaxis()


# # plt.gca().get_xaxis().set_ticks(np.arange(0, 60.1, 10))

# # plt.gca().get_yaxis().set_ticks(np.arange(-15, 3.1, 3))

# plt.gca().get_yaxis().set_major_formatter(ticker.FormatStrFormatter('%0.2f'))

# plt.gca().get_xaxis().set_tick_params(direction='in',labelsize='x-large')

# plt.gca().get_yaxis().set_tick_params(direction='in',labelsize='x-large')

# plt.xlabel('Time [s]', fontproperties=axial_label_font); 

# plt.ylabel('Depth. [m]', fontproperties=axial_label_font); 

# plt.grid(True); 

# plt.legend(ncol= numbercol, loc='upper right', prop=legend_label_font); 

# filename = 'acc_depth_'+ parameteric_case + '.pdf'

# plt.savefig(filename, bbox_inches='tight'); 

# plt.show(); 
