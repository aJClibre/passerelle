#!/home/users/k1024/.local/bin/python3
#/var/www/passerelle/scripts_python3/bin/python
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
# >>> from sendDataToServer import makeRequest
# >>> import requests
# >>> from lxml import etree
# >>> data_get    = "?code=170&feedtype=01"
# >>> data_post   = "<synergi><syn_evenement><ref_evenement>000000431511</ref_evenement><libelle>AIDE AU BRANCARDAGE SIMPLE / LA ROCHELLE / 17</libelle><dateheurecreation>20160205144642</dateheurecreation><dateheurepreminterv>20151113072047</dateheurepreminterv><departement_num>17</departement_num><numinsee>17300</numinsee><nom_commune>LA ROCHELLE</nom_commune><adresse>RUE DE L ADOUR</adresse><x>-1.0084376</x><y>46.28222</y><id_domaine>4</id_domaine><id_categorie>89</id_categorie><id_type>0</id_type><id_sstype>0</id_sstype></syn_evenement><syn_maincourante><ref_evenement>000000431511</ref_evenement><redacteur>Admin. SYSTEL</redacteur><dateheure>20160205144642</dateheure><objet>Envoi d informations</objet><complement>essai d'insertion</complement></syn_maincourante></synergi>"
# >>> header = {'content-type': 'application/xml'}
# >>> r = requests.post("http://sys.pont-entente.org/sys/passerelle/xml"+data_get, data=data_post, headers=header)
# >>> r.text
# '1\n'
###########################################################

print('Content-type: application/xml')
print('')

import cgitb, cgi, sys, os, codecs, io
import urllib.parse

from xmllib import XmlManager
from _vars import EnvVar

import logging

logging.basicConfig(filename='receiveData.log',level=logging.DEBUG, format='%(asctime)s -- %(levelname)s -- %(message)s')

# http://webpython.codepoint.net/cgi_debugging
cgitb.enable() # pour les options voir : http://docs.python.org/library/cgi.html

###params	= cgi.FieldStorage() # recuperation des parametres contenus dans l'URL
params      = urllib.parse.parse_qs( os.environ.get( 'QUERY_STRING' ))

###########
# Read the raw post data in the standart stream
# Impossible to have accentuated letters. Put a try/except to see why
# A lot of solutions have been try :
# params   = cgi.FieldStorage() # but not good for raw input
#input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
#sys.stdin = codecs.getwriter("utf-8")(sys.stdin.detach())
###########
xml_string  = sys.stdin.read( int( os.environ.get( 'CONTENT_LENGTH', 0 )))

def test_param_get( params, name, tuple_ok ) :
    """ GET parameter test
	    Return the error code value (0 or 1 if not in debug mode)
	    
    """
    
    if not params   :
        return 8
	
    if name not in params.keys():
        return 8

    code = cgi.escape( params[ name ][0] )

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
    logging.debug("receiveDataFromSystel.return_code_treatment -- result code: %d", code )

    if test :
        return code
    else :
        if code != 1 :
            return 0
    return 1
    

def receive_code_treatment() : 

    code = test_param_get( params, 'code', EnvVar.listCodePost )
    feed = test_param_get( params, 'feedtype', EnvVar.listFeedtypePost )

    if code * feed != 1 :
        return return_code_treatment( max(code, feed) )
    
    # erreur dans dans les donneees
    if not xml_string : 
        return return_code_treatment( 2 ) 
            
    data = { 'code': params['code'][0], 'xml': xml_string }
    logging.debug("**********************receiveDataFromSystel.receive_code_treatment -- data get :%s" , data )

    xmanage = XmlManager( data )
    logging.debug("**********************receiveDataFromSystel.receive_code_treatment -- xmanage :%s" , xmanage.progress_ok )
    if not xmanage.progress_ok :
        return return_code_treatment( xmanage() ) 
    logging.debug("**********************receiveDataFromSystel.receive_code_treatment -- xmanage.createXmlFile()" )
    xmanage.createXmlFile()

    return return_code_treatment( xmanage() ) 
    
# to avoid \n a the end of the sentence
print( receive_code_treatment(), end="" )

if __name__ == "__main__":
    import doctest
	# python receiveDataFromSystel.py -v
    	###doctest.testmod()
