import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication,  QPushButton, QLabel, QFileDialog


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("image.ui", self)

        self.button = self.findChild(QPushButton, 'pushButton')
        self.label = self.findChild(QLabel, 'label')

        self.button.clicked.connect(self.clicker)

        # Show the app
        self.show()
    
    def clicker(self):
        # self.label.setText('You clicked the button')
        fname, _ = QFileDialog.getOpenFileName(self, "Open File", "D:/Nazar", "All Files (*);; PNG Files (*.png);; JPG Files (*.jpg)")
        if fname:
            self.label.setPixmap(QtGui.QPixmap(fname))


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()