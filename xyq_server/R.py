# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/7 19:56
@Author  : wenjiawei
"""
import json


class R:
    def __init__(self, code=200, msg='', data=None):
        self._code = code
        self._msg = msg
        self._data = data

    def code(self, code=0):
        self._code = code
        return self

    def msg(self, msg=''):
        self._msg = msg
        return self

    def data(self, data=None):
        self._data = data
        return self

    def json(self):
        attr = self.__dict__
        return json.dumps(attr)
