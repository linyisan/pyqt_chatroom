# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emojiboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
import sys

from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Signal, Qt
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QApplication

sys.path.append(os.path.join(os.getcwd(), '..'))

from tools.tools import getEmoji


class Ui_emojiBoard(QWidget):
    signal_on_emojiTableWidgetItem_click = Signal(str)
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.refresh_emojiTableWidget()
        self.bindSlots()

    def setupUi(self):
        self.setObjectName("emojiWidget")
        self.resize(164, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(140, 140))
        self.setMaximumSize(QtCore.QSize(9999, 9999))
        self.emojiTableWidget = QtWidgets.QTableWidget(self)
        self.emojiTableWidget.setGeometry(QtCore.QRect(0, 0, 151, 250))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emojiTableWidget.sizePolicy().hasHeightForWidth())
        self.emojiTableWidget.setSizePolicy(sizePolicy)
        self.emojiTableWidget.setMinimumSize(QtCore.QSize(140, 140))
        self.emojiTableWidget.setMaximumSize(QtCore.QSize(99999, 99999))
        self.emojiTableWidget.setStyleSheet("font-size:18pt;")
        self.emojiTableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.emojiTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.emojiTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.emojiTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.emojiTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.emojiTableWidget.setRowCount(5)
        self.emojiTableWidget.setColumnCount(4)
        self.emojiTableWidget.setObjectName("emojiTableWidget")
        self.emojiTableWidget.horizontalHeader().setVisible(False)
        self.emojiTableWidget.horizontalHeader().setDefaultSectionSize(34)
        self.emojiTableWidget.horizontalHeader().setHighlightSections(True)
        self.emojiTableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.emojiTableWidget.horizontalHeader().setStretchLastSection(False)
        self.emojiTableWidget.verticalHeader().setVisible(False)
        self.emojiTableWidget.verticalHeader().setDefaultSectionSize(34)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, emojiWidget):
        _translate = QtCore.QCoreApplication.translate
        emojiWidget.setWindowTitle(_translate("emojiWidget", "选择表情"))

    def bindSlots(self):
        self.emojiTableWidget.itemClicked.connect(self.on_emojiTableWidgetItem_click)

    def refresh_emojiTableWidget(self):
        '''
        填充emoji表格并设置窗口大小
        :return:
        '''
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup) # 设置窗口样式为无标题栏和弹出式顶层
        etw = self.emojiTableWidget # 表格面板
        etw.setRowCount(5) # 表格列
        etw.setColumnCount(0) # 表格行

        emojiList = getEmoji() # 获取表情符号列表
        rows = etw.rowCount()
        index = 0 # 表情符号列表下标
        while(index < len(emojiList)):
            colPosition = etw.columnCount() # 列位置
            etw.insertColumn(colPosition) # 插入新列
            # 纵向插入
            for rowPosition in range(0, rows):
                if(index < len(emojiList)):
                    # 把表情符号插入表格面板中
                    etw.setItem(rowPosition, colPosition, QTableWidgetItem(emojiList[index]))
                    index += 1

        # 表格，窗体根据内容自适应大小
        etw.setFixedSize(etw.horizontalHeader().length() + etw.verticalHeader().width(), etw.height())
        self.setFixedSize(etw.width(),self.height())

    def on_emojiTableWidgetItem_click(self):
        selectedItems = self.emojiTableWidget.selectedItems()
        self.emojiTableWidget.clearSelection()
        self.close()
        strEmoji = ''
        for selectedItem in selectedItems:
            strEmoji += selectedItem.text()
        self.signal_on_emojiTableWidgetItem_click.emit(strEmoji)

if __name__ == '__main__':
    app = QApplication([])
    ui = Ui_emojiBoard()
    ui.show()
    app.exec_()