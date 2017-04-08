# -find . -name "*.tgz" -delete
for folder in */;
do
	echo ${folder}
	cd ${folder}

	cd 1pure_shear_mono_loading
	sed -i 's/simulate constitutive testing strain control pure shear use material \# 1/simulate constitutive testing strain control pure shear monotonic loading use material \# 1/' main.fei
	sed -i '/maximum_strain*/d' main.fei
	cd ..







	cd ..

done