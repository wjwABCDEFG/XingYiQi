# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/18 23:17
@Author  : wenjiawei
"""
import json
import string
import traceback

from common.Exception import MsgFormatException


class Msg:
    TYPE_OFFLINE = -1
    TYPE_LOGIN = 0
    TYPE_NORMAL = 1     # 发送给服务器
    TYPE_CHAT = 2       # 发送给用户，例如广播，群聊，私聊
    TYPE_RPC = 3        # rpc类消息

    def __init__(self, data, types=1, sender=''):
        self.data = data
        self.types = types
        self.sender = sender

    def __str__(self):
        return self.value

    @property
    def value(self):
        return json.dumps({'types': self.types,
                           'data': self.data,
                           'sender': self.sender})

    @property
    def body(self):
        return {'types': self.types,
                'data': self.data,
                'sender': self.sender}

    @classmethod
    def load(cls, val: string):
        try:
            info = json.loads(val)
            return Msg(info['data'], info['types'], info['sender'])
        except Exception as e:
            traceback.print_exc()
            raise MsgFormatException()
