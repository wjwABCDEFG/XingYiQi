# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/6 16:03
@Author  : wenjiawei
"""
from QiPan import QiPan
from QiZi import Soldier, King


class Game:
    def __init__(self):
        pass

    def start(self, msg=None):
        print(f"游戏开始 {msg}")

        # 初始化棋盘
        pan = QiPan(self)

        # 初始化双方棋子
        King(pan, (0, 2), False)
        Soldier(pan, (0, 0), False)
        Soldier(pan, (0, 1), False)
        Soldier(pan, (0, 3), False)
        Soldier(pan, (0, 4), False)

        King(pan, (4, 2), True)
        Soldier(pan, (4, 0), True)
        Soldier(pan, (4, 1), True)
        Soldier(pan, (4, 3), True)
        Soldier(pan, (4, 4), True)

        pass

    def pause(self, msg=None):
        print(f"游戏暂停 {msg}")

    def over(self, msg=None):
        print(f"游戏结束 {msg}")
