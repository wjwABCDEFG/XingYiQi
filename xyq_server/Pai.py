# -*- coding: utf-8 -*-
"""
Pai打出的牌
5 * 5
mask矩阵
"""
import json
import random
from collections import OrderedDict

from common.Serializable import Serializable


class PaiDui(Serializable):

    def __init__(self, game):
        super().__init__()
        self.player_card_num = 2     # 每个玩家的起始手牌
        self.game = game
        self.remain_list = []
        self.drop_list = []
        self._load()
        self.reset()

    def _load(self):
        pai_list = []
        with open("./pai.json") as f:
            self.pai_info = json.loads(f.read())
        for key, val in self.pai_info.items():
            pai_list.append(Pai(val, key))
        if len(pai_list) < 5:
            raise RuntimeError("牌库太少了，玩不了")
        self.remain_list = pai_list + pai_list

    def reset(self):
        if not self.remain_list and self.drop_list:
            self.remain_list = self.drop_list
        random.shuffle(self.remain_list)
        self.drop_list = []

    def deal_cards(self):
        """
        发牌给两个玩家
        """
        divide = [[], []]
        for i in range(2 * self.player_card_num):
            divide[i % 2].append(self.remain_list.pop())
        self.game.player1.pai_list = divide[0]
        self.game.player2.pai_list = divide[1]

    def take(self, player):
        """
        发牌机发牌给玩家
        """
        if not self.remain_list and self.drop_list:
            self.reset()
        pai = self.remain_list.pop()
        player.pai_list.append(pai)

    def drop(self, pai):
        """
        出牌，置入弃牌堆
        """
        self.drop_list.append(pai)

    def serialize(self) -> OrderedDict:
        return super().serialize()


class Pai(Serializable):

    def __init__(self, data, id='UntitledCard'):
        super().__init__()
        self.matrix = data
        self.id = id

    def check_pos(self, rel_vec) -> bool:
        """
        减产棋子落点是否符合牌型
        :param rel_vec: 相对位置
        :return:
        """
        return self.matrix[2 - rel_vec[0]][2 - rel_vec[1]] == 1

    def serialize(self) -> OrderedDict:
        return OrderedDict([
            ("id", self.id),
            ("info", self.matrix),
        ])

    def deserialize(self, data: dict, hashmap: dict = {}, restore_id: bool = True) -> bool:
        return super().deserialize(data, hashmap, restore_id)
