# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon May  6 23:39:15 2013
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
        MainWindow.resize(831, 312)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.horizontalLayout.addWidget(self.startButton)
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
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.operationTable = QtGui.QTableWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.operationTable.sizePolicy().hasHeightForWidth())
        self.operationTable.setSizePolicy(sizePolicy)
        self.operationTable.setMinimumSize(QtCore.QSize(0, 91))
        self.operationTable.setObjectName(_fromUtf8("operationTable"))
        self.operationTable.setColumnCount(7)
        self.operationTable.setRowCount(4)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(0, 5, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(1, 4, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(1, 5, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(2, 3, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(2, 4, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(2, 5, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(3, 2, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(3, 3, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(3, 4, item)
        item = QtGui.QTableWidgetItem()
        self.operationTable.setItem(3, 5, item)
        self.verticalLayout.addWidget(self.operationTable)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.speedEdit = QtGui.QLineEdit(self.centralwidget)
        self.speedEdit.setObjectName(_fromUtf8("speedEdit"))
        self.horizontalLayout_3.addWidget(self.speedEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 19))
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

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("MainWindow", "start/stop", None, QtGui.QApplication.UnicodeUTF8))
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
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Blink sensitivity", None, QtGui.QApplication.UnicodeUTF8))
        self.eyeBlinkSensitivity.setText(QtGui.QApplication.translate("MainWindow", "0.45", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Low blink freq (Hz)", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerEyeBlinkFrequency.setText(QtGui.QApplication.translate("MainWindow", "5.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "High blink freq (Hz)", None, QtGui.QApplication.UnicodeUTF8))
        self.higherEyeBlinkFrequency.setText(QtGui.QApplication.translate("MainWindow", "20.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Blink once to start</span> a mouse operation. <span style=\" font-weight:600;\">Blink again to stop</span> ongoing operation.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.verticalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Mouse Move", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.verticalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Mouse Speed", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.verticalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("MainWindow", "Mouse Clicks", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.verticalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("MainWindow", "Mouse Drag", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Select", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Select", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("MainWindow", "Select", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("MainWindow", "Select ", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.horizontalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("MainWindow", "Goto", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.horizontalHeaderItem(5)
        item.setText(QtGui.QApplication.translate("MainWindow", "Reverse Goto", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.horizontalHeaderItem(6)
        item.setText(QtGui.QApplication.translate("MainWindow", "NOP", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.operationTable.isSortingEnabled()
        self.operationTable.setSortingEnabled(False)
        item = self.operationTable.item(0, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Left", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(0, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Right", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(0, 2)
        item.setText(QtGui.QApplication.translate("MainWindow", "Up", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(0, 3)
        item.setText(QtGui.QApplication.translate("MainWindow", "Down", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(0, 4)
        item.setText(QtGui.QApplication.translate("MainWindow", "Speed", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(0, 5)
        item.setText(QtGui.QApplication.translate("MainWindow", "Drag", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(1, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Faster", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(1, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Slower", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(1, 4)
        item.setText(QtGui.QApplication.translate("MainWindow", "Clicks", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(1, 5)
        item.setText(QtGui.QApplication.translate("MainWindow", "Move", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(2, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Click", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(2, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Double click", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(2, 2)
        item.setText(QtGui.QApplication.translate("MainWindow", "Right click", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(2, 3)
        item.setText(QtGui.QApplication.translate("MainWindow", "Right dbl click", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(2, 4)
        item.setText(QtGui.QApplication.translate("MainWindow", "Drag", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(2, 5)
        item.setText(QtGui.QApplication.translate("MainWindow", "Speed", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(3, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Click + hold", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(3, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Release click", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(3, 2)
        item.setText(QtGui.QApplication.translate("MainWindow", "Right click + hold", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(3, 3)
        item.setText(QtGui.QApplication.translate("MainWindow", "Release right click", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(3, 4)
        item.setText(QtGui.QApplication.translate("MainWindow", "Movement", None, QtGui.QApplication.UnicodeUTF8))
        item = self.operationTable.item(3, 5)
        item.setText(QtGui.QApplication.translate("MainWindow", "Clicks", None, QtGui.QApplication.UnicodeUTF8))
        self.operationTable.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Speed (pixels/second)", None, QtGui.QApplication.UnicodeUTF8))
        self.speedEdit.setText(QtGui.QApplication.translate("MainWindow", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

