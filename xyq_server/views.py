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


def match(server, client, **kwargs):
    open_id = int(kwargs.get('open_id', None))
    server.hall.enter_hall(client)


def begin(server, client, **kwargs):
    types = kwargs.get('types', None)
    # game_id = int(params.get('game_id', None))
    # game = server.hall.get_game(game_id)
    player_id = int(kwargs.get('player_id', None))
    player = server.hall.get_player(player_id)

    game = player.game

    info = game.serialize()
    info['pai'] = list(map(lambda pai: pai.id, player.pai_list))
    resp = R().Data(info).Dict()
    types != 'RPC' and server.send_to(client, Msg(resp, sender=server.sender).value)
    DEBUG and print(resp)
    DEBUG and game.pan.show()
    return resp


def move(server, client, **kwargs):
    # game_id = int(kwargs.get('game_id', 0))
    player_id = int(kwargs.get('player_id', 0))
    chess_id = int(kwargs.get('chess_id', 0))
    from_pos = kwargs.get('from_pos', None)
    to_pos = kwargs.get('to_pos', None)

    # game = server.hall.get_game(game_id)
    game = server.hall.get_player(player_id).game
    chess = game.pan.chess(chess_id)
    winner = game.pan.move_chess(chess, from_pos, to_pos)
    if not winner:
        resp = R().Data(game.serialize()).Dict()
    else:
        resp = R().Data(f"胜利者是:{player_id}").Dict()

    for player in (game.player1, game.player2):
        server.send_to(player.client, Msg(resp, sender=server.sender).value)
    DEBUG and print(resp)
    DEBUG and game.pan.show()
    return resp


def over(server, client, params):
    return {}


def test(server, client, params):
    resp = R().Data("This is socket test msg...").Dict()
    server.send_all(Msg(resp, sender=server.sender).value)
    return resp
