# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow, MainWindow):
        self.SecondWindow = SecondWindow
        self.MainWindow = MainWindow
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(665, 257)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=self.closeMain)
        self.pushButton.setGeometry(QtCore.QRect(30, 130, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked=self.showMain)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 130, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked=self.hideSecond)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 130, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 601, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 21))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "SecondWindow"))
        self.pushButton.setText(_translate("SecondWindow", "Hide Main"))
        self.pushButton_2.setText(_translate("SecondWindow", "Show Main"))
        self.pushButton_3.setText(_translate("SecondWindow", "Hide This One!"))
        self.label.setText(_translate("SecondWindow", "Type something in the other window"))
    
    def closeMain(self):
        self.MainWindow.hide()

    def showMain(self):
        self.MainWindow.show()
    
    def hideSecond(self):
        self.SecondWindow.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())