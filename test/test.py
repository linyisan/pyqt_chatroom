import os
import struct
import sys
import uuid
from socket import *

from PySide2.QtCore import QObject, Signal
from PySide2.QtGui import QTextDocument

sys.path.append('C:\\Users\\yisan\\PycharmProjects\\pyqt_chatroom')

from PySide2.QtWidgets import QApplication, QFileDialog

from client.ui.logindlg import Ui_LoginDlg
from client.ui.mainboard import Ui_MainBoard
from ui.filedowndlg import Ui_FileDownDlg


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

    def saveFileDlg(self):
        file_path = file_path = QFileDialog.getSaveFileName(self, u'保存文件', u'../client',
                                                            u'all files(*.*)')
        return file_path

def check(num):
    print(num)


def splitStr():
    separator = u'\x02'
    str1 = separator.join(['a', 'b', 'c'])
    str2 = str1.encode()
    str3 = str2.decode()
    # print(str(str1))
    print(str1)
    # print(str1.encode())
    # print('str2:' + str2)
    print('str3:' + str3)
    # print(str3.split(separator))


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
    dict1 = {'msgType': 'LISTFILE', 'msgFrom': 'aef', 'msgTo': 'aef',
             'msgOther': {'files': ['aefcvfe.py'], 'dirs': [], 'filesNum': 1}}
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
    dict1 = {'efe': ('127.0.0.1', 57245), 'fe': ('127.0.0.1', 59353), 'efef': ('127.0.0.1', 61885),
             'fef': ('127.0.0.1', 45)}
    for key in dict1:
        print('%s:%s' % (key, dict1[key]))



class FileServer(QObject):
    signalTest = Signal(int)
    attra = 1
    fileSock = socket(AF_INET, SOCK_STREAM)
    backlog = 10 # 最大连接数，挂起连接队列的最大长度
    uploadBasePath = os.path.join(u'../client', u'upload')


    def getFileServerPort(self):
        print(self.fileSock.getsockname())
        return self.fileSock.getsockname()[1]

def getEmoji():
    ori = ['😀','😁','🤓','💩']

    for item in ori:
        item = item.encode()
        print(item,end=',')
        num = struct.unpack('>L', item)#int.from_bytes(item, byteorder='big', signed=False)
        print(num,end=',')
        print()

    print()
    start = int.from_bytes('😀'.encode(), byteorder='big', signed=False)
    end = int.from_bytes('😼'.encode(),byteorder='big', signed=False)
    emoji = []
    for i in range(start, end, 1):
        emoji.append(struct.pack('>L', i).decode())
        print(struct.pack('>L', i).decode(),end=',')
        # print(int(str(item).encode(), 16))

def inStanceHasSomething():
    c = FileServer()
    # FileServer.signalTest.connect(check) # 信号是实例引用
    c.signalTest.connect(check)
    c.signalTest.emit(12)
    print(hasattr(c, 'attra'))
    print(c.attra)
    print(hasattr(Client1, 'attra'))
    print(FileServer.attra)

def getNewFileDownDlg():
    ui = Ui_FileDownDlg()
    ui.show()
    return ui

def typea():
    ui = Ui_FileDownDlg()
    print(isinstance(ui, Ui_FileDownDlg))
    print(isinstance(None, Ui_FileDownDlg))

def uniqueName():
    fileName = 'C:\\Users\\yisan\\Downloads'
    fileList = {}
    fileList['_'.join([str(uuid.uuid5(uuid.NAMESPACE_DNS, fileName)), fileName])] = 1
    fileList[str(uuid.uuid3(uuid.NAMESPACE_DNS, fileName)) + fileName] = 2
    fileList[str(uuid.uuid5(uuid.NAMESPACE_OID, fileName)) + fileName] = 3
    fileList[str(uuid.uuid5(uuid.NAMESPACE_OID, fileName)) + fileName] = 4

    for k in fileList:
        print(k, '=', fileList[k])
        # if(2 == fileList[k]):
        #     del fileList[k]
        #     break
    print('69c7af3a-f445-30bb-9955-624c1c98c42bC:\\Users\\yisan\\Downloads' in fileList)
    del fileList['69c7af3a-f445-30bb-9955-624c1c98c42bC:\\Users\\yisan\\Downloads']
    print('69c7af3a-f445-30bb-9955-624c1c98c42bC:\\Users\\yisan\\Downloads' in fileList)

    for k in fileList:
        print(k, '=', fileList[k])

def returnAndFinally():
    try:
        print('try')
        return 1
        print(1/0)
    except:
        print('except')
        return 2
    finally:
        print('finally')
        return 3


def ReferenceAndDel():
    userInfoList = [{'name': 'a', 'socket': 1}, {'name': 'a', 'socket': 2}]
    print(len(userInfoList))
    refer = userInfoList[1]
    del refer  # 只是删除了引用，userInfoList还是存在
    userInfoList.remove(refer)
    print(len(userInfoList))


if __name__ == '__main__':
    pass
    app = QApplication([])
    print(type(True))
    # print(returnAndFinally())
    # print(type(Ui_FileDownDlg().signal_refresh_recvProgressBar))
    # print(QMessageBox.Yes == QMessageBox.question(None, '', '', QMessageBox.Yes|QMessageBox.Cancel))
    # print(isinstance(None, Ui_FileDownDlg))
