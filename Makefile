
update_leaf_tar:
	cd eduction_example && 	bash tar_leaf_dir.sh
	cd ..

clean:
	find eduction_example/ -name "*.h5.feioutput" -delete
	find eduction_example/ -name "essi_*.log" -delete
	find eduction_example/ -name "log" -delete


get_figures:
	cp -r eduction_example eduction_example_figure
	find eduction_example_figure/ -type f ! -name '*.pdf' -delete