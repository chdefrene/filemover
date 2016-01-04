#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ntpath, os, sys



####################################
######	Currently only works  ######
######	with shows in 	      ######
######	Favoritter Christian  ######
####################################


""" Set up global script variables """
show = ""
season = -1
path = ""

""" Stores the filepath in the path variable """
temp = sys.argv[1]
#path = os.path.basename(temp)
if os.path.exists(temp):
	path = os.path.basename(temp)

#path = "Christian/Dropbox/Bilder/Profilbilder/Supernatural.S11E05.HDTV.x264-LOL"


""" Returns the file name for any given path """	
def get_file_name(path):
	head, tail = ntpath.split(path)
	return tail or ntpath.basename(head)
	


""" Analyzes the file name and returns a tuple with TV show name and season """
def analyze_file_name(file):
	filename = get_file_name(str(file))
	
	showArray = []
	seasonArray = []
	flag = True
	i=0
	
	while flag:
		# Stores chars of show name until it reaches the SXXEYY part
		if filename[i+1] is not "s" and not filename[i+2].isdigit():
			showArray.append(" ") if filename[i] == "." else showArray.append(filename[i])
			i+=1
		else:
		# Stores season number and ends loop
			if int(filename[i+2]) is not 0:
				seasonArray.append(filename[i+2])
			seasonArray.append(filename[i+3])
			season = int("".join(seasonArray))
			flag = False
	
	
	show = "".join(showArray)
	
	return show, season
	

""" Moves the file from downloads to the correct location. Note: Must be located on the same disk! """	
def move_file(file):
	filename = get_file_name(str(file))
	filetuple = analyze_file_name(file)
	
	drivebase = "/media/Plex/Christian video/Favoritter Christian/"

	oldpath = path
	newpath = drivebase+filetuple[0]+"/Season "+str(filetuple[1])+"/"+filename
	
	#print newpath
	
	os.rename(oldpath, newpath)
	


""" Run script """
move_file(str(path))



