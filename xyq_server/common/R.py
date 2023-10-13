# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/7 19:56
@Author  : wenjiawei
"""
import json


class R:
    def __init__(self, code=200, msg='', data=None):
        self.code = code
        self.msg = msg
        self.data = data

    def Code(self, code=0):
        self.code = code
        return self

    def Msg(self, msg=''):
        self.msg = msg
        return self

    def Data(self, data=None):
        self.data = data
        return self

    def Json(self):
        attr = self.__dict__
        return json.dumps(attr)

    def Dict(self):
        return self.__dict__
