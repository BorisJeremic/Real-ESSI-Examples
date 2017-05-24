

current_dir=${PWD}
deepest_dir_array=( $(find . -type d -links 2 ) )
# deepest_dir_array=( $(find . -type d -links 3 ) )

for element in $(seq 0 $((${#deepest_dir_array[@]} - 1)))
do
	cd ${current_dir}/"${deepest_dir_array[$element]}"

	# cp ${current_dir}/run_and_plot.sh .
	# cp ${current_dir}/pvESSI_camera.py .
	# cp ${current_dir}/Makefile .
	# rm run.sh
	# python plot.py
	# sed -i '/^\s*$/d' main.fei
	# sed -i 's/8NodeBrickLT/8NodeBrick/' *.fei
	# sed -i 's/20NodeBrickLT/20NodeBrick/' *.fei
	# sed -i 's/27NodeBrickLT/27NodeBrick/' *.fei
	# sed -i 's/ProfileSPD/UMFPack/' main.fei
	sed -i 's/verbose_level\ =\ 2//' main.fei
	# sed -i 's/linear_elastic_isotropic_3d/linear_elastic_isotropic_3d_LT/' main.fei

done