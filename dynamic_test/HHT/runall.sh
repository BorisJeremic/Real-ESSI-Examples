#!/bin/bash

# rm -f resultHHT.tex

# if [ "$1" != "" ]; then
#     if command -v $1 1>/dev/null 2>&1; then
#         echo " "
#         # echo "$1 is available"
#     else
#         echo "ERROR! User input argument $1 is not available HHT" 
#         echo "$1 is not available" 
#         exit
#     fi
# else
#     echo "ERROR! Argument 1 is empty! "
#     echo "Please provide the ESSI executable!"
#     exit
# fi

essiExecutable=$1

for folder in */;
do
	cd ${folder}
	file=${folder%?}
	for subfolder in */;
	do 
		cd ${subfolder}
		$essiExecutable  -f ${file}.fei > new.log 
		# echo ${PWD}
		python ../../postHHT.py veri_newmark_dynamic.h5.feioutput -${file:(-3)} #>> ../../resultHHT.tex
		cd ..
	done
	cd ..
done

# cp resultHHT.tex ../document/Tex-files/preprocess_HHT
# cd ../document/Tex-files/preprocess_HHT
# make

# cd ..
# pdflatex veri_dynamic.tex
# pdflatex veri_dynamic.tex
# pdflatex veri_dynamic.tex

# evince veri_dynamic.pdf