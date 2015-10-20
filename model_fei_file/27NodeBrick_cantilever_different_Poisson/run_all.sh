for folder in */  ;
do
	cd ${folder}
		make 
		cd postprocess
			make
		cd ..
	cd ..
done


# find . -name "*.feioutput" -delete
