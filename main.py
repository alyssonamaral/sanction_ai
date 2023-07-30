import ofac_to_df as ofac
from connection import connect, param_dic
import datetime
import pandas as pd

ofac.loadXML()

conn = connect(param_dic)
cursor = conn.cursor()
query = "select publish_date, record_count from public.publish_information order by id desc limit 1"
cursor.execute(query)
results = cursor.fetchall()
cursor.close()
conn.close()
df_publish = pd.DataFrame(results)
df_publish.columns = ['publish_date', 'record_count']
publish_information = ofac.publshInformation()
publish_information['publish_date'] = pd.to_datetime(publish_information['publish_date'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')

if (str(publish_information['publish_date'][0]) == str(0)) and (str(publish_information['record_count'][0]) == str(df_publish['record_count'][0])):
    print('There was no updates in the OFAC')
else:
    try:   
        start = datetime.datetime.now()
        ofac.truncateTables()
        ofac.buildPublshInformation()
        ofac.buildMainDf()
        ofac.buildProgramList()
        ofac.buildAkaList()
        ofac.buildAddressList()
        ofac.buildIdList()
        ofac.buildNationalityList()
        ofac.buildDateOfBirthList()
        ofac.buildPlaceOfBirthList()
        ofac.buildVesselInfo()
        ofac.buildCitizenshipList()
        end = datetime.datetime.now()
        cursor.close()
        conn.close() 
        print(f'Runtime: {end - start}')
    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)