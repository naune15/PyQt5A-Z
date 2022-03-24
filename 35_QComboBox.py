# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 15:21:58 2022

@author: nathaniel.aune

35. QComboBox - simple
QComboBox(parent)
- Methods
    - addItem(QIcon, txt, obj), insertItem(idx, QIcon, txt, obj), insertSeparator(idx)
    - addItems(list), insertItems(idx, list)
    - removeItem(idx), clear()
    - count(), currentIndex(), currentData(), currentText()
    - itemText(idx), itemData(idx), itemIcon(idx)
    - setItemText(idx, txt), setItemDate(idx, obj), setItemIcon(idx, QIcon)
    - setMaxCount(int), setMaxVisibleItems(int), setPlaceHolderText(str)
    - setCurrentIndex(idx), setCurrentText(str)
- Signals
    - currentIndexChanged(idx), currentTextChanged(txt)
    - activated(idx), textActivated(txt)
    - highlighted(idx), textHighlighted(txt)
    
36. QComboBox - editable
Methods
- setEditable(bool), isEditable()
- lineEdit(), setLineEdit()
- clearEditText(), setEditText(txt)
Signal
- editTextChanged(txt)
"""

import sys
from PyQt5.QtWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI") # add widgets, set properties
        self.resize(400,200)
        
        self.cmbStates = QComboBox(self)
        self.cmbStates.move(50,50)
#        self.cmbStates.addItems(["AL","AR","MA","MO","MI"])
        self.cmbStates.addItem("Alabama", {"ab":"AL", "pop":4000000})
        self.cmbStates.addItem("Alaska", {"ab":"AK", "pop":500000})
        self.cmbStates.addItem("Arizona", {"ab":"AZ", "pop":7000000})
        self.cmbStates.currentIndexChanged.connect(self.evt_cmbStates_changed)
        self.cmbStates.highlighted.connect(self.evt_cmbStates_highlighted)
        
        self.lblPop = QLabel("Population: 4000000", self)
        self.lblPop.move(180, 55)
        
        self.cmbPlants = QComboBox(self)
        self.cmbPlants.move(50,80)
        self.cmbPlants.setEditable(True)
        self.cmbPlants.resize(200, 20)
        self.cmbPlants.setDuplicatesEnabled(False)
        self.cmbPlants.addItem("Talictrum occidentalis", "THOC")
        self.cmbPlants.addItem("Bouteloua gracilis", "BDGR")
        self.cmbPlants.addItem("Bromus tectus", "BRTE")
        self.cmbPlants.currentIndexChanged.connect(self.evt_cmbPlants_changed)
        
    def evt_cmbPlants_changed(self, idx):
        if not self.cmbPlants.itemData(idx):
            sStr, b0k = QInputDialog.getText(self, "Add Species Code", "Add a species code for '{}'".format(self.cmbPlants.itemText(idx)))
            if b0k:
                self.cmbPlants.setItemData(idx, sStr)
        QMessageBox.information(self, "Plants", "You selected '{}'".format(self.cmbPlants.itemData(idx)))
        
    def evt_cmbStates_changed(self, idx):
        data = self.cmbStates.itemData(idx)
        QMessageBox.information(self, "ComboBox", "You selected {} \n\nThis state has a population of {}".format(data["ab"], data["pop"]))
        
    def evt_cmbStates_highlighted(self, idx):
        self.lblPop.setText("Population: {}".format(self.cmbStates.itemData(idx)["pop"]))
        
if __name__ == "__main__":
    app = QApplication(sys.argv) # create application
    dlgMain = DlgMain() # create main GUI canvas
    dlgMain.show() # show the GUI
    sys.exit(app.exec_()) #execute the application