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


class IllegalChessException(Exception):
    def __init__(self, msg=""):
        self.msg = msg

    def __str__(self):
        print("非法棋子")


class GameNotFoundException(Exception):
    def __init__(self, msg=""):
        self.msg = msg

    def __str__(self):
        print("房间不存在")


class PlayerNotFoundException(Exception):
    def __init__(self, msg=""):
        self.msg = msg

    def __str__(self):
        print("玩家不存在")
