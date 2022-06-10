from flask import *
from app.bookHistory.BookHistory_model import bookhistory
from app.books import book_bp
from app import bookHistory
from app import db
import datetime

def viewBookHistory():
    rows = bookhistory.query.all()
    return render_template("bookHistory/ViewBookHistory.html", datas=rows)
    db.session.close()

def saveAddBookHistory(uid, judulBuku, penulis):
    created_date = datetime.datetime.now()
    saveAdd = bookhistory(no_buku=uid, nama_buku=judulBuku, penulis_buku=penulis, status_peminjaman="N", flag="Y", created_date=created_date)
    db.session.add(saveAdd)
    db.session.commit()
    return redirect(url_for('book_bp.viewBook'))
    db.session.close()