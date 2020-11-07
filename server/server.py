import os
import struct
import threading
from datetime import datetime
from socket import *

port = 8808
local = '127.0.0.1'


class Server():
    ADDR = (local, port)
    def __init__(self):
        self.servSock = socket(AF_INET, SOCK_DGRAM)
        self.servSock.bind(self.ADDR)
        self.usr_online = {} # name:addr
        self.buffer = 1024
        # self.servSock.listen(120)
        print('服务器已就绪....')

        while True:
            try:
                # clntSock, clntAddr = self.servSock.accept()
                msg, addr = self.servSock.recvfrom(self.buffer)
                msg = msg.decode()
                # print(msg, addr)
                threading.Thread(target=self.handleMsg, args=(msg, addr)).start()
            except(ConnectionResetError):
                print('断线：' + str(addr))



    def handleMsg(self, msg, addr):
        dict_msg = eval(msg)

        if dict_msg['msgType'] == 'ONLINE':
            self.onLine(dict_msg['msgFrom'], addr)

        elif dict_msg['msgType'] == 'OFFLINE':
            self.offLine(dict_msg['msgFrom'], addr)

        elif dict_msg['msgType'] == 'CHATMSG':
            self.broadcast(dict_msg)
        elif dict_msg['msgType'] == 'LISTFILE':
            dict_msg['msgOther'] = self.getFilesList('upload')
            self.broadcast(dict_msg)
        elif dict_msg['msgType'] == 'LISTUSER':
            dict_msg['msgOther'] = self.getUserOnlineList()
            self.broadcast(dict_msg)
        elif dict_msg['msgType'] == 'UPFILE':
            threading.Thread(target=self.uploadFile, kwargs={'str_msg':msg}).start()
        elif dict_msg['msgType'] == 'DOWNFILE':
            threading.Thread(target=self.downloadFile, kwargs={'str_msg':dict_msg}).start()

        else:
            print('传输格式错误')


    def onLine(self, name, addr):
        print(str(addr) + '已连接')
        # self.broadcast('ONLINE' + '##' + name + '##' + '上线了')
        self.broadcast({'msgType':'ONLINE', 'msgFrom':str(name), 'msgTo':'ALL', 'msgOther':'上线了'})
        self.usr_online[name] = addr

    def offLine(self, name, addr):
        del self.usr_online[name]
        print(str(name) + '已下线')
        # self.broadcast('OFFLINE' + '##' + name + '##' + '下线了')
        self.broadcast({'msgType': 'OFFLINE', 'msgFrom': str(name), 'msgTo': 'ALL', 'msgOther': '已下线'})

    def getUserOnlineList(self):
        return self.usr_online

    def broadcast(self, dict_msg):
        '''
        向特定在线用户广播
        :param msg:
        :return:
        '''
        msgTo = str(dict_msg['msgTo'])
        msg = str(dict_msg)
        print(msg)
        # 广播
        if('ALL' == msgTo):
            for user in self.usr_online:
                self.servSock.sendto(msg.encode(), self.usr_online[user])
        # 单播
        else:
            self.servSock.sendto(msg.encode(), self.usr_online[msgTo])

    def downloadFile(self, dict_msg):
        baseFileName = dict_msg['msgOther']['fileName']
        absFileName = os.path.join(os.getcwd(), 'upload', baseFileName)
        if not os.path.isfile(absFileName):
            print(absFileName + ' 不存在')
            return

        fileSizeTotal = os.stat(absFileName).st_size
        self.udpSendMsg('DOWNLOADFILE', self.name, 'ALL',
                        {'fileName': os.path.basename(absFileName), 'fileSize': str(fileSizeTotal)})

        fileSock = socket(AF_INET, SOCK_STREAM)
        fileSock.connect(('127.0.0.1', 8809))

        # fileSock.send(fhead)
        print('client filepath:{0}'.format(absFileName))

        fp = open(absFileName, 'rb')
        fileSizeSent = 0
        while True:
            data = fp.read(1024)
            if not data:
                print('file send over...')
                break
            fileSizeSent += len(data)
            fileSock.send(data)
            self.ui_fileUpDlg.signal_refresh_sendProgressBar.emit(fileSizeSent / fileSizeTotal * 100)
        print(fileSizeSent)
        fileSock.close()


    def getFilesList(self, rootDir):
        files = []
        dirs = []
        absRootDir = os.path.join(os.getcwd(), rootDir)
        # print(absRootDir)
        for fileName in os.listdir(absRootDir):
            absFileName = os.path.join(rootDir, fileName)
            info = {'fileName': fileName,
                     'fileSize': os.stat(absFileName).st_size, # round(os.stat(absFileName).st_size / 1024, 2),
                     'modifyTime': datetime.fromtimestamp(os.stat(absFileName).st_mtime).strftime('%Y-%m-%d')}
            if (os.path.isfile(absFileName)):
                files.append(info)
            elif (os.path.isdir(absFileName)):
                dirs.append(info)
        filesNum = len(files)  # + len(dirs)
        return {'files': files, 'dirs': dirs, 'filesNum': filesNum}


    def uploadFile(self, str_msg):
        # msgType, uploader, receiver, fileName, fileSize = dict_msg.split('##')
        dict_msg = eval(str_msg)
        fileName = dict_msg['msgOther']['fileName']
        fileSize = dict_msg['msgOther']['fileSize']
        fileSock = socket(AF_INET, SOCK_STREAM)
        fileSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        fileSock.bind((local, port + 1))
        fileSock.listen(5)
        fileClntSock, fileClntAddr = fileSock.accept()

        # fileSize = struct.calcsize('128sl')
        # fhead = fileClntSock.recv(self.buffer)
        if fileName:
            # fileName, fileSize = struct.unpack('128sl', fhead)
            fileName = os.path.join('upload', fileName)
            rSize = 0
            fileSize = int(fileSize)
            fp = open(fileName, 'wb')
            print(fileName)
            print('start recving file...')

            while not rSize == fileSize:
                if(fileSize - rSize > self.buffer):
                    rData = fileClntSock.recv(self.buffer)
                    rSize += len(rData)
                else:
                    rData = fileClntSock.recv(fileSize - rSize)
                    rSize = fileSize
                fp.write(rData)
            fp.close()
            print('end recving file...')

        fileClntSock.close()
        fileSock.close()
        self.broadcast(dict_msg)


if __name__ == '__main__':
    serv = Server()

