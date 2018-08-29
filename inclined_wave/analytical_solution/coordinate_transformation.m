%%%%% this is a function to transfer to the global z coordinate to local z coordinate 

%%%%% global coordinate: z positive downward, z=0 is the free surface

%%%%% n-th layer local coordinate: z postive downward, z=0 is the the (n-1) interface. 


%%%%% function output: 

% layer_ID: number of layer the point (with z_global as z coordinate) belongs to
% z_local: local z coordinate


%%%% Note: for (n-1) interfce layer location, we always take z_local as 0 and layer_ID as n. It means it belongs to next layer.   

function [layer_ID, z_local] = coordinate_transformation(z_global, thickness)

	num = size(thickness, 2);    % ### n is the dimension of the thickness variable, should equal to (n-1), where n is total number of layers.   

	if (z_global < thickness(1))

		layer_ID = 1; 

		z_local = z_global; 
	
	elseif (z_global >= sum(thickness(1:num)))

		z_local = z_global - sum(thickness(1:num));

		layer_ID = num +1; 

	else
	 	
	 	for l= 2:num

	 		if( (z_global<sum(thickness(1:l))) && (z_global>=sum(thickness(1:l-1))) )

	 			layer_ID = l; 

	 			z_local = z_global - sum(thickness(1:l-1));

	 			break; 
	 		end
	 	end

	end

end