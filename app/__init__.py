from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from io import BytesIO
from pathlib import Path

db = SQLAlchemy()

migrate = Migrate()

def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    db.app = app

    migrate.init_app(app, db)
    migrate.app = app

    from app.awal import awal_bp as awal
    app.register_blueprint(awal)

    from app.books import book_bp as books
    app.register_blueprint(books)

    from app.user import user_bp as user
    app.register_blueprint(user)
    
    from app.trans import trans_bp as trans
    app.register_blueprint(trans)

    from app.bookHistory import bookHistory_bp as bookHistory
    app.register_blueprint(bookHistory)

    from app.userHistory import userHistory_bp as userHistory
    app.register_blueprint(userHistory)

    return app