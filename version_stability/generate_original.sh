#!/bin/bash

# 1. clean both the current and original HDF5 output 
make -f ./Makefile cleanall $@
# 2. Generate the current HDF5 output
make -f ./Makefile run_essi --no-print-directory $@
# 3. Change the name of the current HDF5 output to original HDF5 output
make -f ./Makefile update   --no-print-directory $@