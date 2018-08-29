
# rm -f resultHHT.tex


for folder in */;
do
	cd ${folder}
	file=${folder%?}
	for subfolder in */;
	do 
		cd ${subfolder}
		essi -f ${file}.fei > new.log 
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