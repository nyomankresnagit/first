from flask import *
from app.user import UserController, user_bp

@user_bp.route('/viewUser')
def viewUser():
    return UserController.viewUser()

@user_bp.route('/editUser/<string:uid>', methods=['POST','GET'])
def editUser(uid):
    if request.method == 'POST':
        return UserController.editUserPost(uid)
    elif request.method == 'GET':
        return UserController.editUserGet(uid)

@user_bp.route('/addUser')
def addUser():
    return render_template("user/AddUser.html")

@user_bp.route('/saveAddUser', methods=['POST'])
def saveAddUser():
    return UserController.saveAddUser()

@user_bp.route('/deleteUser/<string:uid>', methods=['GET'])
def deleteUser(uid):
    return UserController.deleteUser(uid)

@user_bp.route('/searchUser', methods=['POST'])
def searchUser():
    return UserController.searchUser()

@user_bp.route("/importFileUser", methods=['GET', 'POST'])
def importFileUser():
    return UserController.importFileUser()

@user_bp.route("/downloadTemplateUser", methods=['GET'])
def downloadTemplate():
    return UserController.downloadTemplateUser()
