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

from QiZi import QiZi
from common.Exception import IllegalPosException, IllegalChessException
from common.Serializable import Serializable


class QiPan(Serializable):

    def __init__(self, game):
        super().__init__()
        self.matrix = [[None for j in range(5)] for i in range(5)]
        self.chess_list = []
        self.game = game

    def check(self, pos: tuple):
        return 0 <= pos[0] < len(self.matrix) and 0 <= pos[1] < len(self.matrix[0])

    def add_chess(self, chess):
        if self.pos(chess.pos[0], chess.pos[1]): raise IllegalPosException()
        self._set_pos(chess.pos[0], chess.pos[1], chess)
        self.chess_list.append(chess)

    def remove_chess(self, chess):
        if not self.pos(chess.pos[0], chess.pos[1]): raise IllegalPosException()
        self._set_pos(chess.pos[0], chess.pos[1], None)
        self.chess_list.remove(chess)

    def move_chess(self, chess, from_pos, to_pos):
        """
        若返回None，则没人赢，返回winner则有人赢
        :param chess:
        :param from_pos:
        :param to_pos:
        :return:
        """
        if not self.check(from_pos) or not self.check(to_pos): raise IllegalPosException()
        if tuple(chess.pos) != tuple(from_pos): raise IllegalChessException()
        self.remove_chess(chess)
        die_chess = self.pos(to_pos[0], to_pos[1])
        if die_chess:
            winner = self.who_is_winner(die_chess)
            if winner:
                # self.game.over(f"胜利者是{chess.power}")
                return winner
            else:
                self.remove_chess(to_pos)
        chess.move(to_pos)
        self.add_chess(chess)
        return None

    def pos(self, x, y) -> QiZi or None:
        if not self.check((x, y)): raise IllegalPosException()
        return self.matrix[x][y]

    def _set_pos(self, x, y, chess):
        if not self.check((x, y)): raise IllegalPosException()
        self.matrix[x][y] = chess

    def chess(self, chess_id):
        for chess in self.chess_list:
            if chess.id == chess_id:
                return chess
        raise IllegalChessException()

    def who_is_winner(self, die_chess: QiZi):
        if die_chess.role != QiZi.King: return None
        else: return not die_chess.power

    def show(self):
        print('=' * 50)
        for row in self.matrix:
            place_holder = []
            for item in row:
                if isinstance(item, QiZi):
                    char = '王' if item.role == 0 else '兵'
                else:
                    char = '口'
                place_holder.append(char)
            print(place_holder)
        print('=' * 50)

    def serialize(self) -> OrderedDict:
        chess_ser = list(map(lambda chess: chess.serialize(), self.chess_list))
        return OrderedDict([
            ('id', self.id),
            ('chess', chess_ser),
        ])
