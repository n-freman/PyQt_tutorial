from PyQt5 import QtWidgets, QtGui, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('tabs.ui', self)
        self.show()


app = QtWidgets.QApplication(sys.argv)
# app.setStyle('Fusion')
window = Ui()
app.exec_()
