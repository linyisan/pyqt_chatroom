import os
import sys
import threading
import time
import traceback
from socket import *

from PySide2.QtCore import QObject
from PySide2.QtWidgets import QApplication

from ui.mainboard import Ui_MainBoard
from utils.filehandler import FileHandler


class Logic_Client(QObject):
    BUFSIZE = 1024
    lock = threading.Lock()

    def __init__(self):
        super(Logic_Client, self).__init__()
        self.usr_online = {}
        self.mSocket = None
        self.fileHandler = FileHandler(self.tcpSendMsg, self.errorHandle)

    def setUiInstances(self, ui_mainBoard):
        '''
        设置UI实例，与UI进行交互
        :param ui_mainBoard:
        :return:
        '''
        if isinstance(ui_mainBoard, Ui_MainBoard):
            self.ui_mainBoard = ui_mainBoard
            return True
        else:
            return False

    def onLine(self, userName, serverAddr):
        '''
        客户端上线/连接服务器/开始主进程
        :param userName: 用户名
        :param serverAddr: 服务器密码
        :return: 连接结果
        '''
        isConnected = False
        self.mSocket = socket(AF_INET, SOCK_STREAM)
        try:
            self.mSocket.connect(serverAddr)
            self.mSocket.send(userName.encode())

            self.username = self.mSocket.recv(self.BUFSIZE).decode()
            self.fileHandler.username = self.username
            self.recvMsgThread = threading.Thread(target=self.tcpRecvMsg)
            self.recvMsgThread.start()
            isConnected = True
            print('【上线】', (userName, serverAddr))
            # self.tcpSendMsg( 'ONLINE', self.username, 'ALL', self.username + '上线了')
        except:
            self.errorHandle(''.join([serverAddr, '目标主机无法连接']))
        finally:
            return isConnected

    def offLine(self):
        '''
        客户端离线/断开连接/结束通讯/退出程序
        :return:
        '''
        self.tcpSendMsg('OFFLINE', self.username, 'ALL')
        if self.mSocket:
            self.mSocket.close()
        print('【下线】', self.username)
        # self.tcpSendMsg('OFFLINE', self.username, 'ALL', self.username + '下线了')
        os._exit(0)

    def handleMsg(self, str_Msg):
        '''
        处理接收的消息
        :param str_Msg: 以字符串形式的消息
        :return:
        '''
        # 解构消息
        print('<<:' + str_Msg)
        dict_msg = eval(str_Msg)
        msgType = dict_msg['msgType']
        msgFrom = dict_msg['msgFrom']
        msgTo = dict_msg['msgTo']
        msgOther = dict_msg['msgOther']
        time = dict_msg['time']

        # 处理消息类型
        curTime = time
        if ('CHATMSG' == msgType
                or 'ONLINE' == msgType
                or 'OFFLINE' == msgType
                or 'UPFILE' == msgType):
            isMe = 2
            msgBgColor = 'white'
            strFormat = '【{0}】:\n{1}'.format(str(curTime), str(msgOther))
            if (self.username == msgFrom):
                msgBgColor = '#9eea6a'
                isMe = 1
            if (msgType != 'CHATMSG'):
                msgBgColor = '#dadada'
                isMe = 0
                strFormat = '【{0}】:{1}'.format(str(curTime), str(msgOther))
            self.ui_mainBoard.signal_refresh_chatMsgShowListWidget.emit(msgFrom, strFormat, isMe, msgBgColor,
                                                                        'ui/ico/ico.png')
        elif ('LISTFILE' == msgType):
            filesList = msgOther
            self.ui_mainBoard.signal_refresh_filesShowTableWidget.emit(filesList)
        elif ('LISTUSER' == msgType):
            self.usr_online = msgOther
            self.ui_mainBoard.refresh_chatUserOnLineTableWidget(self.usr_online)

    def sendChatMsg(self, msg):
        '''
        构造并发送聊天消息
        :param msg:聊天内容
        :return:
        '''
        self.tcpSendMsg('CHATMSG', self.username, 'ALL', msg)

    def tcpRecvMsg(self):
        '''
        接收消息并进行粘包分割
        :return:
        '''
        try:
            while True:
                rData = self.mSocket.recv(self.BUFSIZE).decode()
                str_msgs = rData.split(u'\x02\x02')  # 以不可见字符分割解决tcp粘包问题
                for str_msg in str_msgs:
                    if str_msg != '':  # 空字符
                        threading.Thread(target=self.handleMsg, args=(str_msg,)).start()
        except:
            self.errorHandle('套接字已关闭，通信结束')
            sys.exit("非正常关闭")

    def tcpSendMsg(self, msgType, msgFrom, msgTo, msgOther=None):
        '''
        底层发送函数，生成规定消息格式
        :param msgType: 消息类型
        :param msgFrom: 消息发出者
        :param msgTo: 消息接收者
        :param msgOther: 消息内容
        :return:
        '''
        msg = {'msgType': msgType, 'msgFrom': msgFrom, 'msgTo': msgTo, 'time': time.strftime('%Y-%m-%d %H:%M:%S'),
               'msgOther': msgOther}
        msg = str(msg) + u'\x02\x02'
        print('>>:' + msg)
        self.mSocket.send(msg.encode())

    def errorHandle(self, errorMsg, isPrintTraceback=True):
        '''
        异常处理/记录
        :param errorMsg:自定义异常内容
        :param isPrintTraceback: 是否打印异常栈
        :return:
        '''
        print('【已捕获异常】', str(errorMsg))
        if (isPrintTraceback):
            traceback.print_exc()


if __name__ == '__main__':
    app = QApplication([])
    ui = Logic_Client()
    ui.show()
    app.exec_()
