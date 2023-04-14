from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
#from models.predict_model import model
from pandas import DataFrame
import os
import pickle

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')

basic_auth = BasicAuth(app)

path = 'artifacts/1/08358ae11ea941c9af24ec914d38217e/artifacts/model/model.pkl'
path = 'model/model.pkl'
modelo = pickle.load(open(path, 'rb'))
@app.route('/')
def home():
    return "Olá, Mundo!"


@app.route('/cotacao/', methods=['POST'])
@basic_auth.required
def cotacao():
    data = request.get_json()
    preco = modelo.predict(DataFrame(data))
    print(preco)

    return jsonify(preco=preco[0].tolist())


app.run(debug=True, host='0.0.0.0', port=5000)


