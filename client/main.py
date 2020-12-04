import os
import sys

from PySide2.QtCore import QPoint
from PySide2.QtWidgets import QMessageBox, QFileDialog, QApplication

from ui.emojiboard import Ui_emojiBoard

sys.path.append(os.path.join(os.getcwd(), '..'))
from tcp_logic import Logic_Client
from tools.tools import covertFileSizeUnit
from ui.filedowndlg import Ui_FileDownDlg
from ui.filesupdlg import Ui_FileUpDlg
from ui.logindlg import Ui_LoginDlg
from ui.mainboard import Ui_MainBoard

SERVER_ADDR = ('127.0.0.1', 8808)


class Client():
    def __init__(self):
        self.isConneted = False
        self.ui_loginDlg = Ui_LoginDlg()
        self.ui_mainBoard = Ui_MainBoard()
        self.ui_emojiBoard = Ui_emojiBoard()
        self.logic_client = Logic_Client()

        self.logic_client.setUiInstances(self.ui_mainBoard)
        self.bindSlots()

    def _start(self):
        self.ui_loginDlg.exec_()

    def on_loginPushButton_click(self):
        loginInfo = self.ui_loginDlg.getLoginInfo()
        if (None == loginInfo): return
        self.isConneted = self.logic_client.onLine(loginInfo[0], loginInfo[1])
        if (self.isConneted):
            self.ui_loginDlg.isExit = False
            self.ui_loginDlg.close()
            self.ui_mainBoard.show()
        else:
            QMessageBox.critical(self.ui_loginDlg, '警告', '服务器连接出错')

    def getNewFileUpDlg(self):
        ui = Ui_FileUpDlg()
        ui.signal_on_sendStopPushButton_click.connect(self.logic_client.fileHandler.interruptFileTransfer)
        return ui

    def getNewFileDownDlg(self):
        ui = Ui_FileDownDlg()
        ui.signal_on_recvStopPushButton_click.connect(self.logic_client.fileHandler.interruptFileTransfer)
        return ui

    def bindSlots(self):
        self.ui_mainBoard.chatSendPushButton.clicked.connect(self.on_chatSendPushButton_click)
        self.ui_mainBoard.filesUploadPushButton.clicked.connect(self.on_filesUploadPushButton_click)
        self.ui_mainBoard.filesFlushPushButton.clicked.connect(self.logic_client.fileHandler.getFilesList)
        self.ui_mainBoard.windowsClosePushButton.clicked.connect(self.on_windowsClosePushButton_click)
        self.ui_mainBoard.chatEmojiPushButton.clicked.connect(self.on_chatEmojiPushButton_click)
        self.ui_loginDlg.loginPushButton.clicked.connect(self.on_loginPushButton_click)

        self.ui_mainBoard.signal_on_filesDownloadPushButton_click.connect(self.on_filesDownloadPushButton_click)
        self.ui_emojiBoard.signal_on_emojiTableWidgetItem_click.connect(
            self.ui_mainBoard.chatMsgEditTextEdit.insertPlainText)

    def on_chatSendPushButton_click(self):
        msgSend = self.ui_mainBoard.chatMsgEditTextEdit.toPlainText()
        self.ui_mainBoard.chatMsgEditTextEdit.clear()
        self.logic_client.sendChatMsg(msgSend)

    def on_chatEmojiPushButton_click(self):
        x = self.ui_mainBoard.chatEmojiPushButton.mapToGlobal(QPoint(0, 0)).x()
        y = self.ui_mainBoard.chatEmojiPushButton.mapToGlobal(QPoint(0, 0)).y()
        self.ui_emojiBoard.move(x, y - self.ui_emojiBoard.height())
        self.ui_emojiBoard.show()

    def on_filesUploadPushButton_click(self):
        fileName, filter = QFileDialog.getOpenFileName(None, '选择你要上传的文件', '.', 'All file(*.*)')
        try:
            fileSizeTotal = os.stat(fileName).st_size
        except FileNotFoundError:
            QMessageBox.critical(self.ui_mainBoard, '警告', '文件不存在！')
            return
        ui_fileUpDlg = self.getNewFileUpDlg()
        ui_fileUpDlg.refresh_sendfileLineEdit(fileName, covertFileSizeUnit(fileSizeTotal))
        ui_fileUpDlg.show()
        self.logic_client.fileHandler.uploadFile(fileName, ui_fileUpDlg)

    def on_filesDownloadPushButton_click(self, fileName, fileSizeTotal):
        fileSizeTotal = int(fileSizeTotal)
        saveFileName, filter = QFileDialog.getSaveFileName(self.ui_mainBoard, u'保存文件',
                                                           os.path.join(os.getcwd(), 'download'), u'all files(*.*)')
        if not saveFileName:
            return
        # print('main_downFile:', fileSizeTotal, saveFileName)
        ui_fileDownDlg = self.getNewFileDownDlg()
        ui_fileDownDlg.show()
        ui_fileDownDlg.refresh_recvFileLineEdit(fileName, covertFileSizeUnit(fileSizeTotal))
        ui_fileDownDlg.refresh_recvProgressBar(0)
        self.logic_client.fileHandler.downloadFile(fileName, fileSizeTotal, saveFileName, ui_fileDownDlg)

    def on_windowsClosePushButton_click(self):
        self.logic_client.offLine()


if __name__ == '__main__':
    app = QApplication([])
    client = Client()
    client._start()
    sys.exit(app.exec_())
