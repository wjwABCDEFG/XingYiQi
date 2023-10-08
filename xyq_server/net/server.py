# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/30 1:10
@Author  : wenjiawei
"""
import views
from R import R
from net.msg import Msg
# from net.rpc_server import RPCServer
from net.socket_server import SocketServer
from utils.singleton import Singleton


@Singleton
# class Server(SocketServer, RPCServer):
class Server(SocketServer):

    def handle_msg(self, msg):
        if msg.types == Msg.TYPE_LOGIN:
            self.client_info[msg.sender]['username'] = msg.data['username']
            self.send_to(self.client_info[msg.sender]['client'], Msg('登录成功', sender=self.sender))

        elif msg.types == Msg.TYPE_CHAT:
            # 群聊，私聊，群组
            # 格式为{'to': 'ALL', 'content': 'hello'}
            to = msg.data['to']
            if to == 'ALL':
                self.send_all(Msg(msg.data['content'], sender=self.sender))
            else:
                for key, info in self.client_info.items():
                    if to != info['username']:
                        continue
                    self.send_to(info['client'], Msg(msg.data['content'], sender=self.sender))

        elif msg.types == Msg.TYPE_RPC:
            func_name = msg.data.get('func_name', '')
            func_args = msg.data.get('func_args', None)
            func_kwargs = msg.data.get('func_kwargs', None)
            callback = func_kwargs.pop('callback', None)
            res = self.rpc_call(func_name, func_args, func_kwargs)
            data = {'user_list': res}
            callback and data.update({'callback': callback})
            to = self.client_info[msg.sender]['client']
            self.send_to(to, Msg(data, types=Msg.TYPE_RPC, sender=self.sender))

        elif msg.types == Msg.TYPE_NORMAL:
            data = views.begin()
            res = R().Data(data).Json()
            to = self.client_info[msg.sender]['client']
            self.send_to(to, Msg(res, types=Msg.TYPE_NORMAL, sender=self.sender))
