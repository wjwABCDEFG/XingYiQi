# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/23 0:05
@Author  : wenjiawei
"""
import threading
from queue import Queue, Empty

from Game import Game
from Player import Player
from common.Exception import GameNotFoundException
from common.R import R
from common.singleton import Singleton
from net.msg import Msg
from state import State


@Singleton
class Hall:
    def __init__(self, server: 'Server'):
        self.server = server
        self.games = {}
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
                    # game.player1 = self.waiting[0]
                    # game.player2 = self.waiting[1]
                    game.player1 = Player(self.waiting[0], None, power=True)
                    game.player2 = Player(self.waiting[1], None, power=False)
                    self.waiting = []
                    self.games[game.id] = game
                    self.server.send_to(game.player1.client, Msg(R().Data({'state': State.MATCHED, 'game_id': game.id}).Dict()).value)
                    self.server.send_to(game.player2.client, Msg(R().Data({'state': State.MATCHED, 'game_id': game.id}).Dict()).value)
            except Empty as e:
                pass

    def get_game(self, game_id):
        if game_id not in self.games:
            raise GameNotFoundException()
        return self.games[game_id]
