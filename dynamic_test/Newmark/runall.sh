#!/bin/bash

# rm -f resultHHT.tex

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



for folder in */;
do
	cd ${folder}
	file=${folder%?}
	for subfolder in */;
	do 
		cd ${subfolder}
		$essiExecutable  -f ${file}.fei > new.log 
		python ../../post.py veri_newmark_dynamic.h5.feioutput ${file:(-3)} #>> ../../result.tex
		cd ..
	done
	cd ..
done

# cp result.tex ../document/Tex-files/preprocess
# cd ../document/Tex-files/preprocess
# make

# cd ..
# pdflatex veri_dynamic.tex
# pdflatex veri_dynamic.tex
# pdflatex veri_dynamic.tex
