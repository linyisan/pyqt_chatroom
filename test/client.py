import os
import traceback
from socket import *
ADDR = ('127.0.0.1', 7878)


def uploadFile(fileName):
    isOK = False  # 文件上传成功标志
    # 文件是否存在
    if not os.path.isfile(fileName):
        print(fileName + ' 不存在')
        return isOK

    # 创建文件传输连接套接字
    fileSock = socket(AF_INET, SOCK_STREAM)
    fileSock.bind(('127.0.0.1', 7878))
    fileSock.listen(1)

    fileSizeTotal = os.stat(fileName).st_size  # 文件总大小(B)
    # 告知服务器连接到本地的相关配置信息
    # self.tcpSendMsg('UPFILE', self.userName, 'ALL',
    #                 {'fileName': os.path.basename(fileName), 'fileSize': fileSizeTotal,
    #                  'fileSockAddr': fileSock.getsockname()})

    # 开始文件传输
    clntSock, clntAddr = fileSock.accept()
    print('start sending file...')
    print(fileSizeTotal, fileName)
    fp = open(fileName, 'rb')
    fileSizeSent = 0  # 已发送的字节数(B)

    # 传输过程
    try:
        # if not self.addFileTransferTask('UPLOAD' + fileName, clntSock):
        #     isOK = False
        #     return isOK
        while True:
            data = fp.read(1024)
            if not data:
                print('file send over...')
                break
            fileSizeSent += len(data)
            # self.ui_fileUpDlg.signal_refresh_sendProgressBar.emit(fileSizeSent / fileSizeTotal * 100)
            for i in range(10):
                clntSock.send(data)
            clntSock.shutdown(SHUT_RDWR)
            # clntSock.close()
            # fileSock.close()

    except:
        isOK = False
        traceback.print_exc()
    finally:
        if (fileSizeTotal == fileSizeSent):
            print('成功发送文件', fileSizeTotal, fileName)
            isOK = True
        # self.removeFileTransferTask('UPLOAD' + fileName)
        fp.close()
        clntSock.close()
        fileSock.close()
        return isOK

if __name__ == '__main__':
    # uploadFile('F:\\迅雷下载\\movie\\[Skytree][空之境界][Kara_no_Kyoukai][第一章 俯瞰风景][GB_JP][x264 FLAC][1080P][BDRIP][天空树中日双语字幕组].mkv')
    mSocket = socket(AF_INET, SOCK_STREAM)
    mSocket.connect(ADDR)
    while True:
        rData = mSocket.recv(1024)
        print(rData, len(rData))
        if(rData == b''):
            break
        # mSocket.send('1'.encode())
    mSocket.close()

