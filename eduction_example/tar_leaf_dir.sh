

current_dir=${PWD}
deepest_dir_array=( $(find . -type d -links 2 ) )

for element in $(seq 0 $((${#deepest_dir_array[@]} - 1)))
do
	cd ${current_dir}/"${deepest_dir_array[$element]}"

	rm -f *.tgz
	tar -czvf ${PWD##*/}.tgz *

done