
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic, QtGui
from PyQt5.QtCore import QObject, pyqtSlot
import gpiozero
import inspect



class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("Mainwindow.ui", self)
        # ------------------------------------------------------
        #           Initializing Boat View
        # ------------------------------------------------------
        self.Bathroom_Light_View.hide()
        self.Bedroom_Light_View.hide()
        self.BiColor_Light_View.hide()
        self.Main_Light_View.hide()
        self.Masthead_Light_View.hide()
        self.Outside_Light_View.hide()
        self.Stern_Light_View.hide()
        self.TriColor_Light_View.hide()
        self.All_Around_Light_View.hide()
        #------------------------------------------------------
        #           Initializing the Light Buttons
        #------------------------------------------------------
        #self.Masthead_Light_Button.clicked.connect(self.LightGUIButtonBindings)
        self.Lights_Quick_Actions_Button_Group.buttonClicked.connect(self.LightButtonBindings)

    def LightButtonBindings(self):
        # First, lets check if any of the criteria
        self.Bathroom_Light_Button.setChecked(False)
        print('test')





app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
