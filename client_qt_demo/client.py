# -*- coding: utf-8 -*-
"""
示例client，python实现
客户端需要把该部分和net部分翻译成gdscript
客户端实现的结构和这里不需要一致，能达到一样的效果即可（比如一般引擎gameplay中会有游戏主循环，handle_msg可以直接放在update函数中，便不需要socket client中的监听线程）
@Time    : 2023/11/6 23:50
@Author  : wenjiawei
"""
import json
import sys

from PySide6.QtWidgets import QApplication

from net.msg import Msg
from net.rpc_client import RPCClient
from net.socket_client import SocketClient
from ui import UIManager


class Client(SocketClient, RPCClient):
    def __init__(self, server_host='', server_port=0):
        SocketClient.__init__(self, server_host, server_port)
        self.ui = UIManager()
        self.bind_event()
        self.start()
        self.game_id = None
        self.player_id = None

    def handle_msg(self, msg: str):
        # 客户端要实现handle_msg，根据业务对msg进行处理
        msg = Msg.load(msg)

        # 日志，返回值打印到右侧ui展示区
        # print(msg.data)
        self.ui.main_window.text_area.append(json.dumps(msg.data, indent=4, ensure_ascii=False))
        self.ui.main_window.text_area.append('=' * 20)

        # 处理数据
        if msg.types == Msg.TYPE_RPC:
            callback = msg.data.pop('callback', None)
            if isinstance(callback, str):
                callback = getattr(self, callback)
            callback and callback(msg.data)
        else:
            resp = msg.data
            if 'state' in resp['data'] and resp['data']['state'] == 'MATCHED':
                self.game_id = resp['data']['game_id']
                self.player_id = resp['data']['player_id']

    def bind_event(self):
        self.ui.main_window.match_btn.clicked.connect(self.match)
        self.ui.main_window.start_btn.clicked.connect(self.enter)
        self.ui.main_window.move_btn.clicked.connect(lambda : self.move(int(self.ui.main_window.chess_text.text()),
                                                                        str(self.ui.main_window.pai_text.text()),
                                                                        eval(self.ui.main_window.from_text.text()),
                                                                        eval(self.ui.main_window.to_text.text())
                                                                        ))

    def match(self):
        """
        tcp示例，由于匹配不是立马返回，需要用tcp
        """
        self.send(Msg({'to': 'ALL',
                       'method': 'match',
                       'params': {'open_id': 123}},     # 微信小程序id，如果暂时没有，可以随意填
                       types=Msg.TYPE_NORMAL,
                       sender=self.sender).value)

    def enter(self):
        """
        rpc示例，获取游戏的棋盘内容，立马获取效果且不需要广播，可以用rpc或者tcp
        这个接口特地设计成tcp和rpc均可，其他接口是发tcp还是rpc以文档为准
        """
        # rpc写法
        self.begin(player_id=self.player_id)
        # tcp写法
        # self.send(Msg({'to': 'ALL',
        #                'method': 'begin',
        #                'params': {'player_id': self.player_id}},
        #               types=Msg.TYPE_NORMAL,
        #               sender=self.sender).value)

    def move(self, chess_id, pai_id, from_pos, to_pos):
        """
        移动棋子
        """
        self.send(Msg({'to': 'ALL',
                       'method': 'move',
                       'params': {
                           'player_id': self.player_id,
                           'chess_id': chess_id,
                           'pai_id': pai_id,
                           'from_pos': from_pos,
                           'to_pos': to_pos
                       }},
                      types=Msg.TYPE_NORMAL,
                      sender=self.sender).value)


if __name__ == '__main__':
    app = QApplication([])
    Client('192.168.0.104', 9999)
    sys.exit(app.exec())
