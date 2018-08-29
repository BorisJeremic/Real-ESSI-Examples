### Private Comparison Script ###
### Sumeet Kumar Sinha, November, 2017 ##

### remove the log files
rm -rf *.log
python compare_HDF5_Displacement_Output.py Analytical_Solution_Adding_Normal_Load.feioutput  Verification_Of_Static_Cycylic_Contact_Adding_Normal_Load.h5.feioutput
python compare_HDF5_Displacement_Output.py Analytical_Solution_Again_Adding_Normal_Load.feioutput  Verification_Of_Static_Cycylic_Contact_Again_Adding_Normal_Load.h5.feioutput
python compare_HDF5_Displacement_Output.py Analytical_Solution_Removing_Normal_Load.feioutput  Verification_Of_Static_Cycylic_Contact_Removing_Normal_Load.h5.feioutput

printf "generating plots"
python plot.py 2> /dev/null
printf " ------------------------ completed !\n"
