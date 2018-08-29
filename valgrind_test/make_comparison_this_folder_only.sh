#!/bin/bash
command -v essi >/dev/null 2>&1 || { echo >&2 "Require essi but it's not in PATH. Aborting."; exit 1; }

cd compare_function/leaf_folder_Makefile/
mv run_and_compare run_and_compare_backup
mv run_and_compare_this_folder_only run_and_compare
cd ../..

make run_essi              --no-print-directory
make compare_txt           --no-print-directory

cd compare_function/leaf_folder_Makefile/
mv run_and_compare run_and_compare_this_folder_only 
mv run_and_compare_backup run_and_compare
cd ../..

# make compare_HDF5_ALL      --no-print-directory
# make compare_terminal_log  --no-print-directory

# We do not want the default print directory in Makefile
# Because we want the relative path for security.
# Inside, Python is employed to print the relative path.