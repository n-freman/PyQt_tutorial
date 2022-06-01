# Lesson about qform layout

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Hello World!')

        # Set layout
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)
        
        my_label = qtw.QLabel("Pick something from the list below")
        my_label.setFont(qtg.QFont('Helvetica', 24))

        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)


        form_layout.addRow(my_label)
        form_layout.addRow('First name', f_name)
        form_layout.addRow('Last name', l_name)
        form_layout.addRow(
            qtw.QPushButton(
                'Press me', 
                clicked=lambda: press_it(),
            )
        )

        # Show the app
        self.show()
        
        def press_it():
            my_label.setText(f'You are {f_name.text()}!')


app = qtw.QApplication([])
mw = MainWindow()


app.exec_()