import os
import sys

from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import QApplication

from client.udp_loginc import Logic_Client
from client.ui.filedowndlg import Ui_FileDownDlg
from client.ui.filesupdlg import Ui_FileUpDlg
from client.ui.logindlg import Ui_LoginDlg
from client.ui.mainboard import Ui_MainBoard


def check():
    print('hello')

class Client1(Ui_MainBoard):
    def __init__(self):
        super().__init__()
        self.ui_loginDlg = Ui_LoginDlg()
        self.ui_mainBoard = Ui_MainBoard()
        # self.ui_fileUpDlg = Ui_FileUpDlg()
        # self.logic_client = Logic_Client()
        # self.ui_fileDownDlg = Ui_FileDownDlg()

        # self.ui_mainBoard.setupUi()
        # self.ui_fileUpDlg.setupUi()

        self.bindSlots()
        # self.ui_loginDlg.loginPushButton.clicked.connect(check)

    def _start(self):
        self.ui_loginDlg.exec_()
        # self.logic_client.start()

    def bindSlots(self):
        self.ui_loginDlg.loginPushButton.clicked.connect(self.on_loginPushButton_click)
        self.ui_mainBoard.chatSendPushButton.clicked.connect(self.on_chatSendPushButton_click)

    def on_loginPushButton_click(self):
        print('bangding')
        self.ui_loginDlg.close()
        self.ui_mainBoard.show()

    def on_chatSendPushButton_click(self):
        print('chatSend')
        self.ui_mainBoard.signal_refresh_chatMsgShowTextBrowser.emit('78')

def check():
    print('ewwf')

def splitStr():
    str1 = u'\x02'
    str1 = str1.join(['a', 'b', 'c'])
    str2 = str1.encode()
    str3 = str2.decode()
    # print(str(str1))
    print(str1)
    # print(str1.encode())
    # print('str2:' + str2)
    print('str3:' + str3)

def getFilesList(rootDir):
    files = []
    dirs = []
    rootDir = os.path.join(os.getcwd(), rootDir)
    for fileName in os.listdir(rootDir):
        if (os.path.isfile(os.path.join(rootDir, fileName))):
            files.append(fileName)
        elif (os.path.isdir(os.path.join(rootDir, fileName))):
            dirs.append(fileName)
    filesNum = len(files)  # + len(dirs)
    return {'files': files, 'dirs': dirs, 'filesNum': filesNum}

def decodeAndDict():
    '''
    eval()会嵌套地把所有字符串转换为字典
    :return:
    '''
    dict1 = {'msgType': 'LISTFILE', 'msgFrom': 'aef', 'msgTo': 'aef', 'msgOther': {'files': ['aefcvfe.py'], 'dirs': [], 'filesNum': 1}}
    str1 = str(dict1)
    byte1 = str1.encode()

    str2 = byte1.decode()
    dict2 = eval(str2)
    print(type(dict2['msgOther']))

def htmlAndGUI():
    str = '\ta\n a'
    print(str)
    html = QTextDocument(str).toHtml()
    print(html)

def dictkeyValue():
    dict1 = {'efe': ('127.0.0.1', 57245), 'fe': ('127.0.0.1', 59353), 'efef': ('127.0.0.1', 61885), 'fef': ('127.0.0.1', 45)}
    for key in dict1:
        print('%s:%s' %(key, dict1[key]))

if __name__ == '__main__':
    pass
    # app = QApplication([])
    # ui = Ui_LoginDlg()
    # ui.loginPushButton.clicked.connect(check)
    # ui = Client1()
    # ui._start()
    # app.exec_()
    # htmlAndGUI()
    dictkeyValue()