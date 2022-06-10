from flask import *
from app.userHistory import UserHistory_controller

@userHistory_bp.route('/viewUserHistory')
def viewUserHistory():
    return UserHistory_controller.viewUserHistory()