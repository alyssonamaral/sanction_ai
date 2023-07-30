import ofac_to_df as ofac
from connection import connect, param_dic
import datetime
import pandas as pd

ofac.loadXML()

conn = connect(param_dic)
cursor = conn.cursor()
query = "select publish_date, record_count from public.publish_information"
cursor.execute(query)
results = cursor.fetchall()
cursor.close()
conn.close()
df_publish = pd.DataFrame(results)
df_publish.columns = ['publish_date', 'record_count']
publish_information = ofac.publshInformation()
publish_information['publish_date'] = pd.to_datetime(publish_information['publish_date'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')

if publish_information['publish_date'][0] == df_publish['publish_date'][0] and publish_information['record_count'][0] == df_publish['record_count'][0]:
    print('There was no updates in the OFAC')
else:
    try:
        start = datetime.datetime.now()
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
        print(f'Runtime: {end - start}')
    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)