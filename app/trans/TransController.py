from flask import *
from app import db, pd, BytesIO
from app.trans.TransModel import trans
from app import trans as transaction
from app.user.UserModel import user
from app.books.BookModel import book
from app.books import book_bp
import datetime

def viewRecord():
    rows = db.session.query(trans).join(user).join(book).filter(trans.flag=="Y").with_entities(trans.id_trans, user.nama_user, book.no_buku, book.nama_buku, book.penulis_buku, trans.lama, trans.tanggal_pengembalian, trans.created_date, trans.updated_date, trans.flag)
    return render_template("trans/ListRecord.html", datas=rows)
    db.session.close()

def rentBookPost(uid):
    idUser = request.form['idUser']
    namaPeminjam = request.form['namaPeminjam']
    noBuku = request.form['noBuku']
    judulBuku = request.form['judulBuku']
    penulis = request.form['penulis']
    lama = request.form['lama']
    tanggalPengembalian = request.form['tanggalPengembalian']
    tanggalPengembalian = datetime.datetime.strptime(tanggalPengembalian, '%Y-%m-%d')
    check = checkData(idUser)
    created_date = datetime.datetime.now()
    updated_date = datetime.datetime.now()
    if check < 2:
        save = trans(no_buku=uid, id_user=idUser, lama=lama, tanggal_pengembalian=tanggalPengembalian, created_date=created_date, updated_date=updated_date, flag="Y")
        db.session.add(save)
        db.session.commit()
        saveBook = book.query.filter(book.no_buku==uid).first()
        saveBook.status_peminjaman = "Y"
        db.session.commit()
        flash("Peminjaman Berhasil")
        return redirect(url_for("trans_bp.viewRecord"))
        db.session.close()
    else:
        flash("Maksimal Peminjaman 2 Buku per User")
        return redirect(url_for("book_bp.viewAvailableBook"))

def checkData(uid):
    rows = trans.query.filter_by(id_user=uid, flag="Y").all()
    print(len(rows))
    return len(rows)

def rentBookGet(uid):
    rows = book.query.filter(book.no_buku==uid).first()
    rows2 = user.query.filter(user.flag=='Y').all()
    return render_template("trans/FormPinjam.html", datas=rows, datas2=rows2)
    db.session.close()

def saveDataPeminjam(uidTrans, uidBuku):
    updated_date = datetime.datetime.now()
    saveBook = book.query.filter_by(no_buku=uidBuku).first()
    saveBook.status_peminjaman = "N"
    db.session.commit()
    saveTrans = trans.query.filter_by(id_trans=uidTrans).first()
    saveTrans.flag = "N"
    saveTrans.updated_date = updated_date
    db.session.commit()
    flash("Data berhasil disimpan.")
    return redirect(url_for("trans_bp.viewRecord"))
    db.session.close()

def export():
    rows = db.session.query(trans).join(user).join(book).filter(trans.flag=="Y").with_entities(trans.id_trans, user.nama_user, book.no_buku, book.nama_buku, book.penulis_buku, trans.lama, trans.tanggal_pengembalian, trans.created_date, trans.updated_date, trans.flag)
    df_1 = pd.DataFrame(rows, columns=['ID Transaksi', 'Nama Peminjam', 'Nomor Buku', 'Judul Buku', 'Penulis', 'Lama Meminjam', 'Tanggal Pengembalian', 'Created Date', 'Updated Date', 'Sudah Dikembalikan'])
    
    #create an output stream
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')

    #taken from the original question
    df_1.to_excel(writer, sheet_name = "Sheet_1")
    workbook = writer.book
    worksheet = writer.sheets["Sheet_1"]
    format = workbook.add_format()
    format.set_bg_color('#eeeeee')
    worksheet.set_column(0,10,28)

    #the writer has done its job
    writer.close()

    #go back to the beginning of the stream
    output.seek(0)

    #finally return the file
    return send_file(output, attachment_filename="Trans_Record.xlsx", as_attachment=True)
    con.close()

def searchTransByName():
    uid = request.form['userId']
    nama = request.form['userName']
    if uid == "":
        uid = "%"
    else:
        uid = uid + "%"
    if nama == "":
        nama = "%"
    else:
        nama = nama + "%"
    searchTrans = db.session.query(trans).join(user).join(book).filter(trans.flag=="Y", user.id_user.like(uid), user.nama_user.like(nama)).with_entities(trans.id_trans, user.nama_user, book.no_buku, book.nama_buku, book.penulis_buku, trans.lama, trans.tanggal_pengembalian, trans.created_date, trans.updated_date, trans.flag)
    return render_template("trans/ListRecord.html", datas=searchTrans)
    db.session.close()

def renderData():
    rows = user.query.filter_by(flag = "Y").all()
    data = {
        'id': rows.id_user,
        'nama': rows.nama_user
    }
    return data