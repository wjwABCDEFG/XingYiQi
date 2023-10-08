# -*- coding: utf-8 -*-
"""
QiZi（棋子）
  0王
  1兵
"""
from collections import OrderedDict

from Pai import Pai
from Serializable import Serializable


class QiZi(Serializable):

    def __init__(self, pan, pos: tuple, power: bool):
        super().__init__()
        self.role = -1
        self.pos = pos
        self.pai = None
        self.pan = pan
        self.power = power
        self.add_chess(pos, self)

    def set_pai(self, pai: Pai):
        # 每一轮都要set一次，牌不一样
        self.pai = pai

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
        x = target[0] - self.pos[0]
        y = target[1] - self.pos[1]
        offset_x = x + 2
        offset_y = y + 2
        return self.pai[offset_x][offset_y] == 1

    def is_win(self):
        return self.role == 1

    def add_chess(self, pos, chess):
        if self.pan.pos(pos[0], pos[1]) and self.pan.pos(pos[0], pos[1]).is_win():
            self.pan.game.over(f"胜利者是{chess.power}")
        self.pan.add_chess_to_pan(chess)

    def remove_chess(self, pos):
        if self.pan.pos(pos[0], pos[1]):
            self.pan.set_pos(pos[0], pos[1], 0)

    def move_chess(self, from_pos, to_pos, chess):
        self.remove_chess(from_pos)
        self.add_chess(to_pos, chess)
        self.move(to_pos)

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
