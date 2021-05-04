from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QLineEdit, QPushButton
from functools import partial
import sys


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.clearDisplay = False
        self.initializeUI()

    def initializeUI(self):
        generalLayout = QVBoxLayout()

        centralWidget = QWidget(self)
        centralWidget.setLayout(generalLayout)

        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setFont(QFont('Arial', 16))
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        buttons = {}
        buttonsLayout = QGridLayout()
        buttonsMap = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            'C': (3, 0), '0': (3, 1), '=': (3, 2), '+': (3, 3)
        }

        for text, position in buttonsMap.items():
            buttons[text] = QPushButton(text)
            buttons[text].setFixedHeight(40)

            if text == 'C':
                buttons[text].clicked.connect(self.clearClicked)
            elif text == '=':
                buttons[text].clicked.connect(self.equalClicked)
            else:
                buttons[text].clicked.connect(partial(self.buttonClicked, text))

            buttonsLayout.addWidget(buttons[text], position[0], position[1])

        generalLayout.addWidget(self.display)
        generalLayout.addLayout(buttonsLayout)

        self.setWindowTitle('Calculator')
        self.setCentralWidget(centralWidget)
        self.show()

    def clearClicked(self):
        self.display.setText('')

    def equalClicked(self):
        try:
            ans = eval(self.display.text())
            self.display.setText(str(ans))
        except:
            self.display.setText('Error')
            self.clearDisplay = True

    def buttonClicked(self, buttonText):
        if self.clearDisplay:
            self.display.setText('')
            self.clearDisplay = False

        text = self.display.text()
        self.display.setText(text + buttonText)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec())
