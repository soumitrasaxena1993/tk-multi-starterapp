# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/datas/saxenas/packages/mikrosVfx/vfxTkCore/dev/studio/install/app_store/tk-multi-starterapp/python/app/ui/browserui.ui'
#
# Created: Thu May 11 15:30:10 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from sgtk.platform.qt import QtCore, QtGui

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
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(552, 502)
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
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 470, 531, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 370, 81, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 400, 131, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 430, 121, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.asset_name = QtGui.QLineEdit(Dialog)
        self.asset_name.setGeometry(QtCore.QRect(180, 370, 351, 22))
        self.asset_name.setObjectName(_fromUtf8("asset_name"))
        self.asset_type = QtGui.QLineEdit(Dialog)
        self.asset_type.setGeometry(QtCore.QRect(180, 400, 351, 22))
        self.asset_type.setObjectName(_fromUtf8("asset_type"))
        self.created_by = QtGui.QLineEdit(Dialog)
        self.created_by.setGeometry(QtCore.QRect(180, 430, 351, 22))
        self.created_by.setObjectName(_fromUtf8("created_by"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Shots", None))
        self.label_2.setText(_translate("Dialog", "Assets", None))
        self.label_3.setText(_translate("Dialog", "Asset name", None))
        self.label_4.setText(_translate("Dialog", "Asset Type", None))
        self.label_5.setText(_translate("Dialog", "Created By", None))

