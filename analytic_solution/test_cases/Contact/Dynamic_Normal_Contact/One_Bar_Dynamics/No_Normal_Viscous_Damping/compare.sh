### Private Comparison Script ###
### Sumeet Kumar Sinha, November, 2017 ##

### remove the log files
rm -rf *.log
python compare_HDF5_Displacement_Output.py Analytical_Displacement.feioutput  One_Bar_Dynamics_Dynamic_Vibration.h5.feioutput

printf "generating plots"
python Displacement_Response.py 2> /dev/null
printf " ------------------------ completed !\n"
