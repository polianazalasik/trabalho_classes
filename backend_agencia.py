from flask import Flask, jsonify
from playhouse.shortcuts import model_to_dict
from agencia import *

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Olá"

@app.route("/listar_pacotes")
def listar_pacotes():
    pacote = list(map(model_to_dict, Pacote.select()))
    return jsonify({'lista' :pacote})

app.run(debug=True, port=4999)