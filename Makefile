
update_leaf_tar:
	cd eduction_example && 	bash tar_leaf_dir.sh
	cd ..

clean:
	find eduction_example/ -name "*.h5.feioutput" -delete
	find eduction_example/ -name "essi_*.log" -delete
