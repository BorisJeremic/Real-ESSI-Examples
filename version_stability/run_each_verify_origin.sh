
#!/bin/bash

parent_dir=$PWD


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


# for path in 'find -mindepth 1 -maxdepth 2 -type d'
for path in `find -mindepth 1 -maxdepth 10 -type d` 
do
    cd $parent_dir/$path
    if [ -f main.fei ]; then
    	if [ -f skip ]; then
    		touch skip
    	else
    		./runAndCompareOrigin.sh $essiExe
    	fi
    fi
done

