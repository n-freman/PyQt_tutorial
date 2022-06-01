# Lesson about spin box

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Pick something from the list below')

        # Set layout
        self.setLayout(qtw.QVBoxLayout())
        
        my_label = qtw.QLabel("Pick something from the list below")
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)

        # Create a Spin Box
        my_spin = qtw.QDoubleSpinBox(
            self,
            value=10,
            maximum=100,
            singleStep=5.3,
            prefix="#",
            suffix=" Order",
            )
        my_spin.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_spin)

        # Create a button
        my_button = qtw.QPushButton(
            'Press me',
            clicked = lambda: press_it()
        )
        self.layout().addWidget(my_button)

        # Show the app
        self.show()
        
        def press_it():
            my_label.setText(f'You Picked {my_spin.value()}!')


app = qtw.QApplication([])
mw = MainWindow()


app.exec_()