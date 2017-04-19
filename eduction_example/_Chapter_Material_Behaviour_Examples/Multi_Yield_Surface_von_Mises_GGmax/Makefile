run:
	essi -f main.fei
cyclic:
	essi -f main_cyclic.fei
stress_strain:
	python plot_stress_strain.py
plot: GGmax
GGmax:
	python plot_GGmax.py
damping:
	python run_and_plot_damping.py

clean:
	rm -f stress-strain*.pdf
	rm -f strain.feioutput
	rm -f stress.feioutput
