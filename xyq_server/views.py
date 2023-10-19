# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/6 18:24
@Author  : wenjiawei
"""
from Game import Game
from common.Exception import IllegalChessException
from common.R import R
from common.config import DEBUG
from net.msg import Msg

game = Game()


def match(request):
    return Game()


def begin(request, param):
    info = game.start(param)
    resp = R().Data(info).Dict()
    request.send_all(Msg(resp, sender=request.sender).value)
    DEBUG and print(resp)
    DEBUG and game.pan.show()
    return resp


def move(request, param):
    player_id = int(param.get('player_id', None))
    game_id = int(param.get('game_id', None))
    chess_id = int(param.get('chess_id', None))
    from_pos = eval(param.get('from_pos', None))
    to_pos = eval(param.get('to_pos', None))

    chess = game.pan.chess(chess_id)
    if not chess: raise IllegalChessException()
    winner = game.pan.move_chess(chess, from_pos, to_pos)
    if not winner:
        resp = R().Data(game.serialize()).Dict()
    else:
        resp = R().Data(f"胜利者是:{player_id}").Dict()
    request.send_all(Msg(resp, sender=request.sender).value)
    DEBUG and print(resp)
    DEBUG and game.pan.show()
    return resp


def over(request):
    return {}
