from flask_sqlalchemy import SQLAlchemy
from app import db

class userhistory(db.Model):
    id_user_history = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False)
    nama_user = db.Column(db.String(99), nullable=False)
    kontak = db.Column(db.String(99), nullable=False)
    flag = db.Column(db.String(2), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, id_user, nama_user, kontak, flag, created_date):
        self.id_user = id_user
        self.nama_user = nama_user
        self.kontak = kontak
        self.flag = flag
        self.created_date = created_date
    
    def __repr__(self):
        return '<user %r>' % self.id_user_history