

current_dir=${PWD}
deepest_dir_array=( $(find . -type d -links 2 ) )
# deepest_dir_array=( $(find . -type d -links 3 ) )

for element in $(seq 0 $((${#deepest_dir_array[@]} - 1)))
do
	cd ${current_dir}/"${deepest_dir_array[$element]}"

	essi -f main.fei

done