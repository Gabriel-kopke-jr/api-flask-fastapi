from flask import Flask, request
from converter import convert_csv_to_json
import pandas as pd

from converter_arquivo_service import get_data_from_request

app = Flask(__name__)

@app.route('/home/')
def hello():
    return "<h1> Welcome boy </h1>"


@app.route('/converter/',methods = ['POST'])
def converter_arquivo():
    data_bytes = request.get_data()
    response = convert_csv_to_json(get_data_from_request(data_bytes))
    return response

if __name__ == '__main__':
    app.run()