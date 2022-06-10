from flask import *
from app.bookHistory import BookHistory_controller, bookHistory_bp

@bookHistory_bp.route('/viewBookHistory')
def viewBookHistory():
    return BookHistory_controller.viewBookHistory()