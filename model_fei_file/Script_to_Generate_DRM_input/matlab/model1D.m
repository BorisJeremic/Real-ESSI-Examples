DRMNode=int32([ 1 2 3 4 46 48 50 52]);

DRMElement=int32([11]);
boundary=int32([ 1 1 1 1 0 0 0 0]);
n_b=int32(4);
n_e=int32(4);
time=int32(linspace(0.01,10,1000));

load('displ.data')
load('acc.data')

DRM_displ=zeros(3*length(DRMNode),length(time));
DRM_acc=zeros(3*length(DRMNode),length(time));

for i=1:4
	DRM_displ(i*3-2,:)=displ(1,:);
	DRM_acc(i*3-2,:)=acc(1,:);
end

for i=5:8
	DRM_displ(i*3-2,:)=displ(2,:);
	DRM_acc(i*3-2,:)=acc(2,:);
end

write_DRM_hdf5('input.hdf5',DRM_displ,DRM_acc,DRMNode,DRMElement,boundary,n_b,n_e,time);
