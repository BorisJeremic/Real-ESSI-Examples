### Private Comparison Script ###
### Sumeet Kumar Sinha, November, 2017 ##

### remove the log files
rm -rf *.log
python compare_HDF5_Element_Output.py Analytical_Solution.feioutput  Monotonic_Contact_Behaviour_Adding_Normal_Load.h5.feioutput
printf "generating plots"
python plot.py 2> /dev/null
printf " ------------------------ completed !\n"
