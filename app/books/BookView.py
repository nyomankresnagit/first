from flask import *
from app.books import BookController, book_bp

@book_bp.route('/viewBook')
def viewBook():
    return BookController.viewBook()

@book_bp.route('/addBook')
def addBook():
    return render_template("books/AddBuku.html")

@book_bp.route('/saveAddBook', methods=['POST'])
def saveAddBook():
    return BookController.saveAddBook()

@book_bp.route('/editBook/<string:uid>', methods=['POST','GET'])
def editBook(uid):
    if request.method == 'POST':
        return BookController.editBookPost(uid)
    elif request.method == 'GET':
        return BookController.editBookGet(uid)

@book_bp.route('/deleteBook/<string:uid>', methods=['GET'])
def deleteBook(uid):
    return BookController.deleteBook(uid)

@book_bp.route('/searchBook', methods=['POST'])
def searchBook():
    return BookController.searchBook()

@book_bp.route('/viewAvailableBook', methods=['GET'])
def viewAvailableBook():
    return BookController.viewAvailableBook()

@book_bp.route('/searchAvailableBook', methods=['POST'])
def searchAvailableBook():
    return BookController.searchAvailableBook()

@book_bp.route("/importFile", methods=['GET', 'POST'])
def importFile():
    return BookController.importFile()

@book_bp.route("/downloadTemplate", methods=['GET'])
def downloadTemplate():
    return BookController.downloadTemplate()

@book_bp.route("/showModal", methods=['POST'])
def showModal():
    return BookController.showModal()
