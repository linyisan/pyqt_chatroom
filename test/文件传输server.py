import os
import traceback
from socket import *

uploadBasePath = os.path.join(u'.', u'upload')

def uploadFile(self, dict_msg):
    isOK = False
    # 读取客户端文件传输连接相关信息
    fileName = dict_msg['msgOther']['fileName'].strip()
    fileSizeTotal = dict_msg['msgOther']['fileSize']
    fileSockAddr = dict_msg['msgOther']['fileSockAddr']

    # 检查数据合法性
    if not fileName or fileSizeTotal < 0:
        return isOK

    # 建立连接
    fileSock = socket(AF_INET, SOCK_STREAM)
    fileSock.connect(fileSockAddr)

    # 开始接收文件
    try:
        fileName = os.path.join(uploadBasePath, fileName)
        fileSzieRecv = 0
        fp = open(fileName, 'wb')
        print('start recving file...')
        print(fileSizeTotal, fileName)

        # 接收过程
        while not fileSzieRecv == fileSizeTotal:
            if (fileSizeTotal - fileSzieRecv > self.BUFSIZE):
                rData = fileSock.recv(self.BUFSIZE)
                fileSzieRecv += len(rData)
            else:
                rData = fileSock.recv(fileSizeTotal - fileSzieRecv)
                fileSzieRecv = fileSizeTotal
                print('end recving file...')
            fp.write(rData)
        isOK = True
        dict_msg['msgOther'] = '{0}上传了文件{1}'.format(dict_msg['msgFrom'], dict_msg['msgOther']['fileName'])
        self.broadcast(dict_msg)
    except:
        isOK = False
        traceback.print_exc()
    finally:
        fp.close()
        fileSock.close()
        return isOK

def downloadFile(self, dict_msg):
    isOK = False
    # 读取客户端文件传输连接相关信息
    baseFileName = dict_msg['msgOther']['fileName']
    absFileName = os.path.join(uploadBasePath, baseFileName)
    fileSockAddr = dict_msg['msgOther']['fileSockAddr']

    # 检查数据合法性
    if not os.path.isfile(absFileName):
        print(absFileName + ' 不存在')
        return isOK

    # 建立连接
    fileSock = socket(AF_INET, SOCK_STREAM)
    fileSock.connect(fileSockAddr)

    # 开始发送文件
    try:
        fp = open(absFileName, 'rb')
        print('start sending file...')
        print(absFileName)
        fileSizeSent = 0
        while True:
            data = fp.read(self.BUFSIZE)
            if not data:
                print('file send over...')
                break
            else:
                fileSock.send(data)
                fileSizeSent += len(data)
    except:
        isOK = False
        traceback.print_exc()
    finally:
        fp.close()
        fileSock.close()
        return isOK