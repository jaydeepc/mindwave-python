# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun May  5 22:03:08 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.horizontalLayout.addWidget(self.startButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.deviceComboBox = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deviceComboBox.sizePolicy().hasHeightForWidth())
        self.deviceComboBox.setSizePolicy(sizePolicy)
        self.deviceComboBox.setObjectName(_fromUtf8("deviceComboBox"))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.deviceComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.eyeBlinkSensitivity = QtGui.QLineEdit(self.centralwidget)
        self.eyeBlinkSensitivity.setObjectName(_fromUtf8("eyeBlinkSensitivity"))
        self.horizontalLayout_2.addWidget(self.eyeBlinkSensitivity)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lowerEyeBlinkFrequency = QtGui.QLineEdit(self.centralwidget)
        self.lowerEyeBlinkFrequency.setObjectName(_fromUtf8("lowerEyeBlinkFrequency"))
        self.horizontalLayout_2.addWidget(self.lowerEyeBlinkFrequency)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.higherEyeBlinkFrequency = QtGui.QLineEdit(self.centralwidget)
        self.higherEyeBlinkFrequency.setObjectName(_fromUtf8("higherEyeBlinkFrequency"))
        self.horizontalLayout_2.addWidget(self.higherEyeBlinkFrequency)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.rawView = PlotWidget(self.centralwidget)
        self.rawView.setObjectName(_fromUtf8("rawView"))
        self.verticalLayout.addWidget(self.rawView)
        self.fftView = PlotWidget(self.centralwidget)
        self.fftView.setObjectName(_fromUtf8("fftView"))
        self.verticalLayout.addWidget(self.fftView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.rawView, self.fftView)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("MainWindow", "Start/Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Device", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceComboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "/dev/rfcomm0", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceComboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "/dev/rfcomm1", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceComboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "/dev/rfcomm2", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceComboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "/dev/ttyUSB0", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceComboBox.setItemText(4, QtGui.QApplication.translate("MainWindow", "/dev/ttyUSB1", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceComboBox.setItemText(5, QtGui.QApplication.translate("MainWindow", "/dev/ttyUSB2", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceComboBox.setItemText(6, QtGui.QApplication.translate("MainWindow", "/dev/ttyS0", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceComboBox.setItemText(7, QtGui.QApplication.translate("MainWindow", "/dev/ttyS1", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceComboBox.setItemText(8, QtGui.QApplication.translate("MainWindow", "/dev/ttyS2", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceComboBox.setItemText(9, QtGui.QApplication.translate("MainWindow", "/dev/tty0", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceComboBox.setItemText(10, QtGui.QApplication.translate("MainWindow", "/dev/tty1", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceComboBox.setItemText(11, QtGui.QApplication.translate("MainWindow", "/dev/tty2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Eye blink sensitivity", None, QtGui.QApplication.UnicodeUTF8))
        self.eyeBlinkSensitivity.setText(QtGui.QApplication.translate("MainWindow", "0.45", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Lower Eye blink frequency  (Hz)", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerEyeBlinkFrequency.setText(QtGui.QApplication.translate("MainWindow", "5.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Higher Eye blink frequency (Hz)", None, QtGui.QApplication.UnicodeUTF8))
        self.higherEyeBlinkFrequency.setText(QtGui.QApplication.translate("MainWindow", "20.0", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

