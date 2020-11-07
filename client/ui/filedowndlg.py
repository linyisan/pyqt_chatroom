# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filedowndlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication


class Ui_FileDownDlg(QDialog):
    signal_refresh_recvFileLineEdit = pyqtSignal(str, int)
    signal_refresh_recvProgressBar = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.bindSlot()


    def setupUi(self):
        self.setObjectName("FileDownDlg")
        self.resize(440, 210)
        self.recvProgressBar = QtWidgets.QProgressBar(self)
        self.recvProgressBar.setGeometry(QtCore.QRect(100, 160, 241, 23))
        self.recvProgressBar.setProperty("value", 0)
        self.recvProgressBar.setObjectName("recvProgressBar")
        self.cntClosePushButton = QtWidgets.QPushButton(self)
        self.cntClosePushButton.setGeometry(QtCore.QRect(340, 60, 75, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cntClosePushButton.setFont(font)
        self.cntClosePushButton.setObjectName("cntClosePushButton")
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
        self.rfileNameLineEdit = QtWidgets.QLineEdit(self)
        self.rfileNameLineEdit.setEnabled(False)
        self.rfileNameLineEdit.setGeometry(QtCore.QRect(100, 60, 201, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.rfileNameLineEdit.setFont(font)
        self.rfileNameLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.rfileNameLineEdit.setReadOnly(True)
        self.rfileNameLineEdit.setObjectName("rfileNameLineEdit")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 51, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(200, 110, 61, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.rfileSizeLineEdit = QtWidgets.QLineEdit(self)
        self.rfileSizeLineEdit.setEnabled(False)
        self.rfileSizeLineEdit.setGeometry(QtCore.QRect(120, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.rfileSizeLineEdit.setFont(font)
        self.rfileSizeLineEdit.setText("")
        self.rfileSizeLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.rfileSizeLineEdit.setReadOnly(True)
        self.rfileSizeLineEdit.setObjectName("rfileSizeLineEdit")
        self.recvSizeLineEdit = QtWidgets.QLineEdit(self)
        self.recvSizeLineEdit.setEnabled(False)
        self.recvSizeLineEdit.setGeometry(QtCore.QRect(260, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.recvSizeLineEdit.setFont(font)
        self.recvSizeLineEdit.setText("")
        self.recvSizeLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.recvSizeLineEdit.setReadOnly(True)
        self.recvSizeLineEdit.setObjectName("recvSizeLineEdit")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(30, 160, 71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.rateLabel = QtWidgets.QLabel(self)
        self.rateLabel.setGeometry(QtCore.QRect(340, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.rateLabel.setFont(font)
        self.rateLabel.setText("")
        self.rateLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.rateLabel.setObjectName("rateLabel")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, FileDownDlg):
        _translate = QtCore.QCoreApplication.translate
        FileDownDlg.setWindowTitle(_translate("FileDownDlg", "接 收 文 件"))
        self.cntClosePushButton.setText(_translate("FileDownDlg", "停  止"))
        self.label.setText(_translate("FileDownDlg", "文 件 接 收"))
        self.label_2.setText(_translate("FileDownDlg", "接 收 文 件"))
        self.label_3.setText(_translate("FileDownDlg", "大   小："))
        self.label_4.setText(_translate("FileDownDlg", "已 接 收："))
        self.label_5.setText(_translate("FileDownDlg", "进         度"))

    def bindSlot(self):
        self.signal_refresh_recvFileLineEdit.connect(self.refresh_recvFileLineEdit)
        self.signal_refresh_recvProgressBar.connect(self.refresh_recvProgressBar)

    @pyqtSlot(str, int)
    def refresh_recvFileLineEdit(self, filePath, fileSizeTotal):
        self.rfileNameLineEdit.setText(filePath)
        self.rfileSizeLineEdit.setText(str(round(fileSizeTotal/1024, 2)) + 'KB')

    @pyqtSlot(int)
    def refresh_recvProgressBar(self, curPercent):
        # QApplication.processEvents()
        self.recvProgressBar.setValue(curPercent)

if __name__ == '__main__':
    app = QApplication([])
    ui = Ui_FileDownDlg()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())