from flask import Flask,jsonify,request
import mysql.connector
import os
import sys
from cliente import cliente_bp
from restaurante import restaurante_bp
from entregador import entregador_bp
from avaliacao import avaliacao_bp


#Criar uma instância do Flask
app = Flask(__name__)


app.register_blueprint(cliente_bp)
app.register_blueprint(restaurante_bp)
app.register_blueprint(entregador_bp)
# app.register_blueprint(produto_bp)
# app.register_blueprint(pedido_bp)
app.register_blueprint(avaliacao_bp)


#Definir uma rota para a página inicial
@app.route('/')
def hello_world():
    return 'Hello, World!'



#Iniciar o aplicativo se este arquivo for executado diretamente
if __name__ == 'main':
    app.run()



