# clean:
rm -f stress-strain*.pdf
rm -f *.feioutput
rm -f essi*.log

# run:
python run_and_plot_damping.py


# for pvESSI, pvpython and paraview if available
# pvpython pvESSI_camera.py *.h5.feioutput
