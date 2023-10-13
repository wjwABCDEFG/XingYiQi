# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/7 23:25
@Author  : wenjiawei
"""


class IllegalPosException(Exception):
    def __init__(self, msg=""):
        self.msg = msg

    def __str__(self):
        print("棋子不可以在此位置")
