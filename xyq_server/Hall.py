# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/23 0:05
@Author  : wenjiawei
"""
import threading
from queue import Queue, Empty

from _socket import SocketType

from Game import Game
from Player import Player
from common.Exception import GameNotFoundException, PlayerNotFoundException, PlayerReEntryException
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

    def line_up(self, client: SocketType):
        """
        排队
        :param client:
        :return:
        """
        # TODO 这里下面两句应该在更早的地方，一连接就进入idle和加入players，line_up只是变成waiting状态和加入等待队列
        player = Player(client)
        self.players[player.id] = player
        player.state = Player.WAITING
        self._queue.put(player)

    def start(self):
        threading.Thread(target=self.process).start()

    def process(self):
        while True:
            try:
                if self._queue.qsize() >= 2:
                    player1 = self._queue.get()
                    player2 = self._queue.get()
                    game = Game(self.server, player1, player2)
                    game.start()    # 游戏开始逻辑移到这里，匹配成功就开始
                    self.games[game.id] = game
                    self.server.send_to(player1.client, Msg(R().Data(player1.body).Dict()).value)
                    self.server.send_to(player2.client, Msg(R().Data(player2.body).Dict()).value)
            except Empty:
                pass

    def get_game(self, game_id):
        if game_id not in self.games:
            raise GameNotFoundException()
        return self.games[game_id]

    def get_player(self, player_id):
        if player_id not in self.players:
            raise PlayerNotFoundException()
        return self.players[player_id]
