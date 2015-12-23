#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ntpath


""" Set up default script variables """
show = ""
season = -1


""" Returns the file name of any given path """	
def get_file_name(path):
		head, tail = ntpath.split(path)
		return tail or ntpath.basename(head)
	

""" Analyzes the filename to find TV show and season"""	
def analyze_file_name(file):
	filename = get_file_name(file)
	return filename
		
		
print analyze_file_name("C/admin/home/Modern-Family.S03E05.XCTV.mkv")