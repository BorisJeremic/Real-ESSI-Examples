

current_dir=${PWD}
deepest_dir_array=( $(find . -type d -links 2 ) )
# deepest_dir_array=( $(find . -type d -links 3 ) )

for element in $(seq 0 $((${#deepest_dir_array[@]} - 1)))
do
	cd ${current_dir}/"${deepest_dir_array[$element]}"


	# sed -i 's/\/\/.*//' main.fei
	# sed -i '/^$/d' main.fei
	# tar -czvf ${PWD##*/}.tgz *
	# cp ${current_dir}/pvESSI_camera.py .
	# python plot.py
	# sed -i '/^\s*$/d' main.fei
	# sed -i 's/8NodeBrickLT/8NodeBrick/' *.fei
	# sed -i 's/20NodeBrickLT/20NodeBrick/' *.fei
	# sed -i 's/27NodeBrickLT/27NodeBrick/' *.fei
	# sed -i 's/ProfileSPD/UMFPack/' *.fei
	# mv beam.fei main.fei
	# sed -i 's/type\ 8NodeBrick\ with/type\ 8NodeBrick\ using\ 2\ Gauss\ points\ each\ direction\ with/' *.fei
	# sed -i 's/type\ 27NodeBrick\ with/type\ 27NodeBrick\ using\ 3\ Gauss\ points\ each\ direction\ with/' *.fei
	# sed -i 's/linear\_elastic\_isotropic\_3d\_LT/linear\_elastic\_isotropic\_3d/' *.fei
	# sed -i 's/verbose_level = 4;/;/' *.fei
	# sed -i 's/VonMises/vonMises/' *.fei
	# sed -i 's/\ Norm_Displacement_Increment/\ Absolute_Norm_Displacement_Increment/' *.fei
	# sed -i 's/\ Norm_Unbalance/\ Absolute_Norm_Unbalanced_Force/' *.fei
	# sed -i 's/\ Absolute_Norm_Unbalanced_Forced_Force/\ Absolute_Norm_Unbalanced_Force/' *.fei
	sed -i 's/\ add\ load\ type\ \#\ \ 1 domain\ reduction\ method/\ add\ load\ \#\ 1\ type\ domain\ reduction\ method/' *.fei
	sed -i 's/\ add\ load\ type\ \#\ \ 2 domain\ reduction\ method/\ add\ load\ \#\ 2\ type\ domain\ reduction\ method/' *.fei

done




# Find directory without main.fei
# find . -type d -links 2 '!' -exec test -e "{}/main.fei" ';' -print
