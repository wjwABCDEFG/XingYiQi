# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/27 1:58
@Author  : wenjiawei
"""
import time

from net.msg import Msg
from net.rpc_client import RPCClient
from net.socket_client import SocketClient


class Client(SocketClient, RPCClient):

    def __init__(self, server_host='', server_port=0):
        super().__init__(server_host, server_port)
        self.game_id = None

    def handle_msg(self, msg: str):
        msg = Msg.load(msg)
        if msg.types == Msg.TYPE_RPC:
            callback = msg.data.pop('callback', None)
            if isinstance(callback, str):
                callback = getattr(self, callback)
            callback and callback(msg.data)
        else:
            print(msg.data)

    def match(self):
        self.send(Msg({'to': 'ALL',
                       'method': 'match',
                       'params': {'open_id': 123}},
                       types=Msg.TYPE_NORMAL,
                       sender=client.sender).value)  # 发送

    def begin(self):
        self.send(Msg({'to': 'ALL',
                       'method': 'begin',
                       'params': ''},
                      types=Msg.TYPE_NORMAL,
                      sender=client.sender).value)  # 发送


if __name__ == '__main__':
    client = Client('192.168.0.104', 9999)
    client.start()

    client.match()
    time.sleep(6)
    client.begin()
