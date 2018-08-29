%%%%% This function is written to calculate inv(E) matrix according to equation (2.16) %%%%%%

%%%% By Hexiang Wang, Feb, 6th, 2018 


function inv_E = transfer_matrix_invE(alp, bet, r_alp, r_bet, Gam, density, c, num)

	inv_E = zeros(4,4);

	inv_E(1,1) = -2*(bet(num)/alp(num))^2; 

	inv_E(1,3) = 1/(density(num)*alp(num)*alp(num)); 

	inv_E(2,2) = c^2*(Gam(num)-1)/(alp(num)*alp(num)*r_alp(num)); 

	inv_E(2,4) = 1/(density(num)*alp(num)*alp(num)*r_alp(num)); 

	inv_E(3,1) = (Gam(num)-1)/(Gam(num)*r_bet(num)); 

	inv_E(3,3) = -1/(density(num)*c*c*Gam(num)*r_bet(num)); 

	inv_E(4,2) = 1; 

	inv_E(4,4) = 1/(density(num)*c*c*Gam(num)); 

end



