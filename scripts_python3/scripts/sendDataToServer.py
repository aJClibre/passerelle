#!/usr/bin/env python3

##############################################
#
# sendDataToServer.py
#
# A simulation of the Systel server which
# sends xml data to our production server
#
##############################################

import requests
#import xml.etree.ElementTree as etr
from lxml import etree

from _vars import EnvVar

xmlTree = {}

def xmlTreeCreate():
	"""
	Create the xml structure
	"""
	xmlTree['root'] 	= etree.Element('synergi')
	xmlTree['event']	= etree.SubElement(xmlTree['root'], 'syn_evenement')
	xmlTree['ref_ev']	= etree.SubElement(xmlTree['event'], 'ref_evenement')
	xmlTree['label']	= etree.SubElement(xmlTree['event'], 'libelle')
	xmlTree['create']	= etree.SubElement(xmlTree['event'], 'dateheurecreation')
	xmlTree['hand']		= etree.SubElement(xmlTree['root'], 'syn_maincourante')
	xmlTree['ref_ha']	= etree.SubElement(xmlTree['hand'], 'ref_evenement')
	xmlTree['comple']	= etree.SubElement(xmlTree['hand'], 'complement')

def xmlTreePopulate():
	xmlTree['ref_ev'].text	= str(298853)
	xmlTree['label'].text	= "TIH / SARTENE / 2A"
	xmlTree['create'].text	= str(20150501150704)
	xmlTree['ref_ha'].text	= str(298853)
	xmlTree['comple'].text	= "Passe à l'état Terminé"

def makeRequest(get, post):
    """
    Function to test with docTest the whole process
    http://sametmax.com/un-gros-guide-bien-gras-sur-les-tests-unitaires-en-python-partie-4/
    $ python sendDataToServer

    >>> from lxml import etree
    >>> data_get    = "?code=ovensia&feedtype=01"
    >>> data_post   = {'xml':  "<synergi><syn_evenement><ref_evenement>298853</ref_evenement><libelle>TIH / SARTENE / 2A</libelle><dateheurecreation>20150501150704</dateheurecreation></syn_evenement><syn_maincourante><ref_evenement>298853</ref_evenement><complement>Passe &#224; l'&#233;tat Termin&#233;</complement></syn_maincourante></synergi>"}
    >>> makeRequest(data_get, data_post)
    1
    <BLANKLINE>
    >>> data_get = "?code=sia&feedtype=01"
    >>> makeRequest(data_get, data_post)
    9
    <BLANKLINE>
    >>> data_get = "?feedtype=01"
    >>> makeRequest(data_get, data_post) # 8
    8
    <BLANKLINE>
    >>> data_get = "?code=ovensia"
    >>> makeRequest(data_get, data_post)
    8
    <BLANKLINE>
    >>> data_get = "?code=ovensia&feedtype=03"
    >>> makeRequest(data_get, data_post)
    9
    <BLANKLINE>
    >>> data_get = ""
    >>> makeRequest(data_get, data_post)
    8
    <BLANKLINE>
    """
    r	= requests.post(EnvVar.url + get, data=post)
    print(r.text)


if __name__ == "__main__":
    
    import doctest
    doctest.testmod()
    """
    xmlTreeCreate()
	xmlTreePopulate()
	headers 	= { 'Content-Type': 'application/xml; charset=UTF-8' }
    """
