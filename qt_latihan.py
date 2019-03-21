import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "gui0.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.submit.clicked.connect(self.CalculateTax)
    def CalculateTax(self):
        price = int(self.box_harga.toPlainText())
        tax = (self.putar.value())
        total_price = price  + ((tax / 100) * price)
        total_price_string = "hasil: " + str(total_price)
        self.hasil.setText(total_price_string)    

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())