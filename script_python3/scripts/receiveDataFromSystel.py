#!/usr/bin/env python
# -*- coding: UTF-8 -*-


###########################################################
#
# File : receiveDataFromSystel.py
# http://192.168.111.191/passerelle/script_python3/scripts/receiveDataFromSystel.py
# Modify the .htaccess and chmod+x to be executable 
#
# 
###########################################################

# pour etre retourne par apache
print('Content-type: text/html\r\n\r')

import cgitb, cgi, sys, os
#import http.client

# http://webpython.codepoint.net/cgi_debugging
cgitb.enable() # pour les options voir : http://docs.python.org/library/cgi.html

params	= cgi.FieldStorage() # recuperation des parametres contenus dans l'URL

# http://stackoverflow.com/questions/464040/how-are-post-and-get-variables-handled-in-python
POST={}
args=sys.stdin.read().split('&')

for arg in args: 
    t=arg.split('=')
    if len(t)>1: k, v=arg.split('='); POST[k]=v

##if not params 	: # si le script est execute en local
##	print("No params !")

dicoParams 	= {} # transformation en dico des params recus
##for p in params :
#	if params.getvalue('module') == 'remote':
##	print("%s:  %s" % (p, params.getvalue(p)))
#	dicoParams[p] = escape(params.getvalue(p)) # toujours escape pour eviter l'injection

# for POST and GET parameters
# http://stackoverflow.com/questions/464040/how-are-post-and-get-variables-handled-in-python
# response from Schien

print("HELLO")
# for POST with json
# http://stackoverflow.com/questions/10718572/post-json-to-python-cgi
