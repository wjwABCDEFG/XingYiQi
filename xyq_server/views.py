# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/6 18:24
@Author  : wenjiawei
"""
from Game import Game
from common.R import R
from net.msg import Msg

game = Game()


def match(request):
    return Game()


def begin(request, param):
    info = game.start(param)
    resp = R().Data(info).Dict()
    request.send_all(Msg(resp, sender=request.sender).value)
    return resp


def play(request):
    return {}


def over(request):
    return {}
