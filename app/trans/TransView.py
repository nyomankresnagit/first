from flask import *
from app.trans import TransController, trans_bp

@trans_bp.route('/viewRecord')
def viewRecord():
    return TransController.viewRecord()

@trans_bp.route('/rentBook/<string:uid>', methods=['GET','POST'])
def rentBook(uid):
    if request.method == 'POST':
        return TransController.rentBookPost(uid)
    elif request.method == 'GET':
        return TransController.rentBookGet(uid)

@trans_bp.route('/saveDataPeminjam/<string:uidTrans>/<string:uidBuku>', methods=['POST'])
def saveDataPeminjam(uidTrans, uidBuku):
    return TransController.saveDataPeminjam(uidTrans, uidBuku)

@trans_bp.route('/export', methods=['GET'])
def export():
    return TransController.export()

@trans_bp.route('/searchTransByName', methods=['POST'])
def searchTransByName():
    return TransController.searchTransByName()

@trans_bp.route('/renderData', methods=['GET'])
def renderData():
    return TransController.renderData()
