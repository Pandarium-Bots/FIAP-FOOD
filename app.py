from flask import Flask,jsonify,request
import mysql.connector
import os
import sys
from cliente import cliente_bp
from restaurante import restaurante_bp
from entregador import entregador_bp
from avaliacao import avaliacao_bp
from pedido import pedido_bp
from produto import produto_bp
from fatura import fatura_bp
from flask_restx import Api, Resource


#Criar uma instância do Flask
app = Flask(__name__)
api = Api(app, version='1.0', title='Minha API', description='Uma API de exemplo', doc='/swagger/')


app.register_blueprint(cliente_bp)
app.register_blueprint(restaurante_bp)
app.register_blueprint(entregador_bp)
app.register_blueprint(produto_bp)
app.register_blueprint(pedido_bp)
app.register_blueprint(avaliacao_bp)
app.register_blueprint(fatura_bp)


#Definir uma rota para a página inicial
@app.route('/')
def hello_world():
    return 'Hello, World!'



#Iniciar o aplicativo se este arquivo for executado diretamente
if __name__ == '__main__':
    app.run()



