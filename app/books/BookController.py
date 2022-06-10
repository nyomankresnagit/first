from flask import *
from app import db, pd, BytesIO
from app.books.BookModel import book
from app.user.UserModel import user
from app.trans.TransModel import trans
from app import books
from app.bookHistory import BookHistory_controller
import datetime

def viewBook():
    rows = book.query.filter_by(flag="Y")
    return render_template("books/ListBuku.html", datas=rows)
    db.session.close()

def saveAddBook():
    judulBuku = request.form.get("judulBuku")
    penulis = request.form.get("penulis")
    created_date = datetime.datetime.now()
    updated_date = datetime.datetime.now()
    saveAdd = book(nama_buku=judulBuku, penulis_buku=penulis, status_peminjaman="N", flag="Y", created_date=created_date, updated_date=updated_date)
    db.session.add(saveAdd)
    db.session.commit()
    flash("Book Added.")
    return redirect(url_for("book_bp.viewBook"))
    db.session.close()

def editBookPost(uid):
    data = checkDataTrans(uid)
    if data >= 1:
        flash("Data Tidak Bisa Diupdate Karena Sedang Bertransaksi.")
        return redirect(url_for("book_bp.viewBook"))
    else:
        updated_date = datetime.datetime.now()
        judulBuku = request.form.get("judulBuku")
        penulis = request.form.get("penulis")
        saveEdit = book.query.filter_by(no_buku=uid).first()
        BookHistory = BookHistory_controller.saveAddBookHistory(uid, saveEdit.nama_buku, saveEdit.penulis_buku)
        saveEdit.nama_buku = judulBuku
        saveEdit.penulis_buku = penulis
        saveEdit.updated_date = updated_date
        db.session.commit()
        flash("Book Successfully Updated.")
        return redirect(url_for("book_bp.viewBook"))
        db.session.close()

def deleteBook(uid):
    data = checkDataTrans(uid)
    if data >= 1:
        flash("Data tidak bisa dihapus karena sedang bertransaksi.")
        return redirect(url_for("book_bp.viewBook"))
    else:
        saveDelete = book.query.filter_by(no_buku=uid).first()
        updated_date = datetime.datetime.now()
        saveDelete.flag = "N"
        saveDelete.updated_date = updated_date
        db.session.commit()
        flash("Data Successfully Deleted")
        return redirect(url_for("book_bp.viewBook"))
        db.session.close()

def searchBook():
    uid = request.form['noBuku']
    judul = request.form['judulBuku']
    penulis = request.form['penulis']
    if uid == "":
        uid = "%"
    if judul == "":
        judul = "%"
    else:
        judul = judul + "%"
    if penulis == "":
        penulis = "%"
    else:
        penulis = penulis + "%"
    rows = book.query.filter(book.nama_buku.like(judul), book.no_buku.like(uid), book.penulis_buku.like(penulis), book.flag=="Y").all()
    return render_template("books/ListBuku.html", datas=rows)
    db.session.close()

def viewAvailableBook():
    rows = book.query.filter(book.status_peminjaman=="N", book.flag=="Y").all()
    rows2 = user.query.all()
    return render_template("books/ListBukuTidakDipinjam.html", datas=rows, datas2=rows2)
    db.session.close()

def searchAvailableBook():
    uid = request.form['noBuku']
    judul = request.form['judulBuku']
    penulis = request.form['penulis']
    if uid == "":
        uid = "%"
    else:
        uid = uid + "%"
    if judul == "":
        judul = "%"
    else:
        judul = judul + "%"
    if penulis == "":
        penulis = "%"
    else:
        penulis = penulis + "%"
    searchBook = book.query.filter(book.nama_buku.like(judul), book.no_buku.like(uid), book.penulis_buku.like(penulis), book.status_peminjaman=="N", book.flag=="Y").all()
    return render_template("books/ListBukuTidakDipinjam.html", datas=searchBook)
    db.session.close()

def importFile():
    if request.method == 'POST':
        # print(request.files['file'])
        f = request.files['file']
        data_xls = pd.read_excel(f)
        # print(data_xls.loc[0][2])
        created_date = datetime.datetime.now()
        updated_date = datetime.datetime.now()
        for i in range(len(data_xls)):
            judul = data_xls.loc[i][1]
            penulis = data_xls.loc[i][2]
            saveAdd = book(nama_buku=judul, penulis_buku=penulis, status_peminjaman="N", flag="Y", created_date=created_date, updated_date=updated_date)
            db.session.add(saveAdd)
            db.session.commit()
        return redirect(url_for("book_bp.viewBook"))
    return render_template("awal/ImportFile.html")

def downloadTemplate():
    df_1 = pd.DataFrame(columns=['Judul Buku', 'Penulis'])
    
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
    return send_file(output, attachment_filename="Template_Buku.xlsx", as_attachment=True)
    con.close()

def checkDataTrans(uid):
    rows = trans.query.filter(trans.no_buku==uid, trans.flag=="Y").all()
    print(len(rows))
    return len(rows)