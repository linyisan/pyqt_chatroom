# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import functools

from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtCore import Qt, Signal, QSize
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHeaderView, QTableWidget, QListWidgetItem, \
    QAbstractItemView, QPushButton

from tools.tools import covertFileSizeUnit


class Ui_MainBoard(QWidget):
    # 更新UI添加新控件时，崩溃，使用信号则不会
    signal_refresh_chatMsgShowListWidget = Signal(str, str, int, str, str)
    signal_refresh_filesShowTableWidget = Signal(dict)
    signal_on_filesDownloadPushButton_click = Signal(str, str)

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.bindSlots()

    def setupUi(self):
        self.setObjectName("MainBoard")
        self.resize(836, 774)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/ico/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("* {\n"
                           "font: 12pt \"Consolas\" ;\n"
                           "}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.chatTab = QtWidgets.QWidget()
        self.chatTab.setStyleSheet("background-color: rgb(228, 225, 224);")
        self.chatTab.setObjectName("chatTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.chatTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.chatMsgShowListWidget = QtWidgets.QListWidget(self.chatTab)
        self.chatMsgShowListWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.chatMsgShowListWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.chatMsgShowListWidget.setObjectName("chatMsgShowListWidget")
        self.horizontalLayout_3.addWidget(self.chatMsgShowListWidget)
        self.chatUserOnLineTableWidget = QtWidgets.QTableWidget(self.chatTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatUserOnLineTableWidget.sizePolicy().hasHeightForWidth())
        self.chatUserOnLineTableWidget.setSizePolicy(sizePolicy)
        self.chatUserOnLineTableWidget.setMaximumSize(QtCore.QSize(120, 16777215))
        self.chatUserOnLineTableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.chatUserOnLineTableWidget.setObjectName("chatUserOnLineTableWidget")
        self.chatUserOnLineTableWidget.setColumnCount(1)
        self.chatUserOnLineTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.chatUserOnLineTableWidget.setHorizontalHeaderItem(0, item)
        self.chatUserOnLineTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.chatUserOnLineTableWidget.horizontalHeader().setStretchLastSection(True)
        self.chatUserOnLineTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.chatUserOnLineTableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_3.addWidget(self.chatUserOnLineTableWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.chatTab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.groupBox_3 = QtWidgets.QGroupBox(self.chatTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chatFileUploadPushButton = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatFileUploadPushButton.sizePolicy().hasHeightForWidth())
        self.chatFileUploadPushButton.setSizePolicy(sizePolicy)
        self.chatFileUploadPushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/ico/fileupload_ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chatFileUploadPushButton.setIcon(icon1)
        self.chatFileUploadPushButton.setIconSize(QtCore.QSize(16, 16))
        self.chatFileUploadPushButton.setObjectName("chatFileUploadPushButton")
        self.horizontalLayout.addWidget(self.chatFileUploadPushButton)
        self.chatEmojiPushButton = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatEmojiPushButton.sizePolicy().hasHeightForWidth())
        self.chatEmojiPushButton.setSizePolicy(sizePolicy)
        self.chatEmojiPushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/ico/emoji_ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chatEmojiPushButton.setIcon(icon2)
        self.chatEmojiPushButton.setIconSize(QtCore.QSize(16, 16))
        self.chatEmojiPushButton.setObjectName("chatEmojiPushButton")
        self.horizontalLayout.addWidget(self.chatEmojiPushButton)
        self.windowsClosePushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.windowsClosePushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.windowsClosePushButton.setStyleSheet("color:red;\n"
                                                  "visibility: hidden;")
        self.windowsClosePushButton.setObjectName("windowsClosePushButton")
        self.windowsClosePushButton.setVisible(False)
        self.horizontalLayout.addWidget(self.windowsClosePushButton)
        spacerItem = QtWidgets.QSpacerItem(699, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.chatMyNameLabel = QtWidgets.QLabel(self.groupBox_3)
        self.chatMyNameLabel.setText("")
        self.chatMyNameLabel.setObjectName("chatMyNameLabel")
        self.horizontalLayout.addWidget(self.chatMyNameLabel)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.chatMsgEditTextEdit = QtWidgets.QTextEdit(self.chatTab)
        self.chatMsgEditTextEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.chatMsgEditTextEdit.sizePolicy().hasHeightForWidth())
        self.chatMsgEditTextEdit.setSizePolicy(sizePolicy)
        self.chatMsgEditTextEdit.setObjectName("chatMsgEditTextEdit")
        self.verticalLayout.addWidget(self.chatMsgEditTextEdit)
        self.line_3 = QtWidgets.QFrame(self.chatTab)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.chatSendPushButton = QtWidgets.QPushButton(self.chatTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatSendPushButton.sizePolicy().hasHeightForWidth())
        self.chatSendPushButton.setSizePolicy(sizePolicy)
        self.chatSendPushButton.setStyleSheet("background-color: rgb(102, 58, 183);\n"
                                              "color:rgb(255, 255, 255);\n"
                                              "\n"
                                              "\n"
                                              "/* border:5px, solid, rgb(0, 0, 0);*/\n"
                                              "")
        self.chatSendPushButton.setObjectName("chatSendPushButton")
        self.verticalLayout.addWidget(self.chatSendPushButton, 0, QtCore.Qt.AlignRight)
        self.line_2 = QtWidgets.QFrame(self.chatTab)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.tabWidget.addTab(self.chatTab, "")
        self.fileTab = QtWidgets.QWidget()
        self.fileTab.setStyleSheet("")
        self.fileTab.setObjectName("fileTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fileTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filesNumLabel = QtWidgets.QLabel(self.fileTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filesNumLabel.sizePolicy().hasHeightForWidth())
        self.filesNumLabel.setSizePolicy(sizePolicy)
        self.filesNumLabel.setObjectName("filesNumLabel")
        self.horizontalLayout_2.addWidget(self.filesNumLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.filesUploadPushButton = QtWidgets.QPushButton(self.fileTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filesUploadPushButton.sizePolicy().hasHeightForWidth())
        self.filesUploadPushButton.setSizePolicy(sizePolicy)
        self.filesUploadPushButton.setStyleSheet("background-color:rgb(18, 183, 245);\n"
                                                 "color:rgb(255, 255, 255)")
        self.filesUploadPushButton.setObjectName("filesUploadPushButton")
        self.horizontalLayout_2.addWidget(self.filesUploadPushButton)
        self.filesFlushPushButton = QtWidgets.QPushButton(self.fileTab)
        self.filesFlushPushButton.setObjectName("filesFlushPushButton")
        self.horizontalLayout_2.addWidget(self.filesFlushPushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.filesShowTableWidget = QtWidgets.QTableWidget(self.fileTab)
        self.filesShowTableWidget.setEnabled(True)
        self.filesShowTableWidget.setMinimumSize(QtCore.QSize(600, 500))
        self.filesShowTableWidget.setStyleSheet("")
        self.filesShowTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.filesShowTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.filesShowTableWidget.setObjectName("filesShowTableWidget")
        self.filesShowTableWidget.setColumnCount(4)
        self.filesShowTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.filesShowTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.filesShowTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.filesShowTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.filesShowTableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_3.addWidget(self.filesShowTableWidget)
        self.tabWidget.addTab(self.fileTab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)

        self.retranslateUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.chatFileUploadPushButton.clicked.connect(self.filesUploadPushButton.click)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainBoard):
        _translate = QtCore.QCoreApplication.translate
        MainBoard.setWindowTitle(_translate("MainBoard", "月聊天室"))
        item = self.chatUserOnLineTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainBoard", "在线用户"))
        self.chatFileUploadPushButton.setToolTip(_translate("MainBoard", "上传文件"))
        self.chatEmojiPushButton.setToolTip(_translate("MainBoard", "选择表情"))
        self.windowsClosePushButton.setText(_translate("MainBoard", "关闭窗口"))
        self.chatMsgEditTextEdit.setHtml(_translate("MainBoard",
                                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.chatMsgEditTextEdit.setPlaceholderText(_translate("MainBoard", "请输入"))
        self.chatSendPushButton.setText(_translate("MainBoard", "发送"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chatTab), _translate("MainBoard", "聊天"))
        self.filesNumLabel.setText(_translate("MainBoard", "共x个文件"))
        self.filesUploadPushButton.setToolTip(_translate("MainBoard", "上传文件"))
        self.filesUploadPushButton.setText(_translate("MainBoard", "十 上传"))
        self.filesFlushPushButton.setToolTip(_translate("MainBoard", "刷新文件列表"))
        self.filesFlushPushButton.setText(_translate("MainBoard", "刷新"))
        item = self.filesShowTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainBoard", "文件"))
        item = self.filesShowTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainBoard", "更新时间"))
        item = self.filesShowTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainBoard", "大小"))
        item = self.filesShowTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainBoard", "-"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fileTab), _translate("MainBoard", "文件"))

    def bindSlots(self):
        self.signal_refresh_chatMsgShowListWidget.connect(self.refresh_chatMsgShowListWidget)
        self.signal_refresh_filesShowTableWidget.connect(self.refresh_filesShowTableWidget)
        self.tabWidget.currentChanged.connect(self.on_changeTabWidget)

    def on_changeTabWidget(self):
        if (1 == self.tabWidget.currentIndex()):
            self.filesFlushPushButton.click()

    def newMsgItemChatFrame(self, userName, msg, isMe, msgBgColor, userHeader):
        '''
        创建消息气泡
        :param userName:用户名
        :param msg: 消息内容
        :param isMe: 是否本人发出的消息，调整控件顺序
        :param msgBgColor: 消息气泡颜色
        :param userHeader: 头像图片路径
        :return: 消息气泡控件
        '''
        chatMsgItemFrame = QtWidgets.QFrame(self)
        chatMsgItemFrame.setGeometry(QtCore.QRect(0, 0, 91, 61))  # ?? ddjust
        chatMsgItemFrame.setStyleSheet("font-size:18pt;")
        chatMsgItemFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        chatMsgItemFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        chatMsgItemFrame.setObjectName("chatMsgItemFrame")
        chatMsgItemFrame.horizontalLayout_4 = QtWidgets.QHBoxLayout(chatMsgItemFrame)
        chatMsgItemFrame.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem_other = QtWidgets.QSpacerItem(92, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        chatMsgItemFrame.vLayyout_middle = QtWidgets.QVBoxLayout()
        chatMsgItemFrame.vLayyout_middle.setObjectName("vLayyout_middle")
        chatMsgItemFrame.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        chatMsgItemFrame.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem_userName = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum)
        chatMsgItemFrame.chatMsgUserNameLabel = QtWidgets.QLabel(chatMsgItemFrame)
        chatMsgItemFrame.chatMsgUserNameLabel.setMinimumSize(QtCore.QSize(0, 16))
        chatMsgItemFrame.chatMsgUserNameLabel.setMaximumSize(QtCore.QSize(16777215, 16))
        chatMsgItemFrame.chatMsgUserNameLabel.setStyleSheet("font:12pt;")
        chatMsgItemFrame.chatMsgUserNameLabel.setText(userName)
        chatMsgItemFrame.chatMsgUserNameLabel.setObjectName("chatMsgUserNameLabel")
        chatMsgItemFrame.vLayyout_middle.addLayout(chatMsgItemFrame.horizontalLayout_3)
        chatMsgItemFrame.chatMsgContentLabel = QtWidgets.QLabel(chatMsgItemFrame)
        chatMsgItemFrame.chatMsgContentLabel.setStyleSheet("background-color:{0};\n"
                                                           "padding:5px;\n"
                                                           "font-size:13pt;\n"
                                                           "border-radius:7px;\n"
                                                           "\n"
                                                           "".format(msgBgColor))
        chatMsgItemFrame.chatMsgContentLabel.setObjectName("chatMsgContentLabel")
        chatMsgItemFrame.chatMsgContentLabel.setText(str(msg))
        chatMsgItemFrame.vLayyout_middle.addWidget(chatMsgItemFrame.chatMsgContentLabel)
        chatMsgItemFrame.vLayout_header = QtWidgets.QVBoxLayout()
        chatMsgItemFrame.vLayout_header.setObjectName("vLayout_header")
        chatMsgItemFrame.chatMsgHeaderLabel = QtWidgets.QLabel(chatMsgItemFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chatMsgItemFrame.chatMsgHeaderLabel.sizePolicy().hasHeightForWidth())
        chatMsgItemFrame.chatMsgHeaderLabel.setSizePolicy(sizePolicy)
        chatMsgItemFrame.chatMsgHeaderLabel.setMinimumSize(QtCore.QSize(32, 32))
        chatMsgItemFrame.chatMsgHeaderLabel.setMaximumSize(QtCore.QSize(32, 32))
        chatMsgItemFrame.chatMsgHeaderLabel.setStyleSheet("background-color:red")
        chatMsgItemFrame.chatMsgHeaderLabel.setText("")
        chatMsgItemFrame.chatMsgHeaderLabel.setPixmap(
            QtGui.QPixmap(userHeader))
        chatMsgItemFrame.chatMsgHeaderLabel.setScaledContents(True)
        chatMsgItemFrame.chatMsgHeaderLabel.setObjectName("chatMsgHeaderLabel")
        chatMsgItemFrame.vLayout_header.addWidget(chatMsgItemFrame.chatMsgHeaderLabel)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        chatMsgItemFrame.vLayout_header.addItem(spacerItem2)

        if 1 == isMe:
            # 偏右
            # 总体布局顺序
            chatMsgItemFrame.horizontalLayout_4.addItem(spacerItem_other)
            chatMsgItemFrame.horizontalLayout_4.addLayout(chatMsgItemFrame.vLayyout_middle)
            chatMsgItemFrame.horizontalLayout_4.addLayout(chatMsgItemFrame.vLayout_header)

            # 用户名布局顺序
            chatMsgItemFrame.horizontalLayout_3.addItem(spacerItem_userName)
            chatMsgItemFrame.horizontalLayout_3.addWidget(chatMsgItemFrame.chatMsgUserNameLabel)

        else:
            # 偏左
            # 总体布局顺序
            chatMsgItemFrame.horizontalLayout_4.addLayout(chatMsgItemFrame.vLayout_header)
            chatMsgItemFrame.horizontalLayout_4.addLayout(chatMsgItemFrame.vLayyout_middle)
            chatMsgItemFrame.horizontalLayout_4.addItem(spacerItem_other)

            # 用户名布局顺序
            chatMsgItemFrame.horizontalLayout_3.addWidget(chatMsgItemFrame.chatMsgUserNameLabel)
            chatMsgItemFrame.horizontalLayout_3.addItem(spacerItem_userName)

        # 根据内容自适应大小
        chatMsgItemFrame.chatMsgContentLabel.setWordWrap(True)
        chatMsgItemFrame.chatMsgContentLabel.adjustSize()
        chatMsgItemFrame.adjustSize()
        return chatMsgItemFrame

    def newMsgItemInformFrame(self, msg, msgBgColor):
        chatMsgItemFrame = QtWidgets.QFrame(self)
        chatMsgItemFrame.setGeometry(QtCore.QRect(0, 0, 91, 61))  # ?? ddjust
        chatMsgItemFrame.setStyleSheet("font-size:18pt;")
        chatMsgItemFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        chatMsgItemFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        chatMsgItemFrame.setObjectName("chatMsgItemFrame")
        horizontalLayout_4 = QtWidgets.QHBoxLayout(chatMsgItemFrame)
        horizontalLayout_4.setObjectName("horizontalLayout_4")

        chatMsgContentLabel = QtWidgets.QLabel()
        horizontalLayout_4.addWidget(chatMsgContentLabel)
        chatMsgContentLabel.setStyleSheet("background-color:{0};\n"
                                                           "padding:5px;\n"
                                                           "font-size:13pt;\n"
                                                           "border-radius:7px;\n"
                                                           "\n"
                                                           "".format(msgBgColor))
        chatMsgContentLabel.setObjectName("chatMsgContentLabel")
        chatMsgContentLabel.setText(str(msg))
        # chatMsgContentLabel.setWordWrap(True)
        chatMsgContentLabel.adjustSize()
        chatMsgContentLabel.setFixedSize(chatMsgContentLabel.width(), chatMsgContentLabel.height())
        return chatMsgItemFrame

    def refresh_chatMsgShowListWidget(self, userName, msg, isMe=1, msgBgColor='#9eea6a',
                                      userHeader='ui/ico/ico.png'):
        '''
        更新聊天展示区/生成消息气泡
        :param userName: 聊天消息发出者
        :param msg: 消息内容
        :param isMe: 消息气泡类型
        :param msgBgColor: 消息气泡背景色
        :param userHeader: 聊天消息气泡头像
        :return:
        '''
        lwit = QListWidgetItem()
        self.chatMsgShowListWidget.addItem(lwit)
        if 0 == isMe:
            mif = self.newMsgItemInformFrame(msg, msgBgColor)
        else:
            mif = self.newMsgItemChatFrame(userName, msg, isMe, msgBgColor, userHeader)
        lwit.setSizeHint(QSize(400, mif.height()))  # ??

        self.chatMsgShowListWidget.setItemWidget(lwit, mif)
        # self.chatMsgShowListWidget.adjustSize()
        # self.chatMsgShowListWidget.setFixedSize(self.chatMsgShowListWidget.h, self.chatMsgShowListWidget.height())

        # 滚动条到末尾
        self.chatMsgShowListWidget.setCurrentRow(self.chatMsgShowListWidget.count() - 1)

    @Slot(dict)
    def refresh_filesShowTableWidget(self, filesAndDirs):
        fv = self.filesShowTableWidget # 表格
        fv.setRowCount(0)  # 清空旧数据
        fv.setEditTriggers(QAbstractItemView.NoEditTriggers) # 禁止编辑
        self.filesNumLabel.setText('共' + str(filesAndDirs['filesNum']) + '个文件')
        for fileInfo in filesAndDirs['files']:
            # 获取文件属性
            fileName = fileInfo['fileName']
            modifyTime = fileInfo['modifyTime']
            fileSize = covertFileSizeUnit(fileInfo['fileSize'])
            # print('ui_refresh:',fileName, modifyTime, fileSize)

            rowPosition = fv.rowCount()
            fv.insertRow(rowPosition)

            # 动态生成按钮
            fileDownloadPushButton = QPushButton(text='下载')
            # fileDeletePushButton = QPushButton(text='删除')
            fileDownloadPushButton.clicked.connect(
                functools.partial(self.on_fileDownloadPushButton_click, fileName, fileInfo['fileSize']))
            # fileDeletePushButton.clicked.connect(functools.partial(self.on_btn_file_delete_clicked, rowPosition))

            # 插入列数据
            fv.setItem(rowPosition, 0, QTableWidgetItem(fileName))
            fv.setItem(rowPosition, 1, QTableWidgetItem(modifyTime))
            fv.setItem(rowPosition, 2, QTableWidgetItem(fileSize))
            fv.setCellWidget(rowPosition, 3, fileDownloadPushButton)
            # fv.setCellWidget(rowPosition, 4, fileDeletePushButton)

            # 设置列宽
            QTableWidget.horizontalHeader(fv).resizeSection(1, 100)
            QTableWidget.horizontalHeader(fv).resizeSection(3, 70)
            QTableWidget.horizontalHeader(fv).resizeSection(4, 70)

        fv.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch) # 第一列自动拉伸

    def refresh_chatUserOnLineTableWidget(self, userOnlineList):
        uv = self.chatUserOnLineTableWidget
        uv.setRowCount(0)
        uv.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for userName in userOnlineList:
            # print(userName, userOnlineList[userName])

            rowPosition = uv.rowCount()
            uv.insertRow(rowPosition)
            uv.setItem(rowPosition, 0, QTableWidgetItem(userName))

    @Slot(str, int)
    def on_fileDownloadPushButton_click(self, fileName, fileSize):
        self.signal_on_filesDownloadPushButton_click.emit(fileName, str(fileSize))

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        super().closeEvent(a0)
        self.windowsClosePushButton.click()


if __name__ == '__main__':
    app = QApplication([])
    ui = Ui_MainBoard()
    ui.show()
    app.exec_()
