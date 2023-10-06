# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/6 16:03
@Author  : wenjiawei
"""


class Game:
    def __init__(self):
        pass

    def start(self, msg=None):
        print(f"游戏开始 {msg}")

    def pause(self, msg=None):
        print(f"游戏暂停 {msg}")

    def over(self, msg=None):
        print(f"游戏结束 {msg}")
