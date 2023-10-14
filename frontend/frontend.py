from flask import Blueprint, jsonify,request,send_from_directory, render_template
import sys
from db import db_mysql_class
from itertools import groupby


front_bp = Blueprint('front', __name__,template_folder='templates')



@front_bp.route('/')
def index():
    return render_template('index.html')


@front_bp.route('/static/<path:filename>')
def custom_static(filename):
    return {'arquivo':filename}
    # print("Validando se chega aqui", file=sys.stderr)
    # return send_from_directory(app.root_path + '/frontend/static/', filename)
