# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
import os
import sys
import threading

from sgtkLib import tkutil

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.
from sgtk.platform.qt import QtCore, QtGui
from .ui.browserui import Ui_Dialog

tank, sgw, project = tkutil.getTk(str(os.environ['PROD']), fast=True)

def show_dialog(app_instance):
    """
    Shows the main dialog window.
    """
    # in order to handle UIs seamlessly, each toolkit engine has methods for launching
    # different types of windows. By using these methods, your windows will be correctly
    # decorated and handled in a consistent fashion by the system. 
    
    # we pass the dialog class to this method and leave the actual construction
    # to be carried out by toolkit.
    app_instance.engine.show_dialog("Soumitra's Browser", app_instance, AppWindow)

class getShotsThread(QtCore.QThread):

    def __init__(self):
        super(getShotsThread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        print "Inside Shot Thread"
        shots = sgw.Shots(project=project)
        shot_names = [x.code for x in shots]
        self.emit(QtCore.SIGNAL('get_shots(QStringList)'), shot_names)

class getAssetsThread(QtCore.QThread):

    def __init__(self, shot):
        super(getAssetsThread, self).__init__()
        self.shot = shot

    def __del__(self):
        self.wait()

    def run(self):
        print "Inside Asset thread"
        shot = sgw.Shot(self.shot, project=project)
        asset_list = [x.code for x in shot.assets]
        self.emit(QtCore.SIGNAL('get_assets(QStringList)'), asset_list)
        print "After Signal emit"

class AssetListModel(QtGui.QStringListModel):

    def __init__(self, values, parent=None):
        super(AssetListModel, self).__init__()
        self.values = values

    def rowCount(self, parent):
        return len(self.values)

    def data(self, index, role):
        #print "Inside Data"

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            value = self.values[row]
            return value

    def setData(self, index, value, role = QtCore.Qt.EditRole):
        print "Setting data"

        if role == QtCore.Qt.EditRole:

            row = index.row()
            self.values[row] = value
            self.dataChanged.emit(index, index)
            return True

class ShotListModel(QtGui.QStringListModel):

    def __init__(self, values, parent=None):
        super(ShotListModel, self).__init__()
        self.values = values

    def rowCount(self, parent):
        return len(self.values)

    def data(self, index, role):
        #print "Inside Data"

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            value = self.values[row]
            return value

    def setData(self, index, value, role = QtCore.Qt.EditRole):
        print "Setting data"

        if role == QtCore.Qt.EditRole:

            row = index.row()
            self.values[row] = value
            self.dataChanged.emit(index, index)
            return True


class AppWindow(QtGui.QWidget, Ui_Dialog):

    def __init__(self):
        super(AppWindow, self).__init__()
        self.setupUi(self)
        self.hide_tk_title_bar = True

        self.asset_list = []
        self.shot_list = []

        self.shot_model = ShotListModel(self.shot_list)
        self.listView.setModel(self.shot_model)

        self.asset_model = AssetListModel(self.asset_list)
        self.listView_2.setModel(self.asset_model)

        self.get_shots_thread = getShotsThread()
        self.connect(self.get_shots_thread, QtCore.SIGNAL("get_shots(QStringList)"), self.get_shots)
        self.connect(self.get_shots_thread, QtCore.SIGNAL("finished()"), self.done)
        self.get_shots_thread.start()
        QtCore.QObject.connect(self.listView.selectionModel(), QtCore.SIGNAL('currentChanged(QModelIndex, QModelIndex)'), self.get_asset_list)
        QtCore.QObject.connect(self.listView_2.selectionModel(), QtCore.SIGNAL('currentChanged(QModelIndex, QModelIndex)'), self.get_asset_info)

    def get_shots(self, shot_list):
        print "Inside get shots"
        self.progressBar.setMaximum(len(shot_list))
        self.progressBar.setValue(0)
        self.shot_model.layoutAboutToBeChanged.emit()
        self.shot_list[:] = []
        for shot in shot_list:
            self.shot_list.append(shot)
        self.shot_model.layoutChanged.emit()

    def get_asset_list(self, current, previous):
        print "Inside get asset list"
        self.progressBar.setValue(0)
        shot_name = str(self.shot_list[current.row()])
        get_assets_thread = getAssetsThread(shot_name)
        self.connect(get_assets_thread, QtCore.SIGNAL("get_assets(QStringList)"), self.get_assets)
        self.connect(get_assets_thread, QtCore.SIGNAL("finished()"), self.done_assets)
        get_assets_thread.start()
        print "After thread start"

    def get_asset_info(self, current, previous):
        print "Inside get asset info"
        asset_name = str(self.asset_list[current.row()])
        asset = sgw.Asset(asset_name, project=project)
        self.asset_name.setText(asset_name)
        self.asset_type.setText(asset.sg_asset_type)
        self.created_by.setText(asset.created_by.firstname + ' ' + asset.created_by.lastname)

    def get_assets(self, asset_list):
        print "Inside get assets"
        self.progressBar.setMaximum(len(asset_list))
        self.asset_model.layoutAboutToBeChanged.emit()
        self.asset_list[:] = []
        for asset in asset_list:
            self.progressBar.setValue(self.progressBar.value()+1)
            self.asset_list.append(asset)
        self.asset_model.layoutChanged.emit()

    def done(self):
        print "Inside done"
        QtGui.QMessageBox.information(self, "Done", "Done fetching shots")
        self.progressBar.setValue(0)

    def done_assets(self):
        print "Inside done"
        self.progressBar.setValue(0)











