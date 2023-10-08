# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/22 22:29
@Author  : wenjiawei
"""
import socket
import threading

from msg import Msg

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999


class SocketClient:

    def __init__(self):
        self.connected = False
        self.s = None
        self.host, self.addr = '', 0

    def start(self):
        self.init_client()
        threading.Thread(target=self.recv_msg, name='t-socket-recv').start()

    def init_client(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((HOST, PORT))
            self.s.setblocking(False)
            self.host, self.addr = self.s.getsockname()
        except Exception as e:
            print('连接服务器失败')

    @property
    def sender(self):
        return f'{self.host}:{self.addr}'

    def send(self, msg: Msg):
        self.s.send(msg.value.encode('utf-8'))

    def recv_msg(self):
        while True:
            # 接收消息
            try:
                # 接收小于 1024 字节的数据
                data = self.s.recv(1024)
                if not data:
                    continue
                msg = data.decode('utf-8')
                msg = Msg.load(msg)
                self.handle_msg(msg)
            except BlockingIOError as e:
                pass

    def handle_msg(self, msg: Msg):
        raise NotImplementedError
