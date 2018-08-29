


cd dt1
sed -i "s/dtspecial/0\.005/"  *.fei
sed -i "s/alphaspecial/-0.20/"  *.fei
cd ..


cd dt2
sed -i "s/dtspecial/0\.01/"  *.fei
sed -i "s/alphaspecial/-0.20/"  *.fei
cd ..


cd dt3
sed -i "s/dtspecial/0\.05/"  *.fei
sed -i "s/alphaspecial/-0.20/"  *.fei
cd ..


cd dt4
sed -i "s/dtspecial/0\.1/"  *.fei
sed -i "s/alphaspecial/-0.20/"  *.fei
cd ..
