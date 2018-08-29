### Private Comparison Script ###
### Sumeet Kumar Sinha, November, 2017 ##

### remove the log files
rm -rf *.log
python compare_HDF5_Element_Output.py Analytical_Solution_Normal_Stress.feioutput  Interface_Surface_Adding_axial_Load.h5.feioutput
python compare_HDF5_Element_Output.py Analytical_Solution_Shear.feioutput  Interface_Surface_Interface.h5.feioutput

printf "generating plots"
python Interface_Test_Normal_Plot.py 2> /dev/null
python Interface_Test_Shear_Plot.py 2> /dev/null
printf " ------------------------ completed !\n"
