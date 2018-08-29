# Since the test_suite is outside the source code, 
# The command essi should be in your system PATH.

# Author: Yuan Feng
# Email : ofeng@ucdavis.edu
# Date  : Mon Jun 27 22:53:38 PDT 2016

# The default is to run_essi and do the compare_txt
testbasic: run_essi compare_txt  

testall: run_essi compare_HDF5_ALL 

# run_essi all the tests and print the results on both the command line and file 
run_essi:
	@script -q -c "time ./compare_function/run_essi.sh" run_essi.log

# This compares the maximum displacement only.
compare_txt:
	@script -q -c "time ./compare_function/compare_txt.sh" verification_results.log
	@make count_for_txt



# This compares all the element outputs (stress strain) and displacements.
compare_terminal_log:
	@script -q -c "time ./compare_function/compare_terminal_log.sh" verification_results_terminal_log.log
	@make count_for_terminal_log
# statistics
# count the test cases and print the results on both the command line and file 
# passed cases / all cases = 58/58.
count_for_txt:
	@python ./compare_function/count.py verification_results.log  
	@python ./compare_function/count.py verification_results.log  >> verification_results.log

count_for_HDF5_all:
	@python ./compare_function/count.py verification_results_HDF5_all.log  
	@python ./compare_function/count.py verification_results_HDF5_all.log  >> verification_results_HDF5_all.log

count_for_terminal_log:
	@python ./compare_function/count.py verification_results_terminal_log.log  
	@python ./compare_function/count.py verification_results_terminal_log.log  >> verification_results_terminal_log.log


# change the name of the current HDF5 results to original results
update:
	@bash ./compare_function/update.sh
	

# clean the current results and maintain the original results
clean:
	-find . -name "*[^original].h5.feioutput" -delete
	-find . -name "new.log" -delete
	-find . -name "*.pyc" -delete
	-find . -name "gmon.out" -delete
	-find ./test_cases -name "essi_*.log" -delete
	-find ./ -name "terminal.log" -delete
	-find ./test_cases -name "status.py" -delete
	# -find ./test_cases -name "compare_*.py" -delete
	# -find ./test_cases -name "valgrind_memcheck.sh" -delete
	-find ./test_cases -name "run_and_compare" -delete
	-find ./test_cases -name "RealESSI_VERSION_INFO.txt" -delete
	-find ./test_cases -name "MSESSI_VERSION_INFO.txt" -delete
	-find . -name "verification_result*" -delete
	-find . -name "*.h5.feioutput" -delete
	-find . -name "numeric_result.txt" -delete
	-find ./test_one_example -name "essi_*.log" -delete
	-rm -f run_essi.log
# clean both the current and original results. 
cleanall:
	-make clean --no-print-directory
	-find ./test_cases -name "run_and_compare" -delete
	-find . -name "*.h5.feioutput" -delete
	-find . -name "*memcheck*.err" -delete
	-find . -name "*memcheck*.out" -delete
	-find . -name "original.log" -delete
# show the results on html. Require the package aha. Install aha by 
# sudo apt-get install aha
html:
	@aha -f verification_results.log > verification_results.html 
	






# option:
# copy html to server 
# @cp verification_results_HDF5_max.html ~/public_html/essi_autotest/
# @cp verification_results_HDF5_all.html ~/public_html/essi_autotest/