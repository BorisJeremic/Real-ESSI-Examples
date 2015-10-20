#!/usr/bin/python
from numpy import *
F=1*1e5
l=6
E=30*1e9
b=1
h=1
I=b*h**3/12.0

disp_bending=l**3*F/3/E/I

nu=linspace(0.0,0.45,10)
nu=append(nu, 0.49)

G=E/2/(1+nu)

A_all=1
kappa=1.2+0.1392*(nu/(1+nu))
A_shear=A_all/kappa

disp_shear=F*l/G/A_shear

disp_bending=disp_bending*linspace(1,1,11)


disp=disp_bending+disp_shear

f_out=open("result_theory.txt","w")
for i in range(11):
	f_out.write("%16.8f\n" %disp[i])

f_out.close()
