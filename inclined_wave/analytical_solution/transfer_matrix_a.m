%%%%%%  This function is written to return transfer matrix a %%%%%%%%%

%%%%%% The implementation formulation refered to N. A. Haskell 1951

%%%% By Hexiang Wang, Feb, 6th, 2018 

function a = transfer_matrix_a(k, r_alp, r_bet, thickness, Gam, density, c, j)

	a = zeros(4,4);   %%% a= D*inv(E) equation (2.17) of N.A. Haskell, 1951  

	P = k*r_alp(j)*thickness(j); 

	Q = k*r_bet(j)*thickness(j); 

	a(1,1) = Gam(j)*cos(P)-(Gam(j)-1)*cos(Q); 

	a(1,2) = 1i*((Gam(j)-1)/r_alp(j)*sin(P) + Gam(j)*r_bet(j)*sin(Q)); 

	a(1,3) = -1/(density(j)*c*c)*(cos(P)-cos(Q)); 

	a(1,4) = 1i*(1/(density(j)*c*c))*(sin(P)/r_alp(j)+r_bet(j)*sin(Q));

	a(2,1) = -1i*(Gam(j)*r_alp(j)*sin(P) + (Gam(j)-1)/r_bet(j)*sin(Q));

	a(2,2) = -(Gam(j)-1)*cos(P) + Gam(j)*cos(Q); 

	a(2,3) = 1i*(1/(density(j)*c*c))*(r_alp(j)*sin(P)+1/r_bet(j)*sin(Q));

	a(2,4) = a(1,3); 

	a(3,1) = density(j)*c*c*Gam(j)*(Gam(j)-1)*(cos(P)-cos(Q)); 

	a(3,2) = 1i*density(j)*c*c*((Gam(j)-1)^2/r_alp(j)*sin(P)+Gam(j)*Gam(j)*r_bet(j)*sin(Q));

	a(3,3) = a(2,2); 

	a(3,4) = a(1,2); 

	a(4,1) = 1i*density(j)*c*c*(Gam(j)^2*r_alp(j)*sin(P)+(Gam(j)-1)^2/r_bet(j)*sin(Q)); 

	a(4,2) = a(3,1); 

	a(4,3) = a(2,1); 

	a(4,4) = a(1,1); 

end
