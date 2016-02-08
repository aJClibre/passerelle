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

#import xml.etree.ElementTree as tree
from lxml import etree
from io import StringIO
from datetime import datetime

from _vars import EnvVar

import logging

logging.basicConfig(filename='receiveData.log',level=logging.DEBUG, format='%(asctime)s -- %(levelname)s -- %(message)s')

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
        
        self.data           = data
        self.data_xml       = self.data['xml']
        self.code           = 0
        self._id            = None
        self.xml_result     = ""
        self.progress_ok    = False
        struct_xml_systel   = '../structureSystel.xsd'
        #struct_xml_orsec    = '../structureOrsec.xsd'
        
        try :
            self.tree = etree.XML( self.data_xml )
        except ( etree.ParseError ) :
            self.code = 2
        
        if self.validateXmlStructure() :
            self.progress_ok    = True
        else :
            #self.code = 3
            self.progress_ok    = True

    def createId( self ):
        """
        Create the file id using the code and the
        time structure : yyyymmddhhmmss
        """
        self._id = datetime.now().strftime('%Y%m%d%H%M%S')
        self._id += self.data['code']
        return self._id

    def validateXmlStructure( self ):
        """
        """
        # http://lxml.de/validation.html#xmlschema
        xml_xsd_file    = etree.parse( '../structureSystel.xsd' )
        xml_xsd         = etree.XMLSchema( xml_xsd_file )
        
        #print(xml_xsd.assertValid( self.tree ))
        return xml_xsd.validate( self.tree )

    def createXmlContent( self ):
        """
        """
        self.event = etree.tostring( self.tree.xpath('syn_evenement')[0], pretty_print = True ).decode("utf-8")
        logging.debug("xmllib.XmlManager.createXmlContent -- event: %s", self.event)
        self.hands = self.tree.xpath('syn_maincourante')
        self.xml_result = '<synergi>\n'
        logging.debug("xmllib.XmlManager.createXmlContent -- 1") 
        if len(self.hands) > 1 :
            for hand in self.tree.iter("syn_maincourante") :
                self.xml_result += self.event + \
                       etree.tostring( hand, encoding = "utf-8", pretty_print = True ).decode("utf-8")
        else :
            self.xml_result = self.data_xml # tree.tostring( self.tree )
        
        logging.debug("xmllib.XmlManager.createXmlContent -- 2")
        self.xml_result += b'</synergi>'
        logging.debug("xmllib.XmlManager.createXmlContent -- %s", self.xml_result)
        return self.xml_result

    def createXmlFile( self ):
        head                = b"<?xml version=\"1.0\" encoding=\"iso-8859-1\"?>"
        #body = etree.tostring(self.xml_result)
        content             = head + b"\n" + self.createXmlContent()
        logging.debug("xmllib.XmlManager.createXmlContent -- %s", content)
        folder_path         = EnvVar.xmlFolderPath + EnvVar.xmlFolderName
        logging.debug("xmllib.XmlManager.createXmlContent -- 4")
        with open( folder_path + self.createId() + ".xml", mode="wb", encoding="iso-8859-1" ) as file_result :
            file_result.write(content.encode(encoding='UTF-8'))
        
        logging.debug("xmllib.XmlManager.createXmlContent -- 5")
        self.code   = 1

    def __call__( self ):
        """
        >>> x()
        1
        """
        return self.code


if __name__ == "__main__":
    import doctest
    data = {'code': '02A', 'xml': """
<synergi>
  <syn_evenement>
    <ref_evenement>298853</ref_evenement>
    <libelle>TIH / SARTENE / 2A</libelle>
    <dateheurecreation>20150501150704</dateheurecreation>
  </syn_evenement>
  <syn_maincourante>
    <ref_evenement>298853</ref_evenement>
    <complement>Passe à l'état Terminé</complement>
  </syn_maincourante>
</synergi>
    """}
    doctest.testmod(extraglobs={'x': XmlManager(data)})
