from flask import *
from app.userHistory.UserHistory_model import userhistory
from app.user import user_bp
from app import db
import datetime

def viewUserHistory():
    rows = userhistory.query.all()
    return render_template("ViewUserHistory.html", datas=rows)

def saveAddUserHistory(uid, nama, kontak):
    created_date = datetime.datetime.now()
    saveAdd = userhistory(id_user=uid, nama_user=nama, kontak=kontak, flag="Y", created_date=created_date)
    db.session.add(saveAdd)
    db.session.commit()
    return redirect(url_for("user_bp.viewUser"))
    db.session.close()