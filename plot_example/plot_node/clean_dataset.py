import h5py
h5file = h5py.File("input.hdf5","a")
del h5file["Accelerations"]
del h5file["Displacements"]
del h5file["Time"]

