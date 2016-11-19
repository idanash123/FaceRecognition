# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editPersonInfo.ui'
#
# Created: Sat Nov 19 19:07:02 2016
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

class Ui_editPersonInfo(object):
    def setupUi(self, editPersonInfo):
        editPersonInfo.setObjectName(_fromUtf8("editPersonInfo"))
        editPersonInfo.resize(571, 455)
        self.logo = QtGui.QLabel(editPersonInfo)
        self.logo.setGeometry(QtCore.QRect(0, 0, 411, 81))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8("icons/logo.png")))
        self.logo.setObjectName(_fromUtf8("logo"))
        self.helpButton = QtGui.QPushButton(editPersonInfo)
        self.helpButton.setGeometry(QtCore.QRect(480, 0, 98, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpButton.setIcon(icon)
        self.helpButton.setIconSize(QtCore.QSize(25, 25))
        self.helpButton.setCheckable(False)
        self.helpButton.setChecked(False)
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.cancelButton = QtGui.QPushButton(editPersonInfo)
        self.cancelButton.setGeometry(QtCore.QRect(270, 360, 151, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setIconSize(QtCore.QSize(20, 20))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.gridLayoutWidget = QtGui.QWidget(editPersonInfo)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 130, 271, 181))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.BdayLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.BdayLabel.setObjectName(_fromUtf8("BdayLabel"))
        self.gridLayout.addWidget(self.BdayLabel, 2, 0, 1, 1)
        self.lastNameLine = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lastNameLine.setObjectName(_fromUtf8("lastNameLine"))
        self.gridLayout.addWidget(self.lastNameLine, 1, 1, 1, 1)
        self.emailLine = QtGui.QLineEdit(self.gridLayoutWidget)
        self.emailLine.setObjectName(_fromUtf8("emailLine"))
        self.gridLayout.addWidget(self.emailLine, 4, 1, 1, 1)
        self.lastNameLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.lastNameLabel.setObjectName(_fromUtf8("lastNameLabel"))
        self.gridLayout.addWidget(self.lastNameLabel, 1, 0, 1, 1)
        self.firstnameLine = QtGui.QLineEdit(self.gridLayoutWidget)
        self.firstnameLine.setObjectName(_fromUtf8("firstnameLine"))
        self.gridLayout.addWidget(self.firstnameLine, 0, 1, 1, 1)
        self.emailLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.gridLayout.addWidget(self.emailLabel, 4, 0, 1, 1)
        self.firstnameLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.firstnameLabel.setObjectName(_fromUtf8("firstnameLabel"))
        self.gridLayout.addWidget(self.firstnameLabel, 0, 0, 1, 1)
        self.addressLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.addressLabel.setObjectName(_fromUtf8("addressLabel"))
        self.gridLayout.addWidget(self.addressLabel, 3, 0, 1, 1)
        self.addressLine = QtGui.QLineEdit(self.gridLayoutWidget)
        self.addressLine.setObjectName(_fromUtf8("addressLine"))
        self.gridLayout.addWidget(self.addressLine, 3, 1, 1, 1)
        self.bDayDateEdit = QtGui.QDateEdit(self.gridLayoutWidget)
        self.bDayDateEdit.setObjectName(_fromUtf8("bDayDateEdit"))
        self.gridLayout.addWidget(self.bDayDateEdit, 2, 1, 1, 1)
        self.saveButton = QtGui.QPushButton(editPersonInfo)
        self.saveButton.setGeometry(QtCore.QRect(90, 360, 151, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon2)
        self.saveButton.setIconSize(QtCore.QSize(20, 20))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))

        self.retranslateUi(editPersonInfo)
        QtCore.QMetaObject.connectSlotsByName(editPersonInfo)

    def retranslateUi(self, editPersonInfo):
        editPersonInfo.setWindowTitle(_translate("editPersonInfo", "editPersonInfo", None))
        self.helpButton.setText(_translate("editPersonInfo", "Help", None))
        self.cancelButton.setText(_translate("editPersonInfo", "Cancel", None))
        self.BdayLabel.setText(_translate("editPersonInfo", "B-day", None))
        self.lastNameLabel.setText(_translate("editPersonInfo", "LastName", None))
        self.emailLabel.setText(_translate("editPersonInfo", "Email", None))
        self.firstnameLabel.setText(_translate("editPersonInfo", "Firstname", None))
        self.addressLabel.setText(_translate("editPersonInfo", "Address", None))
        self.saveButton.setText(_translate("editPersonInfo", "Save", None))

import 1_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    editPersonInfo = QtGui.QDialog()
    ui = Ui_editPersonInfo()
    ui.setupUi(editPersonInfo)
    editPersonInfo.show()
    sys.exit(app.exec_())

