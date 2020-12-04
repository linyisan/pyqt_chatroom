'''
告知服务器端口连接到本地客户端
'''
import os
import traceback
from socket import *


def uploadFile(self, fileName):
    isOK = False # 文件上传成功标志
    # 文件是否存在
    if not os.path.isfile(fileName):
        print(fileName + ' 不存在')
        return isOK

    # 创建文件传输连接套接字
    fileSock = socket(AF_INET, SOCK_STREAM)
    fileSock.bind(('localhost', 0))
    fileSock.listen(1)

    fileSizeTotal = os.stat(fileName).st_size # 文件总大小(B)
    # 告知服务器连接到本地的相关配置信息
    self.tcpSendMsg('UPFILE', self.userName, 'ALL',
                    {'fileName': os.path.basename(fileName), 'fileSize': fileSizeTotal,
                     'fileSockAddr': fileSock.getsockname()})

    # 开始文件传输
    clntSock, clntAddr = fileSock.accept()
    print('start sending file...')
    print(fileSizeTotal, fileName)
    fp = open(fileName, 'rb')
    fileSizeSent = 0 # 已发送的字节数(B)

    # 传输过程
    try:
        while True:
            data = fp.read(self.BUFSIZE)
            if not data:
                print('file send over...')
                break
            fileSizeSent += len(data)
            clntSock.send(data)
            self.ui_fileUpDlg.signal_refresh_sendProgressBar.emit(fileSizeSent / fileSizeTotal * 100)
    except:
        isOK = False
        traceback.print_exc()
    finally:
        if (fileSizeTotal == fileSizeSent):
            print('成功发送文件', fileSizeTotal, fileName)
            isOK = True
        fp.close()
        clntSock.close()
        fileSock.close()
        return isOK



def downloadFile(self, fileName, fileSizeTotal, saveFileName):
    isOK = False
    # 创建文件传输连接套接字
    fileSock = socket(AF_INET, SOCK_STREAM)
    fileSock.bind(('localhost', 0))
    fileSock.listen(1)

    # 告知服务器连接到本地的相关配置信息
    self.tcpSendMsg('DOWNFILE', self.userName, self.userName, {'fileName': fileName, 'fileSockAddr': fileSock.getsockname()})

    # 开始文件传输
    clntSock, clntAddr = fileSock.accept()
    fp = open(saveFileName, 'wb')
    fileSizeSent = 0 # 已发送的字节数(B)
    print('start downloading file...')
    print(fileSizeTotal, fileName)

    # 传输过程
    try:
        while not fileSizeSent == fileSizeTotal:
            if (fileSizeTotal - fileSizeSent > self.BUFSIZE):
                rData = clntSock.recv(self.BUFSIZE)
                fileSizeSent += len(rData)
            else:
                rData = clntSock.recv(fileSizeTotal - fileSizeSent)
                fileSizeSent = fileSizeTotal
                isOK = True
                print('end downloading file...')
            fp.write(rData)
            self.ui_fileDownDlg.signal_refresh_recvProgressBar.emit(fileSizeSent / fileSizeTotal * 100)
    except:
        isOK = False
        traceback.print_exc()
    finally:
        fp.close()
        clntSock.close()
        fileSock.close()
        return isOK