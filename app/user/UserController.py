from flask import *
from app.user.UserModel import user
from app.trans.TransModel import trans
from app.userHistory import UserHistory_controller
from app import db, pd, BytesIO, Path
from app import user as userFolder
import datetime

def viewUser():
    rows = user.query.filter(user.flag=="Y").all()
    return render_template("user/ListUser.html", datas=rows)
    db.session.close()

def editUserPost(uid):
    data = checkDataTrans(uid)
    if data >= 1:
        flash("Data Tidak Bisa Diupdate Karena Sedang Bertransaksi.")
        return redirect(url_for("user_bp.viewUser"))
    else:
        updated_date = datetime.datetime.now()
        namaUser = request.form.get("namaUser")
        kontak = request.form.get("kontak")
        rows = user.query.filter_by(id_user=uid).first()
        saveUserHistory = UserHistory_controller.saveAddUserHistory(uid, rows.nama_user, rows.kontak)
        rows.nama_user = namaUser
        rows.kontak = kontak
        rows.updated_date = updated_date
        db.session.commit()
        flash("Data Successfully Updated.")
        return redirect(url_for("user_bp.viewUser"))
        db.session.close()
        
def editUserGet(uid):
    rows = user.query.get(uid)
    return render_template("user/EditUser.html", datas=rows)
    db.session.close()

def saveAddUser():
    created_date = datetime.datetime.now()
    updated_date = datetime.datetime.now()
    nama_user = request.form.get("namaUser")
    kontak = request.form.get("kontak")
    saveAdd = user(nama_user=nama_user, kontak=kontak, flag="Y", created_date=created_date, updated_date=updated_date)
    db.session.add(saveAdd)
    db.session.commit()
    flash("Data Successfully Added.")
    return redirect(url_for("user_bp.viewUser"))
    db.session.close()

def deleteUser(uid):
    data = checkDataTrans(uid)
    if data >= 1:
        flash("Data tidak bisa dihapus karena sedang bertransaksi.")
        return redirect(url_for("user_bp.viewUser"))
    else:
        updated_date = datetime.datetime.now()
        deleteUser = user.query.filter_by(id_user=uid).first()
        deleteUser.flag = "N"
        deleteUser.updated_date = updated_date
        db.session.commit()
        flash("Data Successfully Deleted.")
        return redirect(url_for("user_bp.viewUser"))
        db.session.close()

def searchUser():
    uid = request.form['idUser']
    nama = request.form['namaUser']
    if uid == "":
        uid = "%"
    else:
        uid = uid + "%"
    if nama == "":
        nama = "%"
    else:
        nama = nama + "%"
    searchUser = user.query.filter(user.id_user.like(uid), user.nama_user.like(nama), user.flag=="Y").all()
    return render_template("user/ListUser.html", datas=searchUser)
    db.session.close()

def importFileUser():
    if request.method == 'POST':
        f = request.files['file']
        data_xls = pd.read_excel(f)
        # print(data_xls.loc[0][2])
        created_date = datetime.datetime.now()
        updated_date = datetime.datetime.now()
        for i in range(len(data_xls)):
            nama = data_xls.loc[i][1]
            cons = int(data_xls.loc[i][2])
            saveAdd = user(nama_user=nama, kontak=cons, flag="Y", created_date=created_date, updated_date=updated_date)
            db.session.add(saveAdd)
            db.session.commit()
        return redirect(url_for("user_bp.viewUser"))
        db.session.close()

def downloadTemplateUser():
    df_1 = pd.DataFrame(columns=['Nama Pengguna', 'Kontak'])
    
    #create an output stream
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')

    #taken from the original question
    df_1.to_excel(writer, sheet_name = "Sheet_1")
    workbook = writer.book
    worksheet = writer.sheets["Sheet_1"]
    format = workbook.add_format()
    format.set_bg_color('#eeeeee')
    worksheet.set_column(0,2)

    #the writer has done its job
    writer.close()

    #go back to the beginning of the stream
    output.seek(0)

    #finally return the file
    return send_file(output, attachment_filename="Template_User.xlsx", as_attachment=True)
    db.session.close()

def checkDataTrans(uid):
    rows = trans.query.filter(trans.id_user==uid, trans.flag=="Y").all()
    print(len(rows))
    return len(rows)