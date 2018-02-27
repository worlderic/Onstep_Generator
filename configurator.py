# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/developpeur/onstep_configurator/configurator.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_configurator(object):
    def setupUi(self, configurator):
        configurator.setObjectName("configurator")
        configurator.resize(613, 882)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("OnStep_Logo_Medium.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        configurator.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(configurator)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_15 = QtWidgets.QLabel(self.centralWidget)
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("OnStep_Logo_Medium.png"))
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_14 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.mount_combo = QtWidgets.QComboBox(self.centralWidget)
        self.mount_combo.setObjectName("mount_combo")
        self.mount_combo.addItem("")
        self.mount_combo.addItem("")
        self.mount_combo.addItem("")
        self.horizontalLayout.addWidget(self.mount_combo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.board_combo = QtWidgets.QComboBox(self.centralWidget)
        self.board_combo.setObjectName("board_combo")
        self.board_combo.addItem("")
        self.board_combo.addItem("")
        self.board_combo.addItem("")
        self.board_combo.addItem("")
        self.board_combo.addItem("")
        self.board_combo.addItem("")
        self.board_combo.addItem("")
        self.board_combo.addItem("")
        self.horizontalLayout_2.addWidget(self.board_combo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.maxrate_spin = QtWidgets.QSpinBox(self.centralWidget)
        self.maxrate_spin.setMaximum(128)
        self.maxrate_spin.setProperty("value", 32)
        self.maxrate_spin.setObjectName("maxrate_spin")
        self.horizontalLayout_3.addWidget(self.maxrate_spin)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.pec_spin = QtWidgets.QSpinBox(self.centralWidget)
        self.pec_spin.setMaximum(100000)
        self.pec_spin.setObjectName("pec_spin")
        self.horizontalLayout_4.addWidget(self.pec_spin)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.centralWidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.comboBox_11 = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_11)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.axis1_worm_spindouble = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.axis1_worm_spindouble.setDecimals(3)
        self.axis1_worm_spindouble.setMinimum(1.0)
        self.axis1_worm_spindouble.setMaximum(99999.99)
        self.axis1_worm_spindouble.setProperty("value", 144.0)
        self.axis1_worm_spindouble.setObjectName("axis1_worm_spindouble")
        self.gridLayout.addWidget(self.axis1_worm_spindouble, 1, 1, 1, 1)
        self.axis1_gear_spindouble = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.axis1_gear_spindouble.setDecimals(3)
        self.axis1_gear_spindouble.setMinimum(1.0)
        self.axis1_gear_spindouble.setMaximum(99999.99)
        self.axis1_gear_spindouble.setObjectName("axis1_gear_spindouble")
        self.gridLayout.addWidget(self.axis1_gear_spindouble, 2, 1, 1, 1)
        self.axis2_gear_spindouble = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.axis2_gear_spindouble.setDecimals(3)
        self.axis2_gear_spindouble.setMinimum(1.0)
        self.axis2_gear_spindouble.setMaximum(99999.99)
        self.axis2_gear_spindouble.setProperty("value", 1.0)
        self.axis2_gear_spindouble.setObjectName("axis2_gear_spindouble")
        self.gridLayout.addWidget(self.axis2_gear_spindouble, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.axis2_worm_spindouble = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.axis2_worm_spindouble.setDecimals(3)
        self.axis2_worm_spindouble.setMinimum(1.0)
        self.axis2_worm_spindouble.setMaximum(99999.99)
        self.axis2_worm_spindouble.setProperty("value", 144.0)
        self.axis2_worm_spindouble.setObjectName("axis2_worm_spindouble")
        self.gridLayout.addWidget(self.axis2_worm_spindouble, 1, 2, 1, 1)
        self.axis1_motor_combo = QtWidgets.QComboBox(self.centralWidget)
        self.axis1_motor_combo.setObjectName("axis1_motor_combo")
        self.axis1_motor_combo.addItem("")
        self.axis1_motor_combo.addItem("")
        self.axis1_motor_combo.addItem("")
        self.gridLayout.addWidget(self.axis1_motor_combo, 3, 1, 1, 1)
        self.axis1_driver_combo = QtWidgets.QComboBox(self.centralWidget)
        self.axis1_driver_combo.setObjectName("axis1_driver_combo")
        self.axis1_driver_combo.addItem("")
        self.axis1_driver_combo.addItem("")
        self.axis1_driver_combo.addItem("")
        self.axis1_driver_combo.addItem("")
        self.axis1_driver_combo.addItem("")
        self.axis1_driver_combo.addItem("")
        self.axis1_driver_combo.addItem("")
        self.axis1_driver_combo.addItem("")
        self.axis1_driver_combo.addItem("")
        self.gridLayout.addWidget(self.axis1_driver_combo, 6, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.axis2_motor_combo = QtWidgets.QComboBox(self.centralWidget)
        self.axis2_motor_combo.setObjectName("axis2_motor_combo")
        self.axis2_motor_combo.addItem("")
        self.axis2_motor_combo.addItem("")
        self.axis2_motor_combo.addItem("")
        self.gridLayout.addWidget(self.axis2_motor_combo, 3, 2, 1, 1)
        self.axis2_driver_combo = QtWidgets.QComboBox(self.centralWidget)
        self.axis2_driver_combo.setObjectName("axis2_driver_combo")
        self.axis2_driver_combo.addItem("")
        self.axis2_driver_combo.addItem("")
        self.axis2_driver_combo.addItem("")
        self.axis2_driver_combo.addItem("")
        self.axis2_driver_combo.addItem("")
        self.axis2_driver_combo.addItem("")
        self.axis2_driver_combo.addItem("")
        self.axis2_driver_combo.addItem("")
        self.axis2_driver_combo.addItem("")
        self.gridLayout.addWidget(self.axis2_driver_combo, 6, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.axis1_micro_combo = QtWidgets.QComboBox(self.centralWidget)
        self.axis1_micro_combo.setObjectName("axis1_micro_combo")
        self.axis1_micro_combo.addItem("")
        self.axis1_micro_combo.addItem("")
        self.axis1_micro_combo.addItem("")
        self.axis1_micro_combo.addItem("")
        self.axis1_micro_combo.addItem("")
        self.axis1_micro_combo.addItem("")
        self.axis1_micro_combo.addItem("")
        self.axis1_micro_combo.addItem("")
        self.axis1_micro_combo.addItem("")
        self.gridLayout.addWidget(self.axis1_micro_combo, 4, 1, 1, 1)
        self.axis2_micro_combo = QtWidgets.QComboBox(self.centralWidget)
        self.axis2_micro_combo.setObjectName("axis2_micro_combo")
        self.axis2_micro_combo.addItem("")
        self.axis2_micro_combo.addItem("")
        self.axis2_micro_combo.addItem("")
        self.axis2_micro_combo.addItem("")
        self.axis2_micro_combo.addItem("")
        self.axis2_micro_combo.addItem("")
        self.axis2_micro_combo.addItem("")
        self.axis2_micro_combo.addItem("")
        self.axis2_micro_combo.addItem("")
        self.gridLayout.addWidget(self.axis2_micro_combo, 4, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.axis1_mod_combo = QtWidgets.QComboBox(self.centralWidget)
        self.axis1_mod_combo.setObjectName("axis1_mod_combo")
        self.axis1_mod_combo.addItem("")
        self.axis1_mod_combo.addItem("")
        self.gridLayout.addWidget(self.axis1_mod_combo, 5, 1, 1, 1)
        self.axis2_mod_combo = QtWidgets.QComboBox(self.centralWidget)
        self.axis2_mod_combo.setObjectName("axis2_mod_combo")
        self.axis2_mod_combo.addItem("")
        self.axis2_mod_combo.addItem("")
        self.gridLayout.addWidget(self.axis2_mod_combo, 5, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.generate_buttom = QtWidgets.QPushButton(self.centralWidget)
        self.generate_buttom.setObjectName("generate_buttom")
        self.verticalLayout.addWidget(self.generate_buttom)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.path_line = QtWidgets.QLineEdit(self.centralWidget)
        self.path_line.setObjectName("path_line")
        self.horizontalLayout_6.addWidget(self.path_line)
        self.path_button = QtWidgets.QToolButton(self.centralWidget)
        self.path_button.setObjectName("path_button")
        self.horizontalLayout_6.addWidget(self.path_button)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.prompt_textbrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.prompt_textbrowser.setObjectName("prompt_textbrowser")
        self.verticalLayout.addWidget(self.prompt_textbrowser)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        configurator.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(configurator)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 613, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuOnStep_Configurator = QtWidgets.QMenu(self.menuBar)
        self.menuOnStep_Configurator.setObjectName("menuOnStep_Configurator")
        self.menuInfo = QtWidgets.QMenu(self.menuBar)
        self.menuInfo.setObjectName("menuInfo")
        configurator.setMenuBar(self.menuBar)
        self.actionSave = QtWidgets.QAction(configurator)
        self.actionSave.setCheckable(False)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(configurator)
        self.actionLoad.setCheckable(False)
        self.actionLoad.setObjectName("actionLoad")
        self.actionAbout = QtWidgets.QAction(configurator)
        self.actionAbout.setCheckable(False)
        self.actionAbout.setEnabled(True)
        self.actionAbout.setObjectName("actionAbout")
        self.menuOnStep_Configurator.addAction(self.actionSave)
        self.menuOnStep_Configurator.addAction(self.actionLoad)
        self.menuInfo.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuOnStep_Configurator.menuAction())
        self.menuBar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(configurator)
        self.buttonBox.clicked['QAbstractButton*'].connect(configurator.close)
        QtCore.QMetaObject.connectSlotsByName(configurator)

    def retranslateUi(self, configurator):
        _translate = QtCore.QCoreApplication.translate
        configurator.setWindowTitle(_translate("configurator", "configurator"))
        self.label_14.setText(_translate("configurator", "Configuration Parameters"))
        self.label_7.setText(_translate("configurator", "Mount Type"))
        self.mount_combo.setItemText(0, _translate("configurator", "Equatorial"))
        self.mount_combo.setItemText(1, _translate("configurator", "Alt-Azimuth"))
        self.mount_combo.setItemText(2, _translate("configurator", "Fork"))
        self.label_8.setText(_translate("configurator", "Board Type"))
        self.board_combo.setItemText(0, _translate("configurator", "RAMPS 1.4 or 1.5"))
        self.board_combo.setItemText(1, _translate("configurator", "MiniPCB (2 axis)"))
        self.board_combo.setItemText(2, _translate("configurator", "MaxPCB (4 axis)"))
        self.board_combo.setItemText(3, _translate("configurator", "STM32F1"))
        self.board_combo.setItemText(4, _translate("configurator", "TivaC"))
        self.board_combo.setItemText(5, _translate("configurator", "Classic"))
        self.board_combo.setItemText(6, _translate("configurator", "Mega2560 Alternate"))
        self.board_combo.setItemText(7, _translate("configurator", "Custom"))
        self.label_10.setText(_translate("configurator", "Max Rate Ratio"))
        self.label_9.setText(_translate("configurator", "PEC Buffer Size"))
        self.label_13.setText(_translate("configurator", "Auto Sideral Traking mod"))
        self.comboBox_11.setItemText(0, _translate("configurator", "Off"))
        self.comboBox_11.setItemText(1, _translate("configurator", "On"))
        self.label_4.setText(_translate("configurator", "Gears/Pulleys Ratio"))
        self.label_6.setText(_translate("configurator", "MicroSteps Tracking"))
        self.label.setText(_translate("configurator", "Axis 1"))
        self.label_2.setText(_translate("configurator", "Axis 2"))
        self.axis1_motor_combo.setItemText(0, _translate("configurator", "200 steps, 1.8°/step"))
        self.axis1_motor_combo.setItemText(1, _translate("configurator", "400 steps, 1.8°/step"))
        self.axis1_motor_combo.setItemText(2, _translate("configurator", "48 steps, 7.5°/step"))
        self.axis1_driver_combo.setItemText(0, _translate("configurator", "A4988"))
        self.axis1_driver_combo.setItemText(1, _translate("configurator", "DRV8825"))
        self.axis1_driver_combo.setItemText(2, _translate("configurator", "LV8729 or RAPS128"))
        self.axis1_driver_combo.setItemText(3, _translate("configurator", "TMC2208"))
        self.axis1_driver_combo.setItemText(4, _translate("configurator", "TMC2130"))
        self.axis1_driver_combo.setItemText(5, _translate("configurator", "TMC2130 (Quiet)"))
        self.axis1_driver_combo.setItemText(6, _translate("configurator", "TMC2130 (VQuiet)"))
        self.axis1_driver_combo.setItemText(7, _translate("configurator", "TMC2130 (Quiet, LowPWR)"))
        self.axis1_driver_combo.setItemText(8, _translate("configurator", "TMC2130 (VQuiet, LowPWR)"))
        self.label_5.setText(_translate("configurator", "Stepper-Steps"))
        self.axis2_motor_combo.setItemText(0, _translate("configurator", "200 steps, 1.8°/step"))
        self.axis2_motor_combo.setItemText(1, _translate("configurator", "400 steps, 0.9°/step"))
        self.axis2_motor_combo.setItemText(2, _translate("configurator", "48 steps, 7.5°/step"))
        self.axis2_driver_combo.setItemText(0, _translate("configurator", "A4988"))
        self.axis2_driver_combo.setItemText(1, _translate("configurator", "DRV8825"))
        self.axis2_driver_combo.setItemText(2, _translate("configurator", "LV8729 or RAPS128"))
        self.axis2_driver_combo.setItemText(3, _translate("configurator", "TMC2208"))
        self.axis2_driver_combo.setItemText(4, _translate("configurator", "TMC2130"))
        self.axis2_driver_combo.setItemText(5, _translate("configurator", "TMC2130 (Quiet)"))
        self.axis2_driver_combo.setItemText(6, _translate("configurator", "TMC2130 (VQuiet)"))
        self.axis2_driver_combo.setItemText(7, _translate("configurator", "TMC2130 (Quiet, LowPWR)"))
        self.axis2_driver_combo.setItemText(8, _translate("configurator", "TMC2130 (VQuiet, LowPWR)"))
        self.label_3.setText(_translate("configurator", "Worm Wheel Ratio"))
        self.axis1_micro_combo.setItemText(0, _translate("configurator", "1"))
        self.axis1_micro_combo.setItemText(1, _translate("configurator", "2"))
        self.axis1_micro_combo.setItemText(2, _translate("configurator", "4"))
        self.axis1_micro_combo.setItemText(3, _translate("configurator", "8"))
        self.axis1_micro_combo.setItemText(4, _translate("configurator", "16"))
        self.axis1_micro_combo.setItemText(5, _translate("configurator", "32"))
        self.axis1_micro_combo.setItemText(6, _translate("configurator", "64"))
        self.axis1_micro_combo.setItemText(7, _translate("configurator", "128"))
        self.axis1_micro_combo.setItemText(8, _translate("configurator", "256"))
        self.axis2_micro_combo.setItemText(0, _translate("configurator", "1"))
        self.axis2_micro_combo.setItemText(1, _translate("configurator", "2"))
        self.axis2_micro_combo.setItemText(2, _translate("configurator", "4"))
        self.axis2_micro_combo.setItemText(3, _translate("configurator", "8"))
        self.axis2_micro_combo.setItemText(4, _translate("configurator", "16"))
        self.axis2_micro_combo.setItemText(5, _translate("configurator", "32"))
        self.axis2_micro_combo.setItemText(6, _translate("configurator", "64"))
        self.axis2_micro_combo.setItemText(7, _translate("configurator", "128"))
        self.axis2_micro_combo.setItemText(8, _translate("configurator", "256"))
        self.label_11.setText(_translate("configurator", "MicroSteps Slewing"))
        self.label_12.setText(_translate("configurator", "Driver Model"))
        self.axis1_mod_combo.setItemText(0, _translate("configurator", "Same as tracking"))
        self.axis1_mod_combo.setItemText(1, _translate("configurator", "Off"))
        self.axis2_mod_combo.setItemText(0, _translate("configurator", "Same as tracking"))
        self.axis2_mod_combo.setItemText(1, _translate("configurator", "Off"))
        self.generate_buttom.setText(_translate("configurator", "Generate"))
        self.path_button.setText(_translate("configurator", "..."))
        self.prompt_textbrowser.setHtml(_translate("configurator", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Configure your setup for Onstep !</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Standby...</p></body></html>"))
        self.menuOnStep_Configurator.setTitle(_translate("configurator", "File"))
        self.menuInfo.setTitle(_translate("configurator", "Info"))
        self.actionSave.setText(_translate("configurator", "Save"))
        self.actionSave.setShortcut(_translate("configurator", "Ctrl+S"))
        self.actionLoad.setText(_translate("configurator", "Load"))
        self.actionLoad.setShortcut(_translate("configurator", "Ctrl+O"))
        self.actionAbout.setText(_translate("configurator", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    configurator = QtWidgets.QMainWindow()
    ui = Ui_configurator()
    ui.setupUi(configurator)
    configurator.show()
    sys.exit(app.exec_())

