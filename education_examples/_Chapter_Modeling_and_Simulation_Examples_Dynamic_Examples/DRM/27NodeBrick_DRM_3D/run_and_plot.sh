rm -f *.feioutput
rm -f petsc_log.txt
rm -f essi*.log

if hash essi_parallel 2>/dev/null; then # check if essi_parallel is available
    mpirun -np 4 essi_parallel -f main.fei
else
    echo "ERROR!!! Example 27NodeBrick_DRM_3D require essi_parallel but it's not installed!! " 
    exit
fi

# python plot.py

# for pvESSI, pvpython and paraview if available
# pvpython pvESSI_camera.py *h5.feioutput
