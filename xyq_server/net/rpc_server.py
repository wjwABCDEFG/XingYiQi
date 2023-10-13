# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/24 21:36
@Author  : wenjiawei
"""


class RPCServer(object):
    def __init__(self):
        self.funcs = {}

    def rpc_call(self, func_name, func_args, func_kwargs):
        from net import rpc_views
        if hasattr(rpc_views, func_name):
            func = getattr(rpc_views, func_name)
            return func(*func_args, **func_kwargs)
        if hasattr(self, func_name):
            func = getattr(self, func_name)
            return func(*func_args, **func_kwargs)
        elif func_name in self.funcs:
            return self.funcs[func_name](*func_args, **func_kwargs)
        else:
            return '[404] Can not match function'

    def register_function(self, fn, name=None):
        """
        除了rpc_views中的方法会默认注册，也可以使用该方法主动注册任意函数
        """
        if name is None:
            name = fn.__name__
        self.funcs[name] = fn
