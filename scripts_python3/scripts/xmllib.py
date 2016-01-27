#!/usr/bin/env python
# -*- coding: UTF-8 -*-

################################
# xmllib.py
# 
# Contient les classes appelees ppour la reception et le traitement 
# des donnees xml envoyees par Systel (requete POST)
# 
# * XmlManager = recoit, verifie les donnees xml
# 
################################

import xml.etree.ElementTree as tree
from lxml import etree

from datetime import datetime

class XmlManager( object ) :
    """
    Valide la structure des donnees
    Valide la valeur des donnees
    cree un fichier si tout ok
    """

    def __init__( self, data ):
        """
        data = {'xml': params.getvalue('xml'), 'code': params.getvalue('code')}
        type string
        """
        
        self.data   = data
        self.data_xml   = self.data['xml']
        self.code   = 1
        self._id    = None

        try : 
            self.root = etree.fromstring( self.data_xml )
        except ( etree.ParseError ) :
            self.code = 3

    def getRoot( self ):
        """
        >>> x.getRoot()
        'synergi'
        """
        return self.root.tag

    def createId( self ):
        """
        Create the file id using the code and the
        time structure : yyyymmddhhmmss
        """
        self._id = datetime.now().strftime('%Y%m%d%H%M%S')
        elf._id += self.data['code']
        print(self._id)
        pass

    def validateXmlStructure( self ):
        # http://lxml.de/validation.html#xmlschema
        pass

    def extractEvent( self ):
        pass

    def manageMultipleHands( self ):
        pass

    def createFile( self ):
        
        pass 

    def __call__( self ):
        """
        >>> x()
        1
        """
        return self.code 


if __name__ == "__main__":
    import doctest
    data = {'code': '2A', 'xml': """
<synergi>
  <syn_evenement>
    <ref_evenement>298853</ref_evenement>
    <libelle>TIH / SARTENE / 2A</libelle>
    <dateheurecreation>20150501150704</dateheurecreation>
  </syn_evenement>
  <syn_maincourante>
    <ref_evenement>298853</ref_evenement>
    <complement>Passe &#224; l'&#233;tat Termin&#233;</complement>
  </syn_maincourante>
</synergi>
    """}
    doctest.testmod(extraglobs={'x': XmlManager(data)})
