# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/29 23:10
@Author  : wenjiawei
"""


def Singleton(cls):
    _instance = {}

    def inner(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return inner
