essi -f 0main_all.fei
essi -f 1main_stage1.fei
essi -f 2main_restart.fei
h5diff t_2.h5.feioutput t_2_restart.h5.feioutput
h5diff t_3.h5.feioutput t_3_restart.h5.feioutput

