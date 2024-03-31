# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/6 16:00
@Author  : wenjiawei
"""
import views
from net.server import Server

if __name__ == "__main__":
    s = Server()
    s.start()
    # s.register_function(views.match)
    # s.register_function(views.begin)

