import xml.etree.ElementTree as et 
import requests
import pandas as pd

def parseXml():
    tree = et.parse("resources/sdnOfac.xml")
    root = tree.getroot()
    return root

#building main df
def buildMainDf():
    tree = et.parse("resources/sdnOfac.xml")
    root = tree.getroot()
 
    df_base_cols = ["uid", "lastName", "sdnType"]
    rows = []

    for child in root:
        for child in child:
            print(child.tag)

    for actor in root.findall('{http://tempuri.org/sdnList.xsd}sdnEntry'):
        uid = actor.find('{http://tempuri.org/sdnList.xsd}uid').text if actor is not None else None
        lastName = actor.find('{http://tempuri.org/sdnList.xsd}lastName').text if actor is not None else None
        sdnType = actor.find('{http://tempuri.org/sdnList.xsd}sdnType').text if actor is not None else None

        rows.append({"uid": uid, "lastName": lastName, "sdnType": sdnType})
    
    df_base = pd.DataFrame(rows, columns = df_base_cols)
    return (df_base)

def buildProgramList():
    tree = et.parse("resources/sdnOfac.xml")
    root = tree.getroot()
 
    df_base_cols = ["uid", "program"]
    rows = []

    for actor in root.findall('{http://tempuri.org/sdnList.xsd}sdnEntry'):

        uid = actor.find('{http://tempuri.org/sdnList.xsd}uid').text if actor is not None else None

        for actor in actor.findall('{http://tempuri.org/sdnList.xsd}programList'):
            program = actor.find('{http://tempuri.org/sdnList.xsd}program').text if actor is not None else None
            rows.append({"uid": uid, "program": program})

    
    df_base = pd.DataFrame(rows, columns = df_base_cols)
    return(df_base)
    

def loadXML():

    url = 'https://www.treasury.gov/ofac/downloads/sdn.xml'
    resp = requests.get(url)

    with open('resources/sdnOfac.xml', 'wb') as f:
        f.write(resp.content)

buildProgramList()
# buildMainDf()