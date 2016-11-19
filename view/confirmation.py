# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Confirmation.ui'
#
# Created: Sat Nov 19 19:05:40 2016
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

class Ui_Confirmation(object):
    def setupUi(self, Confirmation):
        Confirmation.setObjectName(_fromUtf8("Confirmation"))
        Confirmation.resize(510, 270)
        Confirmation.setAutoFillBackground(True)
        self.logo = QtGui.QLabel(Confirmation)
        self.logo.setGeometry(QtCore.QRect(0, 0, 411, 81))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8("icons/logo.png")))
        self.logo.setObjectName(_fromUtf8("logo"))
        self.helpButton = QtGui.QPushButton(Confirmation)
        self.helpButton.setGeometry(QtCore.QRect(410, 0, 98, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpButton.setIcon(icon)
        self.helpButton.setIconSize(QtCore.QSize(25, 25))
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.cancelButton = QtGui.QPushButton(Confirmation)
        self.cancelButton.setGeometry(QtCore.QRect(280, 220, 98, 27))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/return.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setIconSize(QtCore.QSize(23, 22))
        self.cancelButton.setCheckable(False)
        self.cancelButton.setChecked(False)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.yesButton = QtGui.QPushButton(Confirmation)
        self.yesButton.setGeometry(QtCore.QRect(140, 220, 98, 27))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Yes.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yesButton.setIcon(icon2)
        self.yesButton.setObjectName(_fromUtf8("yesButton"))
        self.alertLabel = QtGui.QLabel(Confirmation)
        self.alertLabel.setGeometry(QtCore.QRect(80, 100, 91, 101))
        self.alertLabel.setText(_fromUtf8(""))
        self.alertLabel.setPixmap(QtGui.QPixmap(_fromUtf8("icons/alert.png")))
        self.alertLabel.setObjectName(_fromUtf8("alertLabel"))
        self.label = QtGui.QLabel(Confirmation)
        self.label.setGeometry(QtCore.QRect(160, 130, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Confirmation)
        QtCore.QMetaObject.connectSlotsByName(Confirmation)

    def retranslateUi(self, Confirmation):
        Confirmation.setWindowTitle(_translate("Confirmation", "Confirmation", None))
        self.helpButton.setText(_translate("Confirmation", "Help", None))
        self.cancelButton.setText(_translate("Confirmation", "Cancel", None))
        self.yesButton.setText(_translate("Confirmation", "yes", None))
        self.label.setText(_translate("Confirmation", "Are you sure?", None))

import 1_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Confirmation = QtGui.QDialog()
    ui = Ui_Confirmation()
    ui.setupUi(Confirmation)
    Confirmation.show()
    sys.exit(app.exec_())

