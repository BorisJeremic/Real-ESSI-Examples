#!/bin/bash
# ********************************************************************
# Author: Yuan Feng
# Date: Sun Sep 24 12:00:55 PDT 2017
# Comments: 
# 	1. This script will compress the complete files three tgz files
#      for three classifications of examples.
#   2. The compressed file is then used as the downloadable link 
#      for lecture_notes or other documentation.
# ********************************************************************

-find . -name "*.tgz" -delete
for folder in */;
do
	cd ${folder}
	tar -czvf ${folder%?}.tgz *
	cd ..
done