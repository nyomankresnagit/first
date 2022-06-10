from flask_sqlalchemy import SQLAlchemy
from app import db

class user(db.Model):
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_user = db.Column(db.String(99), nullable=False)
    kontak = db.Column(db.String(99), nullable=False)
    flag = db.Column(db.String(2), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    updated_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, nama_user, kontak, flag, created_date, updated_date):
        self.nama_user = nama_user
        self.kontak = kontak
        self.flag = flag
        self.created_date = created_date
        self.updated_date = updated_date
    
    def __repr__(self):
        return '<user %r>' % self.id_user