#!/bin/bash
# Format
# python script_path/script.py your_outputfilename.feioutput node_tag <x|y|z>

# Example:

# plot displacment in time and frequency domain at node #  in x direction.
python postprocess/plot_node_disp.py full_box_D_imposed_motion.h5.feioutput 8211 x
python postprocess/plot_node_disp.py full_box_D_imposed_motion.h5.feioutput 6045 x
python postprocess/plot_node_disp.py full_box_D_imposed_motion.h5.feioutput 3157 x

# # plot acceleration in time and frequency domain at node #  in x direction.
python postprocess/plot_node_acce.py full_box_D_imposed_motion.h5.feioutput 8211 x
python postprocess/plot_node_acce.py full_box_D_imposed_motion.h5.feioutput 6045 x
python postprocess/plot_node_acce.py full_box_D_imposed_motion.h5.feioutput 3157 x

# # plot response spectrum (pseudo acceleration/displacement) in frequency domain at node # 3391 in x direction.
python postprocess/plot_node_spectrum_in_freq.py full_box_D_imposed_motion.h5.feioutput 8211 x
python postprocess/plot_node_spectrum_in_freq.py full_box_D_imposed_motion.h5.feioutput 6045 x
python postprocess/plot_node_spectrum_in_freq.py full_box_D_imposed_motion.h5.feioutput 3157 x

# # plot response spectrum (pseudo acceleration/displacement) in period domain at node # 3391 in x direction.
python postprocess/plot_node_spectrum_in_period.py full_box_D_imposed_motion.h5.feioutput 8211 x
python postprocess/plot_node_spectrum_in_period.py full_box_D_imposed_motion.h5.feioutput 6045 x
python postprocess/plot_node_spectrum_in_period.py full_box_D_imposed_motion.h5.feioutput 3157 x
