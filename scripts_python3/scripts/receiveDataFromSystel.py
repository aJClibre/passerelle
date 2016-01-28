#!/var/www/passerelle/scripts_python3/bin/python
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
#print('Content-type: application/json\r\n\r')
print('Content-type: text/plain')
print('')

import cgitb, cgi, sys, os
from xmllib import XmlManager

# http://webpython.codepoint.net/cgi_debugging
cgitb.enable() # pour les options voir : http://docs.python.org/library/cgi.html

params	= cgi.FieldStorage() # recuperation des parametres contenus dans l'URL
##args_get = os.getenv("QUERY_STRING")
##print( args_get )

def test_param_get( params, name, tuple_ok ) :
    """ GET parameter test
	    Return the error code value (0 or 1 if not in debug mode)
	    
    """
    
    if not params   :
        return 8
	
    if name not in params.keys():
        return 8

    code = cgi.escape( params.getvalue( name ) )

    if code not in tuple_ok :
        return 9

    return 1 


def return_code_treatment( code ) :
    """
    return the code treatment considering
    the test context
    0 or 1 if not in test
    """
    test = True

    if test :
        return code
    else :
        if code != 1 :
            return 0
    return 1
    

def receive_code_treatment() : 

    code = test_param_get( params, 'code', ( 'ovensia', ) )
    feed = test_param_get( params, 'feedtype', ( '01', ) )

    if code * feed != 1 :
        return return_code_treatment( max(code, feed) )
    
    # erreur dans dans les donneees
    if 'xml' not in params.keys(): 
        return return_code_treatment( 2 ) 
            
    data = { 'code': params.getvalue('code'), 'xml': params.getvalue('xml') }
    # print(type(params.getvalue('xml')))
    xmanage = XmlManager( data )
    
    if not xmanage.progress_ok :
        return return_code_treatment( xmanage() ) # return False

    xmanage.createXmlFile()

    #if not xmanage.progress_ok :
    return return_code_treatment( xmanage() ) # return False
    

print( receive_code_treatment() )

if __name__ == "__main__":
    import doctest
	# python receiveDataFromSystel.py -v
    	###doctest.testmod()
