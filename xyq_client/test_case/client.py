# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/9 1:41
@Author  : wenjiawei
"""
from test_case.msg import Msg
from test_case.socket_client import SocketClient


class Client(SocketClient):
    def handle_msg(self, msg: Msg):
        if msg.types == Msg.TYPE_RPC:
            callback = msg.data.pop('callback', None)
            if isinstance(callback, str):
                callback = getattr(self, callback)
            callback and callback(**msg.data)
        else:
            print(msg)
