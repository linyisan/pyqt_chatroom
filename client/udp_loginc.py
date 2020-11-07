import os
import time

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import threading
from socket import *


SERVER_ADDR = ('127.0.0.1', 8808)
BUFSIZE = 1024



class Logic_Client():
    clntSock = socket(AF_INET, SOCK_DGRAM)
    usr_online = {}
    # def __init__(self):
    #     super(Logic_Client, self).__init__()
    #     self.name = name
    #     print(self.name)
        # self.login(self.name)


    def setUiInstances(self, ui_mainBoard, ui_fileDownDlg, ui_fileUpDlg):
        '''
        设置UI实例
        :param ui_mainBoard:
        :param ui_fileDownDlg:
        :param ui_fileUpDlg:
        :return:
        '''
        self.ui__mainBoadr = ui_mainBoard
        self.ui_fileDownDlg = ui_fileDownDlg
        self.ui_fileUpDlg = ui_fileUpDlg


    def start(self):
        mThread = threading.Thread(target=self.recvMsg)
        mThread.setDaemon(True)
        mThread.start()

        self.getUserOnlineList()

        # self.uploadFile('C:\\Users\\yisan\\Desktop\\epub制作\\渴望死亡的小丑.txt')
        # self.udpSendMsg('a', 'b', 'b')

        # self.clntSock.sendto(('OFFLINE##' + self.name).encode(), SERVER_ADDR)


    def login(self, name):
        self.name = name
        # self.clntSock.sendto(('ONLINE' + '##' + self.name).encode(), SERVER_ADDR)
        self.udpSendMsg('ONLINE', self.name, 'ALL')

    def recvMsg(self):
        while True:
            rData, ADDR = self.clntSock.recvfrom(BUFSIZE)
            print('<<:' + rData.decode())
            rData = rData.decode()
            # msgParts = rData.split(u'\x02')
            dict_msg = eval(rData)
            msgType = dict_msg['msgType']
            msgFrom = dict_msg['msgFrom']
            msgTo = dict_msg['msgTo']
            msgOther = dict_msg['msgOther']
            print(dict_msg)
            # print('recvMsg:' + msgOther)

            curTime = time.strftime('%Y-%m-%d %H:%M:%S')
            if('CHATMSG' == msgType
                    or 'ONLINE' == msgType
                    or 'OFFLINE' == msgType):
                strFormat = '&lt;{0}&gt;【{1}】:\n{2}'.format(str(msgFrom), str(curTime), str(msgOther))
                self.ui__mainBoadr.signal_refresh_chatMsgShowTextBrowser.emit(strFormat)
            elif('LISTFILE' == msgType):
                self.filesList = msgOther
                self.ui__mainBoadr.signal_refresh_filesShowTableWidget.emit(self.filesList)
            elif('LISTUSER' == msgType):
                self.usr_online = msgOther
                self.ui__mainBoadr.refresh_chatUserOnLineTableWidget(self.usr_online)

    def uploadFile(self, fileName):
        if not os.path.isfile(fileName):
            print(fileName + ' 不存在')
            return

        # fileSize = struct.calcsize('128sl')
        # self.clntSock.sendto(('UPFILE##' + self.name + '##' + os.path.basename(fileName) + '##' + str(os.stat(fileName).st_size)).encode(), SERVER_ADDR)
        fileSizeTotal = os.stat(fileName).st_size
        self.udpSendMsg('UPFILE', self.name, 'ALL', {'fileName': os.path.basename(fileName), 'fileSize':str(fileSizeTotal)})
        # fhead = struct.pack(b'128sl', os.path.basename(fileName).encode(),
        #                         os.stat(fileName).st_size)

        fileSock = socket(AF_INET, SOCK_STREAM)
        fileSock.connect(('127.0.0.1', 8809))

        # fileSock.send(fhead)
        print('client filepath:{0}'.format(fileName))

        fp = open(fileName, 'rb')
        fileSizeSent = 0
        while True:
            data = fp.read(BUFSIZE)
            if not data:
                print('file send over...')
                break
            fileSizeSent += len(data)
            fileSock.send(data)
            self.ui_fileUpDlg.signal_refresh_sendProgressBar.emit(fileSizeSent / fileSizeTotal * 100)
        print(fileSizeSent)
        fileSock.close()

    def downloadFile(self, fileName, fileSize):
        self.udpSendMsg('DOWNLOADFILE', self.name, self.name, {'fileName':fileName})
        fileSock = socket(AF_INET, SOCK_STREAM)
        fileSock.connect(('127.0.0.1', 8810))

        # fileSock.send(fhead)
        print('client filepath:{0}'.format(fileName))
        print('start downloading file...')
        fp = open(fileName, 'wb')
        rSize = 0
        while not rSize == fileSize:
            if(fileSize - rSize > BUFSIZE):
                rData = fileSock.recv(BUFSIZE)
                rSize += len(rData)
            else:
                rData = fileSock.recv(fileSize - rSize)
                rSize = fileSize
            fp.write(rData)
        fp.close()
        fileSock.close()
        print('end downloading file...')

    def sendChatMsg(self, msg):
        # self.clntSock.sendto(('CHATMSG' + '##' + self.name + '##' + msg).encode(), SERVER_ADDR)
        self.udpSendMsg('CHATMSG', self.name, 'ALL', msg)


    def offLine(self):
        # self.clntSock.sendto(('OFFLINE##' + self.name).encode(), SERVER_ADDR)
        self.udpSendMsg('OFFLINE', self.name, 'ALL')

    def udpSendMsg(self, *args):
        # msg = u'\x02'.join(args)
        msg = {'msgType': args[0], 'msgFrom':args[1], 'msgTo':args[2], 'msgOther':None}
        if(len(args) > 3):
            msg['msgOther'] = args[3]
        msg = str(msg)
        print('>>:' + msg)
        self.clntSock.sendto(msg.encode(), SERVER_ADDR)

    def getFilesList(self):
        self.udpSendMsg('LISTFILE', self.name, self.name)

    def getUserOnlineList(self):
        self.udpSendMsg('LISTUSER', self.name, self.name)

if __name__ == '__main__':
    app = QApplication([])
    ui = Logic_Client()
    ui.show()
    app.exec_()