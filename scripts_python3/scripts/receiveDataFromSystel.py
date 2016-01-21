#!/usr/bin/env python
# -*- coding: UTF-8 -*-


###########################################################
#
# File : receiveDataFromSystel.py
# http://192.168.111.191/passerelle/script_python3/scripts/receiveDataFromSystel.py
# Modify the .htaccess and chmod+x to be executable 
# 
# Use bpython to test
# $ cd passerelle/scripts_python3
# $ bpython
# >>> import requests
# >>> r = requests.post("http://192.168.111.191/passerelle/scripts_python3/scripts/receiveDataFromSystel.py", data={"data": {"1": "data1","2": "data2"}})
# 
###########################################################

# pour etre retourne par apache
print('Content-type: application/json\r\n\r')

import cgitb, cgi, sys, os
import json

# http://webpython.codepoint.net/cgi_debugging
cgitb.enable() # pour les options voir : http://docs.python.org/library/cgi.html

dicoParams      = {} # transformation en dico des params recus
result 		= {}
success		= True
message		= ''

params	= cgi.FieldStorage() # recuperation des parametres contenus dans l'URL
#print(params)
#print(sys.stdin.read())

if not params 	: # si le script est execute en local
	success         = False
	message		= "No params"

#print(params.getvalue('data'))

#for p in params :
#	print(p)
#	if params.getvalue('module') == 'remote':
#	print("%s:  %s" % (p, params.getvalue(p)))
##	dicoParams[p] = cgi.escape(params.getvalue(p)) # toujours escape pour eviter l'injection

result = { 'success':success, 'message':message }
print( json.dumps(result) )
