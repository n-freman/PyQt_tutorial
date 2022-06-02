import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication,  QPushButton, QLabel, QFileDialog


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("df.ui", self)

        self.button = self.findChild(QPushButton, 'pushButton')
        self.label = self.findChild(QLabel, 'label')
        
        self.button.clicked.connect(self.clicker)
        self.button.setStyleSheet('''
            QPushButton {
                border: 2px dashed #8f8f91;
                border-radius: 6px;
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                stop: 0 #f6f7fa, stop: 1 #dadbde);
                min-width: 135rem;
            }

        ''')

        # Show the app
        self.show()
    
    def clicker(self):
        # self.label.setText('You clicked the button')
        fname, _ = QFileDialog.getOpenFileName(self, "Open File", "D:/Nazar", "All Files (*);; Python Files (*.py);; PNG Files (*.png)")
        if fname:
            self.label.setPixmap(QtGui.QPixmap(fname))


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()