import threading
import traceback
from socket import *

from util.ServerMessageHandler import ServerMessageHandler

port = 8808
local = '127.0.0.1'


class Server():
    ADDR = (local, port)

    def __init__(self):
        self.servSock = socket(AF_INET, SOCK_STREAM)
        self.BUFSIZE = 1024
        self.userInfoList_online = []  # [{'name':, 'socket':, 'addr':}]
        # self.msgHandler = ServerMessageHandler(self.userInfoList_online, self.errorHandle)


    def start(self):
        self.servSock.bind(self.ADDR)
        self.servSock.listen(120)
        print('服务器已就绪....')
        while True:
            clntSock, clntAddr = self.servSock.accept()
            threading.Thread(target=self.tcp_connect, args=(clntSock, clntAddr)).start()

    def tcp_connect(self, clntSock, clntAddr):
        '''
        处理每个客户端连接/通信
        :param clntSock:客户端套接字
        :param clntAddr:客户端地址和端口信息
        :return:
        '''
        userName = None
        try:
            self.msgHandler = ServerMessageHandler(func_errorHandle=self.errorHandle, userInfoList_online=self.userInfoList_online, dict_msg=None)
            # 首先是确认用户名(唯一性)
            userName = clntSock.recv(self.BUFSIZE).decode()
            userName = self.msgHandler.onLine(userName, clntSock, clntAddr)

            # 处理信息（核心）
            isEnd = False
            while not isEnd:
                rData = clntSock.recv(self.BUFSIZE).decode()
                str_msgs = rData.split(u'\x02\x02')  # 以不可见字符分割解决tcp粘包问题
                for str_msg in str_msgs:
                    if (str_msg != ''):  # 空字符
                        dict_msg = eval(str_msg)
                        if('OFFLINE' == dict_msg['msgType']):
                            isEnd = True
                        self.msgHandler = ServerMessageHandler(func_errorHandle=self.errorHandle, userInfoList_online=self.userInfoList_online, dict_msg=dict_msg)
                        self.msgHandler.start()
        except:
            self.errorHandle(userName + '连接强制断开', True)
            self.msgHandler.offLine(userName)


    def errorHandle(self, errorMsg, isPrintTraceback=True):
        print('【已捕获异常】', str(errorMsg))
        if(isPrintTraceback):
            traceback.print_exc()


if __name__ == '__main__':
    serv = Server()
    serv.start()
