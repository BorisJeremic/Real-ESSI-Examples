


function [allStrain, allG] =  GGmaxInterpolate(strain, govergmax)
	len = length(govergmax) ; 
	newG = zeros(len-1,1);
	newStrain = zeros(len-1,1) ; 
	for i = 1 : len-1
		newG(i) = 0.5*(govergmax(i) + govergmax(i+1));
	end

	for i = 1 : len-1
		newStrain(i) = sqrt(strain(i) * strain(i+1));
	end

	allG(1:2:2*len-1) = govergmax
	allG(2:2:2*len-1) = newG

	allStrain(1:2:2*len-1) = strain
	allStrain(2:2:2*len-1) = newStrain
	allStrain(2) =allStrain(3)/3. ; 
	semilogx(allStrain,allG)

end


% print()