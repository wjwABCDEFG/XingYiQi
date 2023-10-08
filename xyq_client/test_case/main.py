# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/9 0:56
@Author  : wenjiawei
"""
from msg import Msg
from socket_client import SocketClient

if __name__ == '__main__':
    s_client = SocketClient()
    s_client.start()                                                                            # socket连接
    user = f'{s_client.host}:{s_client.addr}'                                                   # 玩家信息
    s_client.send(Msg({'username': 'wenjiawei'}, types=Msg.TYPE_LOGIN, sender=user))            # 登录
    s_client.send(Msg({'to': 'ALL',
                       'method': 'begin',
                       'param': {
                           'player1': 'wenjiawei',
                           'player2': 'chenzilve'
                       }},
                      types=Msg.TYPE_NORMAL,
                      sender=user))                                                             # 发送
    pass
