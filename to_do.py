# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'to_do.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

# Create a db or connect to one
conn = sqlite3.connect('mylist.db')
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE if not exists todo_list(
    list_item text);"""
)

# Commit the changes
conn.commit()

# Close connection
conn.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_button = QtWidgets.QPushButton(self.centralwidget, clicked=self.add_it)
        self.add_button.setGeometry(QtCore.QRect(20, 72, 130, 26))
        self.add_button.setObjectName("add_button")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget, clicked=self.delete_it)
        self.delete_button.setGeometry(QtCore.QRect(170, 72, 130, 26))
        self.delete_button.setObjectName("delete_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget, clicked=self.clear_it)
        self.clear_button.setGeometry(QtCore.QRect(320, 72, 130, 26))
        self.clear_button.setObjectName("clear_button")
        self.line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit.setGeometry(QtCore.QRect(20, 20, 580, 41))
        self.line_edit.setObjectName("line_edit")
        self.list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.list_widget.setGeometry(QtCore.QRect(20, 110, 580, 331))
        self.list_widget.setObjectName("list_widget")
        self.save_button = QtWidgets.QPushButton(self.centralwidget, clicked=self.save_it)
        self.save_button.setGeometry(QtCore.QRect(470, 72, 130, 26))
        self.save_button.setObjectName("save_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Grab all the items from the database
        self.grab_all()
    
    def grab_all(self):
        # Create a db or connect to one
        conn = sqlite3.connect('mylist.db')
        c = conn.cursor()
        c.execute("""SELECT * FROM todo_list""")
        records = c.fetchall()
        
        # Commit the changes
        conn.commit()

        # Close connection
        conn.close()

        # Loop through records and add to screen
        for record in records:
            self.list_widget.addItem(str(record[0]))

    # Add item to list
    def add_it(self):
        if self.line_edit.text() != '':
            item = self.line_edit.text()
            self.line_edit.setText('')
            self.list_widget.addItem(item)
    
    # Delete item from list
    def delete_it(self):
        # Grab the selected row
        clicked = self.list_widget.currentRow()
        # if clicked != -1:
        self.list_widget.takeItem(clicked)


    # Clear all items from list
    def clear_it(self):
        self.list_widget.clear()
    # Looping through the list_widget and pull out each item
    def get_all_items(self, items):
        for index in range(self.list_widget.count()):
            items.append(self.list_widget.item(index).text())

    # Save items to db
    def save_it(self):
        items = []
        self.get_all_items(items)
        # Create a db or connect to one
        conn = sqlite3.connect('mylist.db')
        c = conn.cursor()
        
        # Delete everything in the db table
        c.execute("""DELETE FROM todo_list;""")
        for item in items:
            c.execute("""INSERT INTO todo_list VALUES(
                :item);""",
                {
                    'item': item,
                }
            )
        
        # Commit the changes
        conn.commit()

        # Close connection
        conn.close()

        # Pop up box
        msg = QMessageBox()
        msg.setWindowTitle("Saved To Database!")
        msg.setText('Your Todo List Has Been Saved!')
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Fo List"))
        self.add_button.setText(_translate("MainWindow", "Add Item To List"))
        self.delete_button.setText(_translate("MainWindow", "Delete Item From List"))
        self.clear_button.setText(_translate("MainWindow", "Clear The List"))
        self.save_button.setText(_translate("MainWindow", "Save To Database"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
