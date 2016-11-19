# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Sat Nov 19 19:07:46 2016
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(571, 455)
        self.recognitionButton = QtGui.QPushButton(MainWindow)
        self.recognitionButton.setGeometry(QtCore.QRect(60, 180, 191, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.recognitionButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/recognize.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recognitionButton.setIcon(icon)
        self.recognitionButton.setIconSize(QtCore.QSize(40, 40))
        self.recognitionButton.setObjectName(_fromUtf8("recognitionButton"))
        self.manageDBButton = QtGui.QPushButton(MainWindow)
        self.manageDBButton.setGeometry(QtCore.QRect(60, 240, 191, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.manageDBButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/manageDb.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.manageDBButton.setIcon(icon1)
        self.manageDBButton.setIconSize(QtCore.QSize(30, 26))
        self.manageDBButton.setObjectName(_fromUtf8("manageDBButton"))
        self.logo = QtGui.QLabel(MainWindow)
        self.logo.setGeometry(QtCore.QRect(0, 0, 411, 81))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8("icons/logo.png")))
        self.logo.setObjectName(_fromUtf8("logo"))
        self.helpButton = QtGui.QPushButton(MainWindow)
        self.helpButton.setGeometry(QtCore.QRect(470, 0, 98, 27))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpButton.setIcon(icon2)
        self.helpButton.setIconSize(QtCore.QSize(25, 25))
        self.helpButton.setCheckable(False)
        self.helpButton.setChecked(False)
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.trainDBButton_2 = QtGui.QPushButton(MainWindow)
        self.trainDBButton_2.setGeometry(QtCore.QRect(60, 300, 191, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.trainDBButton_2.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/dbbackup_icon-500x500_c.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trainDBButton_2.setIcon(icon3)
        self.trainDBButton_2.setIconSize(QtCore.QSize(40, 40))
        self.trainDBButton_2.setObjectName(_fromUtf8("trainDBButton_2"))
        self.label = QtGui.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(290, 110, 271, 321))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/xcPiSQM.png")))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.recognitionButton.setText(_translate("MainWindow", "Recognition Mode", None))
        self.manageDBButton.setText(_translate("MainWindow", "Manage DataBase", None))
        self.helpButton.setText(_translate("MainWindow", "Help", None))
        self.trainDBButton_2.setText(_translate("MainWindow", "Train Data Base", None))

import 1_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

