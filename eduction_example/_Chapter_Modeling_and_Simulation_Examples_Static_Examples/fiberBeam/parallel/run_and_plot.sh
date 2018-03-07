rm -f *.feioutput
rm -f essi*.log

if hash essi_parallel 2>/dev/null; then # check if essi_parallel is available
    mpirun -np 4 essi_parallel -f main.fei
else
    echo "Warning!!! Example FiberBeam::parallel require essi_parallel but it's not installed!! " 
	essi -f main.fei
fi


# python plot.py *h5.feioutput

# for pvESSI, pvpython and paraview if available
# pvpython pvESSI_camera.py *h5.feioutput
