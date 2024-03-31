# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/6 18:24
@Author  : wenjiawei
"""
from Pai import Pai
# from Player import Player
from common.Exception import IllegalChessException, IllegalPosException, TurnException
from common.R import R
from common.config import DEBUG
from net.msg import Msg
from net.rpc_server import rpc_view


def match(server, client, *args, **kwargs):
    open_id = int(kwargs.get('open_id', None))
    server.hall.line_up(client)


@rpc_view()
def begin(server, client, *args, **kwargs):
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


def move(server, client, *args, **kwargs):
    # game_id = int(kwargs.get('game_id', 0))
    player_id = int(kwargs.get('player_id', 0))
    pai_id = str(kwargs.get('pai_id', ''))
    chess_id = int(kwargs.get('chess_id', 0))
    from_pos = kwargs.get('from_pos', None)
    to_pos = kwargs.get('to_pos', None)

    # game = server.hall.get_game(game_id)
    player = server.hall.get_player(player_id)
    game = player.game

    if game.power != player.power: raise TurnException()

    # 检查落点
    pai = Pai(game.paidui.pai_info[pai_id], pai_id)
    can_move = pai.check_pos((to_pos[0] - from_pos[0], to_pos[1] - from_pos[1]))
    if not can_move: raise IllegalPosException()

    # 移动棋子
    chess = game.pan.chess(chess_id)
    winner = game.pan.move_chess(chess, from_pos, to_pos)

    if winner:
        info = f"胜利者是:{player_id}"
    else:
        game.paidui.drop(pai)                       # 置入弃牌堆
        game.power = not game.power                 # 交换权
        game.paidui.take(game.get_cur_player())     # 发牌
        info = game.serialize()

    for player in (game.player1, game.player2):
        resp = R().Data(game.serialize()).Dict()
        if not winner:
            info['pai'] = list(map(lambda item: item.id, player.pai_list))
        server.send_to(player.client, Msg(resp, sender=server.sender).value)
    DEBUG and print(resp)
    DEBUG and game.pan.show()
    return resp
