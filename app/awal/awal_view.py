from flask import *
from app.awal import awal_bp

@awal_bp.route('/')
def awal():
    return render_template("awal/Awal.html")