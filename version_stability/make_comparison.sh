#!/bin/bash
make run_essi              --no-print-directory
make compare_HDF5_max      --no-print-directory
make compare_HDF5_ALL      --no-print-directory
make compare_terminal_log  --no-print-directory

# We do not want the default print directory in Makefile
# Because we want the relative path for security.
# Inside, Python is employed to print the relative path.