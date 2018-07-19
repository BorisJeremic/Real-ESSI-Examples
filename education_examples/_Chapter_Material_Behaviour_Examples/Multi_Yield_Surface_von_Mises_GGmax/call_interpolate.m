govergmax = [1,0.99563892,0.96674888,0.87318337,0.78735192,0.46719464,0.32043423,0.10940113,0.06347752] ; 
strain = [0,1E-6,1E-5,5E-5,1E-4, 0.0005, 0.001, 0.005, 0.01] ; 

[newStrain, newGoverGmax] = GGmaxInterpolate(strain, govergmax)
[allStrain, allGoverGmax] = GGmaxInterpolate(newStrain, newGoverGmax)