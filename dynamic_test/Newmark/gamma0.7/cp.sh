mkdir dt1
mkdir dt2
mkdir dt3
mkdir dt4

cp *.fei ./dt1
cp *.fei ./dt2
cp *.fei ./dt3
cp *.fei ./dt4


cd dt1
sed -i "s/dt\ =\ 0\.01/dt=0\.005/"  gamma0.7.fei
cd ..


cd dt2
sed -i "s/dt\ =\ 0\.01/dt=0\.01/"  gamma0.7.fei
cd ..


cd dt3
sed -i "s/dt\ =\ 0\.01/dt=0\.05/"  gamma0.7.fei
cd ..


cd dt4
sed -i "s/dt\ =\ 0\.01/dt=0\.1/"  gamma0.7.fei
cd ..
