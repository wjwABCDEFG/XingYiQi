# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/7 20:48
@Author  : wenjiawei
"""
from typing import OrderedDict


class Serializable:

    def __init__(self):
        self.id = id(self)

    def serialize(self) -> OrderedDict:
        raise NotImplemented()

    def deserialize(self, data: dict, hashmap: dict = {}, restore_id: bool = True) -> bool:
        raise NotImplemented()
