import ofac_to_df as ofac
import numpy as np
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/search_ofac',methods=['GET'])
def search_ofac():
    payload = request.get_json()

    name = payload.get('Name')
    lastName = name.split()[-1].upper()
    firstName = ' '.join(name.split()[:-1])

    df = ofac.buildMainDf()

    rows = df[(df['firstName'] == firstName) & (df['lastName'] == lastName)] #tenho que verificar se há outras combinacoes de nome e fazer uma decision tree

    print (rows)

    return 'Aopa'


app.run(port=5000,host='localhost',debug=True)