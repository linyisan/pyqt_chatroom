import os
import traceback
from socket import *

ADDR = ('127.0.0.1', 7878)
uploadBasePath = os.path.join('..', 'server', u'upload')

def uploadFile():
    isOK = False
    # 读取客户端文件传输连接相关信息
    fileName = '空之境界.mp4'#dict_msg['msgOther']['fileName'].strip()
    fileSizeTotal = 939951339#dict_msg['msgOther']['fileSize']
    # fileSockAddr = dict_msg['msgOther']['fileSockAddr']

    # 检查数据合法性
    if not fileName or fileSizeTotal < 0:
        return isOK

    # 建立连接
    fileSock = socket(AF_INET, SOCK_STREAM)
    fileSock.connect(('127.0.0.1', 7878))

    # 开始接收文件
    fileName = os.path.join(uploadBasePath, fileName)
    fileSzieRecv = 0
    fp = open(fileName, 'wb')
    print('start recving file...')
    print(fileSizeTotal, fileName)
    try:
        # 接收过程
        while not fileSzieRecv == fileSizeTotal:
            if (fileSizeTotal - fileSzieRecv > 1024):
                rData = fileSock.recv(1024)
                fileSzieRecv += len(rData)
                # fileSock.send(rData)
                print(rData)
            else:
                rData = fileSock.recv(fileSizeTotal - fileSzieRecv)
                fileSzieRecv = fileSizeTotal
                print('end recving file...')
            fp.write(rData)
        isOK = True
        # dict_msg['msgOther'] = '{0}上传了文件{1}'.format(dict_msg['msgFrom'], dict_msg['msgOther']['fileName'])
        # self.broadcast(dict_msg)
    except:
        isOK = False
        traceback.print_exc()
    finally:
        fp.close()
        fileSock.close()
        return isOK

if __name__ == '__main__':
    # uploadFile()
    mSocket = socket(AF_INET, SOCK_STREAM)
    mSocket.bind(ADDR)
    mSocket.listen(1)
    clntSock, clntAddr = mSocket.accept()
    # for i in range(100):
    #     clntSock.send(str(i).encode())
    # while True:
    #     print(clntSock.recv(1024))
    print(len('abcd'))
    clntSock.send('abcd'.encode())
    clntSock.close()
    mSocket.close()