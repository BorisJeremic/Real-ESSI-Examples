#!/usr/bin/python
import sys
import os
import re
import subprocess
# import my own command line color function
sys.path.append("." )
from mycolor_fun import *

# read the verification_results.txt
result_file=sys.argv[1]
result_text= open(result_file,"r")
result=result_text.read()

# find all words "pass" and count the number
num_pass=re.findall(r"Case Passed", result)
passed_number=len(num_pass)

# find all words "/test_cases/" and count the number
num_cases=subprocess.check_output("find ./test_cases/ -type d -links 2 | wc -l", shell=True)
total_cases=int(num_cases)

# print '//*************************************'
print headblankline()
print headstep()
print headstatistics(),'{0} {1}/{2} '.format('Passed cases / All cases=',passed_number,total_cases)













# num_all=re.findall(r"/test_cases/", result)
# total_cases=len(num_all)