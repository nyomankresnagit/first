from flask import Blueprint

bookHistory_bp = Blueprint('bookHistory_bp', __name__, template_folder = 'templates')

from app.bookHistory.BookHistory_view import viewBookHistory