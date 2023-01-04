import ofac_to_df as ofac
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/search_ofac',methods=['GET'])
def search_ofac():
    payload = request.get_json()
    print(payload)
    return 'Aopa'


app.run(port=5000,host='localhost',debug=True)