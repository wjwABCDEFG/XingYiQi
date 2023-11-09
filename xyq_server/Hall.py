# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/23 0:05
@Author  : wenjiawei
"""
import threading
from queue import Queue, Empty

from Game import Game
from Player import Player
from common.Exception import GameNotFoundException, PlayerNotFoundException
from common.R import R
from common.singleton import Singleton
from net.msg import Msg
from state import State


@Singleton
class Hall:
    def __init__(self, server: 'Server'):
        self.server = server
        self.games = {}
        self.players = {}
        self._queue = Queue()
        self.waiting = []

    def enter_hall(self, player):
        self._queue.put(player)

    def start(self):
        threading.Thread(target=self.process).start()

    def process(self):
        while True:
            try:
                player = self._queue.get(block=False)
                self.waiting.append(player)
                if len(self.waiting) == 2:
                    game = Game(self.server)
                    player1 = Player(self.waiting[0], game, None, power=True)
                    player2 = Player(self.waiting[1], game, None, power=False)
                    game.player1 = player1
                    game.player2 = player2
                    self.players[player1.id] = player1
                    self.players[player2.id] = player2
                    self.games[game.id] = game
                    self.waiting = []
                    game.start(game.id)    # 游戏开始逻辑移到这里，匹配成功就开始
                    self.server.send_to(player1.client, Msg(R().Data({'state': State.MATCHED, 'game_id': game.id, 'player_id': player1.id}).Dict()).value)
                    self.server.send_to(player2.client, Msg(R().Data({'state': State.MATCHED, 'game_id': game.id, 'player_id': player2.id}).Dict()).value)
            except Empty as e:
                pass

    def get_game(self, game_id):
        if game_id not in self.games:
            raise GameNotFoundException()
        return self.games[game_id]

    def get_player(self, player_id):
        if player_id not in self.players:
            raise PlayerNotFoundException()
        return self.players[player_id]
