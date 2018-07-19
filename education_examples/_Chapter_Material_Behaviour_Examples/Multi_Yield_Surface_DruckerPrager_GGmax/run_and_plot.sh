# clean:
rm -f stress-strain*.pdf
rm -f *.feioutput
rm -f essi*.log

# run:
essi -f main.fei
# plot GGmax
python plot_GGmax.py


# for pvESSI, pvpython and paraview if available
# pvpython pvESSI_camera.py *.h5.feioutput
