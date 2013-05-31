# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri May 31 23:41:19 2013
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
        Panel.resize(601, 118)
        self.gridLayout = QtGui.QGridLayout(Panel)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Panel)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.midiChannelEdit = QtGui.QLineEdit(Panel)
        self.midiChannelEdit.setObjectName(_fromUtf8("midiChannelEdit"))
        self.gridLayout.addWidget(self.midiChannelEdit, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(Panel)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.allowedVelsEdit = QtGui.QLineEdit(Panel)
        self.allowedVelsEdit.setObjectName(_fromUtf8("allowedVelsEdit"))
        self.gridLayout.addWidget(self.allowedVelsEdit, 0, 4, 1, 1)
        self.label_2 = QtGui.QLabel(Panel)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.centralNoteEdit = QtGui.QLineEdit(Panel)
        self.centralNoteEdit.setObjectName(_fromUtf8("centralNoteEdit"))
        self.gridLayout.addWidget(self.centralNoteEdit, 2, 2, 1, 1)
        self.label_4 = QtGui.QLabel(Panel)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.notesPerSecondEdit = QtGui.QLineEdit(Panel)
        self.notesPerSecondEdit.setObjectName(_fromUtf8("notesPerSecondEdit"))
        self.gridLayout.addWidget(self.notesPerSecondEdit, 3, 2, 1, 1)
        self.maxJitterEdit = QtGui.QLineEdit(Panel)
        self.maxJitterEdit.setObjectName(_fromUtf8("maxJitterEdit"))
        self.gridLayout.addWidget(self.maxJitterEdit, 3, 4, 1, 1)
        self.label_5 = QtGui.QLabel(Panel)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 3, 1, 1)
        self.label_6 = QtGui.QLabel(Panel)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 3, 1, 1)
        self.spreadEdit = QtGui.QLineEdit(Panel)
        self.spreadEdit.setObjectName(_fromUtf8("spreadEdit"))
        self.gridLayout.addWidget(self.spreadEdit, 2, 4, 1, 1)
        self.label.setBuddy(self.midiChannelEdit)
        self.label_3.setBuddy(self.allowedVelsEdit)
        self.label_2.setBuddy(self.centralNoteEdit)
        self.label_4.setBuddy(self.notesPerSecondEdit)
        self.label_5.setBuddy(self.maxJitterEdit)
        self.label_6.setBuddy(self.spreadEdit)

        self.retranslateUi(Panel)
        QtCore.QMetaObject.connectSlotsByName(Panel)
        Panel.setTabOrder(self.midiChannelEdit, self.allowedVelsEdit)
        Panel.setTabOrder(self.allowedVelsEdit, self.centralNoteEdit)
        Panel.setTabOrder(self.centralNoteEdit, self.spreadEdit)
        Panel.setTabOrder(self.spreadEdit, self.notesPerSecondEdit)
        Panel.setTabOrder(self.notesPerSecondEdit, self.maxJitterEdit)

    def retranslateUi(self, Panel):
        Panel.setWindowTitle(_translate("Panel", "Form", None))
        self.label.setText(_translate("Panel", "Midi channels", None))
        self.midiChannelEdit.setText(_translate("Panel", "0,2,3", None))
        self.label_3.setText(_translate("Panel", "Allowed vels", None))
        self.allowedVelsEdit.setText(_translate("Panel", "80:120:10", None))
        self.label_2.setText(_translate("Panel", "Central note", None))
        self.centralNoteEdit.setText(_translate("Panel", "C4", None))
        self.label_4.setText(_translate("Panel", "Notes/second", None))
        self.notesPerSecondEdit.setText(_translate("Panel", "10", None))
        self.maxJitterEdit.setText(_translate("Panel", "0.5", None))
        self.label_5.setText(_translate("Panel", "Max jitter", None))
        self.label_6.setText(_translate("Panel", "Spread", None))
        self.spreadEdit.setText(_translate("Panel", "5", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Panel = QtGui.QWidget()
    ui = Ui_Panel()
    ui.setupUi(Panel)
    Panel.show()
    sys.exit(app.exec_())

