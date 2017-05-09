# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/datas/saxenas/packages/mikrosVfx/vfxTkCore/dev/studio/install/app_store/tk-multi-starterapp/python/app/ui/browserui.ui'
#
# Created: Tue May  9 15:33:48 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Soumitra's Browser"))
        Dialog.resize(552, 423)
        self.listView = QtGui.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(10, 50, 256, 311))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 161, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(290, 30, 161, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.listView_2 = QtGui.QListView(Dialog)
        self.listView_2.setGeometry(QtCore.QRect(280, 50, 256, 311))
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(380, 370, 81, 22))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Shots", None))
        self.label_2.setText(_translate("Dialog", "Assets", None))
        self.pushButton.setText(_translate("Dialog", "Refresh", None))

