# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:59:10 2022

28. The QLabel Widget
PyQt5 from A - Z Series on Udemy, by 

QLabel(str, parent)
setText(str)
setNum(int or dbl)
setPixmap(QPixmap)
    - can create QPixmap object

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
        
        self.btn = QPushButton("Change Label", self)
        self.btn.move(48,48)
        self.btn.resize(120, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)
        
        self.lbl = QLabel("Old Text", self) #self refers to DlgMain object
        self.lbl.move(48,100)
        self.lbl.resize(100,100)
        font = QFont("Times New Roman", 20, 75, True)
        self.lbl.setFont(font)
        
    def evt_btn_clicked(self):
        #making rich text...
        str = """
        <h1>Header</h1>
        <ul>
            <li>Red</li>
            <li>Blue</li>
        </ul>
        """
        self.lbl.setText(str)
        pxm = QPixmap("fotos/Mizuna2.0.wonderdraft_map.png")
        self.lbl.setPixmap(pxm)
        self.lbl.repaint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())