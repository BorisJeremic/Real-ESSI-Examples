rm -f *.feioutput
rm -f essi*.log
essi_debug -f main.fei

python plot.py

# python plot_load.py *h5.feioutput

# for pvESSI, pvpython and paraview if available
# pvpython pvESSI_camera.py *h5.feioutput
