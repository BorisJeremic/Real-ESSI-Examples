F=100;
l=6;
E=1e8;
b=1;
h=1;
I=b*h^3/12;

disp_bending=F.*l.^3./3./E./I

nu=0:0.05:0.45;
nu=[nu 0.49];
G=E./2./(1+nu);
A=1;


disp_shear=F.*l./G./A;

disp_bending=disp_bending*ones(1,11);

disp=disp_bending+disp_shear;



%6:::  8.64e-4
%10:   4e-3
%%%%%%%%%%%%%%%%%%%%

