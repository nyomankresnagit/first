from flask import Blueprint

trans_bp = Blueprint('trans_bp', __name__, template_folder = 'templates', static_folder='static')

from app.trans.TransView import viewRecord