from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from check import *

import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        global value_list, text, player
        player = 1
        text = "X"
        value_list = [0,0,0,0,0,0,0,0,0]

        self.setWindowTitle("Крестики-нолики")
        self.setGeometry(250, 250, 300, 400)

        self.button_1 = QPushButton("1", self)
        self.label_1 = QLabel(self)
        self.setParametrs(self.button_1, self.label_1, 0, 0, 100, 100)

        self.button_2 = QPushButton("2", self)
        self.label_2 = QLabel(self)
        self.setParametrs(self.button_2, self.label_2, 100, 0, 100, 100)

        self.button_3 = QPushButton("3", self)
        self.label_3 = QLabel(self)
        self.setParametrs(self.button_3, self.label_3, 200, 0, 100, 100)

        self.button_4 = QPushButton("4", self)
        self.label_4 = QLabel(self)
        self.setParametrs(self.button_4, self.label_4, 0, 100, 100, 100)

        self.button_5 = QPushButton("5", self)
        self.label_5 = QLabel(self)
        self.setParametrs(self.button_5, self.label_5, 100, 100, 100, 100)

        self.button_6 = QPushButton("6", self)
        self.label_6 = QLabel(self)
        self.setParametrs(self.button_6, self.label_6, 200, 100, 100, 100)

        self.button_7 = QPushButton("7", self)
        self.label_7 = QLabel(self)
        self.setParametrs(self.button_7, self.label_7, 0, 200, 100, 100)

        self.button_8 = QPushButton("8", self)
        self.label_8 = QLabel(self)
        self.setParametrs(self.button_8, self.label_8, 100, 200, 100, 100)

        self.button_9 = QPushButton("9", self)
        self.label_9 = QLabel(self)
        self.setParametrs(self.button_9, self.label_9, 200, 200, 100, 100)

        self.label_status = QLabel(self)
        self.label_status.setStyleSheet("font-size: 15pt")
        self.label_status.setGeometry(50, 300, 300, 100)
        self.label_status.setText("Ходит первый игрок!")

        self.button_1.clicked.connect(self.clickme)
        self.button_2.clicked.connect(self.clickme)
        self.button_3.clicked.connect(self.clickme)
        self.button_4.clicked.connect(self.clickme)
        self.button_5.clicked.connect(self.clickme)
        self.button_6.clicked.connect(self.clickme)
        self.button_7.clicked.connect(self.clickme)
        self.button_8.clicked.connect(self.clickme)
        self.button_9.clicked.connect(self.clickme)

        self.show()

    def setParametrs(self, button, label, a, b, c ,d):
        button.setGeometry(a, b, c, d)
        label.setStyleSheet("font-size: 45pt")
        label.setGeometry(a + 30, b, c, d)
        label.setHidden(True)

    def clickme(self):
        global value_list, text
        source = self.sender()
        source.hide()
        self.changeLabel(int(self.sender().text()))
        value_list[int(self.sender().text()) - 1] = str(text)
        if check_gorizontal(value_list) or check_vertical(value_list) or check_diagonal(value_list):
            self.button_1.setDisabled(True)
            self.button_2.setDisabled(True)
            self.button_3.setDisabled(True)
            self.button_4.setDisabled(True)
            self.button_5.setDisabled(True)
            self.button_6.setDisabled(True)
            self.button_7.setDisabled(True)
            self.button_8.setDisabled(True)
            self.button_9.setDisabled(True)
            if player == 1:
                self.label_status.setText("Победил первый игрок!")
            else:
                self.label_status.setText("Победил второй игрок!")
        elif check_table(value_list):
            self.label_status.setGeometry(120, 300, 300, 100)
            self.label_status.setText("Ничья")
        change_player()

    def changeLabel(self, int):
        if int == 1 : 
            self.label_1.setHidden(False) 
            self.label_1.setText(text)
        elif int == 2 : 
            self.label_2.setHidden(False)
            self.label_2.setText(text)
        elif int == 3 : 
            self.label_3.setHidden(False)
            self.label_3.setText(text)
        elif int == 4 : 
            self.label_4.setHidden(False)
            self.label_4.setText(text)
        elif int == 5 : 
            self.label_5.setHidden(False)
            self.label_5.setText(text)
        elif int == 6 : 
            self.label_6.setHidden(False)
            self.label_6.setText(text)
        elif int == 7 : 
            self.label_7.setHidden(False)
            self.label_7.setText(text)
        elif int == 8 : 
            self.label_8.setHidden(False)
            self.label_8.setText(text)
        else: 
            self.label_9.setHidden(False)
            self.label_9.setText(text)

        if player == 1:
            self.label_status.setText("Ходит второй игрок!")
        else:
            self.label_status.setText("Ходит первый игрок!")

def change_player():
    global text, player
    if player:
        player = 0
    else:
        player = 1

    if player:
        text = "X"
    else:
        text = "O"

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == "__main__":
    main()