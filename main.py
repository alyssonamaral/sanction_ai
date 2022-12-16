import xml.etree.ElementTree as et 
import requests


# def parseXml():

#     tree = et.parse("resources/sdn_advanced.xml")
#     root = tree.getroot()
#     rows = []

#     for child in root:
#         print(child.tag, child.attrib)

#     for ReferenceValueSets in root.iter('AliasTypeValues'):
#         print(ReferenceValueSets.attrib)   

#     for alias in root.findall("./ReferenceValueSets"):
#         print(alias.attrib)
        
def loadXML():

    url = 'https://www.treasury.gov/ofac/downloads/sdn.xml'
    resp = requests.get(url)

    with open('resources/sdnOfac.xml', 'wb') as f:
        f.write(resp.content)

# parseXml()
loadXML()
