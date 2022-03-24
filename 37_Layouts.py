# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 15:27:47 2022

37. Layouts

Absolute positioning
- Best for simple apps, otherwise lots of work
- Not elastic, suffers when window is changed
Layouts
- QLayout - abstract class
    - addWidget(), removeWidget(), count(), setAlignment(), setEnabled(bool)
    - QBoxLayout
        - QVBoxLayout(), QHBoxLayou() - v for vertical, h for horizontal
        - addLayout(lyt, int), addStretch(int), setDirection()
    - QFormLayout()
        - addRow(lbl, QWidget), insertRow(idx, lbl, QWidget), removeRow(idx), setLabelAlignmnt(Qt.QAlignment)
    - QGridLayout()
        - addWidget(QWidget, x, y, xspan, yspan)

@author: nathaniel.aune
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI") # add widgets, set properties
        
        ### Create QHboxlayout widgets
#        self.lbl1 = QLabel("First Label") # no parent, to be added to layout
#        self.btn2 = QPushButton("Button 2")
#        self.led3 = QLineEdit("Line Edit 3")
#        self.cmb4 = QComboBox()
#        self.cmb4.addItems(["Item 1","Item 2","Item 3"])
        
        ### Create Form widgets
#        self.ledFname = QLineEdit("Joe")
#        self.ledLname = QLineEdit("Smith")
#        self.dteStarted = QDateTimeEdit()
#        self.spbAge = QSpinBox()
#        self.btnSubmit = QPushButton("Submit")
        
        
        ### Create GridLayout widgets
        self.btn0 = QPushButton("0")
        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")
        
        ### Setup QHBoxlayout
        #self.mainLayout = QHBoxLayout()
#        self.mainLayout = QVBoxLayout()
#        self.mainLayout.addStretch()
#        self.mainLayout.addWidget(self.lbl1)
#        self.mainLayout.addWidget(self.btn2)
#        self.mainLayout.addWidget(self.led3)
#        self.mainLayout.addWidget(self.cmb4)
#        
        
        ### Setup QFormLayout
#        self.mainLayout = QFormLayout()
#        self.mainLayout.setLabelAlignment(Qt.AlignLeft)
#        self.mainLayout.setRowWrapPolicy(QFormLayout.WrapLongRows)
#        self.mainLayout.addRow("First Name:", self.ledFname)
#        self.mainLayout.addRow("Last Name:", self.ledLname)
#        self.mainLayout.addRow("Date started:", self.dteStarted)
#        self.mainLayout.addRow("Age:", self.spbAge)
#        self.mainLayout.addRow("", self.btnSubmit)
        
        ### Setup QGridLayout
        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.btn0, 4, 0)
        self.mainLayout.addWidget(self.btn1, 4, 1)
        self.mainLayout.addWidget(self.btn2, 4, 2)
        self.mainLayout.addWidget(self.btn2, 3, 0)

        self.setLayout(self.mainLayout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv) # create application
    dlgMain = DlgMain() # create main GUI canvas
    dlgMain.show() # show the GUI
    sys.exit(app.exec_()) #execute the application