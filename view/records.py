# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'records.ui'
#
# Created: Sat Nov 19 19:10:26 2016
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_Record(object):
    def setupUi(self, Record):
        Record.setObjectName(_fromUtf8("Record"))
        Record.resize(571, 455)
        self.startRecButton = QtGui.QPushButton(Record)
        self.startRecButton.setGeometry(QtCore.QRect(127, 380, 141, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/startRec.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startRecButton.setIcon(icon)
        self.startRecButton.setIconSize(QtCore.QSize(28, 28))
        self.startRecButton.setObjectName(_fromUtf8("startRecButton"))
        self.stopRecButton = QtGui.QPushButton(Record)
        self.stopRecButton.setGeometry(QtCore.QRect(330, 380, 141, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/stopRec.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopRecButton.setIcon(icon1)
        self.stopRecButton.setIconSize(QtCore.QSize(25, 25))
        self.stopRecButton.setObjectName(_fromUtf8("stopRecButton"))
        self.helpButton = QtGui.QPushButton(Record)
        self.helpButton.setGeometry(QtCore.QRect(470, 0, 98, 27))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpButton.setIcon(icon2)
        self.helpButton.setIconSize(QtCore.QSize(25, 25))
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.frame = QtGui.QFrame(Record)
        self.frame.setGeometry(QtCore.QRect(60, 100, 471, 261))
        self.frame.setBaseSize(QtCore.QSize(0, 0))
        self.frame.setToolTip(_fromUtf8(""))
        self.frame.setStatusTip(_fromUtf8(""))
        self.frame.setWhatsThis(_fromUtf8(""))
        self.frame.setAccessibleName(_fromUtf8(""))
        self.frame.setAccessibleDescription(_fromUtf8(""))
        self.frame.setAutoFillBackground(False)
        self.frame.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(10)
        self.frame.setMidLineWidth(10)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.RecLabel = QtGui.QLabel(self.frame)
        self.RecLabel.setGeometry(QtCore.QRect(10, 0, 461, 261))
        self.RecLabel.setText(_fromUtf8(""))
        self.RecLabel.setPixmap(QtGui.QPixmap(_fromUtf8("icons/recording.png")))
        self.RecLabel.setObjectName(_fromUtf8("RecLabel"))
        self.logo = QtGui.QLabel(Record)
        self.logo.setGeometry(QtCore.QRect(0, 0, 411, 81))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8("icons/logo.png")))
        self.logo.setObjectName(_fromUtf8("logo"))
        self.backButton = QtGui.QPushButton(Record)
        self.backButton.setGeometry(QtCore.QRect(470, 420, 98, 27))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon3)
        self.backButton.setIconSize(QtCore.QSize(23, 22))
        self.backButton.setCheckable(False)
        self.backButton.setChecked(False)
        self.backButton.setObjectName(_fromUtf8("backButton"))

        self.retranslateUi(Record)
        QtCore.QMetaObject.connectSlotsByName(Record)

    def retranslateUi(self, Record):
        Record.setWindowTitle(_translate("Record", "Record", None))
        self.startRecButton.setText(_translate("Record", "Start record", None))
        self.stopRecButton.setText(_translate("Record", "Stop record", None))
        self.helpButton.setText(_translate("Record", "Help", None))
        self.backButton.setText(_translate("Record", "Back", None))

import 1_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Record = QtGui.QDialog()
    ui = Ui_Record()
    ui.setupUi(Record)
    Record.show()
    sys.exit(app.exec_())

