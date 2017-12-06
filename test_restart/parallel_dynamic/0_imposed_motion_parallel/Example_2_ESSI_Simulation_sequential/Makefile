
# Default Makefile Variables 
NP=4 

all: 
	 essi -f /home/yuan/Dropbox/Research/0short_course_ESSI/Day_1_Part_2_PreProcessing/A_Examples/Example_2/Example_2_ESSI_Simulation/Example_2_analysis.fei

serial: 
	 essi -f /home/yuan/Dropbox/Research/0short_course_ESSI/Day_1_Part_2_PreProcessing/A_Examples/Example_2/Example_2_ESSI_Simulation/Example_2_analysis.fei

parallel: 
	 mpirun -np ${NP} pessi -f /home/yuan/Dropbox/Research/0short_course_ESSI/Day_1_Part_2_PreProcessing/A_Examples/Example_2/Example_2_ESSI_Simulation/Example_2_analysis.fei

clean: 
	 rm *.feioutput 

