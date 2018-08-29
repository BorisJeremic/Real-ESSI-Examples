

current_dir=${PWD}
deepest_dir_array=( $(find . -type d -links 2 ) )
# deepest_dir_array=( $(find . -type d -links 3 ) )

for element in $(seq 0 $((${#deepest_dir_array[@]} - 1)))
do
	cd ${current_dir}/"${deepest_dir_array[$element]}"

	# cp ${current_dir}/extract_numerical_solution.py .
	# sed -i 's/8NodeBrickLT/8NodeBrick/' *.fei
	# sed -i 's/20NodeBrickLT/20NodeBrick/' *.fei
	# sed -i 's/27NodeBrickLT/27NodeBrick/' *.fei
	# sed -i 's/linear_elastic_isotropic_3d_LT/linear_elastic_isotropic_3d/' main.fei
	# sed -i 's/linear_elastic_isotropic_3d/linear_elastic_isotropic_3d_LT/' main.fei
	sed -i '/^\/\//d' main.fei
	sed -i 's/ProfileSPD/UMFPack/' main.fei
	sed -i 's/define\ solver\ UMFPack;/if(IS_PARALLEL==0)\n{define solver UMFPack;}\nelse\n{define solver parallel;}/' main.fei
done