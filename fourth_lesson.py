# Lesson about text edit

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Hello World!')

        # Set layout
        self.setLayout(qtw.QVBoxLayout())
        
        my_label = qtw.QLabel("Pick something from the list below")
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)

        # Create a Combo Box
        my_text = qtw.QTextEdit(
            self,
            html="<h1>Big Header Text</h1>",
            acceptRichText=True,
            lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="Hello World!",
            readOnly=False,
        )
        my_text.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_text)

        # Create a button
        my_button = qtw.QPushButton(
            'Press me',
            clicked = lambda: press_it()
        )
        self.layout().addWidget(my_button)

        # Show the app
        self.show()
        
        def press_it():
            my_label.setText(f'You Picked {my_text.toPlainText()}!')
            my_text.setPlainText('You pressed the button!')


app = qtw.QApplication([])
mw = MainWindow()


app.exec_()