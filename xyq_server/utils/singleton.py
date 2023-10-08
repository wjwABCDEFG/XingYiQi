# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/29 23:10
@Author  : wenjiawei
"""


def Singleton(cls):
    _instance = {}

    def inner(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return inner
