from flask import Flask, jsonify
from playhouse.shortcuts import model_to_dict
from  import *

app = Flask(__name__)

@app.route("/")
def inicio():
    return ""

@app.route("/listar_clientes")
def listar_clientes():
    cliente = list(map(model_to_dict, Cliente.select()))
    return jsonify ({'lista' :cliente})

app.run(debug=True, port=4999)