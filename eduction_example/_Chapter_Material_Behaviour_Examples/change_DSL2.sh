

current_dir=${PWD}
typea=( $(find . -type d -name '2pure_shear_cyclic_loading' ) )
# typea=( $(find . -type d -links 3 ) )

for element in $(seq 0 $((${#typea[@]} - 1)))
do
	cd ${current_dir}/"${typea[$element]}"


	sed -i 's/simulate constitutive testing strain control pure shear use material \# 1/simulate constitutive testing strain control pure shear cyclic loading use material \# 1/' main.fei
	sed -i 's/number_of_increment/number_of_cycles/' main.fei
	sed -i 's/number_of_cycles\ =\ 500/number_of_cycles\ =\ 1/' main.fei
	sed -i 's/number_of_cycles\ =\ 499/number_of_cycles\ =\ 1/' main.fei
	
	sed -i 's/yield_function_relative_tolerance = 1E-2/yield_function_relative_tolerance = 1E-6/' main.fei 
	sed -i 's/stress_relative_tolerance = 1E-3/stress_relative_tolerance = 1E-6/' main.fei 
	

	# cp ${current_dir}/plot.py .
	# python plot.py
	# sed -i '/^\s*$/d' main.fei
	# sed -i 's/8NodeBrickLT/8NodeBrick/' *.fei
	# sed -i 's/20NodeBrickLT/20NodeBrick/' *.fei
	# sed -i 's/27NodeBrickLT/27NodeBrick/' *.fei
	# sed -i 's/ProfileSPD/UMFPack/' main.fei
	# sed -i 's/linear_elastic_isotropic_3d/linear_elastic_isotropic_3d_LT/' main.fei

done