# -*- coding: utf-8 -*-
"""
QiZi
  0王
  1兵
"""
from Pai import Pai


class QiZi:
    def __init__(self, pan, pos: tuple, power: bool):
        self.role = -1
        self.pos = pos
        self.pai = None
        self.pan = pan
        self.power = power

    def set_pai(self, pai: Pai):
        # 每一轮都要set一次，牌不一样
        self.pai = pai

    def movable_list(self):
        """
        玩家点击时，显示可以走的位置
        """
        pass

    def move(self, target: tuple):
        if self._is_movable(target):
            self.pos = target
            self.power = not self.power

    def _is_movable(self, target) -> bool:
        x = target[0] - self.pos[0]
        y = target[1] - self.pos[1]
        offset_x = x + 2
        offset_y = y + 2
        return self.pai[offset_x][offset_y] == 1

    def is_win(self):
        return self.role == 1


class King(QiZi):
    def __init__(self, pan, pos: tuple, power: bool):
        super().__init__(pan, pos, power)
        self.role = 0


class Soldier(QiZi):
    def __init__(self, pan, pos: tuple, power: bool):
        super().__init__(pan, pos, power)
        self.role = 1
