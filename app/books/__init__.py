from flask import Blueprint

book_bp = Blueprint('book_bp', __name__, template_folder = 'templates', static_folder='static')

from app.books.BookView import viewBook