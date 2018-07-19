rm -f *.feioutput
rm -f essi*.log

cd 1_Degree   && essi -f main.fei && cd ..
cd 5_Degrees  && essi -f main.fei && cd ..
cd 30_Degrees && essi -f main.fei && cd ..
cd 45_Degrees && essi -f main.fei && cd ..
cd 75_Degrees && essi -f main.fei && cd ..
cd 88_Degrees && essi -f main.fei && cd ..
cd 90_Degrees && essi -f main.fei && cd ..

