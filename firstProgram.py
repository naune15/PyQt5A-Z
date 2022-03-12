# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 14:56:28 2021

@author: nathaniel.aune
"""

import sys
from PyQt5.QtWidgets import *

#create application
app = QApplication(sys.argv)
#create main GUI canvas
dlgMain = QWidget() #also try QDialog() or QMainWindow()
dlgMain.setWindowTitle("My GUI")
#show GUI
dlgMain.show()

sys.exit(app.exec_())