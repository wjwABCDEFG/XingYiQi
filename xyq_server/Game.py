# -*- coding: utf-8 -*-
"""
游戏全局规则，对应菜单栏
@Time    : 2023/10/6 16:03
@Author  : wenjiawei
"""
import random
from collections import OrderedDict

from _socket import SocketType

from Pai import PaiDui
from Player import Player
from QiPan import QiPan
from QiZi import Soldier, King
from common.Serializable import Serializable


class Game(Serializable):

    def __init__(self, server: SocketType, player1: Player, player2: Player):
        super().__init__()
        self.server = server
        self.pan = None
        self.paidui = None
        self.player1 = player1
        self.player2 = player2
        self.power = True
        self._init_state()

    def _init_state(self):
        self.player1.game = self
        self.player1.state = Player.PLAYING
        self.player2.game = self
        self.player2.state = Player.PLAYING
        random_first = random.choice([True, False])
        self.player1.power = random_first
        self.player2.power = not random_first

    def start(self):
        print(f"游戏开始 {self.id}")

        # 初始化棋盘
        pan = QiPan(self)
        self.pan = pan

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

        # 初始化牌堆
        self.paidui = PaiDui(self)
        self.paidui.deal_cards()

    def pause(self):
        print(f"游戏暂停 {self.id}")

    def over(self):
        print(f"游戏结束 {self.id}")

    def get_player(self, player_id):
        if self.player1.id == player_id:
            return self.player1
        else:
            return self.player2

    def get_cur_player(self):
        if self.player1.power == self.power:
            return self.player1
        else:
            return self.player2

    def serialize(self):
        return OrderedDict([
            ('id', self.id),
            ("game_id", self.id),
            ("pan", self.pan.serialize()),
            ("pai", []),      # 游戏设置成仅返回用户自己的牌，防止作弊，在serialize后各自再补全该参数
        ])
