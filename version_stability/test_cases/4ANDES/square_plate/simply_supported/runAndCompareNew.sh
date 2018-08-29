#!/bin/bash

if [ "$1" != "" ]; then
    if command -v $1 1>/dev/null 2>&1; then
        echo " "
        # echo "$1 is available"
    else
        echo "ERROR! User input argument $1 is not available" 
        echo "$1 is not available" 
        exit
    fi
else
    echo "ERROR! Argument 1 is empty! "
    echo "Please provide the ESSI executable!"
    exit
fi

essiExe=$1

echo "Running test-case with $1 in ... "
pwd

$essiExe -f main.fei > new.log



# compare
python compare_HDF5_max.py *.feioutput >> new.log

python compare_HDF5_ALL.py *.feioutput >> new.log

python compare_essi_version.py >> new.log

cat new.log



# rm -rf *_original.h5.feioutput
# rename the current hdf5 results to old hdf5 results
# find . -name '*.h5.feioutput' -exec bash -c 'mv $0 ${0/\.h5.feioutput/\_original\.h5.feioutput}' {} \;


# python extract_numerical_solution.py *.h5.feioutput

# python compare_txt.py


