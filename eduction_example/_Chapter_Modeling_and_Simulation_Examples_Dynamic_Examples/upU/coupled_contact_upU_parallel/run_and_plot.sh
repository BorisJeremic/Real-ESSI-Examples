rm -f *.feioutput
rm -f essi*.log
rm -f gmon.out
rm -f RealESSI_VERSION_INFO.txt
rm -f petsc_log.txt

if hash essi_parallel 2>/dev/null; then # check if essi_parallel is available
    mpirun -np 4 essi_parallel -f main.fei
else
    echo "ERROR!!! Example Consolidation_Test_Parallel require essi_parallel but it's not installed!!" 
    exit
fi
# python plot.py

# for pvESSI, pvpython and paraview if available
# pvpython pvESSI_camera.py *h5.feioutput
