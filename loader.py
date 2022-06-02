import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication,  QLabel, QTextEdit, QPushButton


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("loader.ui", self)

        # Define our Widgets
        self.label = self.findChild(QLabel, 'label')
        self.textEdit = self.findChild(QTextEdit, 'textEdit')
        self.button = self.findChild(QPushButton, 'pushButton')
        self.clear_button = self.findChild(QPushButton, 'pushButton_2')

        # Do something
        self.button.clicked.connect(self.clicker)
        self.clear_button.clicked.connect(self.clear)

        # Show the app
        self.show()
    
    def clicker(self):
        self.label.setText(f'Hello there {self.textEdit.toPlainText()}')
    
    def clear(self):
        self.label.setText('Enter your name...')
        self.textEdit.setPlainText('')


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()