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

# http://webpython.codepoint.net/cgi_debugging
cgitb.enable() # pour les options voir : http://docs.python.org/library/cgi.html

params	= cgi.FieldStorage() # recuperation des parametres contenus dans l'URL

print("data:")
