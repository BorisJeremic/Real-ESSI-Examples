clear
clc
displacement = hdf5read('veri_newmark_dynamic.h5.feioutput','Model/Nodes/Generalized_Displacements');
displace=displacement';
nodeDispl=displace(7,:);
nodeDispl(end)=[];
 
time=hdf5read('veri_newmark_dynamic.h5.feioutput','time');

totsize=length(time);

psize=totsize/10;

plot(time(1:psize),nodeDispl(1:psize),'-r*');

hold on;

u0=0.1;
omega=2*pi;

exactDisp=u0*cos(omega*time);

% plot(time(1:psize),exactDisp(1:psize),'--b');
hold off;

% legend('Real ESSI Displacement','Analytic Displacement','Location','east');

xlabel('dt/T');
ylabel('Displacement');
set(gca,'FontName','Times New Roman' );
set(gca,'FontSize',25);
% set(gca,'xtick',0:0.1:0.5)
grid on;
% ylim ([0 0.01])
alpha=num2str(000);
out_jpg_name=strcat('disp',alpha,'HHT');
print(gcf,'-djpeg',out_jpg_name)