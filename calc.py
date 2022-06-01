from PyQt5 import QtWidgets, QtGui, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('calculator.ui', self)
        self.setWindowIcon(QtGui.QIcon('calc.png'))
        self.setWindowTitle('Calculator by Nazar#')
        self.one_button.clicked.connect(lambda: self.add_to_problem('1'))
        self.two_button.clicked.connect(lambda: self.add_to_problem('2'))
        self.three_button.clicked.connect(lambda: self.add_to_problem('3'))
        self.four_button.clicked.connect(lambda: self.add_to_problem('4'))
        self.five_button.clicked.connect(lambda: self.add_to_problem('5'))
        self.six_button.clicked.connect(lambda: self.add_to_problem('6'))
        self.seven_button.clicked.connect(lambda: self.add_to_problem('7'))
        self.eight_button.clicked.connect(lambda: self.add_to_problem('8'))
        self.nine_button.clicked.connect(lambda: self.add_to_problem('9'))
        self.zero_button.clicked.connect(lambda: self.add_to_problem('0'))
        self.divide_button.clicked.connect(lambda: self.add_to_problem('/'))
        self.multiply_button.clicked.connect(lambda: self.add_to_problem('*'))
        self.plus_button.clicked.connect(lambda: self.add_to_problem('+'))
        self.minus_button.clicked.connect(lambda: self.add_to_problem('-'))
        self.equal_button.clicked.connect(self.get_answer)
        self.clear_button.clicked.connect(self.clear)
        self.show()
    
    def add_to_problem(self, text):
        self.problem.setText(self.problem.text()+text)
    
    def get_answer(self):
        try:
            answer = eval(self.problem.text())
        except SyntaxError:
            answer = ''
        self.answer.setText(str(answer))
        self.problem.setText('')
    
    def clear(self):
        self.problem.setText('')


app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
window = Ui()
app.exec_()
