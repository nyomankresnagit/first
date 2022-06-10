from flask_sqlalchemy import SQLAlchemy
from app import db

class book(db.Model):
    no_buku = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_buku = db.Column(db.String(80), nullable=False)
    penulis_buku = db.Column(db.String(80), nullable=False)
    status_peminjaman = db.Column(db.String(2), nullable=False)
    flag = db.Column(db.String(2), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    updated_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, nama_buku, penulis_buku, status_peminjaman, flag, created_date, updated_date):
        self.nama_buku = nama_buku
        self.penulis_buku = penulis_buku
        self.status_peminjaman = status_peminjaman
        self.flag = flag
        self.created_date = created_date
        self.updated_date = updated_date
    
    def __repr__(self):
        return '<book %r>' % self.no_buku