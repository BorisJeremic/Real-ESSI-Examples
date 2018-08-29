%%%%%  This file is written to calculate incident SV wave into multi-layered medium %%%%%

%%%%% By Hexiang Wang

%%%%% Feb, 6th , 2018

clc; close all; clear; 

%%%%========== Define usr input =============================%%%%%

incidnt_angle = 45.0/180*pi; %%% incident angle in rad  

density = [2000, 2000];      %%% [2300, 2300, 2300];  %%% This is density for layered ground 

%%% Two type of input are provided: one is to provide bet, alp and initially assign v as 0

%%% Another type is to provide bet, v and initially assign alp as 0.  

bet = [1000.0, 1000.0];     %%% [2000.0, 2000.0, 2000.0];     %[750, 800, 1200]; %%  [500, 750, 1000];   %% Vs rotational wave velocity for layered ground 

alp = [1700.0, 1700.0];      %%% [0.0, 0.0, 0.0]; %% [850.0, 1000.0, 1500.0];   % [0.0, 0.0, 0.0];  % alp = [750, 1000, 1500];   %%% Vp dilational wave velocity for layered ground 
 
v =  [0.0, 0.0];            %% [0.3, 0.3, 0.3]; %% [0.0, 0.0, 0.0];  %% [0.2, 0.3, 0.35];  %%% possion ratio  

%%%

thickness = [600];   %% layer thickness, the last layer is infinite thick

f = 2.0;      %% Hz, frequency

damping = [0.0, 0.0];

%%% careful with conversion between potential magnitude and dilational & rotational wave solution magnitudes

incident_amplitude = 20.0;   %%% amplitude for incident rotational wave solutions 

%%%%

x_lower = 0; 

x_upper = 100; 

y_lower = -200; 

y_upper = 0;

x_interval = 25; 

y_interval = 2; 

t_low = 0; 

dt = 0.005; 

t_up = 1; 

tolerance = 1e-6; 

file_ID = fopen('dis.txt', 'w');  


%%% Note that in damping case, vertical level magnitudes also depend on horizontal location. The in-depth magnitude output here corresponds to verification_point_IDx.    
file_ID1 = fopen('magnitude_depth.txt','w');   


%%% Same as in-depth magnitude, cord rotation in damping case also corresponds to horizontal location 
file_ID2 = fopen('cord_rotation.txt','w');   


%%% Same as in-depth magnitude, point rotation in damping case also corresponds to horizontal location 
file_ID3 = fopen('point_rotation.txt','w'); 

verification_point_IDx = 3;    %%% verification comparison point x=0; 

verification_point_IDy = 17;     %%% verification comparison point y= 0; 

%%%%========= End usr input ===================================%%%%%% 

num_layer = size(alp, 2); 

%%%% calcuate v or alp based on the relations
%%%% relation between Vp, Vs and Possion ratio v
%%  v = 0.5-0.5/((Vp/Vs)^2-1)
%% vp/vs = ((1-v)/(0.5-v))^(0.5)

if ( v(1) == 0.0 )

	v= 0.5-0.5./((alp./bet).^2-1); 

elseif (alp(1)==0.0)

	alp= bet.*((1.0-v)./(0.5-v)).^(0.5);

else  

	disp('Too many parameters are specified: YOu can either specify v or alp. Check if your Poisson ratio are compatible with wave velocities.'); 

end


for k1= 1:num_layer

	bet(k1) = bet(k1)*(1 + damping(k1)*1i);

	alp(k1) = alp(k1)*(1 + damping(k1)*1i);  

end 


p = 2*pi*f; %% radial frequency 

c = bet(num_layer)/sin(incidnt_angle); %% horizontal phase velocity

k = p/c; 

Gam = 2*(bet/c).^2;  %% gamma_m 

r_alp = zeros(1, num_layer);  %%% refracted alp angle

r_bet = zeros(1, num_layer);  %%% refracted bet angle 


for i = 1: num_layer

	if alp(i) <= c

		r_alp(i) = ((c/alp(i))^2-1)^(0.5);

	else

		r_alp(i) = -1i*(1-(c/alp(i))^2)^(0.5);    

	end

	if bet(i) <= c

		r_bet(i) = ((c/bet(i))^2-1)^(0.5);

	else

		r_bet(i) = -1i*(1-(c/bet(i))^2)^(0.5);    
	
	end

end

incident_amplitude = incident_amplitude*p^2/(2*bet(num_layer)*bet(num_layer));  %%% careful with conversion between potential magnitude and dilational & rotational wave solution magnitudes

%%%% recursive to formulate matrix J %%%% 

J = zeros(4,4);  %%% J = inv(En)a(n-1)a(n-2)...a(1);  [N.A. Haskell, 1951] 

%%% Original implementation

%% calculate inv(En) according to Eq(2.16) of N.A. Haskell 1951

% J(1,1) = -2*(bet(num_layer)/alp(num_layer))^2; 

% J(1,3) = 1/(density(num_layer)*alp(num_layer)*alp(num_layer)); 

% J(2,2) = c^2*(Gam(num_layer)-1)/(alp(num_layer)*alp(num_layer)*r_alp(num_layer)); 

% J(2,4) = 1/(density(num_layer)*alp(num_layer)*alp(num_layer)*r_alp(num_layer)); 

% J(3,1) = (Gam(num_layer)-1)/(Gam(num_layer)*r_bet(num_layer)); 

% J(3,3) = -1/(density(num_layer)*c*c*Gam(num_layer)*r_bet(num_layer)); 

% J(4,2) = 1; 

% J(4,4) = 1/(density(num_layer)*c*c*Gam(num_layer)); 

%%%%%

J = transfer_matrix_invE(alp, bet, r_alp, r_bet, Gam, density, c, num_layer); 

% E_verification = inv(J1)

for j = num_layer-1:-1:1

	%%%% Original implementation  of matrix a 

	% a = zeros(4,4);   %%% a= D*inv(E) equation (2.17) of N.A. Haskell, 1951  

	% P = k*r_alp(j)*thickness(j); 

	% Q = k*r_bet(j)*thickness(j); 

	% a(1,1) = Gam(j)*cos(P)-(Gam(j)-1)*cos(Q); 

	% a(1,2) = 1i*[(Gam(j)-1)/r_alp(j)*sin(P) + Gam(j)*r_bet(j)*sin(Q)]; 

	% a(1,3) = -1/(density(j)*c*c)*(cos(P)-cos(Q)); 

	% a(1,4) = 1i*(1/(density(j)*c*c))*(sin(P)/r_alp(j)+r_bet(j)*sin(Q));

	% a(2,1) = -1i*(Gam(j)*r_alp(j)*sin(P) + (Gam(j)-1)/r_bet(j)*sin(Q));

	% a(2,2) = -(Gam(j)-1)*cos(P) + Gam(j)*cos(Q); 

	% a(2,3) = 1i*(1/(density(j)*c*c))*(r_alp(j)*sin(P)+1/r_bet(j)*sin(Q));

	% a(2,4) = a(1,3); 

	% a(3,1) = density(j)*c*c*Gam(j)*(Gam(j)-1)*(cos(P)-cos(Q)); 

	% a(3,2) = 1i*density(j)*c*c*((Gam(j)-1)^2/r_alp(j)*sin(P)+Gam(j)*Gam(j)*r_bet(j)*sin(Q));

	% a(3,3) = a(2,2); 

	% a(3,4) = a(1,2); 

	% a(4,1) = 1i*density(j)*c*c*(Gam(j)^2*r_alp(j)*sin(P)+(Gam(j)-1)^2/r_bet(j)*sin(Q)); 

	% a(4,2) = a(3,1); 

	% a(4,3) = a(2,1); 

	% a(4,4) = a(1,1); 

	%%%%%%%%%%


	a = transfer_matrix_a(k, r_alp, r_bet, thickness, Gam, density, c, j); 

	J = J*a; 

end

J_inv = inv(J); 

A = zeros(2,2); 

b = zeros(2,1); 

A(1,1) = J_inv(3,1) + J_inv(3,2); 

A(1,2) = J_inv(3,3) + J_inv(3,4); 

A(2,1) = J_inv(4,1) + J_inv(4,2); 

A(2,2) = J_inv(4,3) + J_inv(4,4); 

b(1,1) = J_inv(3,3) - J_inv(3,4); 

b(2,1) = J_inv(4,3) - J_inv(4,4); 

x = inv(A)*b; 

x_rp = x(1)*incident_amplitude;   %%% amplitude for reflected P potential at n layer

x_rsv = x(2)*incident_amplitude;  %%% amplitude for reflected SV potential at n layer  


RHS = J_inv*[x_rp; x_rp; x_rsv-incident_amplitude; x_rsv+incident_amplitude]; %%% corresponding to initial condition (velocity and stress [u0/c, w0/c, 0, 0] RHS of equation 2.19 of Haskell etc) at intrface 0. The third and fourth term should be zero because of free surface.   

%%% eliminate numerical error %%%

% RHS(3,1)=0.0;   %%% corresponding to sigma0=0

% RHS(4,1)=0.0;   %%% corresponding to tau_0=0 

%%%%%

potential_magnitude_LHS = zeros(4, num_layer);  %%% The potential amplitude matrix store the LHS constants of magnitude of different wave potentials (LHS of equation 2.19)

potential_magnitude_LHS(:,1) = transfer_matrix_invE(alp, bet, r_alp, r_bet, Gam, density, c, 1)*RHS;  %%%% potential magnitude constants for the first layer 

for kk = 2:num_layer

	temp = potential_magnitude_LHS(:,kk-1); 

	temp = transfer_matrix_invE(alp, bet, r_alp, r_bet, Gam, density, c, kk)*transfer_matrix_a(k, r_alp, r_bet, thickness, Gam, density, c, kk-1)*inv(transfer_matrix_invE(alp, bet, r_alp, r_bet, Gam, density, c, kk-1))*temp;  %%% according to the recursive relationship LHS(n) = inv(En)*a(n-1)*E(n-1)*LHS(n-1); 

	potential_magnitude_LHS(:, kk) = temp; 
end


%%% double check for verification %%%%

if ( ( abs(potential_magnitude_LHS(1, num_layer)-x_rp)<tolerance ) && (abs(potential_magnitude_LHS(2, num_layer)- x_rp)<tolerance) && ( abs(potential_magnitude_LHS(3,num_layer)-x_rsv+incident_amplitude)<tolerance ) && ( abs(potential_magnitude_LHS(4,num_layer)-x_rsv-incident_amplitude)<tolerance) )

	disp('Verification passed!!!'); 

else
	
	disp('Something is wrong, check the code!!!'); 

end


%%% potential_magnitude_LHS contains (potential_P_incident+potential_P_reflect, potential_P_reflect-potential_P_incident, potential_S_reflect-potential_S_incident, potential_S_incident+potential_S_reflect); 
%%% potential_magnitude contains(potential_P_reflect, potential_P_incident, potential_S_reflect, potential_S_incident)  

potential_magnitude = zeros(4, num_layer); 

potential_magnitude(1,:) = 1/2*(potential_magnitude_LHS(1,:)+potential_magnitude_LHS(2,:)); 

potential_magnitude(2,:) = 1/2*(potential_magnitude_LHS(1,:)-potential_magnitude_LHS(2,:)); 

potential_magnitude(3,:) = 1/2*(potential_magnitude_LHS(3,:)+potential_magnitude_LHS(4,:));

potential_magnitude(4,:) = 1/2*(potential_magnitude_LHS(4,:)-potential_magnitude_LHS(3,:));


%%%% incident P is 0 at n layer %%%%
% potential_magnitude(2, num_layer) = 0.0; 
%%%%%



%%%%% 
% potential_magnitude(2, 1) = 0.0; 
%%%%%




%%%%%%%%% This part is for plotting shot pictures %%%%%%%%%%%%% 

t = t_low : dt : t_up;  

t = t' ; 

[x_coord, y_coord] = meshgrid(x_lower:x_interval:x_upper, y_lower:y_interval:y_upper); 

No_x_dim = size(x_coord, 2); 

No_y_dim = size(x_coord, 1);  

No_time_step = size(t,1); 

%%%% oupout time series time displacement for verification %%%%%





%%%% change y global coordinate to local coordinate

for i1= 1: No_time_step

	ux = zeros(No_y_dim, No_x_dim); 

	uy = zeros(No_y_dim, No_x_dim); 

	current_time = t(i1); 

	for k1 = 1:No_y_dim
	% for k1 = 1:2
	
		for j1 = 1:No_x_dim

			current_x = x_coord(k1,j1); 

			current_y = -1*y_coord(k1,j1); 

			[layer_ID, y_local] = coordinate_transformation(current_y, thickness); 

			ip_magnitude= potential_magnitude(2, layer_ID);

			rp_magnitude= potential_magnitude(1, layer_ID); 

			isv_magnitude = potential_magnitude(4, layer_ID); 

			rsv_magnitude = potential_magnitude(3, layer_ID);  

			current_alp = alp(layer_ID); 

			current_bet = bet(layer_ID); 

			current_r_alp = r_alp(layer_ID); 

			current_r_bet = r_bet(layer_ID);  

			ux(k1,j1) = (1i*k*(current_alp/p)^2*((ip_magnitude+rp_magnitude)*cos(k*current_r_alp*y_local)+ 1i*(ip_magnitude-rp_magnitude)*sin(k*current_r_alp*y_local))-...                
						2*(1i)*k*current_r_bet*(current_bet/p)^2*((isv_magnitude-rsv_magnitude)*cos(k*current_r_bet*y_local) + 1i*(isv_magnitude+rsv_magnitude)*sin(k*current_r_bet*y_local)) )*exp(1i*(p*current_time-k*current_x)); 



			%%%% verification expression


			ux_mag = abs(ux(k1,j1)); 

			ux(k1,j1) = real(ux(k1,j1)); 

			uy(k1,j1) = (-1i*k*current_r_alp*(current_alp/p)^2*((ip_magnitude-rp_magnitude)*cos(k*current_r_alp*y_local)+ 1i*(ip_magnitude+rp_magnitude)*sin(k*current_r_alp*y_local))-...
			 			2*(1i)*k*(current_bet/p)^2*((rsv_magnitude+isv_magnitude)*cos(k*current_r_bet*y_local)+1i*(isv_magnitude-rsv_magnitude)*sin(k*current_r_bet*y_local)) )*exp(1i*(p*current_time-k*current_x)); 

			uy_mag = abs(uy(k1,j1));

			uy(k1,j1) = real(uy(k1,j1))*(-1);  


			%%%% Add this part to output displacement for comparison and verification %%%%

			if ( (j1 == verification_point_IDx) && (k1== verification_point_IDy) )

				if (i1==1)

					fprintf(file_ID, '%4.2f %4.2f \n', current_x, current_y);
				end

				fprintf(file_ID, '%3.5f   %3.5f   %3.5f\n', current_time, ux(k1, j1), uy(k1, j1));   %%% three columns: current time, x direction displacement and y direction displacement  

			end

			%%%%%

			if ((i1==1) && (j1 == verification_point_IDx))

				fprintf(file_ID1, '%3.5f  %3.5f    %3.5f    %3.5f\n', current_x, current_y, ux_mag, uy_mag); %%% three columns: depth coordinates, x direction displacement magnitude and y direction displacement magnitude
		
				fprintf(file_ID2, '%3.5f  %3.5f    %3.5f\n', current_x, current_y, 4*uy_mag/abs(2*pi/k)); 

				point_rotation_mag = abs((-1i*k*(-1i*k*current_r_alp*(current_alp/p)^2*((ip_magnitude-rp_magnitude)*cos(k*current_r_alp*y_local)+ 1i*(ip_magnitude+rp_magnitude)*sin(k*current_r_alp*y_local))-...
			 			2*(1i)*k*(current_bet/p)^2*((rsv_magnitude+isv_magnitude)*cos(k*current_r_bet*y_local)+1i*(isv_magnitude-rsv_magnitude)*sin(k*current_r_bet*y_local))) -  1i*k*(current_alp/p)^2*k*current_r_alp*(-(ip_magnitude+rp_magnitude)*sin(k*current_r_alp*y_local)+ 1i*(ip_magnitude-rp_magnitude)*cos(k*current_r_alp*y_local))+...
			 			2*(1i)*k*current_r_bet*(current_bet/p)^2*k*current_r_bet*((rsv_magnitude-isv_magnitude)*sin(k*current_r_bet*y_local)+ 1i*(isv_magnitude+rsv_magnitude)*cos(k*current_r_bet*y_local)) )*exp(1i*(p*current_time-k*current_x)));  

				fprintf(file_ID3, '%3.5f   %3.5f    %3.5f\n', current_x, current_y, point_rotation_mag); 			
			
			end


		end


	end

	% ### Plot 2D quiver figure ###

	% figure_name = 'SV_wave_layered_'; 
    
 %    quiver(x_coord, y_coord, ux, uy); 
       
	% xlabel('X [m]');

	% ylabel('Y [m]');
    
 %    xlim([-50,650]); 
    
 %    grid on;

	% figure_name = strcat(figure_name,num2str(i1));

	% figure_name = strcat(figure_name,'.jpg');  

	% saveas(gcf, figure_name);

	% close all;

	% ### Ending plot of 2D quiver figure ### 
end 


fclose(file_ID); 
fclose(file_ID1); 
fclose(file_ID2); 
fclose(file_ID3); 














%%% one is first calculate the potential function and then displacement magnitude [use equation 2.19, 2.3, 2.4].  
%%%% below we provide 2 options to recover the solution field%%%%%

%%% Another is calculate the velocity and then displacement [use equation 2.18]

% V = zeros(4, num_layer); %%% The magnitude stores LHS of equation 2.18 of different interface from 0 to n-1

% V(:, 1) = RHS; 

% for k = 2: num_layer 

% 	V(:, k) = transfer_matrix_a(k, r_alp, r_bet, thickness, Gam, density, c, m)*V(:,k-1); 
% end

% V = V*; %%% velocity to displacement 

%%%%%%

