from flask import Blueprint
from .frontend import front_bp

front_bp = Blueprint('frontend', __name__, template_folder='templates')