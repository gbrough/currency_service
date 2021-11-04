from flask import Flask, jsonify, Response
import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

@app.route("/hello")
def hello() -> Response:
    """Simple example of an API endpoint"""
    return jsonify({"message": "ohai"})

@app.route("/hello/<string:name>")
def hello_name(name: str) -> Response:
    """Simple example using an URL parameter"""
    return jsonify({"message": "ohai {}".format(name)})


# See Readme for endpoint 1 requirements
@app.route("/rate/<string:currency1>/<string:currency2>" , methods=['GET'])
def get_rate(currency1: float, currency2: float) -> Response:
    url = 'https://freecurrencyapi.net/api/v2/latest?apikey={}'.format(API_KEY)
    response = requests.get(url)
    return jsonify({"currency1": currency1, "currency2": currency2, "rate": response.json()['data'][currency2]})



@app.route("/convert/<string:currency1>/<string:currency2>/<string:amount>" , methods=['GET'])
def get_convert(currency1: float, currency2: float, amount: float) -> Response:
    url = 'https://freecurrencyapi.net/api/v2/latest?apikey={}'.format(API_KEY)
    response = requests.get(url)
    return jsonify({"currency1": currency1, "currency2": currency2, "amount": round(float(amount) * response.json()['data'][currency2], 2)})


