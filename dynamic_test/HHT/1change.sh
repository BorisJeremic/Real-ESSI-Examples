for folder in */;
do
	cd ${folder}
	file=${folder%?}
	for subfolder in */;
	do 
		cd ${subfolder}
		rm *.fei 
		# python ../../post.py veri_newmark_dynamic.h5.feioutput ${file:(-3)} >> ../../resultHHT.tex
		cp ../../alpha0.fei .
		mv alpha0.fei ${file}.fei 
		cd ..
	done
	cd ..
done