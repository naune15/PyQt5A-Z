# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 14:05:20 2022

@author: nathaniel.aune

32. QLineEdit
QLineEdit(parent)
QLineEdit(str, parent)
methods
- text(), setText(str), clear()
- setPlaceHolderText(str)
- setReadOnly(bool)
- setEchoMode(QLineEdit.Password)
- setAlignment(Qt.Alignment)
- setMaxLength(int)
signals
- textChanged(str) <--changed automatically
- textEdited(str) <--changed only by user input
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.ledTitle = QLineEdit(self.windowTitle(), self)
        self.ledTitle.move(50,50)
        self.ledTitle.setPlaceholderText("Enter a new dialog title")
        #self.ledTitle.setReadOnly(True)
        #self.ledTitle.setEchoMode(QLineEdit.Password)
        self.ledTitle.setAlignment(Qt.AlignCenter)
        self.btnChange = QPushButton("Update Title", self)
        self.btnChange.move(50,80)
        self.btnChange.clicked.connect(self.evt_btnChanged_clicked)
        self.ledTitle.textChanged.connect(self.evt_ledTitle_textChanged)
        
    def evt_btnChanged_clicked(self):
        res = QMessageBox.question(self, "Line Edit", "Are you sure you want to change the window title to '" + self.ledTitle.text() + "?")
        if res == QMessageBox.Yes:
            self.setWindowTitle(self.ledTitle.text())
    
    def evt_ledTitle_textChanged(self, title):
        self.setWindowTitle(title)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())