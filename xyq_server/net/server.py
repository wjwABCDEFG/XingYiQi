# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/30 1:10
@Author  : wenjiawei
"""
import traceback

import views
from Hall import Hall
from common.R import R
from net.msg import Msg
from net.rpc_server import RPCServer
from net.socket_server import SocketServer
from common.singleton import Singleton


@Singleton
class Server(SocketServer):

    def __init__(self):
        SocketServer.__init__(self)
        self._rpc_server = RPCServer()
        self.hall = Hall(self)
        self.hall.start()

    def handle_msg(self, client, msg):
        to = None
        try:
            msg = Msg.load(msg)
            host, port = client.getpeername()
            msg.sender = f'{host}:{port}'
            to = self.client_info[msg.sender]['client']
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
                # func_kwargs.update({'server': self, 'client': to, 'types': 'RPC'})
                func = getattr(views, func_name)
                res = func(self, to, *func_args, **func_kwargs)
                if not res: res = {}
                callback and res.update({'callback': callback})
                self.send_to(to, Msg(res, types=Msg.TYPE_RPC, sender=self.sender).value)
            elif msg.types == Msg.TYPE_NORMAL:
                req = msg.data
                func = getattr(views, req['method'])
                func(self, to, **req['params'])
        except Exception as e:
            print(msg)
            traceback.print_exc()
            to and self.send_to(to, Msg(data={'code': 500, 'msg': str(e)}, types=Msg.TYPE_NORMAL, sender=self.sender).value)
