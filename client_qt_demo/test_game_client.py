# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/12 22:57
@Author  : wenjiawei
"""
import time

from net.msg import Msg
from net.rpc_client import RPCClient
from net.socket_client import SocketClient


class Client(SocketClient, RPCClient):
    def handle_msg(self, msg: str):
        msg = Msg.load(msg)
        if msg.types == Msg.TYPE_RPC:
            callback = msg.data.pop('callback', None)
            if isinstance(callback, str):
                callback = getattr(self, callback)
            callback and callback(msg.data)
        else:
            print(msg.data)

    def rpc_cb(self, resp):
        print('rpc_cb')
        print(resp['data'])

    def begin(self):
        self.send(Msg({'to': 'ALL',
                       'method': 'test',
                       'params': ''},
                       types=Msg.TYPE_NORMAL,
                       sender=client.sender).value)  # 发送


if __name__ == '__main__':
    client = Client('26.26.26.1', 9999)
    client.start()

    while True:
        client.begin()
        time.sleep(5)
