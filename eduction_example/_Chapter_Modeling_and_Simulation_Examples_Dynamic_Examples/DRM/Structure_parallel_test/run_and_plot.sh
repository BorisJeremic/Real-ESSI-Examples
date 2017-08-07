
rm *.feioutput 

if hash essi_parallel 2>/dev/null; then # check if essi_parallel is available
    mpirun -np 4 essi_parallel -f main.fei
else
    echo "ERROR!!! Example 27NodeBrick_DRM_3D require essi_parallel but it's not installed!! " 
    exit
fi

# mpirun -np 3 essi_parallel -f main.fei
