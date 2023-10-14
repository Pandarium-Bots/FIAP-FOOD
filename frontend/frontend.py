from flask import Blueprint, jsonify,request,send_from_directory, render_template
import sys
from db import db_mysql_class
from itertools import groupby


front_bp = Blueprint('frontend', __name__,template_folder='templates')



@front_bp.route('/index')
@front_bp.route('/index/')
def index():
    return render_template('index.html')


