# -*- coding: utf-8 -*-
"""
QiPan棋盘:
5*5二维数组

power
  0蓝 1红
@Time    : 2023/10/6 13:54
@Author  : wenjiawei
"""
from Exception import IllegalPosException


class QiPan:

    def __init__(self, game):
        self.matrix = [[0 for j in range(5)] for i in range(5)]
        self.chess_list = []
        self.game = game

    def check(self, pos: tuple):
        return 0 <= pos[0] < len(self.matrix) and 0 <= pos[1] < len(self.matrix[0])

    def add_chess_to_pan(self, chess):
        self.chess_list.append(chess)

    def pos(self, x, y):
        if not self.check((x, y)): raise IllegalPosException()
        return self.matrix[x][y]

    def set_pos(self, x, y, chess):
        if not self.check((x, y)): raise IllegalPosException()
        self.matrix[x][y] = chess