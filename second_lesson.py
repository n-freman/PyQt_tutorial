# Lesson about combo box

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

        # Create a Combo Box
        my_combo = qtw.QComboBox(
            self, 
            editable=True,
            insertPolicy=qtw.QComboBox.InsertAtBottom,
        )
        # Adding items to the Combo Box
        my_combo.addItem('Pepperoni', 'Something')
        my_combo.addItem('Cheese', 2)
        my_combo.addItem('Mushroom', qtw.QWidget)
        my_combo.addItem('Peppers')
        my_combo.addItems(['One', 'Two', 'Three'])
        my_combo.insertItem(2, 'Third Thing')
        my_combo.insertItems(2, ['First', 'Second', 'Third'])
        self.layout().addWidget(my_combo)

        # Create a button
        my_button = qtw.QPushButton(
            'Press me',
            clicked = lambda: press_it()
        )
        self.layout().addWidget(my_button)

        # Show the app
        self.show()
        
        def press_it():
            my_label.setText(f'You Picked {my_combo.currentIndex()}!')


app = qtw.QApplication([])
mw = MainWindow()


app.exec_()