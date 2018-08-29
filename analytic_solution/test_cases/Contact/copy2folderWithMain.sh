#!/bin/bash

parent_dir=$PWD

# for d in $parent_dir/*/
# do
# 	(cd "$d" && pwd)
# done


# for path in 'find -mindepth 1 -maxdepth 2 -type d'
for path in `find -mindepth 1 -maxdepth 10 -type d` 
do
    cd $parent_dir/$path
    if [ -f main.fei ]; then
    	cp $parent_dir/skip $parent_dir/$path
    fi
done
