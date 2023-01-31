from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont

import pyperclip

from main import generate_email, get_token


token = get_token()

class Alert(QWidget):
    def __init__(self, formal):
        super().__init__()

        lines = formal.split("\n")
        max_line_length = max(len(line) for line in lines)

        self.setMinimumSize(QSize(max_line_length * 16, 2 * len(lines) * 16))

        self.setWindowTitle("Formal Text")

        self.formalLabel = QLabel(self)
        self.formalLabel.setText("Formal: ")

        self.formalTextLabel = QLabel(self)
        self.formalTextLabel.setText(formal)

        buttonCopy = QPushButton("Copy", self)
        buttonCopy.clicked.connect(self.copy)

        self.formalTextLabel.move(80, 20)
        self.formalTextLabel.resize(QSize(max_line_length * 16, 2 * len(lines) * 16))

        myFont = QFont()
        myFont.setBold(True)

        self.formalTextLabel.setFont(myFont)

        self.formalLabel.move(20, 20)
        
        buttonCopy.resize(200, 32)
        buttonCopy.move(80, 60)
    
    def copy(self):
        pyperclip.copy(self.formalTextLabel.text())


class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()

        self.setMinimumSize(QSize(320, 140))
        self.setWindowTitle("To Formal Email...")

        self.informalLabel = QLabel(self)
        self.informalLabel.setText("Informal: ")
        
        self.informalText = QLineEdit(self)

        buttonToFormal = QPushButton('To Formal!', self)

        buttonToFormal.clicked.connect(self.clickMethod)

        self.informalText.move(80, 20)
        self.informalText.resize(200, 32)

        self.informalLabel.move(20, 20)
        
        buttonToFormal.resize(200, 32)
        buttonToFormal.move(80, 60)
    
    def clickMethod(self):
        informal_text = self.informalText.text()
        formal_text = generate_email(informal_text, token)

        self.alert = Alert(formal_text)

        self.alert.show()

def main():
    app = QtWidgets.QApplication([])

    mainWindow = MainWindow()

    mainWindow.show()

    app.exec()


if __name__ == "__main__":
    main()