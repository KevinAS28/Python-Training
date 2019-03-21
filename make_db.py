import sys
from PyQt4 import QtCore, QtGui, uic
import MySQLdb
qtCreatorFile = "make_db.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
def SQL_com(perintah, host="127.0.0.1", user="root"):
    db = MySQLdb.connect(host=host, user=user)
    cur = db.cursor()
    cur.execute(perintah)
    output = ""
    for baris in cur.fetchall():
        output += baris
    return output
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Buat.clicked.connect(self.Buat_db)
    def Buat_db(self):
        nama_db = self.Kotak_nama.toPlainText()
        
        #tax = (self.putar.value())
        #total_price = price  + ((tax / 100) * price)
        #total_price_string = "hasil: " + str(total_price)
        self.hasil.setText("DataBase %s telah dibuat\n%s" %(nama_db, str(SQL_com("create database %s" %(nama_db)))))    

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())