### Private Comparison Script ###

rm *.log
python compare_HDF5_ALL.py Analytical_Solution.feioutput  Verification_of_contact_yield_surface_Shear_Loading.h5.feioutput
printf "generating plots"
python plot.py 2> /dev/null
printf " ------------------------ completed !\n"