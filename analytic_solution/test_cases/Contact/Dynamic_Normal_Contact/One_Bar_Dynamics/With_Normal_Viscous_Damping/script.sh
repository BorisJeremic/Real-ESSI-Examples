cd ct_0.1
essi -f main.fei
cp One_Bar_Dynamics_Dynamic_Vibration.h5.feioutput Analytical_Displacement.feioutput
bash compare.sh
cd ..

cd ct_1
essi -f main.fei
cp One_Bar_Dynamics_Dynamic_Vibration.h5.feioutput Analytical_Displacement.feioutput
bash compare.sh
cd ..

cd ct_10
essi -f main.fei
cp One_Bar_Dynamics_Dynamic_Vibration.h5.feioutput Analytical_Displacement.feioutput
bash compare.sh
cd ..

