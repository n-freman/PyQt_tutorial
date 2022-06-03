import sys
from datetime import datetime
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber
from PyQt5.QtCore import QTime, QTimer


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("clock.ui", self)
        self.lcd = self.findChild(QLCDNumber, 'lcdNumber')
        self.lcd.setDigitCount(12)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.timer = QTimer()
        self.timer.timeout.connect(self.lcd_number)
        
        # Start the timer and update every second
        self.timer.start(1000)

        # Call the lcd function
        self.lcd_number()

        # Show the app
        self.show()
    
    def lcd_number(self):
        time = datetime.now()
        f_time = time.strftime("%H:%M:%S %p")

        self.lcd.display(f_time)


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()