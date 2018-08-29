#!/bin/bash
time valgrind --tool=memcheck --leak-check=full  --show-reachable=yes --freelist-vol=100000000  $1 -f $3 1> $1.memcheck.$(date '+%F-%T').out 2> $1.memcheck.$(date '+%F-%T').err  