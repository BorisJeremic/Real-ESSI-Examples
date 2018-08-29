#!/bin/bash
# Location of this file: /Real-ESSI/
# Remove the compiled executable
# rm -rf build_verification_sequential
# rm -rf build_verification_parallel
# rm -rf build_current
# rm -rf build_previous
# rm -f ./CompGeoMechUCD_Miscellaneous/examples/essi_verify
# rm -f ./CompGeoMechUCD_Miscellaneous/examples/essi_verify_parallel
# rm -f ./CompGeoMechUCD_Miscellaneous/examples/essi_verify_version_stability


echo "/**************************************************************"
echo "Clean the verification results in analytic solutions ..."
echo "**************************************************************/"
cd analytic_solution
make cleanall
cd ..


echo "/**************************************************************"
echo "Clean the verification results in valgrind memory leak test ..."
echo "**************************************************************/"
cd valgrind_test
make cleanall
cd ..

# echo "/**************************************************************"
# echo "Clean the verification results in education example ..."
# echo "**************************************************************/"
# cd education_example
# bash clean.sh
# cd ..

echo "/**************************************************************"
echo "Clean the verification results in dynamic tests ..."
echo "**************************************************************/"
cd dynamic_test
bash clean.sh
cd ..

echo "/**************************************************************"
echo "Clean the verification results in parallel tests ..."
echo "**************************************************************/"
cd parallel
make cleanall
cd ..

echo "/**************************************************************"
echo "Clean the verification results in code stability ..."
echo "**************************************************************/"
cd version_stability
make cleanall
cd ..

echo "/**************************************************************"
echo "Clean the verification results in inclined wave ..."
echo "**************************************************************/"
cd inclined_wave
bash clean.sh
cd ..