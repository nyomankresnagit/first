from flask_sqlalchemy import SQLAlchemy
from app import db

class bookhistory(db.Model):
    no_buku_history = db.Column(db.Integer, primary_key=True, autoincrement=True)
    no_buku = db.Column(db.Integer, db.ForeignKey('book.no_buku'), nullable=False)
    nama_buku = db.Column(db.String(80), nullable=False)
    penulis_buku = db.Column(db.String(80), nullable=False)
    status_peminjaman = db.Column(db.String(2), nullable=False)
    flag = db.Column(db.String(2), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, no_buku, nama_buku, penulis_buku, status_peminjaman, flag, created_date):
        self.no_buku = no_buku
        self.nama_buku = nama_buku
        self.penulis_buku = penulis_buku
        self.status_peminjaman = status_peminjaman
        self.flag = flag
        self.created_date = created_date
    
    def __repr__(self):
        return '<bookHistory %r>' % self.no_buku_history