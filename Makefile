
update_leaf_tar:
	cd eduction_example && 	bash tar_leaf_dir.sh
	cd ..

clean:
	find eduction_example/ -name "*.h5.feioutput" -delete
	find eduction_example/ -name "essi_*.log" -delete
	find eduction_example/ -name "log" -delete
	
cleanall: clean
	find eduction_example/ -name "*.tgz" -delete

package_for_prof:
	cd eduction_example && rm -f eduction_example.tgz && bash tar_for_prof.sh


get_figures:
	cp -r eduction_example eduction_example_figure
	find eduction_example_figure/ -type f ! -name '*.pdf' -delete