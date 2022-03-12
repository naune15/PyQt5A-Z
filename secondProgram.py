# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 14:56:28 2021

@author: nathaniel.aune
"""

import sys
from PyQt5.QtWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI") # add widgets, set properties
        self.resize(200,200)
        
        self.ledText = QLineEdit("My GUI", self)
        self.ledText.move(50,50)
        
if __name__ == "__main__":
    app = QApplication(sys.argv) # create application
    dlgMain = DlgMain() # create main GUI canvas
    dlgMain.show() # show the GUI
    sys.exit(app.exec_()) #execute the application