# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PersonRecords.ui'
#
# Created: Sat Nov 19 19:08:54 2016
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

class Ui_PersonRecords(object):
    def setupUi(self, PersonRecords):
        PersonRecords.setObjectName(_fromUtf8("PersonRecords"))
        PersonRecords.resize(571, 455)
        self.logo = QtGui.QLabel(PersonRecords)
        self.logo.setGeometry(QtCore.QRect(0, 0, 411, 81))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8("icons/logo.png")))
        self.logo.setObjectName(_fromUtf8("logo"))
        self.helpButton = QtGui.QPushButton(PersonRecords)
        self.helpButton.setGeometry(QtCore.QRect(470, 0, 98, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpButton.setIcon(icon)
        self.helpButton.setIconSize(QtCore.QSize(25, 25))
        self.helpButton.setCheckable(False)
        self.helpButton.setChecked(False)
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.chooseLabel = QtGui.QLabel(PersonRecords)
        self.chooseLabel.setGeometry(QtCore.QRect(90, 130, 111, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.chooseLabel.setFont(font)
        self.chooseLabel.setObjectName(_fromUtf8("chooseLabel"))
        self.recordsList = QtGui.QListWidget(PersonRecords)
        self.recordsList.setGeometry(QtCore.QRect(90, 160, 321, 191))
        self.recordsList.setObjectName(_fromUtf8("recordsList"))
        item = QtGui.QListWidgetItem()
        self.recordsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.recordsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.recordsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.recordsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.recordsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.recordsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.recordsList.addItem(item)
        self.deleteRecordButton = QtGui.QPushButton(PersonRecords)
        self.deleteRecordButton.setEnabled(True)
        self.deleteRecordButton.setGeometry(QtCore.QRect(90, 360, 151, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Delete_Icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteRecordButton.setIcon(icon1)
        self.deleteRecordButton.setIconSize(QtCore.QSize(24, 24))
        self.deleteRecordButton.setObjectName(_fromUtf8("deleteRecordButton"))
        self.addNewRecordButton = QtGui.QPushButton(PersonRecords)
        self.addNewRecordButton.setGeometry(QtCore.QRect(260, 360, 151, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addNewRecordButton.setIcon(icon2)
        self.addNewRecordButton.setIconSize(QtCore.QSize(20, 20))
        self.addNewRecordButton.setObjectName(_fromUtf8("addNewRecordButton"))
        self.backButton = QtGui.QPushButton(PersonRecords)
        self.backButton.setGeometry(QtCore.QRect(470, 420, 98, 27))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon3)
        self.backButton.setIconSize(QtCore.QSize(23, 22))
        self.backButton.setCheckable(False)
        self.backButton.setChecked(False)
        self.backButton.setObjectName(_fromUtf8("backButton"))

        self.retranslateUi(PersonRecords)
        QtCore.QMetaObject.connectSlotsByName(PersonRecords)

    def retranslateUi(self, PersonRecords):
        PersonRecords.setWindowTitle(_translate("PersonRecords", "PersonRecords", None))
        self.helpButton.setText(_translate("PersonRecords", "Help", None))
        self.chooseLabel.setText(_translate("PersonRecords", "choose record:", None))
        __sortingEnabled = self.recordsList.isSortingEnabled()
        self.recordsList.setSortingEnabled(False)
        item = self.recordsList.item(0)
        item.setText(_translate("PersonRecords", "record001 15/5/16", None))
        item = self.recordsList.item(1)
        item.setText(_translate("PersonRecords", "record002 15/5/16", None))
        item = self.recordsList.item(2)
        item.setText(_translate("PersonRecords", "record003 15/5/16", None))
        item = self.recordsList.item(3)
        item.setText(_translate("PersonRecords", "record004 15/5/16", None))
        item = self.recordsList.item(4)
        item.setText(_translate("PersonRecords", "record005 17/5/16", None))
        item = self.recordsList.item(5)
        item.setText(_translate("PersonRecords", "record006 18/5/16", None))
        item = self.recordsList.item(6)
        item.setText(_translate("PersonRecords", "record007 20/5/16", None))
        self.recordsList.setSortingEnabled(__sortingEnabled)
        self.deleteRecordButton.setText(_translate("PersonRecords", "Delete record", None))
        self.addNewRecordButton.setText(_translate("PersonRecords", "Add new record", None))
        self.backButton.setText(_translate("PersonRecords", "Back", None))

import 1_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PersonRecords = QtGui.QDialog()
    ui = Ui_PersonRecords()
    ui.setupUi(PersonRecords)
    PersonRecords.show()
    sys.exit(app.exec_())

