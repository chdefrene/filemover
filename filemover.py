#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ntpath, os, sys


""" Set up default script variables """
show = ""
season = -1

temp = sys.argv[1]
#print path
if os.path.exists(temp):
	path = os.path.basename(path)


""" Returns the file name of any given path """	
def get_file_name(path):
		head, tail = ntpath.split(path)
		return tail or ntpath.basename(head)
	

""" Analyzes the filename to find TV show and season"""	
def analyze_file_name(file):
	filename = get_file_name(file)
	return filename
		
		
print analyze_file_name(str(path))