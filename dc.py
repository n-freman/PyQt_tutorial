import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication,  QComboBox, QLabel


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("dc.ui", self)

        self.combo1 = self.findChild(QComboBox, 'comboBox')
        self.combo2 = self.findChild(QComboBox, 'comboBox_2')
        self.label = self.findChild(QLabel, 'label')

        self.combo1.addItem('Male', ['John', 'Wes', 'Dan'])
        self.combo1.addItem('Female', ['April', 'Steph', 'Beth'])

        # Click The First Dropdown
        self.combo1.activated.connect(self.clicker)
        self.combo2.activated.connect(self.clicker2)


        # Show the app
        self.show()
    
    def clicker(self, index):
        # Clear the second Box
        self.combo2.clear()
        # Do the dependent thing
        self.combo2.addItems(self.combo1.itemData(index))
    
    def clicker2(self, index):
        self.label.setText(f'You Picked {self.combo2.currentText()} - {self.combo1.currentText()}')


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()