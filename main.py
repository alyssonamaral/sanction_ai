import xml.etree.ElementTree as et 
import requests
import pandas as pd
from connection import insertDf 

def loadXML():
    url = 'https://www.treasury.gov/ofac/downloads/sdn.xml'
    resp = requests.get(url)

    with open('resources/sdnOfac.xml', 'wb') as f:
        f.write(resp.content)

def parseXml():
    tree = et.parse("resources/sdnOfac.xml")
    root = tree.getroot()
    return root

def buildPublshInformation():
    root = parseXml()
 
    df_base_cols = ["Publish_Date", "Record_Count"]
    rows = []

    for actor in root.findall('{http://tempuri.org/sdnList.xsd}publshInformation'):
        Publish_Date = actor.find('{http://tempuri.org/sdnList.xsd}Publish_Date').text if actor.find('{http://tempuri.org/sdnList.xsd}Publish_Date') is not None else None
        Record_Count = actor.find('{http://tempuri.org/sdnList.xsd}Record_Count').text if actor.find('{http://tempuri.org/sdnList.xsd}Record_Count') is not None else None
        
        rows.append({"Publish_Date": Publish_Date, "Record_Count": Record_Count})
    
    table_name = 'publish_information'
    df_base = pd.DataFrame(rows, columns = df_base_cols)
    df_base['Record_Count'] = pd.to_numeric(df_base['Record_Count'])
   
    insertDf(df_base)
    
    return (df_base)

def buildMainDf():
    root = parseXml()
 
    df_base_cols = ["uid", "lastName", "sdnType", "firstName", "title", "remarks"]
    rows = []

    for actor in root.findall('{http://tempuri.org/sdnList.xsd}sdnEntry'):
        uid = actor.find('{http://tempuri.org/sdnList.xsd}uid').text if actor.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None
        firstName = actor.find('{http://tempuri.org/sdnList.xsd}firstName').text if actor.find('{http://tempuri.org/sdnList.xsd}firstName') is not None else None
        lastName = actor.find('{http://tempuri.org/sdnList.xsd}lastName').text if actor.find('{http://tempuri.org/sdnList.xsd}lastName') is not None else None
        title = actor.find('{http://tempuri.org/sdnList.xsd}title').text if actor.find('{http://tempuri.org/sdnList.xsd}title') is not None else None
        sdnType = actor.find('{http://tempuri.org/sdnList.xsd}sdnType').text if actor.find('{http://tempuri.org/sdnList.xsd}sdnType') is not None else None
        remarks = actor.find('{http://tempuri.org/sdnList.xsd}remarks').text if actor.find('{http://tempuri.org/sdnList.xsd}remarks') is not None else None

        rows.append({"uid": uid, "lastName": lastName, "firstName": firstName, "title": title, "sdnType": sdnType, "remarks": remarks})
    
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

def buildNationalityList():
    root = parseXml()

    df_base_cols = ["uid", "nationalityId", "country", "mainEntry"]
    rows = []

    for actor in root.findall('{http://tempuri.org/sdnList.xsd}sdnEntry'):
        
        uid = actor.find('{http://tempuri.org/sdnList.xsd}uid').text if actor.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None

        for actor in actor.findall('{http://tempuri.org/sdnList.xsd}nationalityList'):
            for address in actor.findall('{http://tempuri.org/sdnList.xsd}nationality'):
                nationalityId = address.find('{http://tempuri.org/sdnList.xsd}uid').text if address.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None
                country = address.find('{http://tempuri.org/sdnList.xsd}country').text if address.find('{http://tempuri.org/sdnList.xsd}country') is not None else None
                mainEntry = address.find('{http://tempuri.org/sdnList.xsd}mainEntry').text if address.find('{http://tempuri.org/sdnList.xsd}mainEntry') is not None else None

                rows.append({"uid": uid, "nationalityId": nationalityId, "country": country, "mainEntry": mainEntry})   
    
    df_base = pd.DataFrame(rows, columns = df_base_cols)
    return(df_base)

def buildDateOfBirthList():
    root = parseXml()

    df_base_cols = ["uid", "dateOfBirthId", "dateOfBirth", "mainEntry"]
    rows = []

    for actor in root.findall('{http://tempuri.org/sdnList.xsd}sdnEntry'):
        
        uid = actor.find('{http://tempuri.org/sdnList.xsd}uid').text if actor.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None

        for actor in actor.findall('{http://tempuri.org/sdnList.xsd}dateOfBirthList'):
            for address in actor.findall('{http://tempuri.org/sdnList.xsd}dateOfBirthItem'):
                dateOfBirthId = address.find('{http://tempuri.org/sdnList.xsd}uid').text if address.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None
                dateOfBirth = address.find('{http://tempuri.org/sdnList.xsd}dateOfBirth').text if address.find('{http://tempuri.org/sdnList.xsd}dateOfBirth') is not None else None
                mainEntry = address.find('{http://tempuri.org/sdnList.xsd}mainEntry').text if address.find('{http://tempuri.org/sdnList.xsd}mainEntry') is not None else None

                rows.append({"uid": uid, "dateOfBirthId": dateOfBirthId, "dateOfBirth": dateOfBirth, "mainEntry": mainEntry})   
    
    df_base = pd.DataFrame(rows, columns = df_base_cols)
    return(df_base)

def buildPlaceOfBirthList():
    root = parseXml()

    df_base_cols = ["uid", "placeOfBirthId", "placeOfBirth", "mainEntry"]
    rows = []

    for actor in root.findall('{http://tempuri.org/sdnList.xsd}sdnEntry'):
        
        uid = actor.find('{http://tempuri.org/sdnList.xsd}uid').text if actor.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None

        for actor in actor.findall('{http://tempuri.org/sdnList.xsd}placeOfBirthList'):
            for address in actor.findall('{http://tempuri.org/sdnList.xsd}placeOfBirthItem'):
                placeOfBirthId = address.find('{http://tempuri.org/sdnList.xsd}uid').text if address.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None
                placeOfBirth = address.find('{http://tempuri.org/sdnList.xsd}placeOfBirth').text if address.find('{http://tempuri.org/sdnList.xsd}placeOfBirth') is not None else None
                mainEntry = address.find('{http://tempuri.org/sdnList.xsd}mainEntry').text if address.find('{http://tempuri.org/sdnList.xsd}mainEntry') is not None else None

                rows.append({"uid": uid, "placeOfBirthId": placeOfBirthId, "placeOfBirth": placeOfBirth, "mainEntry": mainEntry})   
    
    df_base = pd.DataFrame(rows, columns = df_base_cols)
    return(df_base)

def buildVesselInfo():
    root = parseXml()

    df_base_cols = ["uid", "callSign", "vesselType", "vesselFlag", "vesselOwner", "tonnage", "grossRegisteredTonnage"]
    rows = []

    for actor in root.findall('{http://tempuri.org/sdnList.xsd}sdnEntry'):
        
        uid = actor.find('{http://tempuri.org/sdnList.xsd}uid').text if actor.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None

        for address in actor.findall('{http://tempuri.org/sdnList.xsd}vesselInfo'):
            callSign = address.find('{http://tempuri.org/sdnList.xsd}callSign').text if address.find('{http://tempuri.org/sdnList.xsd}callSign') is not None else None
            vesselType = address.find('{http://tempuri.org/sdnList.xsd}vesselType').text if address.find('{http://tempuri.org/sdnList.xsd}vesselType') is not None else None
            vesselFlag = address.find('{http://tempuri.org/sdnList.xsd}vesselFlag').text if address.find('{http://tempuri.org/sdnList.xsd}vesselFlag') is not None else None
            vesselOwner = address.find('{http://tempuri.org/sdnList.xsd}vesselOwner').text if address.find('{http://tempuri.org/sdnList.xsd}vesselOwner') is not None else None
            tonnage = address.find('{http://tempuri.org/sdnList.xsd}tonnage').text if address.find('{http://tempuri.org/sdnList.xsd}tonnage') is not None else None
            grossRegisteredTonnage = address.find('{http://tempuri.org/sdnList.xsd}grossRegisteredTonnage').text if address.find('{http://tempuri.org/sdnList.xsd}grossRegisteredTonnage') is not None else None

            rows.append({"uid": uid, "callSign": callSign, "vesselType": vesselType, "vesselFlag": vesselFlag, "vesselOwner": vesselOwner, "tonnage": tonnage, "grossRegisteredTonnage": grossRegisteredTonnage})   
    
    df_base = pd.DataFrame(rows, columns = df_base_cols)
    return(df_base)

def buildCitizenshipList():
    root = parseXml()

    df_base_cols = ["uid", "citizenshipId", "country", "mainEntry"]
    rows = []

    for actor in root.findall('{http://tempuri.org/sdnList.xsd}sdnEntry'):
        
        uid = actor.find('{http://tempuri.org/sdnList.xsd}uid').text if actor.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None

        for actor in actor.findall('{http://tempuri.org/sdnList.xsd}citizenshipList'):
            for address in actor.findall('{http://tempuri.org/sdnList.xsd}citizenship'):
                citizenshipId = address.find('{http://tempuri.org/sdnList.xsd}uid').text if address.find('{http://tempuri.org/sdnList.xsd}uid') is not None else None
                country = address.find('{http://tempuri.org/sdnList.xsd}country').text if address.find('{http://tempuri.org/sdnList.xsd}country') is not None else None
                mainEntry = address.find('{http://tempuri.org/sdnList.xsd}mainEntry').text if address.find('{http://tempuri.org/sdnList.xsd}mainEntry') is not None else None

                rows.append({"uid": uid, "citizenshipId": citizenshipId, "country": country, "mainEntry": mainEntry})   
    
    df_base = pd.DataFrame(rows, columns = df_base_cols)
    return(df_base)

buildPublshInformation()