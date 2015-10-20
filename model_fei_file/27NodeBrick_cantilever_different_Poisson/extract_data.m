
cur_dir=pwd;

folder={ '10'; '20'; '30'; '40'; '50'; '60'; '70'; '80'; ...
	'90'; '100'; '110'; '120'; '130'; '140'; '150'; '160';...
	 '170'; '180'; '190'; '200'; '210'; '220'; };

essi_res=zeros(22,11);
theory_res=zeros(22,11);
formatSpec = '%f';

for j=1:1:22
	cd (fullfile(cur_dir,folder{j},'postprocess'))
	% 
	file_in1=fopen('result_essi.txt','r');
	essi_res(j,:) = fscanf(file_in1,formatSpec);
	fclose(file_in1);
	% 
	file_in2=fopen('result_theory.txt','r');
	theory_res(j,:) = fscanf(file_in2,formatSpec);
	fclose(file_in2);
end

cd (cur_dir)

nu=linspace(0,0.45,10);
nu=[nu 0.49];

elastic_mod=linspace(10,220,22);

err=abs(essi_res-theory_res)./theory_res;
err=err*100;
surf(nu,elastic_mod,err);


xlabel('Poisson''s ratio');
ylabel('Elastic modulus/(GPa)');
zlabel('Error / (%)');

set(gca,'FontName','Times New Roman' );
set(gca,'FontSize',23);

% axis tight;

print(gcf,'-djpeg','error3D.jpeg');
