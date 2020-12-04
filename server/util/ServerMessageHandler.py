import os
import random
import threading
import time
from datetime import datetime
from socket import *


class ServerMessageHandler(threading.Thread):
    BUFSIZE = 1024
    uploadBasePath = os.path.join('.', u'upload')
    rLock = threading.RLock()

    def __init__(self, func_errorHandle, userInfoList_online, dict_msg):
        super(ServerMessageHandler, self).__init__()
        self.dict_msg = dict_msg
        self.userInfoList_online = userInfoList_online  # [{'name':, 'socket':, 'addr':}]
        self.errorHandle = func_errorHandle

    def run(self) -> None:
        super().run()
        self.handleMsg(self.dict_msg)

    def handleMsg(self, dict_msg):
        '''
        核心函数：处理来自客户端的信息
        :param str_msg:
        :return:
        '''
        if dict_msg['msgType'] == 'ONLINE':
            self.broadcast(dict_msg)
        elif dict_msg['msgType'] == 'OFFLINE':
            self.offLine(dict_msg['msgFrom'])
        elif dict_msg['msgType'] == 'CHATMSG':
            self.broadcast(dict_msg)
        elif dict_msg['msgType'] == 'LISTFILE':
            dict_msg['msgOther'] = self.getFilesList(self.uploadBasePath)
            self.broadcast(dict_msg)
        elif dict_msg['msgType'] == 'LISTUSER':
            self.broadcast(dict_msg)
        elif dict_msg['msgType'] == 'UPFILE':
            self.uploadFile(dict_msg)
        elif dict_msg['msgType'] == 'DOWNFILE':
            self.downloadFile(dict_msg)
        else:
            print('传输格式错误')

    def onLine(self, userName, clntSock, clntAddr):
        '''
        某用户上线
        检查名字合法性
        更新在线用户们信息
        广播上线消息和在线用户信息
        :param userName:
        :param clntSock:
        :param clntAddr:
        :return:
        '''
        # for userInfo in self.userInfoList_online:
        #     if (userName == userInfo['name']):
        #         print('用户名已存在，随机取名')
        #         userName = userName + '_2'
        self.rLock.acquire()
        while self.getUserInfo(userName):
            print('用户名已存在，随机取名')
            userName = userName + '_' + str(random.randint(1, 100))

        self.userInfoList_online.append({'name': userName, 'socket': clntSock, 'addr': clntAddr})
        print('【上线】', self.userInfoList_online[-1])
        clntSock.send(userName.encode())
        self.broadcast(
            {'msgType': 'ONLINE', 'msgFrom': str(userName), 'msgTo': 'ALL',
             'msgOther': str(userName) + '上线了', 'time': time.strftime('%Y-%m-%d %H:%M:%S')})
        self.getUserOnlineList()
        self.rLock.release()
        return userName

    def offLine(self, username):
        '''
        某用户下线
        更新在线用户列表
        关闭该用户套接字
        广播下线消息和在线用户列表
        :param username:
        :return:从用户列表中删除结果
        '''
        self.rLock.acquire()
        userInfo = self.getUserInfo(username)
        if not userInfo:
            return False
        print('【下线】', userInfo)
        userInfo['socket'].close()
        # userInfo['socket'] = None
        self.userInfoList_online.remove(userInfo)
        self.broadcast(
            {'msgType': 'OFFLINE', 'msgFrom': str(username), 'msgTo': 'ALL',
             'msgOther': str(username) + '已下线', 'time': time.strftime('%Y-%m-%d %H:%M:%S')})
        self.getUserOnlineList()
        self.rLock.release()
        return True

    def getUserInfo(self, username):
        '''
        获取用户信息
        :param username:
        :return: 用户信息项目
        '''
        if not username:
            return None
        for i in range(len(self.userInfoList_online)):
            if (username == self.userInfoList_online[i]['name']):
                return self.userInfoList_online[i]
        return None

    def getUserOnlineList(self):
        '''
        向所有用户发送在线用户名单
        :return:
        '''
        userNameList = []
        for userInfo in self.userInfoList_online:
            userNameList.append(userInfo['name'])
        self.broadcast({'msgType': 'LISTUSER', 'msgFrom': 'ALL', 'msgTo': 'ALL', 'msgOther': userNameList, 'time': time.strftime('%Y-%m-%d %H:%M:%S')})

    def downloadFile(self, dict_msg):
        isOK = False
        # 读取客户端文件传输连接相关信息
        baseFileName = dict_msg['msgOther']['fileName']
        absFileName = os.path.join(self.uploadBasePath, baseFileName)
        fileSockAddr = dict_msg['msgOther']['fileSockAddr']

        # 建立连接
        fileSock = socket(AF_INET, SOCK_STREAM)
        fileSock.connect(fileSockAddr)

        # 检查数据合法性
        if not os.path.exists(absFileName):
            fileSock.close()
            raise Exception(absFileName + ' 不存在')

        # 开始发送文件
        fp = open(absFileName, 'rb')
        print('【文件下载】', '开始', absFileName)
        fileSizeSent = 0
        try:
            while True:
                data = fp.read(self.BUFSIZE)
                if not data:
                    print('【文件下载】', '结束', absFileName)
                    break
                else:
                    fileSock.send(data)
                    fileSizeSent += len(data)
        except:
            isOK = False
            self.errorHandle('文件下载通道已关闭', False)
        finally:
            fp.close()
            fileSock.close()
            return isOK

    def getFilesList(self, rootDir):
        files = []
        dirs = []
        absRootDir = os.path.join(os.getcwd(), rootDir)
        # print(absRootDir)
        for fileName in os.listdir(absRootDir):
            absFileName = os.path.join(rootDir, fileName)
            info = {'fileName': fileName,
                    'fileSize': os.stat(absFileName).st_size,  # round(os.stat(absFileName).st_size / 1024, 2),
                    'modifyTime': datetime.fromtimestamp(os.stat(absFileName).st_mtime).strftime('%Y-%m-%d')}
            if (os.path.isfile(absFileName)):
                files.append(info)
            elif (os.path.isdir(absFileName)):
                dirs.append(info)
        filesNum = len(files)  # + len(dirs)
        return {'files': files, 'dirs': dirs, 'filesNum': filesNum}

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
        absFileName = os.path.join(self.uploadBasePath, fileName)
        fileSzieRecv = 0
        fp = open(absFileName, 'wb')
        print('【文件上传】', '开始', (fileSizeTotal, absFileName))

        # 接收过程
        try:
            while not fileSzieRecv == fileSizeTotal:
                if (fileSizeTotal - fileSzieRecv > self.BUFSIZE):
                    rData = fileSock.recv(self.BUFSIZE)
                    fileSzieRecv += len(rData)
                    # print(rData)
                    # 因为Python中recv()是阻塞的(握手挥手)，只有连接断开或异常(send)时，接收到的是b''空字节类型，因此需要判断这种情况就断开连接。
                    if (b'' == rData):
                        raise Exception('文件上传通道已关闭')
                else:
                    rData = fileSock.recv(fileSizeTotal - fileSzieRecv)
                    fileSzieRecv = fileSizeTotal
                    print('【文件上传】', '结束', fileSizeTotal, absFileName)
                fp.write(rData)
        except:
            isOK = False
            self.errorHandle('文件上传通道已关闭', False)
        finally:
            fp.close()
            fileSock.close()
            if (fileSzieRecv == fileSizeTotal):
                isOK = True
                dict_msg['msgOther'] = '{0}上传了文件{1}'.format(dict_msg['msgFrom'], dict_msg['msgOther']['fileName'])
                self.broadcast(dict_msg)
            else:
                isOK = False
                os.remove(absFileName)
                print('【删除文件】文件上传失败', absFileName)
            return isOK

    def broadcast(self, dict_msg):
        '''
        向特定在线用户广播
        :param msg:
        :return:
        '''
        msgTo = str(dict_msg['msgTo'])
        msg = str(dict_msg) + u'\x02\x02'  # 以不可见字符解决tcp粘包问题
        print('>>:' + msg)

        # 广播
        if ('ALL' == msgTo):
            for userInfo in self.userInfoList_online:
                userInfo['socket'].send(msg.encode())
        # 单播
        else:
            for userInfo in self.userInfoList_online:
                if (msgTo == userInfo['name']):
                    userInfo['socket'].send(msg.encode())
