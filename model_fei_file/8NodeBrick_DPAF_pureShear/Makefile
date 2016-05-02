all:
	essi -nf main.fei
	python extrESSIHDF5.py GGmax_confinement.h5.feioutput GGmax_shear.h5.feioutput

clean:
	-rm GGmax_confinement.h5.feioutput GGmax_shear.h5.feioutput
	-rm GGmax-shear.pdf