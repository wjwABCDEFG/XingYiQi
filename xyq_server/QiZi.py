# -*- coding: utf-8 -*-
"""
QiZi（棋子）
  0王
  1兵
"""
from collections import OrderedDict

from Pai import Pai
from common.Serializable import Serializable


class QiZi(Serializable):

    King    = 0
    Soldier = 1

    def __init__(self, pan: 'QiPan', pos: tuple, power: bool):
        super().__init__()
        self.role = -1
        self.pos = pos
        self.pai = None
        self.pan = pan
        self.power = power
        self.pan.add_chess(self)

    def set_pai(self, pai: Pai):
        # 每一轮都要set一次，牌不一样
        self.pai = pai

    def set_pos(self, pos):
        self.pos = pos

    def movable_list(self):
        """
        玩家点击时，显示可以走的位置
        注意要排除己方棋子的位置
        """
        pass

    def move(self, target: tuple):
        if self._is_movable(target):
            self.pos = target
            self.power = not self.power

    def _is_movable(self, target) -> bool:
        # x = target[0] - self.pos[0]
        # y = target[1] - self.pos[1]
        # offset_x = x + 2
        # offset_y = y + 2
        # return self.pai[offset_x][offset_y] == 1
        # TODO
        return True

    def serialize(self):
        return OrderedDict([
            ('id', self.id),
            ('pos', self.pos),
            ('camp', self.power),
            ('role', self.role),
        ])

    def deserialize(self, data: dict, hashmap: dict = {}, restore_id: bool = True) -> bool:
        pass


class King(QiZi):
    def __init__(self, pan, pos: tuple, power: bool):
        super().__init__(pan, pos, power)
        self.role = 0


class Soldier(QiZi):
    def __init__(self, pan, pos: tuple, power: bool):
        super().__init__(pan, pos, power)
        self.role = 1
