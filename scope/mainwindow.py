# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri May  3 20:14:25 2013
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
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
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
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.rawView = PlotWidget(self.centralwidget)
        self.rawView.setObjectName(_fromUtf8("rawView"))
        self.verticalLayout.addWidget(self.rawView)
        self.deltaView = PlotWidget(self.centralwidget)
        self.deltaView.setObjectName(_fromUtf8("deltaView"))
        self.verticalLayout.addWidget(self.deltaView)
        self.thetaView = PlotWidget(self.centralwidget)
        self.thetaView.setObjectName(_fromUtf8("thetaView"))
        self.verticalLayout.addWidget(self.thetaView)
        self.alphaView = PlotWidget(self.centralwidget)
        self.alphaView.setObjectName(_fromUtf8("alphaView"))
        self.verticalLayout.addWidget(self.alphaView)
        self.betaView = PlotWidget(self.centralwidget)
        self.betaView.setObjectName(_fromUtf8("betaView"))
        self.verticalLayout.addWidget(self.betaView)
        self.gammaView = PlotWidget(self.centralwidget)
        self.gammaView.setObjectName(_fromUtf8("gammaView"))
        self.verticalLayout.addWidget(self.gammaView)
        self.restView = PlotWidget(self.centralwidget)
        self.restView.setObjectName(_fromUtf8("restView"))
        self.verticalLayout.addWidget(self.restView)
        self.verticalLayout_2.addLayout(self.verticalLayout)
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
        MainWindow.setTabOrder(self.startButton, self.rawView)
        MainWindow.setTabOrder(self.rawView, self.deltaView)
        MainWindow.setTabOrder(self.deltaView, self.thetaView)
        MainWindow.setTabOrder(self.thetaView, self.alphaView)
        MainWindow.setTabOrder(self.alphaView, self.betaView)
        MainWindow.setTabOrder(self.betaView, self.gammaView)
        MainWindow.setTabOrder(self.gammaView, self.restView)

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

