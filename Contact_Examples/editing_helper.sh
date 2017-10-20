#!/bin/bash
# ********************************************************************
# Author: Yuan Feng
# Date: Sun Sep 24 12:00:55 PDT 2017
# Comments: When DSLs are updated, this editing helper will be 
#           used to help update all DSLs in examples.
# ********************************************************************


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

	# sed -i 's/HardContact\ with\ elastic_perfectly_plastic_shear_model/StressBasedHardContact_ElPPlShear/' *.fei
	# sed -i 's/normal_stiffness/axial_stiffness/' *.fei
	# sed -i 's/initial_tangential_stiffness/initial_shear_stiffness/' *.fei
	# sed -i 's/normal_viscous_damping/axial_viscous_damping/' *.fei
	# sed -i 's/tangential_viscous_damping/shear_viscous_damping/' *.fei
	# sed -i 's/HardContact\ with\ elastic_perfectly_plastic_shear_model/StressBasedHardContact_ElPPlShear/' *.fei
	# sed -i 's/HardContact\ with\ nonlinear_hardening_shear_model/StressBasedHardContact_NonLinHardShear/' *.fei
	# sed -i 's/HardContact\ with\ nonlinear_hardening_softening_shear_model/StressBasedHardContact_NonLinHardSoftShear/' *.fei
	
	# sed -i 's/SoftContact\ with\ elastic_perfectly_plastic_shear_model/StressBasedSoftContact_ElPPlShear/' *.fei
	# sed -i 's/SoftContact\ with\ nonlinear_hardening_shear_model/StressBasedSoftContact_NonLinHardShear/' *.fei
	# sed -i 's/SoftContact\ with\ nonlinear_hardening_softening_shear_model/StressBasedSoftContact_NonLinHardSoftShear/' *.fei
done




# Find directory without main.fei
# find . -type d -links 2 '!' -exec test -e "{}/main.fei" ';' -print
