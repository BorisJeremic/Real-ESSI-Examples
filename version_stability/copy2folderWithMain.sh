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
    	cp $parent_dir/runAndCompareNew.sh $parent_dir/$path
    	# cp $parent_dir/runAndCompareOrigin.sh $parent_dir/$path
    	cp $parent_dir/compare_HDF5_max.py $parent_dir/$path
    	# cp $parent_dir/compare_HDF5_ALL.py $parent_dir/$path
    fi
done
