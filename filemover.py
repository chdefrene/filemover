#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ntpath, os, sys


""" Set up default script variables """
show = ""
season = -1
path = ""

""" Store filepath """
temp = sys.argv[1]
#path = os.path.basename(temp)
#if os.path.exists(temp):
#	path = os.path.basename(temp)

path = "Christian/Dropbox/Bilder/Profilbilder/Jekyll.And.Hyde.S01E08.Moroll.HDTV.x264-ORGANiC "


""" Returns the file name for any given path """	
def get_file_name(path):
	head, tail = ntpath.split(path)
	return tail or ntpath.basename(head)
	


""" Analyzes the file name to find TV show and season	"""
def analyze_file_name(file):
	filename = get_file_name(str(file))
	
	#print filename
	
	showArray = []
	seasonArray = []
	flag = True
	i=0
	
	while flag:
		# Check if char is the S in SXXEYY and if next is the first X
		if filename[i+1] is not "s" and not filename[i+2].isdigit():
			showArray.append(" ") if filename[i] == "." else showArray.append(filename[i])
			i+=1
		else:
			if int(filename[i+2]) is not 0:
				seasonArray.append(filename[i+2])
			seasonArray.append(filename[i+3])
			season = int("".join(seasonArray))
			flag = False
	
	
	show = "".join(showArray)
	
	#print "Season: "+str(season)
	#print "Show: "+show
	
	return show, season

""" Run script """
print analyze_file_name(str(path))




