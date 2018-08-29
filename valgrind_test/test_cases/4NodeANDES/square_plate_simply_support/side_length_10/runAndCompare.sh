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

pwd

bash valgrind_memcheck.sh $essiExe -f main.fei 

cat *.memcheck.*.out > terminal.log

python extract_numerical_solution.py *.h5.feioutput  >> terminal.log

python compare_txt.py >> terminal.log

cat terminal.log

