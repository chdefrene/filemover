#!/usr/bin/python

if sys.version_info >= (3,0):
	import urllib.request
	from xmlrpc.client import ServerProxy, Error
else: # python2
	import urllib2
	from xmlrpclib import ServerProxy, Error
	
hello