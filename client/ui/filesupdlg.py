# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filesupdlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog


class Ui_FileUpDlg(QDialog):
    signal_refresh_sendFileLineEdit = pyqtSignal(str, int)
    signal_refresh_sendProgressBar = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.bindSlot()

    def setupUi(self):
        self.setObjectName("FileUpDlg")
        self.resize(440, 210)
        self.openFilePushButton = QtWidgets.QPushButton(self)
        self.openFilePushButton.setGeometry(QtCore.QRect(300, 60, 31, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.openFilePushButton.setFont(font)
        self.openFilePushButton.setObjectName("openFilePushButton")
        self.sendFilePushButton = QtWidgets.QPushButton(self)
        self.sendFilePushButton.setGeometry(QtCore.QRect(340, 60, 75, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sendFilePushButton.setFont(font)
        self.sendFilePushButton.setObjectName("sendFilePushButton")
        self.sendProgressBar = QtWidgets.QProgressBar(self)
        self.sendProgressBar.setGeometry(QtCore.QRect(100, 160, 241, 23))
        self.sendProgressBar.setProperty("value", 0)
        self.sendProgressBar.setObjectName("sendProgressBar")
        self.srvClosePushButton = QtWidgets.QPushButton(self)
        self.srvClosePushButton.setGeometry(QtCore.QRect(340, 150, 75, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.srvClosePushButton.setFont(font)
        self.srvClosePushButton.setObjectName("srvClosePushButton")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(170, 15, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.sfileNameLineEdit = QtWidgets.QLineEdit(self)
        self.sfileNameLineEdit.setEnabled(False)
        self.sfileNameLineEdit.setGeometry(QtCore.QRect(100, 60, 201, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.sfileNameLineEdit.setFont(font)
        self.sfileNameLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.sfileNameLineEdit.setReadOnly(True)
        self.sfileNameLineEdit.setObjectName("sfileNameLineEdit")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 51, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.sfileSizeLineEdit = QtWidgets.QLineEdit(self)
        self.sfileSizeLineEdit.setEnabled(False)
        self.sfileSizeLineEdit.setGeometry(QtCore.QRect(100, 110, 211, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.sfileSizeLineEdit.setFont(font)
        self.sfileSizeLineEdit.setText("")
        self.sfileSizeLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.sfileSizeLineEdit.setReadOnly(True)
        self.sfileSizeLineEdit.setObjectName("sfileSizeLineEdit")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(30, 160, 71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, FileUpDlg):
        _translate = QtCore.QCoreApplication.translate
        FileUpDlg.setWindowTitle(_translate("FileUpDlg", "发 送 文 件"))
        self.openFilePushButton.setText(_translate("FileUpDlg", "..."))
        self.sendFilePushButton.setText(_translate("FileUpDlg", "发  送"))
        self.srvClosePushButton.setText(_translate("FileUpDlg", "停  止"))
        self.label.setText(_translate("FileUpDlg", "文 件 发 送"))
        self.label_2.setText(_translate("FileUpDlg", "发 送 文 件"))
        self.label_3.setText(_translate("FileUpDlg", "大   小："))
        self.label_5.setText(_translate("FileUpDlg", "进         度"))

    def bindSlot(self):
        self.signal_refresh_sendFileLineEdit.connect(self.refresh_sendfileLineEdit)
        self.signal_refresh_sendProgressBar.connect(self.refresh_sendProgressBar)

    @pyqtSlot(str, int)
    def refresh_sendfileLineEdit(self, filePath, fileSizeTotal):
        self.sfileNameLineEdit.setText(filePath)
        self.sfileSizeLineEdit.setText(str(round(fileSizeTotal/1024, 2)) + 'KB')

    @pyqtSlot(int)
    def refresh_sendProgressBar(self, curPercent):
        # QApplication.processEvents()
        self.sendProgressBar.setValue(curPercent)

if __name__ == '__main__':
    app = QApplication([])
    ui = Ui_FileUpDlg()
    ui.setupUi()
    # ui.openFilePushButton.clicked.connect(ui.on_openFilePushButton_click)
    ui.show()
    app.exec_()