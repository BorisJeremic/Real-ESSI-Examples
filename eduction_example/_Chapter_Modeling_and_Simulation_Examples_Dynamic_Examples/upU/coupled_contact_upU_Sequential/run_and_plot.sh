rm -f *.feioutput
rm -f essi*.log
rm -f gmon.out
rm -f RealESSI_VERSION_INFO.txt
rm -f petsc_log.txt

essi -f main.fei

# python plot.py

# for pvESSI, pvpython and paraview if available
# pvpython pvESSI_camera.py *h5.feioutput
