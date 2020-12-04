import os
import traceback
import uuid
from socket import *

from ui.filedowndlg import Ui_FileDownDlg
from ui.filesupdlg import Ui_FileUpDlg


class FileHandler():
    fileTransferTasks = {}  # {文件UUID:通信socket, }
    BUFSIZE = 1024

    def __init__(self, func_sendMsg, func_errorHandle):
        super(FileHandler, self).__init__()
        self.username = None
        self.sendMsg = func_sendMsg
        self.errorHandle = func_errorHandle

    def getFilesList(self):
        self.sendMsg('LISTFILE', self.username, self.username, {})

    def uploadFile(self, fileName, ui_fileUpDlg):
        '''
        文件上传
        :param fileName: 文件绝对路径
        :param ui_fileUpDlg: UI
        :return: 操作结果
        '''
        isOK = False  # 文件上传成功标志

        # 文件是否存在
        if not os.path.isfile(fileName):
            print(fileName + ' 不存在')
            return isOK

        # 创建文件传输连接套接字
        fileSock = socket(AF_INET, SOCK_STREAM)
        fileSock.bind(('localhost', 0))
        fileSock.listen(1)

        fileSizeTotal = os.stat(fileName).st_size  # 文件总大小(B)
        # 告知服务器连接到本地的相关配置信息
        self.sendMsg('UPFILE', self.username, 'ALL',
                     {'fileName': os.path.basename(fileName), 'fileSize': fileSizeTotal,
                      'fileSockAddr': fileSock.getsockname()})

        # 开始文件传输
        clntSock, clntAddr = fileSock.accept()
        print('【文件上传】', '开始', (fileSizeTotal, fileName))
        print(fileSizeTotal, fileName)
        fp = open(fileName, 'rb')
        fileSizeSent = 0  # 已发送的字节数(B)

        # 传输过程
        try:
            if not self.addFileTransferTask('UPLOAD' + fileName, clntSock):
                isOK = False
                return isOK
            while True:
                data = fp.read(self.BUFSIZE)
                if not data:
                    print('\n【文件上传】', '结束', (fileSizeTotal, fileName))
                    break
                fileSizeSent += len(data)
                clntSock.send(data)
                if (isinstance(ui_fileUpDlg, Ui_FileUpDlg)):
                    ui_fileUpDlg.refresh_sendProgressBar(fileSizeSent / fileSizeTotal * 100)
                print('\r', '【进度】', fileSizeSent / fileSizeTotal * 100, fileName, end='')
        except:
            isOK = False
            self.errorHandle('文件上传通道已关闭', False)
        finally:
            if (fileSizeTotal == fileSizeSent):
                print('成功发送文件', fileSizeTotal, fileName)
                isOK = True
            self.removeFileTransferTask('UPLOAD' + fileName)
            fp.close()
            clntSock.close()
            fileSock.close()
            return isOK

    def downloadFile(self, fileName, fileSizeTotal, saveFileName, ui_fileDownDlg):
        isOK = False
        # 创建文件传输连接套接字
        fileSock = socket(AF_INET, SOCK_STREAM)
        fileSock.bind(('localhost', 0))
        fileSock.listen(1)

        # 告知服务器连接到本地的相关配置信息
        self.sendMsg('DOWNFILE', self.username, self.username,
                     {'fileName': fileName, 'fileSockAddr': fileSock.getsockname()})
        # 开始文件传输
        clntSock, clntAddr = fileSock.accept()
        fp = open(saveFileName, 'wb')
        fileSizeSent = 0  # 已发送的字节数(B)
        print('【文件下载】', '开始', (fileSizeTotal, fileName))

        # 传输过程
        try:
            if not self.addFileTransferTask('DOWNLOAD' + fileName, clntSock):
                isOK = False
                return isOK
            while not fileSizeSent == fileSizeTotal:
                if (fileSizeTotal - fileSizeSent > self.BUFSIZE):
                    rData = clntSock.recv(self.BUFSIZE)
                    fileSizeSent += len(rData)
                else:
                    rData = clntSock.recv(fileSizeTotal - fileSizeSent)
                    fileSizeSent = fileSizeTotal
                    isOK = True
                    print('\n【文件下载】', '结束', (fileSizeTotal, fileName))
                fp.write(rData)
                if (isinstance(ui_fileDownDlg, Ui_FileDownDlg)):
                    ui_fileDownDlg.refresh_recvProgressBar(fileSizeSent / fileSizeTotal * 100)
                print('\r', '【进度】', fileSizeSent / fileSizeTotal * 100, fileName, end='')
        except:
            isOK = False
            self.errorHandle('文件下载通道已关闭', False)
        finally:
            self.removeFileTransferTask('DOWNLOAD' + fileName)
            fp.close()
            clntSock.close()
            fileSock.close()
            if(fileSizeSent == fileSizeTotal):
                isOK = True
            return isOK

    def interruptFileTransfer(self, fileName, isUpload):
        print('\n【阻止传输】', fileName)
        if isUpload:
            fileName = 'UPLOAD' + fileName
        else:
            fileName = 'DOWNLOAD' + fileName
        fileSock = self.removeFileTransferTask(fileName)
        if not fileSock:
            return False
        else:
            # fileSock.shutdown(SHUT_RDWR)
            fileSock.close()
            return True

    def getFileUUID(self, fileName):
        return str(uuid.uuid5(uuid.NAMESPACE_DNS, fileName))

    def isExistFileTrasferTask(self, fileUUID):
        if (fileUUID in self.fileTransferTasks):
            return True
        else:
            return False

    def addFileTransferTask(self, fileName, fileSock):
        fileUUID = self.getFileUUID(fileName)
        if self.isExistFileTrasferTask(self.isExistFileTrasferTask(fileUUID)):
            return False
        self.fileTransferTasks[fileUUID] = fileSock
        print('【文件任务】', '添加', fileName, fileUUID)
        return True

    def removeFileTransferTask(self, fileName):
        fileUUID = self.getFileUUID(fileName)
        if not self.isExistFileTrasferTask(fileUUID):
            return None
        fileSock = self.fileTransferTasks[fileUUID]
        del self.fileTransferTasks[fileUUID]
        print('\n【文件任务】', '移除', fileName, fileUUID)
        return fileSock
