### Private Comparison Script ###
### Sumeet Kumar Sinha, November, 2017 ##

### remove the log files
rm -rf *.log
python compare_HDF5_Element_Output.py Analytical_Solution_Normal_Stress.feioutput  Monotonic_Contact_Behaviour_Adding_Normal_Load.h5.feioutput
python compare_HDF5_Element_Output.py Analytical_Solution_Shear.feioutput  Monotonic_Contact_Behaviour_Adding_Tangential_Load.h5.feioutput

printf "generating plots"
python Normal_Stress_Plot.py 2> /dev/null
python Normalized_Shear_Stress_Plot.py 2> /dev/null
printf " ------------------------ completed !\n"
