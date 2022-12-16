import xml.etree.ElementTree as et 


def parseXml():

    tree = et.parse("resources/sdn_advanced.xml")
    root = tree.getroot()

    for child in root:
        print(child.tag, child.attrib)

parseXml()
