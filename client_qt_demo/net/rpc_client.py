# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/24 21:42
@Author  : wenjiawei
"""
from net.msg import Msg


class RPCClient(object):
    def __getattr__(self, item):
        def func(*args, **kwargs):
            stub = {
                'func_name': item,
                'func_args': args,
                'func_kwargs': kwargs
            }
            self.send(Msg(stub, Msg.TYPE_RPC, sender=self.sender).value)

        setattr(self, item, func)
        return func
