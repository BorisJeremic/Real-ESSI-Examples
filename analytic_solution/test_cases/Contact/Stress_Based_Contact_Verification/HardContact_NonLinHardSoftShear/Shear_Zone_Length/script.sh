cd SZ_h_1
essi -f main.fei
cp Monotonic_Contact_Behaviour_Adding_Normal_Load.h5.feioutput Analytical_Solution_Normal_Stress.feioutput
cp Monotonic_Contact_Behaviour_Adding_Tangential_Load.h5.feioutput Analytical_Solution_Shear.feioutput
bash compare.sh
cd ..

cd SZ_h_1e3
essi -f main.fei
cp Monotonic_Contact_Behaviour_Adding_Normal_Load.h5.feioutput Analytical_Solution_Normal_Stress.feioutput
cp Monotonic_Contact_Behaviour_Adding_Tangential_Load.h5.feioutput Analytical_Solution_Shear.feioutput
bash compare.sh
cd ..

cd SZ_h_1e4
essi -f main.fei
cp Monotonic_Contact_Behaviour_Adding_Normal_Load.h5.feioutput Analytical_Solution_Normal_Stress.feioutput
cp Monotonic_Contact_Behaviour_Adding_Tangential_Load.h5.feioutput Analytical_Solution_Shear.feioutput
bash compare.sh
cd ..

cd SZ_h_1e-3
essi -f main.fei
cp Monotonic_Contact_Behaviour_Adding_Normal_Load.h5.feioutput Analytical_Solution_Normal_Stress.feioutput
cp Monotonic_Contact_Behaviour_Adding_Tangential_Load.h5.feioutput Analytical_Solution_Shear.feioutput
bash compare.sh
cd ..


python Normalized_Shear_Stress_Plot.py 

python Normal_Stress_Plot.py 

