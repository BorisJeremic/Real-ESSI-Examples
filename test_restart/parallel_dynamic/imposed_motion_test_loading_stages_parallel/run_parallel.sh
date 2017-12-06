mpirun -np 3 essi_parallel -f 0main_all.fei
mpirun -np 3 essi_parallel -f 1main_stage1.fei
mpirun -np 3 essi_parallel -f 2main_restart.fei

# h5diff t_2.h5.feioutput t_2_restart.h5.feioutput

