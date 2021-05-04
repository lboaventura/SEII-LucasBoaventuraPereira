from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QFileDialog
import sys


class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.filename = ''
        self.initializeUI()

    def initializeUI(self):
        openAction = QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.openFile)

        saveAction = QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveFile)

        menubar = self.menuBar()

        file = menubar.addMenu('File')
        file.addAction(openAction)
        file.addAction(saveAction)

        self.status = self.statusBar()

        self.text = QTextEdit(self)

        self.setWindowTitle('Notepad')
        self.setCentralWidget(self.text)
        self.setGeometry(100, 100, 700, 600)
        self.show()

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, 'Open file', '/home', 'Plain text files (*.txt)')

        if filename != '':
            self.filename = filename

            with open(self.filename, 'r') as f:
                self.text.setText(f.read())

            self.status.showMessage(f'File {self.filename} opened')
        else:
            self.status.showMessage('No file selected')

    def saveFile(self):
        if self.filename != '':
            with open(self.filename, 'w') as f:
                f.write(self.text.toPlainText())

            self.status.showMessage(f'File {self.filename} saved')
        else:
            self.status.showMessage('No file opened to save')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec())
