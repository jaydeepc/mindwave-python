# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu May 30 22:36:34 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Panel(object):
    def setupUi(self, Panel):
        Panel.setObjectName(_fromUtf8("Panel"))
        Panel.resize(601, 64)
        self.gridLayout = QtGui.QGridLayout(Panel)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Panel)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.midiChannelEdit = QtGui.QLineEdit(Panel)
        self.midiChannelEdit.setObjectName(_fromUtf8("midiChannelEdit"))
        self.gridLayout.addWidget(self.midiChannelEdit, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Panel)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.allowedVelsEdit = QtGui.QLineEdit(Panel)
        self.allowedVelsEdit.setObjectName(_fromUtf8("allowedVelsEdit"))
        self.gridLayout.addWidget(self.allowedVelsEdit, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(Panel)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.allowedNotesEdit = QtGui.QLineEdit(Panel)
        self.allowedNotesEdit.setObjectName(_fromUtf8("allowedNotesEdit"))
        self.gridLayout.addWidget(self.allowedNotesEdit, 1, 1, 1, 1)
        self.label.setBuddy(self.midiChannelEdit)
        self.label_3.setBuddy(self.allowedVelsEdit)
        self.label_2.setBuddy(self.allowedNotesEdit)

        self.retranslateUi(Panel)
        QtCore.QMetaObject.connectSlotsByName(Panel)
        Panel.setTabOrder(self.midiChannelEdit, self.allowedVelsEdit)
        Panel.setTabOrder(self.allowedVelsEdit, self.allowedNotesEdit)

    def retranslateUi(self, Panel):
        Panel.setWindowTitle(_translate("Panel", "Form", None))
        self.label.setText(_translate("Panel", "Midi channels", None))
        self.midiChannelEdit.setText(_translate("Panel", "0,2,3", None))
        self.label_3.setText(_translate("Panel", "Allowed vels", None))
        self.allowedVelsEdit.setText(_translate("Panel", "80:120:10", None))
        self.label_2.setText(_translate("Panel", "Allowed notes", None))
        self.allowedNotesEdit.setText(_translate("Panel", "60:72:2, C4:C5:1", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Panel = QtGui.QWidget()
    ui = Ui_Panel()
    ui.setupUi(Panel)
    Panel.show()
    sys.exit(app.exec_())

