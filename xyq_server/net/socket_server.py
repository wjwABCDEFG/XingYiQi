# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/22 0:37
@Author  : wenjiawei
"""

import socket
import traceback

from net.msg import Msg

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
BUFFSIZE = 1024  # 定义一次从socket缓冲区最多读入1024个字节


class SocketServer:

    def __init__(self):
        self.server_socket = None
        self.client_list = []       # socket_client对象
        self.client_info = {}       # 为了方便根据ip查找，key:ip:addr, value:{ip: ip, port: addr, client: socket_client对象}

    def start(self):
        self.init_server()

        while True:
            # 等待客户端连接
            self.accept_all()
            # 接收消息
            self.recv_all()

    def init_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen(5)
        self.server_socket.setblocking(False)
        print(f"Server is running at {HOST}:{PORT}...")

    def accept_all(self):
        try:
            client_socket, addr = self.server_socket.accept()
            client_socket.setblocking(False)
            print("新连接: %s" % str(addr))
            self.client_list.append(client_socket)
            ip, addr = client_socket.getpeername()
            self.client_info[f'{ip}:{addr}'] = {'ip': ip, 'port': addr, 'client': client_socket}
            self.send_to(client_socket, Msg("{'code': 200, 'data': 'connect server success', 'msg': ''}").value)
        except BlockingIOError as e:
            # accept的非阻塞异常
            pass

    def recv_all(self):
        for client_socket in self.client_list:
            try:
                data = client_socket.recv(BUFFSIZE)
                if not data:
                    continue
                msg = data.decode('utf-8')
                print(f'接收数据：{msg}')
                self.handle_msg(msg)
            except BlockingIOError as e:
                pass
            except ConnectionResetError as e:
                print(f"{client_socket.getpeername()}离开了")
                self.offline(client=client_socket)
            except Exception as e:
                print("可能是for循环里面remove连接出错了")
                traceback.print_exc()

    def send_all(self, msg: str):
        for client_socket in self.client_list:
            try:
                self.send_to(client_socket, msg)
            except Exception as e:
                print(f'用户{client_socket.getpeername()}断线了')
                self.offline(client=client_socket)

    def send_to(self, client, msg: str):
        key = self.get_client_key(client)
        if key not in self.client_info:
            # TODO 如果离线消息要保留，要在这里加入离线消息队列
            print('对方已离线')
            return
        try:
            client.send(msg.encode())
        except Exception as e:
            print('用户断线了')
            self.offline(info=key)

    def offline(self, client=None, info=''):
        # TODO 要发给他的好友，离线通知
        if client:
            self.client_list.remove(client)
            self.client_info.pop(self.get_client_key(client))
            return
        if info:
            info = self.client_info.pop(info)
            self.client_list.remove(info['client'])
            return

    def handle_msg(self, msg: str):
        raise NotImplementedError

    def get_client_key(self, client):
        if not client: return None
        ip, addr = client.getpeername()
        return f'{ip}:{addr}'

    @property
    def sender(self):
        return f'{HOST}:{PORT}'
