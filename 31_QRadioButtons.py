# -*- coding: utf-8 -*-
"""
Created on Mon March 21 15:30:11 2022

31. QRadioButton
Inherits from QAbstractButton
QRadioButton(str, parent)
By default radio buttons are autoexclusive
- Only one radio button in a single parent widget can be checked
- Checking one unchecks the others
To make more than one group of radio buttons
- QButtonGroup -- a parent group for radio buttons
    - addButton(QAbstractButton, id)
    - checkedButton()
    - checkedId()
    - Within QButtonGroup, check boxes can be exclusive and radio buttons can be non-exclusive (why would you do that though?)
        - setExclusive(bool)
    
@author: nathaniel.aune
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        
        self.lbl = QLabel("My Label", self)
        self.lbl.setStyleSheet("color:red; font-size:15px")
        self.lbl.move(50, 30)
        
        ### Color Button Group
        self.btgColor = QButtonGroup()
        self.btgSize = QButtonGroup()
        
        self.rbtRed = QRadioButton("Red", self)
        self.rbtRed.move(50, 60)
        self.rbtRed.setChecked(True)
        self.btgColor.addButton(self.rbtRed)
        self.rbtRed.clicked.connect(self.evt_rbt_clicked)
        
        self.rbtBlue = QRadioButton("Blue", self)
        self.rbtBlue.move(50, 90)
        self.btgColor.addButton(self.rbtBlue)
        self.rbtBlue.clicked.connect(self.evt_rbt_clicked)
        
        self.rbtGreen = QRadioButton("Green", self)
        self.rbtGreen.move(50, 120)
        self.btgColor.addButton(self.rbtGreen)
        self.rbtGreen.clicked.connect(self.evt_rbt_clicked)
        
        
        ### Text Size Button
        self.rbtSmall = QRadioButton("Small Text", self)
        self.rbtSmall.move(50, 150)
        self.btgSize.addButton(self.rbtSmall, 10)
        self.rbtSmall.clicked.connect(self.evt_rbt_clicked)
        
        self.rbtMedium = QRadioButton("Medium Text", self)
        self.rbtMedium.move(50, 180)
        self.btgSize.addButton(self.rbtMedium, 15)
        self.rbtMedium.setChecked(True)
        self.rbtMedium.clicked.connect(self.evt_rbt_clicked)
        
        self.rbtLarge = QRadioButton("large Text", self)
        self.rbtLarge.move(50, 210)
        self.btgSize.addButton(self.rbtLarge, 20)
        self.rbtLarge.clicked.connect(self.evt_rbt_clicked)
        
    def evt_rbt_clicked(self):
        rbt = self.sender() #sender returns the widget that sent the event
        clr = self.btgColor.checkedButton()
        size = self.btgSize.checkedId()
        ss = "color:"+clr.text()+"; font-size:"+str(size)+"px"
        print(ss)
        self.lbl.setStyleSheet(ss)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
    
