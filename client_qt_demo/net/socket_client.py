# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/22 22:29
@Author  : wenjiawei
"""
import socket
import threading


class SocketClient:

    def __init__(self, server_host='', server_port=0):
        self.connected = False
        self.s = None
        self.host, self.addr = '', 0
        self.server_host, self.server_port = server_host, server_port

    def start(self):
        self.init_client()
        threading.Thread(target=self.recv_msg, name='t-socket-recv').start()

    def init_client(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.server_host, self.server_port))
            self.s.setblocking(False)
            self.host, self.addr = self.s.getsockname()
        except Exception as e:
            raise Exception('连接服务器失败')

    @property
    def sender(self):
        return f'{self.host}:{self.addr}'

    def send(self, msg: str):
        self.s.send(msg.encode('utf-8'))

    def recv_msg(self):
        while True:
            # 接收消息
            try:
                # 接收小于 1024 字节的数据
                data = self.s.recv(1024)
                if not data:
                    continue
                msg = data.decode('utf-8')
                self.handle_msg(msg)
            except BlockingIOError as e:
                pass

    def handle_msg(self, msg: str):
        raise NotImplementedError
