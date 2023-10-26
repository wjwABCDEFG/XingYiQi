# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/23 0:05
@Author  : wenjiawei
"""
import threading
from queue import Queue, Empty

from Game import Game
from common.Exception import GameNotFoundException
from common.R import R
from common.singleton import Singleton
from net.msg import Msg


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
                    game = Game()
                    game.player1 = self.waiting[0]
                    game.player2 = self.waiting[1]
                    self.waiting = []
                    self.games[game.id] = game
                    self.server.send_to(game.player1, Msg(R().Data({'game_id': game.id}).Dict()).value)
                    self.server.send_to(game.player2, Msg(R().Data({'game_id': game.id}).Dict()).value)
            except Empty as e:
                pass

    def get_game(self, game_id):
        if game_id not in self.games:
            raise GameNotFoundException()
        return self.games[game_id]
