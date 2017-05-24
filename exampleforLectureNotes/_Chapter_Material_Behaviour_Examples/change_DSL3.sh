

current_dir=${PWD}
type1=( $(find . -type d -name '3uniaxial_strain_mono_loading' ) )
# type1=( $(find . -type d -links 3 ) )

for element in $(seq 0 $((${#type1[@]} - 1)))
do
	cd ${current_dir}/"${type1[$element]}"


	sed -i 's/simulate constitutive testing strain control uniaxial loading use material \# 1/simulate constitutive testing strain control uniaxial monotonic loading use material \# 1/' main.fei
	sed -i '/maximum_strain*/d' main.fei
	
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