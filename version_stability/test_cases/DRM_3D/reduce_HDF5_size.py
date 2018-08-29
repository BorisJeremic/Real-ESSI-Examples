import numpy as np
import matplotlib.pyplot as plt  
import h5py 

h5in_filename = "input.hdf5.DRM"
h5out_filename = "test.input.DRM"

h5in=h5py.File(h5in_filename,"r")
f_out = h5py.File(h5out_filename, "w")

SIZE = 60

# =================
Accelerations=h5in['/Accelerations'][()]
Accelerations_reduce = Accelerations[:,0:SIZE]
out_accel = f_out.create_dataset("/Accelerations", data = Accelerations_reduce)

# =================
DRM_nodes = h5in['/DRM Nodes'][()]
out = f_out.create_dataset("/DRM Nodes", data = DRM_nodes)

# =================
Displacements=h5in['/Displacements'][()]
Displacements_reduce = Displacements[:,0:SIZE]
out = f_out.create_dataset("/Displacements", data = Displacements_reduce)

# =================
Elements = h5in['/Elements'][()]
out = f_out.create_dataset("/Elements", data = Elements)

# =================
IsBoundaryNode = h5in['/Is Boundary Node'][()]
out = f_out.create_dataset("/Is Boundary Node", data = IsBoundaryNode)

# =================
NumberofBoundaryNodes = h5in['/Number of Boundary Nodes'][()]
out = f_out.create_dataset("/Number of Boundary Nodes", data = NumberofBoundaryNodes)

# =================
NumberofExteriorNodes = h5in['/Number of Exterior Nodes'][()]
out = f_out.create_dataset("/Number of Exterior Nodes", data = NumberofExteriorNodes)

# =================
Time = h5in['/Time'][()]
Time_reduce = Time[0:SIZE]
out = f_out.create_dataset("/Time", data = Time_reduce)

f_out.close()


