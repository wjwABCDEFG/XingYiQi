# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/24 21:36
@Author  : wenjiawei
"""
from typing import Callable, NoReturn

from common.singleton import Singleton


@Singleton
class RPCServer(object):
    def __init__(self):
        self.funcs = {}

    def rpc_call(self, func_name: str, func_args, func_kwargs):
        if hasattr(self, func_name):
            func = getattr(self, func_name)
            return func(*func_args, **func_kwargs)
        elif func_name in self.funcs:
            return self.funcs[func_name](*func_args, **func_kwargs)
        else:
            return '[404] Can not match function'

    def register_function(self, fn: Callable, name: str = None) -> NoReturn:
        """
        除了rpc_views中的方法会默认注册，也可以使用该方法主动注册任意函数
        """
        if name is None:
            name = fn.__name__
        self.funcs[name] = fn


def rpc_view(name=''):
    def _wrapper(func):
        def __wrapper(*args, **kwargs):
            func_name = name
            if not func_name:
                func_name = func.__name__
            RPCServer().register_function(func, func_name)
            RPCServer().rpc_call(func_name, args, kwargs)

        return __wrapper
    return _wrapper
