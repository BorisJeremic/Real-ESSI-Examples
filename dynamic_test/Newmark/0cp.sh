
for folder in */;
do
	cd ${folder}
	file=${folder%?}
	for subfolder in */;
	do 
		cd ${subfolder}
		# rm *.fei 
		# python ../../post.py veri_newmark_dynamic.h5.feioutput ${file:(-3)} >> ../../resultHHT.tex
		cp ../../measure_damping.m .
		matlab -nojvm -nosplash -r measure_damping
		cd ..
	done
	cd ..
done
