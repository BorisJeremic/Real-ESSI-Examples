

rm result.tex

for folder in */;
do
	cd ${folder}
	file=${folder%?}
	for subfolder in */;
	do 
		cd ${subfolder}
			sed -i "s/ceil(5/ceil(100/" *.fei
		cd ..
	done
	cd ..
done


