# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 15:08:11 2022

30. QCheckBox
Inherits from QAbstractButton
- Methods
    - isChecked()
    - setChecked(bool)
- signals
    - clicked(bool)
    - toggled(bool)
QCheckBox(str, parent)
- methods
    - isTristate(), setTristate(bool)
    - checkState(), setCheckState(Qt.CheckState)
- signals
    -stateChanged(int)
    
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
        
        self.chkEnabled = QCheckBox("Enabled", self)
        self.chkEnabled.move(30, 40)
        self.chkEnabled.setChecked(True)
        self.chkEnabled.toggled.connect(self.evt_chkEnabled_toggled)
        
        self.chkThree = QCheckBox("Three State", self)
        self.chkThree.move(30, 70)
        self.chkThree.setTristate(True)
        self.chkThree.stateChanged.connect(self.evt_chkThree_changed)
        
        self.lbl = QLabel("Old Text", self) #self refers to DlgMain object
        self.lbl.move(48,100)
        self.lbl.resize(100,100)
        font = QFont("Times New Roman", 20, 75, True)
        self.lbl.setFont(font)
        
    def evt_chkEnabled_toggled(self, chkd):
        if chkd:
            self.lbl.setDisabled(False)
        else:
            self.lbl.setDisabled(True)
            
    def evt_chkThree_changed(self, state):
        print(state)
        if state == 0:
            QMessageBox.information(self, "State", "Unchecked")
        elif state == 2:
            QMessageBox.information(self, "State", "Checked")
        else:
            QMessageBox.information(self, "State", "Partially Checked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())