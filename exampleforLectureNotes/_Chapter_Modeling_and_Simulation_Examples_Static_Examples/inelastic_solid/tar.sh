-find . -name "*.tgz" -delete
for folder in */;
do
	cd ${folder}
	tar -czvf ${folder%?}.tgz *
	cd ..
done