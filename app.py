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

# - a GET endpoint to get a currency rate
#     - Returns the conversion rate from currency1 to currency2 as a floating point number.
#     - The rate should be the value of 1 unit of currency1 in currency2.
#     - The return value should be a JSON object restating the request parameters and the rate.

@app.route("/rate/<string:currency1>/<string:currency2>" , methods=['GET'])
def get_rate(currency1: float, currency2: float) -> Response:
    url = 'https://freecurrencyapi.net/api/v2/latest?apikey={}'.format(API_KEY)
    response = requests.get(url)
    return jsonify({"currency1": currency1, "currency2": currency2, "rate": response.json()['data'][currency2]})

# - a GET endpoint that converts a value in one currency to another
#     - returns an amount in one currency, converted to an amount in another currency.
#     - The return value should be a JSON object restating the request parameters and the converted amount.
#     - All results should be rounded to 2 decimal points.

@app.route("/convert/<string:currency1>/<string:currency2>/<string:amount>" , methods=['GET'])
def get_convert(currency1: float, currency2: float, amount: float) -> Response:
    url = 'https://freecurrencyapi.net/api/v2/latest?apikey={}'.format(API_KEY)
    response = requests.get(url)
    return jsonify({"currency1": currency1, "currency2": currency2, "amount": round(float(amount) * response.json()['data'][currency2], 2)})


