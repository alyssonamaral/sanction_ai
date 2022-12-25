import xml.etree.ElementTree as et 
import requests
import pandas as pd


def loadXML():
    url = 'https://www.treasury.gov/ofac/downloads/sdn.xml'
    resp = requests.get(url)

    with open('resources/sdnOfac.xml', 'wb') as f:
        f.write(resp.content)

def parseXml():
    tree = et.parse("resources/sdnOfac.xml")
    root = tree.getroot()
    return root

def buildMainDf():
    root = parseXml()
 
    df_base_cols = ["uid", "lastName", "sdnType"]
    rows = []

    for child in root:
        for child in child:
            print(child.tag)

    for actor in root.findall('{http://tempuri.org/sdnList.xsd}sdnEntry'):
        uid = actor.find('{http://tempuri.org/sdnList.xsd}uid').text if actor.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None
        lastName = actor.find('{http://tempuri.org/sdnList.xsd}lastName').text if actor.find('{http://tempuri.org/sdnList.xsd}lastName') is not None else None
        sdnType = actor.find('{http://tempuri.org/sdnList.xsd}sdnType').text if actor.find('{http://tempuri.org/sdnList.xsd}sdnType') is not None else None

        rows.append({"uid": uid, "lastName": lastName, "sdnType": sdnType})
    
    df_base = pd.DataFrame(rows, columns = df_base_cols)
    return (df_base)

def buildProgramList():
    root = parseXml()
 
    df_base_cols = ["uid", "program"]
    rows = []

    for actor in root.findall('{http://tempuri.org/sdnList.xsd}sdnEntry'):

        uid = actor.find('{http://tempuri.org/sdnList.xsd}uid').text if actor.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None

        for actor in actor.findall('{http://tempuri.org/sdnList.xsd}programList'):
            program = actor.find('{http://tempuri.org/sdnList.xsd}program').text if actor.find('{http://tempuri.org/sdnList.xsd}program') is not None else None
            rows.append({"uid": uid, "program": program})
   
    df_base = pd.DataFrame(rows, columns = df_base_cols)
    return(df_base)

def buildAkaList():
    root = parseXml()
 
    df_base_cols = ["uid", "akaUid", "type", "category", "lastName"]
    rows = []

    for actor in root.findall('{http://tempuri.org/sdnList.xsd}sdnEntry'):

        uid = actor.find('{http://tempuri.org/sdnList.xsd}uid').text if actor.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None

        for actor in actor.findall('{http://tempuri.org/sdnList.xsd}akaList'):
            for aka in actor.findall('{http://tempuri.org/sdnList.xsd}aka'):
                akaUid = aka.find('{http://tempuri.org/sdnList.xsd}uid').text if aka.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None
                type = aka.find('{http://tempuri.org/sdnList.xsd}type').text if aka.find('{http://tempuri.org/sdnList.xsd}type') is not None else None
                category = aka.find('{http://tempuri.org/sdnList.xsd}category').text if aka.find('{http://tempuri.org/sdnList.xsd}category') is not None else None
                lastName = aka.find('{http://tempuri.org/sdnList.xsd}lastName').text if aka.find('{http://tempuri.org/sdnList.xsd}lastName') is not None else None

                rows.append({"uid": uid, "akaUid": akaUid, "type": type, "category": category, "lastName": lastName})   
    
    df_base = pd.DataFrame(rows, columns = df_base_cols)
    return(df_base)

def buildAddressList():
    root = parseXml()
 
    df_base_cols = ["uid", "addressUid", "city", "country", "address1", "address2", "address3", "postalCode", "stateOrProvince"]
    rows = []

    for actor in root.findall('{http://tempuri.org/sdnList.xsd}sdnEntry'):

        uid = actor.find('{http://tempuri.org/sdnList.xsd}uid').text if actor.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None

        for actor in actor.findall('{http://tempuri.org/sdnList.xsd}addressList'):
            for address in actor.findall('{http://tempuri.org/sdnList.xsd}address'):
                addressUid = address.find('{http://tempuri.org/sdnList.xsd}uid').text if address.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None
                city = address.find('{http://tempuri.org/sdnList.xsd}city').text if address.find('{http://tempuri.org/sdnList.xsd}city') is not None else None
                country = address.find('{http://tempuri.org/sdnList.xsd}country').text if address.find('{http://tempuri.org/sdnList.xsd}country') is not None else None
                address1 = address.find('{http://tempuri.org/sdnList.xsd}address1').text if address.find('{http://tempuri.org/sdnList.xsd}address1') is not None else None
                address2 = address.find('{http://tempuri.org/sdnList.xsd}address2').text if address.find('{http://tempuri.org/sdnList.xsd}address2') is not None else None
                address3 = address.find('{http://tempuri.org/sdnList.xsd}address3').text if address.find('{http://tempuri.org/sdnList.xsd}address3') is not None else None
                postalCode = address.find('{http://tempuri.org/sdnList.xsd}postalCode').text if address.find('{http://tempuri.org/sdnList.xsd}postalCode') is not None else None
                stateOrProvince = address.find('{http://tempuri.org/sdnList.xsd}stateOrProvince').text if address.find('{http://tempuri.org/sdnList.xsd}stateOrProvince') is not None else None

                rows.append({"uid": uid, "addressUid": addressUid, "city": city, "country": country, "address1": address1, "address2": address2, "address3": address3, "postalCode": postalCode, "stateOrProvince": stateOrProvince})   
    
    df_base = pd.DataFrame(rows, columns = df_base_cols)
    return(df_base)

def buildIdList():
    root = parseXml()

    df_base_cols = ["uid", "idUid", "idType", "idNumber", "idCountry", "issueDate", "expirationDate"]
    rows = []

    for actor in root.findall('{http://tempuri.org/sdnList.xsd}sdnEntry'):
        
        uid = actor.find('{http://tempuri.org/sdnList.xsd}uid').text if actor.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None

        for actor in actor.findall('{http://tempuri.org/sdnList.xsd}idList'):
            for address in actor.findall('{http://tempuri.org/sdnList.xsd}id'):
                idUid = address.find('{http://tempuri.org/sdnList.xsd}uid').text if address.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None
                idNumber = address.find('{http://tempuri.org/sdnList.xsd}idNumber').text if address.find('{http://tempuri.org/sdnList.xsd}idNumber') is not None else None
                idCountry = address.find('{http://tempuri.org/sdnList.xsd}idCountry').text if address.find('{http://tempuri.org/sdnList.xsd}idCountry') is not None else None
                idType = address.find('{http://tempuri.org/sdnList.xsd}idType').text if address.find('{http://tempuri.org/sdnList.xsd}idType') is not None else None
                issueDate = address.find('{http://tempuri.org/sdnList.xsd}issueDate').text if address.find('{http://tempuri.org/sdnList.xsd}issueDate') is not None else None
                expirationDate = address.find('{http://tempuri.org/sdnList.xsd}expirationDate').text if address.find('{http://tempuri.org/sdnList.xsd}expirationDate') is not None else None

                rows.append({"uid": uid, "idUid": idUid, "idNumber": idNumber, "idCountry": idCountry, "idType": idType, "issueDate": issueDate, "expirationDate": expirationDate})   
              
    df_base = pd.DataFrame(rows, columns = df_base_cols)
    return(df_base)


buildIdList()