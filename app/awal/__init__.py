from flask import Blueprint

awal_bp = Blueprint('awal_bp', __name__, template_folder='templates', static_folder='static')

from app.awal.awal_view import awal