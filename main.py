import requests
import json

from flask import Flask, request


app = Flask(__name__)


def valid_authentication(token):

    send = requests.post(
            'http://127.0.0.1:5000/api/valid_token',
            data=json.dumps({
                'token': str(token)
            }, timeout=[1,2])
        )

    return send.text, send.status_code

@app.route('/cadastro', methods=['POST'])
def cadastrar_user():
    pass


@app.route('/index', methods=['GET'])
def index():

    response, status_code = valid_authentication(request.headers['Authorization'])

    if status_code == 200:
        return {'msg': "Autorizado" }, status_code

    return {'error': response }, status_code


@app.route('/balance', methods=['GET'])
def saldo():

    response, status_code = valid_authentication(request.headers['Authorization'])

    if status_code == 200:
        return {'SALDO': "R$10000000,00" }, status_code

    return {'error': response }, status_code


app.run(host='0.0.0.0', port=3000)