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
            pai_info = json.loads(f.read())
        for key, val in pai_info.items():
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

    def take(self):
        """
        出牌
        """
        if not self.remain_list and self.drop_list:
            self.reset()
        top = self.remain_list.pop()
        self.drop_list.append(top)
        return top

    def serialize(self) -> OrderedDict:
        return super().serialize()


class Pai(Serializable):

    def __init__(self, data, name='UntitledCard'):
        super().__init__()
        self.name = name
        self.matrix = data

    def serialize(self) -> OrderedDict:
        return OrderedDict([
            ("info", self.matrix),
        ])

    def deserialize(self, data: dict, hashmap: dict = {}, restore_id: bool = True) -> bool:
        return super().deserialize(data, hashmap, restore_id)


if __name__ == '__main__':
    paidui = PaiDui()
