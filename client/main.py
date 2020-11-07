import os
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog

from udp_loginc import Logic_Client
from ui.filedowndlg import Ui_FileDownDlg
from ui.filesupdlg import Ui_FileUpDlg
from ui.logindlg import Ui_LoginDlg
from ui.mainboard import Ui_MainBoard


class Client():
    def __init__(self):
        self.ui_loginDlg = Ui_LoginDlg()
        self.ui_mainBoard = Ui_MainBoard()
        self.ui_fileDownDlg = Ui_FileDownDlg()
        self.ui_fileUpDlg = Ui_FileUpDlg()
        self.logic_client = Logic_Client()

        self.logic_client.setUiInstances(self.ui_mainBoard, self.ui_fileDownDlg, self.ui_fileUpDlg)
        self.bindSlots()




    def _start(self):
        self.ui_loginDlg.exec_()
        self.logic_client.start()

    def bindSlots(self):
        self.ui_loginDlg.loginPushButton.clicked.connect(self.on_loginPushButton_click)
        self.ui_mainBoard.chatSendPushButton.clicked.connect(self.on_chatSendPushButton_click)
        self.ui_mainBoard.filesUploadPushButton.clicked.connect(self.on_filesUploadPushButton_click)
        self.ui_mainBoard.filesFlushPushButton.clicked.connect(self.logic_client.getFilesList)
        # self.ui_mainBoard.tabWidget.currentChanged(2).connect()

        self.ui_fileUpDlg.openFilePushButton.clicked.connect(self.on_openFilePushButton_click)
        self.ui_fileUpDlg.sendFilePushButton.clicked.connect(self.on_sendFilePushButton_click)

    def on_chatSendPushButton_click(self):
        msgSend = self.ui_mainBoard.chatMsgEditTextEdit.toPlainText()
        self.ui_mainBoard.chatMsgEditTextEdit.clear()
        self.logic_client.sendChatMsg(msgSend)

    def on_filesUploadPushButton_click(self):
        self.ui_fileUpDlg.exec_()

    def on_sendFilePushButton_click(self):
        self.logic_client.uploadFile(self.ui_fileUpDlg.fileNameSend)
        # self.ui_fileUpDlg.openFilePushButton.setEnabled(False)

    def on_openFilePushButton_click(self):
        fileName, filter = QFileDialog.getOpenFileName(self.ui_mainBoard, '选择你要上传的文件', '.', 'All file(*.*)')
        print(fileName, filter)
        fileSizeTotal = os.stat(fileName).st_size
        self.ui_fileUpDlg.signal_refresh_sendFileLineEdit.emit(fileName, fileSizeTotal)
        self.ui_fileUpDlg.signal_refresh_sendProgressBar.emit(0)
        self.ui_fileUpDlg.fileNameSend = fileName
        # self.logic_client.uploadFile(fileName)

    def on_loginPushButton_click(self):
        userInfo = {'username':self.ui_loginDlg.usrLineEdit.text(), 'pwd':self.ui_loginDlg.pwdLineEdit.text()}
        print('ui登录:' + str(userInfo))
        self.logic_client.login(userInfo['username'])
        self.ui_loginDlg.close()
        self.ui_mainBoard.show()


if __name__ == '__main__':
    app = QApplication([])
    client = Client()
    client._start()
    sys.exit(app.exec_())
