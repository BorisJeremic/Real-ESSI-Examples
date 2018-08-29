for folder in */;
do
	cd ${folder}
	file=${folder%?}
	./cp.sh
	cd ..
done