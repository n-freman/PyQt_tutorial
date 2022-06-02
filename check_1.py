from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(313, 258)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.red_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.red_checkBox.setGeometry(QtCore.QRect(95, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.red_checkBox.setFont(font)
        self.red_checkBox.setObjectName("red_checkBox")
        self.blue_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.blue_checkBox.setGeometry(QtCore.QRect(95, 70, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.blue_checkBox.setFont(font)
        self.blue_checkBox.setObjectName("blue_checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(95, 170, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Update Check Boxes
        self.red_checkBox.stateChanged.connect(self.checked)
        self.blue_checkBox.toggled.connect(self.checked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CheckBoxes"))
        self.red_checkBox.setText(_translate("MainWindow", "Red"))
        self.blue_checkBox.setText(_translate("MainWindow", "Blue"))
        self.label.setText(_translate("MainWindow", "Pick A Color"))
    
    def checked(self):
        if self.red_checkBox.isChecked():
            self.red = 'Red'
        else:
            self.red = ''
        if self.blue_checkBox.isChecked():
            self.blue = 'Blue'
        else:
            self.blue = ''
        self.label.setText(f'{self.red} {self.blue}')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
