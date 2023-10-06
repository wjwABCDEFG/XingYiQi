# -*- coding: utf-8 -*-
"""
QiPan:
    5*5二维数组

Pai
  5 * 5
  mask矩阵


power
  0蓝 1红
@Time    : 2023/10/6 13:54
@Author  : wenjiawei
"""


class QiPan:

    def __init__(self, game):
        self.matrix = [[0 for j in range(5)] for i in range(5)]
        self.game = game

    def check(self, pos: tuple):
        return 0 <= pos[0] < len(self.matrix) and 0 <= pos[1] < len(self.matrix[0])

    # def add_chess(self, pos, chess):
    #     if self.matrix[pos[0]][pos[1]]:
    #         if self.matrix[pos[0]][pos[1]].is_win():
    #             self.game.over(f"胜利者是{chess.power}")
    #     self.matrix[pos[0]][pos[1]] = chess
    #
    # def remove_chess(self, pos):
    #     if self.matrix[pos[0]][pos[1]]:
    #         self.matrix[pos[0]][pos[1]] = 0
    #
    # def move_chess(self, from_pos, to_pos, chess):
    #     self.remove_chess(from_pos)
    #     self.add_chess(to_pos, chess)
