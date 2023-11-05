# -*- coding: utf-8 -*-
"""
游戏全局规则，对应菜单栏
@Time    : 2023/10/6 16:03
@Author  : wenjiawei
"""
from collections import OrderedDict

from Pai import PaiDui
from QiPan import QiPan
from QiZi import Soldier, King
from common.R import R
from common.Serializable import Serializable
from net.msg import Msg


class Game(Serializable):

    def __init__(self, server):
        super().__init__()
        self.server = server
        self.pan = None
        self.paidui = None
        self.player1 = None
        self.player2 = None

    def start(self, msg=None):
        print(f"游戏开始 {msg}")

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

        # 返回给客户端，很多时候由于发给两个客户端的消息是不同的，不能统一返回，提到这一层来
        common_info = self.serialize()
        for player in [self.player1, self.player2]:
            common_info['pai'] = list(map(lambda pai: pai.id, player.pai_list))
            resp = R().Data(common_info).Dict()
            self.server.send_to(player.client, Msg(resp, sender=self.server.sender).value)

    def pause(self, msg=None):
        print(f"游戏暂停 {msg}")

    def over(self, msg=None):
        print(f"游戏结束 {msg}")

    def serialize(self):
        return OrderedDict([
            ('id', self.id),
            ("game_id", self.id),
            ("pan", self.pan.serialize()),
        ])
