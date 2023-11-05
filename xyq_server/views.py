# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/6 18:24
@Author  : wenjiawei
"""
# from Player import Player
from common.Exception import IllegalChessException
from common.R import R
from common.config import DEBUG
from net.msg import Msg


def match(server, client, params):
    open_id = int(params.get('open_id', None))
    # player = Player(client, open_id)
    server.hall.enter_hall(client)


def begin(server, client, params):
    game_id = int(params.get('game_id', None))
    game = server.hall.get_game(game_id)
    game.start(params)
    # resp = R().Data(info).Dict()
    # server.send_all(Msg(resp, sender=server.sender).value)
    # DEBUG and print(resp)
    # DEBUG and game.pan.show()
    # return resp


def move(server, client, params):
    game_id = int(params.get('game_id', 0))
    player_id = int(params.get('player_id', 0))
    chess_id = int(params.get('chess_id', 0))
    from_pos = eval(params.get('from_pos', None))
    to_pos = eval(params.get('to_pos', None))

    game = server.hall.get_game(game_id)
    chess = game.pan.chess(chess_id)
    if not chess: raise IllegalChessException()
    winner = game.pan.move_chess(chess, from_pos, to_pos)
    if not winner:
        resp = R().Data(game.serialize()).Dict()
    else:
        resp = R().Data(f"胜利者是:{player_id}").Dict()
    server.send_all(Msg(resp, sender=server.sender).value)
    DEBUG and print(resp)
    DEBUG and game.pan.show()
    return resp


def over(server, client, params):
    return {}


def test(server, client, params):
    resp = R().Data("This is socket test msg...").Dict()
    server.send_all(Msg(resp, sender=server.sender).value)
    return resp
