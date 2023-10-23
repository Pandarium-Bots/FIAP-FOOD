from flask import Blueprint, jsonify,request,send_from_directory, render_template
import sys
from db import db_mysql_class
from itertools import groupby
from restaurante import restaurante_rotas as restaurantes
import requests
import json

front_bp = Blueprint('frontend', __name__,template_folder='templates')



@front_bp.route('/')
@front_bp.route('/inicio')
@front_bp.route('/inicio/')
def index():
    return render_template('index.html',title = 'Inicio')


@front_bp.route('/restaurantes')
@front_bp.route('/restaurantes/')
def restaurantes_front():
    response, get_status = restaurantes.get_restaurantes_all()
    # print(json.loads(response.data),file=sys.stderr)
    # print(type(json.loads(response.data)),file=sys.stderr)
    if get_status == 200:
        return render_template('restaurantes.html',rest_list=json.loads(response.data), title = 'Restaurantes')
    else:
        return render_template('restaurantes.html',rest_list=[{'nome':'Nenhum restaurante encontrado'}], title = 'Restaurantes')
        



@front_bp.route('/restaurantes/<string:categoria>')
def restaurantes_front_categoria(categoria):
    response, get_status = restaurantes.get_restaurantes_categoria(categoria)
    # print(json.loads(response.data),file=sys.stderr)
    # print(type(json.loads(response.data)),file=sys.stderr)
    if get_status == 200:
        return render_template('restaurantes.html',rest_list=json.loads(response.data), title = 'Restaurantes')
    else:
        return render_template('restaurantes.html',rest_list=[{'nome':'Nenhum restaurante encontrado'}], title = 'Restaurantes')
        