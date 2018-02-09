#!/bin/bash

# clean previous results
rm -f *.feioutput
rm -f essi*.log

# run essi simulation
essi -f main.fei

# postprocessing: plot results
# python plot.py *h5.feioutput

