# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecognizeMode.ui'
#
# Created: Sat Nov 19 19:09:24 2016
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

class Ui_RecognitionMode(object):
    def setupUi(self, RecognitionMode):
        RecognitionMode.setObjectName(_fromUtf8("RecognitionMode"))
        RecognitionMode.resize(571, 455)
        self.logo = QtGui.QLabel(RecognitionMode)
        self.logo.setGeometry(QtCore.QRect(0, 0, 411, 81))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8("icons/logo.png")))
        self.logo.setObjectName(_fromUtf8("logo"))
        self.helpButton = QtGui.QPushButton(RecognitionMode)
        self.helpButton.setGeometry(QtCore.QRect(470, 0, 98, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpButton.setIcon(icon)
        self.helpButton.setIconSize(QtCore.QSize(25, 25))
        self.helpButton.setCheckable(False)
        self.helpButton.setChecked(False)
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.frame = QtGui.QFrame(RecognitionMode)
        self.frame.setGeometry(QtCore.QRect(60, 70, 471, 261))
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
        self.listWidget = QtGui.QListWidget(RecognitionMode)
        self.listWidget.setGeometry(QtCore.QRect(30, 360, 501, 61))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.backButton = QtGui.QPushButton(RecognitionMode)
        self.backButton.setGeometry(QtCore.QRect(460, 425, 98, 27))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon1)
        self.backButton.setIconSize(QtCore.QSize(23, 25))
        self.backButton.setCheckable(False)
        self.backButton.setChecked(False)
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.RecLabel = QtGui.QLabel(RecognitionMode)
        self.RecLabel.setGeometry(QtCore.QRect(70, 80, 461, 261))
        self.RecLabel.setText(_fromUtf8(""))
        self.RecLabel.setPixmap(QtGui.QPixmap(_fromUtf8("icons/detection.png")))
        self.RecLabel.setObjectName(_fromUtf8("RecLabel"))
        self.label = QtGui.QLabel(RecognitionMode)
        self.label.setGeometry(QtCore.QRect(30, 340, 151, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(RecognitionMode)
        QtCore.QMetaObject.connectSlotsByName(RecognitionMode)

    def retranslateUi(self, RecognitionMode):
        RecognitionMode.setWindowTitle(_translate("RecognitionMode", "RecognitionMode", None))
        self.helpButton.setText(_translate("RecognitionMode", "Help", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("RecognitionMode", "Shai Charsky, 26, shai.charsky@gmail.com", None))
        item = self.listWidget.item(1)
        item.setText(_translate("RecognitionMode", "Idan Ash, 27, idanash@gmail.com", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.backButton.setText(_translate("RecognitionMode", "Back", None))
        self.label.setText(_translate("RecognitionMode", "Recognized persons:", None))

import 1_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    RecognitionMode = QtGui.QDialog()
    ui = Ui_RecognitionMode()
    ui.setupUi(RecognitionMode)
    RecognitionMode.show()
    sys.exit(app.exec_())

