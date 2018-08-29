

# rm -f result.tex

for folder in */;
do
	cd ${folder}
	file=${folder%?}
	for subfolder in */;
	do 
		cd ${subfolder}
		essi -f ${file}.fei >new.log
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
