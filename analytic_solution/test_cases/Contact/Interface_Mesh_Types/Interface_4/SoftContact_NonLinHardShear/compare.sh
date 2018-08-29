### Private Comparison Script ###
### Sumeet Kumar Sinha, November, 2017 ##

### remove the log files
rm -rf *.log
python compare_HDF5_Element_Output.py Origin_Interface_Surface_Adding_axial_Load.feioutput  Interface_Surface_Adding_axial_Load.h5.feioutput
python compare_HDF5_Element_Output.py Origin_Interface_Surface_Interface.feioutput  Interface_Surface_Interface.h5.feioutput
# 
printf "generating plots"
python Interface_Test_Normal_Plot.py 2> /dev/null
python Interface_Test_Shear_Plot.py 
printf " ------------------------ completed !\n"
