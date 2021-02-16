
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic, QtGui
from PyQt5.QtCore import QObject, pyqtSlot
import gpiozero

def LightGUIBindings ():
    #Check for the three exclusionary bindings first
    MainWindow.Nav_Lights_Button_Group.setChecked(True)
    # if MainWindow.Under_Sail_Button.isChecked():
    #     self.Stern_Light_Button.setChecked(True)
    #     self.Tricolor_Light_Button.setChecked(True)
    #     self.Bicolor_Light_Button.setChecked(True)
    #     self.Masthead_Light_Button.setChecked(False)
    #     self.All_Around_Light_Button.setChecked(False)
    # if MainWindow.Under_Power_Button.isChecked():
    #     self.Masthead_Light_Button.setChecked(True)
    #     self.Stern_Light_Button.setChecked(True)
    #     self.Bicolor_Light_Button.setChecked(True)
    #     self.Tricolor_Light_Button.setChecked(False)
    #     self.All_Around_Light_Button.setChecked(False)
    # if MainWindow.At_Anchor_Button.isChecked():
    #     self.All_Around_Light_Button.setChecked(True)
    #     self.Tricolor_Light_Button.setChecked(False)
    #     self.Masthead_Light_Button.setChecked(False)
    #     self.Stern_Light_Button.setChecked(False)
    #     self.Bicolor_Light_Button.setChecked(False)
    #
    #
    # if MainWindow.Masthead_Light_Button.isChecked()
    # MainWindow.Stern_Light_Button
    # MainWindow.Cabin_Light_Button
    # MainWindow.Bathroom_Light_Button
    # MainWindow.Bedroom_Light_Button
    # MainWindow.Tricolor_Light_Button
    # MainWindow.Bicolor_Light_Button
    # MainWindow.Deck_Light_Button
    # MainWindow.All_Around_Light_Button



class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("Mainwindow.ui", self)
        # ------------------------------------------------------
        #           Initializing Boat View
        # ------------------------------------------------------
        self.Boat_View.setStyleSheet("border-image: url(./UI\ Images/Boat-Red.png);")
        self.Bathroom_Light_View.setStyleSheet("border-image: url(./UI\ Images/Bathroom-Light.png);")
        self.Bedroom_Light_View.setStyleSheet("border-image: url(./UI\ Images/Bedroom-Light.png);")
        self.BiColor_Light_View.setStyleSheet("border-image: url(./UI\ Images/BIColor-Light.png);")
        self.Main_Light_View.setStyleSheet("border-image: url(./UI\ Images/Main-Light.png);")
        self.Masthead_Light_View.setStyleSheet("border-image: url(./UI\ Images/Masthead-Light.png);")
        self.Outside_Light_View.setStyleSheet("border-image: url(./UI\ Images/Outside-Light.png);")
        self.Stern_Light_View.setStyleSheet("border-image: url(./UI\ Images/Stern-Light.png);")
        self.TriColor_Light_View.setStyleSheet("border-image: url(./UI\ Images/TriColor-Light.png);")
        self.All_Around_Light_View.setStyleSheet("border-image: url(./UI\ Images/Anchor-Light.png);")
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
        self.Masthead_Light_Button.clicked.connect(GUIBindings)
        self.Stern_Light_Button.clicked.connect(GUIBindings)
        self.Cabin_Light_Button.clicked.connect(self.LightGUIButtonBindings)
        self.Bathroom_Light_Button.clicked.connect(self.LightGUIButtonBindings)
        self.Bedroom_Light_Button.clicked.connect(self.LightGUIButtonBindings)
        self.Tricolor_Light_Button.clicked.connect(self.LightGUIButtonBindings)
        self.Bicolor_Light_Button.clicked.connect(self.LightGUIButtonBindings)
        self.Deck_Light_Button.clicked.connect(self.LightGUIButtonBindings)
        self.All_Around_Light_Button.clicked.connect(self.LightGUIButtonBindings)
        self.Under_Sail_Button.clicked.connect(self.LightGUIButtonBindings)
        self.Under_Power_Button.clicked.connect(self.LightGUIButtonBindings)
        self.At_Anchor_Button.clicked.connect(self.LightGUIButtonBindings)
        # ------------------------------------------------------
        #           Initializing the engine controller
        # ------------------------------------------------------
        self.Speed_Throttle.setStyleSheet("""QSlider::groove:horizontal {border-image: url(UI Images/Throttle_Guage.png);
	                                            height: 60;
                                                position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */
                                                left: 4px; right: 4px;
	                                            margin: 100 10px;}
                                            QSlider::handle:horizontal {
                                                height: 100;
                                                border-image: url(UI Images/Throttle.png);
                                                margin: -20px -13px;}""")
        self.Speed_Throttle.sliderPressed.connect(self.MotorControlerGUIButtonAndSliderBindings)
        self.Reverse_Hull_Speed_Button.clicked.connect(self.MotorControlerGUIButtonAndSliderBindings)
        self.Reverse_Efficient_Speed_Button.clicked.connect(self.MotorControlerGUIButtonAndSliderBindings)
        self.Stop_Motor_Button.clicked.connect(self.MotorControlerGUIButtonAndSliderBindings)
        self.Forward_Efficient_Speed_Button.clicked.connect(self.MotorControlerGUIButtonAndSliderBindings)
        self.Forward_Hull_Speed_Button.clicked.connect(self.MotorControlerGUIButtonAndSliderBindings)
        self.Motor_Power_Button.clicked.connect(self.MotorControlerGUIButtonAndSliderBindings)

    def LightGUIButtonBindings(self):
        # Boat Lights
        if self.sender() is self.Masthead_Light_Button:
            if self.Masthead_Light_Button.isChecked():
                self.Masthead_Light_View.show()
                self.Under_Sail_Button.setChecked(False)
                self.At_Anchor_Button.setChecked(False)
                # Check the "Inder Power BUtton" if criteria is met
                if self.Masthead_Light_Button.isChecked():
                    if self.Stern_Light_Button.isChecked():
                        if self.Bicolor_Light_Button.isChecked():
                            if not self.Tricolor_Light_Button.isChecked():
                                self.Under_Power_Button.setChecked(True)
            else:
                self.Masthead_Light_View.hide()
                self.Under_Power_Button.setChecked(False)
        if self.sender() is self.Stern_Light_Button:
            if self.Stern_Light_Button.isChecked():
                self.Stern_Light_View.show()
                self.At_Anchor_Button.setChecked(False)
                # Check the "Inder Power BUtton" if criteria is met
                if self.Masthead_Light_Button.isChecked():
                    if self.Stern_Light_Button.isChecked():
                        if self.Bicolor_Light_Button.isChecked():
                            if not self.Tricolor_Light_Button.isChecked():
                                self.Under_Power_Button.setChecked(True)
            else:
                self.Stern_Light_View.hide()
                self.Under_Sail_Button.setChecked(False)
                self.Under_Power_Button.setChecked(False)
        if self.sender() is self.Cabin_Light_Button:
            if self.Cabin_Light_Button.isChecked():
                self.Main_Light_View.show()
            else:
                self.Main_Light_View.hide()
        if self.sender() is self.Bathroom_Light_Button:
            if self.Bathroom_Light_Button.isChecked():
                self.Bathroom_Light_View.show()
            else:
                self.Bathroom_Light_View.hide()
        if self.sender() is self.Bedroom_Light_Button:
            if self.Bedroom_Light_Button.isChecked():
                self.Bedroom_Light_View.show()
            else:
                self.Bedroom_Light_View.hide()
        if self.sender() is self.Tricolor_Light_Button:
            if self.Tricolor_Light_Button.isChecked():
                self.TriColor_Light_View.show()
                self.Under_Power_Button.setChecked(False)
                self.At_Anchor_Button.setChecked(False)
                # Check the "Under Sail Button" if criteria is met
                if self.Tricolor_Light_Button.isChecked():
                    if self.Stern_Light_Button.isChecked():
                        if self.Bicolor_Light_Button.isChecked():
                            if not self.Masthead_Light_Button.isChecked():
                                self.Under_Sail_Button.setChecked(True)
            else:
                self.TriColor_Light_View.hide()
                self.Under_Sail_Button.setChecked(False)
        if self.sender() is self.Bicolor_Light_Button:
            if self.Bicolor_Light_Button.isChecked():
                self.BiColor_Light_View.show()
                self.At_Anchor_Button.setChecked(False)
                # Check the "Inder Power BUtton" if criteria is met
                if self.Masthead_Light_Button.isChecked():
                    if self.Stern_Light_Button.isChecked():
                        if self.Bicolor_Light_Button.isChecked():
                            if not self.Tricolor_Light_Button.isChecked():
                                self.Under_Power_Button.setChecked(True)
            else:
                self.BiColor_Light_View.hide()
                self.Under_Sail_Button.setChecked(False)
                self.Under_Power_Button.setChecked(False)
        if self.sender() is self.Deck_Light_Button:
            if self.Deck_Light_Button.isChecked():
                self.Outside_Light_View.show()
            else:
                self.Outside_Light_View.hide()
        if self.sender() is self.All_Around_Light_Button:
            if self.All_Around_Light_Button.isChecked():
                self.All_Around_Light_View.show()
                # Check the "Inder Power" or "Under sail" if criteria is met
                if not self.Masthead_Light_Button.isChecked():
                    if not self.Stern_Light_Button.isChecked():
                        if not self.Bicolor_Light_Button.isChecked():
                            if not self.Tricolor_Light_Button.isChecked():
                                if self.All_Around_Light_Button.isChecked():
                                    self.At_Anchor_Button.setChecked(True)
            else:
                self.All_Around_Light_View.hide()
                self.At_Anchor_Button.setChecked(False)
        if self.sender() is self.Under_Sail_Button:
            if self.Under_Sail_Button.isChecked():
                self.TriColor_Light_View.show()
                self.BiColor_Light_View.show()
                self.Stern_Light_View.show()
                self.Stern_Light_Button.setChecked(True)
                self.Tricolor_Light_Button.setChecked(True)
                self.Bicolor_Light_Button.setChecked(True)
                # Disable the under power button
                self.Masthead_Light_View.hide()
                self.Masthead_Light_Button.setChecked(False)
                self.Under_Power_Button.setChecked(False)
                # Dissable all conflicting "At Anchor" Nav LIghts
                self.All_Around_Light_View.hide()
                self.At_Anchor_Button.setChecked(False)
                self.All_Around_Light_Button.setChecked(False)
            else:
                self.TriColor_Light_View.hide()
                self.BiColor_Light_View.hide()
                self.Stern_Light_View.hide()
                self.Stern_Light_Button.setChecked(False)
                self.Tricolor_Light_Button.setChecked(False)
                self.Bicolor_Light_Button.setChecked(False)
        if self.sender() is self.Under_Power_Button:
            if self.Under_Power_Button.isChecked():
                self.Masthead_Light_View.show()
                self.BiColor_Light_View.show()
                self.Stern_Light_View.show()
                self.Masthead_Light_Button.setChecked(True)
                self.Stern_Light_Button.setChecked(True)
                self.Bicolor_Light_Button.setChecked(True)
                # Disable the under sail button
                self.TriColor_Light_View.hide()
                self.Under_Sail_Button.setChecked(False)
                self.Tricolor_Light_Button.setChecked(False)
                # Disable the at anchor button
                self.All_Around_Light_View.hide()
                self.At_Anchor_Button.setChecked(False)
                self.All_Around_Light_Button.setChecked(False)
            else:
                self.Masthead_Light_View.hide()
                self.BiColor_Light_View.hide()
                self.Stern_Light_View.hide()
                self.Masthead_Light_Button.setChecked(False)
                self.Stern_Light_Button.setChecked(False)
                self.Bicolor_Light_Button.setChecked(False)
        if self.sender() is self.At_Anchor_Button:
            if self.At_Anchor_Button.isChecked():
                self.All_Around_Light_View.show()
                self.All_Around_Light_Button.setChecked(True)
                # Disable the under sail button and under power
                self.BiColor_Light_View.hide()
                self.Stern_Light_View.hide()
                self.TriColor_Light_View.hide()
                self.Masthead_Light_View.hide()
                self.Under_Sail_Button.setChecked(False)
                self.Tricolor_Light_Button.setChecked(False)
                self.Masthead_Light_Button.setChecked(False)
                self.Under_Power_Button.setChecked(False)
                self.Stern_Light_Button.setChecked(False)
                self.Bicolor_Light_Button.setChecked(False)
            else:
                self.All_Around_Light_View.hide()
                self.All_Around_Light_Button.setChecked(False)

    def MotorControlerGUIButtonAndSliderBindings(self):
        if self.sender() is self.Speed_Throttle.sliderPressed():
            print("it worked!")








app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
