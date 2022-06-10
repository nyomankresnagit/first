from flask_sqlalchemy import SQLAlchemy
from app import db

class trans(db.Model):
    id_trans = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False)
    no_buku = db.Column(db.Integer, db.ForeignKey('book.no_buku'), nullable=False)
    lama = db.Column(db.Integer, nullable=False)
    tanggal_pengembalian = db.Column(db.DateTime, nullable=False)
    flag = db.Column(db.String(2), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    updated_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, id_user, no_buku, tanggal_pengembalian, lama, flag, created_date, updated_date):
        self.id_user = id_user
        self.no_buku = no_buku
        self.tanggal_pengembalian = tanggal_pengembalian
        self.lama = lama
        self.flag = flag
        self.created_date = created_date
        self.updated_date = updated_date
    
    def __repr__(self):
        return '<trans %r>' % self.id_trans