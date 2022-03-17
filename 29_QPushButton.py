# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:38:19 2022
29. QPushButton
PyQt5 from A - Z Series on Udemy, by Michael Miller

Inherits from QAbstractButton
- Methods
    - setIcon(QIcon) 
    - setText(str)
    - setAutoRepeat(bool), setAutoRepeatDelay(msec), setAutoRepeaInterval(msec)
- Signals
    - clicked
QPushButton(str, parent)
- setFlat(bool), setDefault(bool)

https://doc.qt.io/qt-5/qpushbutton.html

@author: nathaniel.aune
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200,200)
        
        self.btn = QPushButton("Disable Label", self)
        self.btn.setIcon(QIcon(QPixmap("fotos/icon.jpg")))
        self.btn.setFlat(True)
        self.btn.move(48,48)
        self.btn.resize(120, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)
        
        self.lbl = QLabel("Old Text", self) #self refers to DlgMain object
        self.lbl.move(48,100)
        self.lbl.resize(100,100)
        font = QFont("Times New Roman", 20, 75, True)
        self.lbl.setFont(font)
        
    def evt_btn_clicked(self):
        if self.lbl.isEnabled():
            self.lbl.setDisabled(True)
            self.lbl.repaint()
            self.btn.setText("Enable Label")
            self.lbl.repaint()
        else:
            self.lbl.setDisabled(False)
            self.lbl.repaint()
            self.btn.setText("Disable Label")
            self.lbl.repaint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())