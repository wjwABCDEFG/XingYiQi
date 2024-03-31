# 暂时先不要这个对象，不维护player列表，只有socket列表
# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/6 17:53
@Author  : wenjiawei
所谓power,称为权,其实具体在游戏里就是阵营的意思,比如红蓝阵营
"""
from _socket import SocketType

from common.Serializable import Serializable
from common.db import g_mongo


class Player(Serializable):
    IDLE = 0
    WAITING = 1
    PLAYING = 2

    def __init__(self, client: SocketType = None, game: 'Game' = None, power: bool = None):
        super().__init__()
        self.client = client
        self.power = power
        self.game = game
        self.user_info = {}
        self.pai_list = []
        self.state = Player.IDLE

    def get_user_info(self, id):
        if not self.user_info:
            self.user_info = g_mongo.user.find_one({'open_id': id})
        return self.user_info

    @property
    def body(self):
        return {'state': self.state,
                'game_id': self.game.id,
                'player_id': self.id,
                'power': self.power}
