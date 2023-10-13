# -*- coding: utf-8 -*-
"""
QiPan棋盘:
5*5二维数组

power
  0蓝 1红
@Time    : 2023/10/6 13:54
@Author  : wenjiawei
"""
from collections import OrderedDict

from common.Exception import IllegalPosException
from common.Serializable import Serializable


class QiPan(Serializable):

    def __init__(self, game):
        super().__init__()
        self.matrix = [[0 for j in range(5)] for i in range(5)]
        self.chess_list = []
        self.game = game

    def check(self, pos: tuple):
        return 0 <= pos[0] < len(self.matrix) and 0 <= pos[1] < len(self.matrix[0])

    def add_chess_to_pan(self, chess):
        self.set_pos(chess.pos[0], chess.pos[1], chess)
        self.chess_list.append(chess)

    def pos(self, x, y):
        if not self.check((x, y)): raise IllegalPosException()
        return self.matrix[x][y]

    def set_pos(self, x, y, chess):
        if not self.check((x, y)): raise IllegalPosException()
        self.matrix[x][y] = chess

    def serialize(self) -> OrderedDict:
        chess_ser = list(map(lambda chess: chess.serialize(), self.chess_list))
        return OrderedDict([
            ('id', self.id),
            ('chess', chess_ser),
        ])
