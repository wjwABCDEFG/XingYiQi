# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/7 23:25
@Author  : wenjiawei
"""


class MsgFormatException(Exception):
    def __init__(self, msg=""):
        self.msg = msg

    def __str__(self):
        return "消息格式错误" + self.msg


class IllegalPosException(Exception):
    def __init__(self, msg=""):
        self.msg = msg

    def __str__(self):
        return "棋子不可以在此位置" + self.msg


class IllegalChessException(Exception):
    def __init__(self, msg=""):
        self.msg = msg

    def __str__(self):
        return "非法棋子" + self.msg


class GameNotFoundException(Exception):
    def __init__(self, msg=""):
        self.msg = msg

    def __str__(self):
        return "房间不存在" + self.msg


class PlayerNotFoundException(Exception):
    def __init__(self, msg=""):
        self.msg = msg

    def __str__(self):
        return "玩家不存在" + self.msg


class PlayerReEntryException(Exception):
    def __init__(self, msg=""):
        self.msg = msg

    def __str__(self):
        return "玩家已经在排队中" + self.msg


class TurnException(Exception):
    def __init__(self, msg=""):
        self.msg = msg

    def __str__(self):
        return "不是您的回合，无法移动棋子" + self.msg
