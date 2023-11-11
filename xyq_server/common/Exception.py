# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/7 23:25
@Author  : wenjiawei
"""


class MsgFormatException(Exception):
    def __init__(self, msg=""):
        self.msg = msg

    def __str__(self):
        return "消息格式错误"


class IllegalPosException(Exception):
    def __init__(self, msg=""):
        self.msg = msg

    def __str__(self):
        return "棋子不可以在此位置"


class IllegalChessException(Exception):
    def __init__(self, msg=""):
        self.msg = msg

    def __str__(self):
        return "非法棋子"


class GameNotFoundException(Exception):
    def __init__(self, msg=""):
        self.msg = msg

    def __str__(self):
        return "房间不存在"


class PlayerNotFoundException(Exception):
    def __init__(self, msg=""):
        self.msg = msg

    def __str__(self):
        return "玩家不存在"


class TurnException(Exception):
    def __init__(self, msg=""):
        self.msg = msg

    def __str__(self):
        return "不是您的回合，无法移动棋子"
