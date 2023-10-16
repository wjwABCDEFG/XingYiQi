# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/30 1:10
@Author  : wenjiawei
"""
import views
from common.R import R
from net.msg import Msg
from net.rpc_server import RPCServer
from net.socket_server import SocketServer
from common.singleton import Singleton


@Singleton
class Server(SocketServer, RPCServer):

    def __init__(self):
        super().__init__()
        self.game_list = []

    def handle_msg(self, msg):
        msg = Msg.load(msg)
        # if msg.types == Msg.TYPE_LOGIN:
        #     self.client_info[msg.sender]['username'] = msg.data['username']
        #     self.send_to(self.client_info[msg.sender]['client'], Msg('登录成功', sender=self.sender))
        #
        # elif msg.types == Msg.TYPE_CHAT:
        #     # 群聊，私聊，群组
        #     # 格式为{'to': 'ALL', 'content': 'hello'}
        #     to = msg.data['to']
        #     if to == 'ALL':
        #         self.send_all(Msg(msg.data['content'], sender=self.sender))
        #     else:
        #         for key, info in self.client_info.items():
        #             if to != info['username']:
        #                 continue
        #             self.send_to(info['client'], Msg(msg.data['content'], sender=self.sender))

        if msg.types == Msg.TYPE_RPC:
            func_name = msg.data.get('func_name', '')
            func_args = msg.data.get('func_args', None)
            func_kwargs = msg.data.get('func_kwargs', None)
            callback = func_kwargs.pop('callback', None)
            res = self.rpc_call(func_name, func_args, func_kwargs)
            callback and res.update({'callback': callback})
            to = self.client_info[msg.sender]['client']
            self.send_to(to, Msg(res, types=Msg.TYPE_RPC, sender=self.sender).value)
        elif msg.types == Msg.TYPE_NORMAL:
            req = msg.data
            func = getattr(views, req['method'])
            func(self, req['params'])
            # self.send_all(msg.value)

    def test_rpc(self, user_id):
        return R().Data(f'{user_id}, welcome to rpc api').Dict()