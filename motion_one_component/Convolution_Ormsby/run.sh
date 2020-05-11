#!/bin/bash 

rm -rf *.log

rm -rf z_at_depth*

rm -rf *.pdf

essi -f main.fei

python plot.py

