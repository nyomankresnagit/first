from flask import Blueprint

userHistory_bp = Blueprint('userHistory_bp', __name__, template_folder='templates', static_folder='static')

from app.userHistory.UserHistory_controller import viewUserHistory