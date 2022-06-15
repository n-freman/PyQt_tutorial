import sys


from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QTableWidget,
    QLCDNumber,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QWidget,
    QPushButton
)
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore
from datetime import datetime


class Window(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("QStackedLayout Example")

        # Create a top-level layout
        outerlayout = QHBoxLayout()
        menu_layout = QVBoxLayout()
        order_layout = QVBoxLayout()
        products_layout = QGridLayout()
        order_button_layout = QHBoxLayout()

        menu_layout.addWidget(QPushButton('Home button'))
        menu_layout.addWidget(QPushButton('Details button'))
        menu_layout.addWidget(QPushButton('Orders button'))
        menu_layout.addWidget(QPushButton('About button'))

        for i in range(3):
            for j in range(3):
                products_layout.addWidget(QLabel(f'{(i+1)*(j+1)} product'), i, j)

        order_layout.addWidget(QLCDNumber())
        order_layout.addWidget(QTableWidget(), 4)
        order_button_layout.addWidget(QPushButton('+'), 1)
        order_button_layout.addWidget(QPushButton('DELETE'), 1)
        order_button_layout.addWidget(QPushButton('-'), 1)
        order_layout.addLayout(order_button_layout, 5)

        self.lcd = order_layout.itemAt(0).widget()
        self.lcd.setDigitCount(8)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.timer = QTimer()
        self.timer.timeout.connect(self.lcd_number)
        
        outerlayout.addLayout(menu_layout)
        outerlayout.addLayout(products_layout, 4)
        outerlayout.addLayout(order_layout, 2)

        self.setLayout(outerlayout)

        self.timer.start(1000)

        self.lcd_number()

    def lcd_number(self):
        time = datetime.now()
        f_time = time.strftime("%H:%M:%S")

        self.lcd.display(f_time)



if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = Window()

    File = open("styles/Darkeum.qss",'r')
    with File:
        qss = File.read()
        app.setStyleSheet(qss)
    

    window.show()

    sys.exit(app.exec_())