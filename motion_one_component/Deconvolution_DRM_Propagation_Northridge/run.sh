#!/bin/bash 

rm -rf *.log

rm -rf z_at_depth*

rm -rf *.pdf

rm -rf *.feioutput

essi -f main.fei

python python_plot_parameteric_study.py

