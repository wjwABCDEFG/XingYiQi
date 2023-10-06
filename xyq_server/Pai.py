# -*- coding: utf-8 -*-
"""
5 * 5
mask矩阵
"""
import random


class PaiDui:

    def __init__(self, pai_list):
        if len(pai_list) < 5:
            raise RuntimeError("牌库太少了，玩不了")
        self.remain_list = []
        self.drop_list = []
        self.reset(pai_list)
        self.begin()

    def reset(self, pai_list):
        self.remain_list = pai_list
        random.shuffle(self.remain_list)
        self.drop_list = []

    def begin(self):
        """
        发牌给两个玩家
        """
        res = [[], []]
        for i in range(4):
            item = self.remain_list.pop(random.randrange(len(self.remain_list)))
            res[i % 2].append(item)
        return res

    def take(self):
        if not self.remain_list and self.drop_list:
            self.reset(self.drop_list)
        return self.remain_list.pop()

    def drop(self, pai):
        self.drop_list.append(pai)


class Pai:
    def __init__(self):
        self.matrix = [[0 for j in range(5)] for i in range(5)]


class Pai1(Pai):
    def __init__(self):
        super().__init__()
        self.matrix = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]


class Pai2(Pai):
    def __init__(self):
        super().__init__()
        self.matrix = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]]


class Pai3(Pai):
    def __init__(self):
        super().__init__()
        self.matrix = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0]]


class Pai4(Pai):
    def __init__(self):
        super().__init__()
        self.matrix = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0]]


class Pai5(Pai):
    def __init__(self):
        super().__init__()
        self.matrix = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]]
