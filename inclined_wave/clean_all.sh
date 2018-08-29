#!/bin/bash

parent_dir=$PWD

for path in `find -mindepth 1 -maxdepth 10 -type d` 
do
    cd $parent_dir/$path
    if [ -f *.feioutput ]; then
    	if [ -f skip ]; then
    		touch skip
    	else
    	   rm -rf *.feioutput
           rm *.log
    	fi
    fi
    cd $parent_dir
done